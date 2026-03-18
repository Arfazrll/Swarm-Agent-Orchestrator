import os
import uuid
import threading
from flask import Flask, render_template, request, jsonify, send_file
from core.swarm_logic import run_swarm_backend, latest_result
from core.pdf_generator import generate_pdf

app = Flask(__name__)

# Directory for generated files
OUTPUT_DIR = "generated_docs"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Store job status
jobs = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/run", methods=["POST"])
def run_swarm():
    data = request.json
    topic = data.get("topic")
    if not topic:
        return jsonify({"error": "Topic is required"}), 400
    
    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "status": "running",
        "topic": topic,
        "logs": ["Initialising Swarm agents..."],
        "pdf_url": None,
        "title": ""
    }
    
    def background_task(tid, t_topic):
        try:
            # Note: run_swarm_backend needs to be modified to handle local job state
            # but for this MVP, we'll monitor the global latest_result
            # and move data to our job store.
            
            # Reset global logic state
            from core.swarm_logic import latest_result as lr
            lr["logs"] = []
            lr["status"] = "running"
            
            run_swarm_backend(t_topic)
            
            # Once finished, generate PDF
            if lr["status"] == "completed":
                pdf_filename = f"{tid}.pdf"
                pdf_path = os.path.join(OUTPUT_DIR, pdf_filename)
                
                if generate_pdf(lr["content"], pdf_path, lr["title"]):
                    jobs[tid]["status"] = "completed"
                    jobs[tid]["pdf_url"] = f"/api/download/{pdf_filename}"
                    jobs[tid]["title"] = lr["title"]
                else:
                    jobs[tid]["status"] = "failed"
                    jobs[tid]["logs"].append("Error: Failed to generate PDF document.")
            else:
                jobs[tid]["status"] = "failed"
                jobs[tid]["logs"].append("Error: Swarm process did not complete successfully.")
                
        except Exception as e:
            jobs[tid]["status"] = "error"
            jobs[tid]["logs"].append(f"System Error: {str(e)}")

    thread = threading.Thread(target=background_task, args=(job_id, topic))
    thread.start()
    
    return jsonify({"job_id": job_id})

@app.route("/api/status/<job_id>")
def get_status(job_id):
    if job_id not in jobs:
        return jsonify({"error": "Job not found"}), 404
    
    # Sync logs from global logic state if the job is still running
    from core.swarm_logic import latest_result as lr
    if jobs[job_id]["status"] == "running":
        jobs[job_id]["logs"] = lr["logs"][:]
        
    return jsonify(jobs[job_id])

@app.route("/api/download/<filename>")
def download_pdf(filename):
    path = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "File not found", 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
