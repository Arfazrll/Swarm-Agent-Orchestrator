document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generateBtn');
    const topicInput = document.getElementById('topicInput');
    const statusContainer = document.getElementById('statusContainer');
    const logContainer = document.getElementById('logContainer');
    const logsWindow = document.getElementById('logs');
    const resultContainer = document.getElementById('resultContainer');
    const currentStatus = document.getElementById('currentStatus');
    const progressBar = document.getElementById('progressBar');
    const downloadLink = document.getElementById('downloadLink');
    const resetBtn = document.getElementById('resetBtn');
    const resultTitle = document.getElementById('resultTitle');

    let pollInterval = null;
    let progress = 0;

    // Initial Animations
    gsap.from('.glow-text', { y: -50, opacity: 0, duration: 1, ease: 'power4.out' });
    gsap.from('.card', { y: 50, opacity: 0, duration: 1.2, delay: 0.3, ease: 'power3.out' });

    generateBtn.addEventListener('click', async () => {
        const topic = topicInput.value.trim();
        if (!topic) {
            gsap.to(topicInput, { x: 10, repeat: 5, yoyo: true, duration: 0.05 });
            return;
        }

        // UI Transition
        generateBtn.disabled = true;
        gsap.to('.input-group', { opacity: 0, height: 0, marginTop: 0, marginBottom: 0, display: 'none', duration: 0.5 });
        
        statusContainer.classList.remove('hidden');
        logContainer.classList.remove('hidden');
        gsap.from('#statusContainer', { opacity: 0, y: 20 });
        gsap.from('#logContainer', { opacity: 0, y: 20, delay: 0.2 });

        try {
            const response = await fetch('/api/run', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic })
            });
            const data = await response.json();
            
            if (data.job_id) {
                startPolling(data.job_id);
            } else {
                showError("Could not start Swarm job.");
            }
        } catch (err) {
            showError("Network error. Please try again.");
        }
    });

    function startPolling(jobId) {
        pollInterval = setInterval(async () => {
            try {
                const response = await fetch(`/api/status/${jobId}`);
                const data = await response.json();

                updateUI(data);

                if (data.status === 'completed') {
                    clearInterval(pollInterval);
                    showResult(data);
                } else if (data.status === 'failed' || data.status === 'error') {
                    clearInterval(pollInterval);
                    showError(data.logs.slice(-1)[0]);
                }
            } catch (err) {
                console.error("Polling error", err);
            }
        }, 2000);
    }

    function updateUI(data) {
        // Mock progress based on log count or status
        if (data.status === 'running') {
            const stepCount = data.logs.length;
            progress = Math.min(progress + 5, 90); // Slow artificial progress
            if (stepCount > 3) progress = Math.max(progress, 30);
            if (stepCount > 5) progress = Math.max(progress, 60);
            
            progressBar.style.width = `${progress}%`;
            
            // Update last log
            if (data.logs.length > 0) {
                const lastLog = data.logs[data.logs.length - 1];
                currentStatus.innerText = lastLog.length > 50 ? lastLog.substring(0, 50) + '...' : lastLog;
                
                // Refresh full logs window
                logsWindow.innerHTML = data.logs.map(log => `<p>> ${log}</p>`).join('');
                logsWindow.scrollTop = logsWindow.scrollHeight;
            }
        }
    }

    function showResult(data) {
        progressBar.style.width = '100%';
        currentStatus.innerText = "Task Finished!";
        
        setTimeout(() => {
            gsap.to([statusContainer, logContainer], { opacity: 0, duration: 0.5, onComplete: () => {
                statusContainer.classList.add('hidden');
                logContainer.classList.add('hidden');
                
                resultContainer.classList.remove('hidden');
                resultTitle.innerText = data.title || "Success!";
                downloadLink.href = data.pdf_url;
                
                gsap.from('#resultContainer', { opacity: 0, scale: 0.9, duration: 1, ease: 'elastic.out(1, 0.5)' });
            }});
        }, 1000);
    }

    function showError(msg) {
        currentStatus.innerText = "Error: " + msg;
        currentStatus.style.color = "#ef4444";
        progressBar.style.background = "#ef4444";
        generateBtn.disabled = false;
    }

    resetBtn.addEventListener('click', () => {
        location.reload();
    });
});
