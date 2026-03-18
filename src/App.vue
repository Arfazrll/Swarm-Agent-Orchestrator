<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { 
  Rocket, 
  Terminal, 
  FileText, 
  Download, 
  Search, 
  Zap, 
  Cpu, 
  ShieldCheck,
  ChevronRight,
  Sparkles,
  Layout,
  RefreshCcw,
  ArrowRight,
  AlertCircle
} from 'lucide-vue-next';
import axios from 'axios';
import { gsap } from 'gsap';

const topic = ref("");
const jobStatus = ref<"idle" | "running" | "completed" | "error">("idle");
const logs = ref<string[]>([]);
const pdfUrl = ref<string | null>(null);
const blogTitle = ref("");
const currentStep = ref(0);

const steps = [
  { id: 1, name: 'Analysing Topic', icon: Search },
  { id: 2, name: 'Strategic Planning', icon: Layout },
  { id: 3, name: 'Deep Research', icon: Cpu },
  { id: 4, name: 'AI Drafting', icon: FileText },
  { id: 5, name: 'Polish & Export', icon: ShieldCheck }
];

const features = [
  { 
    title: "Multi-Agent Swarm", 
    desc: "Coordination between specialized AI agents for planning, research, and writing.",
    icon: Zap
  },
  { 
    title: "Llama 3.3 70B", 
    desc: "Powered by state-of-the-art open models for high-reasoning output.",
    icon: Terminal
  },
  { 
    title: "PDF Generation", 
    desc: "Automated export to professional PDF format with clean typography.",
    icon: FileText
  }
];

const startGeneration = async () => {
  if (!topic.value) return;
  
  jobStatus.value = "running";
  logs.value = ["Initiating Swarm Orchestrator..."];
  pdfUrl.value = null;
  currentStep.value = 0;

  try {
    const res = await axios.post("/api/run", { topic: topic.value });
    const jobId = res.data.job_id;
    pollStatus(jobId);
    
    // Simulate step progress
    const stepInterval = setInterval(() => {
      if (currentStep.value < 4) {
        currentStep.value++;
      } else {
        clearInterval(stepInterval);
      }
    }, 4000);
  } catch (err) {
    jobStatus.value = "error";
    logs.value.push("Error: Failed to connect to backend api.");
  }
};

const pollStatus = async (jobId: string) => {
  const interval = setInterval(async () => {
    try {
      const res = await axios.get(`/api/status/${jobId}`);
      const data = res.data;
      
      logs.value = data.logs;
      
      if (data.status === "completed") {
        clearInterval(interval);
        jobStatus.value = "completed";
        pdfUrl.value = data.pdf_url;
        blogTitle.value = data.title;
        currentStep.value = 4;
        
        gsap.from(".success-state", {
          y: 20,
          opacity: 0,
          duration: 0.8,
          ease: "expo.out"
        });
      } else if (data.status === "error" || data.status === "failed") {
        clearInterval(interval);
        jobStatus.value = "error";
      }
    } catch (err) {
      clearInterval(interval);
      jobStatus.value = "error";
      logs.value.push("System Error: Connection lost.");
    }
  }, 2000);
};

onMounted(() => {
  gsap.from(".hero-content > *", {
    y: 30,
    opacity: 0,
    duration: 1,
    stagger: 0.2,
    ease: "power4.out"
  });
});
</script>

<template>
  <div class="min-h-screen bg-white relative overflow-hidden">
    <!-- Grid Overlay -->
    <div class="absolute inset-0 grid-bg opacity-40 pointer-events-none"></div>
    
    <!-- Top Nav -->
    <nav class="fixed top-6 left-1/2 -translate-x-1/2 z-50 px-6 py-3 bg-white/80 backdrop-blur-md border border-black/5 rounded-full flex items-center gap-6 shadow-sm">
      <div class="flex items-center gap-2">
        <div class="w-6 h-6 bg-black rounded-lg flex items-center justify-center">
          <Rocket class="w-3.5 h-3.5 text-white" />
        </div>
        <span class="font-bold text-sm tracking-tight">SWARM AI</span>
      </div>
      <div class="h-4 w-px bg-black/10"></div>
      <div class="flex gap-4 text-xs font-semibold uppercase tracking-widest text-neutral-500">
        <a href="#" class="hover:text-black transition-colors">Platform</a>
        <a href="#" class="hover:text-black transition-colors">Agents</a>
        <a href="#" class="hover:text-black transition-colors">API</a>
      </div>
    </nav>

    <main class="relative z-10 pt-32 pb-20 px-4">
      <div class="max-w-[1100px] mx-auto">
        <!-- Hero Section -->
        <section class="hero-content text-center mb-24">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-neutral-100 border border-black/5 mb-6">
            <Sparkles class="w-3 h-3 text-black" />
            <span class="text-[10px] uppercase font-bold tracking-widest text-neutral-600">v1.2.0 Production Ready</span>
          </div>
          <h1 class="text-6xl md:text-8xl mb-8 leading-[0.9] bg-clip-text text-black">
            AUTONOMOUS<br/>CONTENT GENERATION.
          </h1>
          <p class="text-xl text-neutral-500 max-w-2xl mx-auto mb-10 font-medium">
            Deploy a swarm of AI agents to research, plan, and draft professional grade articles in seconds.
          </p>

          <!-- Input Area -->
          <div class="max-w-2xl mx-auto p-2 bg-neutral-100 rounded-2xl border border-black/5 shadow-inner">
            <div class="flex gap-2">
              <input 
                v-model="topic"
                @keyup.enter="startGeneration"
                placeholder="What should the swarm write about?"
                class="flex-1 px-6 py-4 rounded-xl bg-white border border-black/5 focus:outline-none focus:ring-2 focus:ring-black/5 text-black placeholder:text-neutral-400 font-medium"
              />
              <button 
                @click="startGeneration"
                :disabled="jobStatus === 'running'"
                class="px-8 py-4 bg-black text-white rounded-xl font-bold flex items-center gap-2 hover:bg-neutral-800 transition-all active:scale-95 disabled:opacity-50"
              >
                <span>{{ jobStatus === 'running' ? 'Deploying...' : 'Generate' }}</span>
                <ArrowRight v-if="jobStatus !== 'running'" class="w-4 h-4" />
                <RefreshCcw v-else class="w-4 h-4 animate-spin" />
              </button>
            </div>
          </div>
        </section>

        <!-- Generation View -->
        <section v-if="jobStatus !== 'idle'" class="mb-24">
          <div class="bento-card rounded-3xl p-10 relative overflow-hidden">
            <!-- Progress Steps -->
            <div class="flex justify-between items-center mb-12 relative z-10">
              <div v-for="(step, index) in steps" :key="step.id" class="flex flex-col items-center gap-3">
                <div 
                  :class="[
                    'w-12 h-12 rounded-full flex items-center justify-center border-2 transition-all duration-500',
                    currentStep >= index ? 'bg-black border-black text-white scale-110' : 'bg-white border-neutral-200 text-neutral-400'
                  ]"
                >
                  <component :is="step.icon" class="w-5 h-5" />
                </div>
                <span :class="['text-[10px] font-bold uppercase tracking-tight', currentStep >= index ? 'text-black' : 'text-neutral-400']">
                  {{ step.name }}
                </span>
              </div>
              <!-- Connector Lines -->
              <div class="absolute top-6 left-12 right-12 h-0.5 bg-neutral-100 -z-10">
                <div 
                  class="h-full bg-black transition-all duration-1000"
                  :style="{ width: `${(currentStep / 4) * 100}%` }"
                ></div>
              </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <!-- Logs Panel -->
              <div class="bg-neutral-50 rounded-2xl p-6 border border-black/5 font-mono text-sm h-80 overflow-y-auto">
                <div v-for="(log, index) in logs" :key="index" class="mb-2 text-neutral-600 flex gap-3">
                  <span class="text-neutral-300">[{{ Number(index) + 1 }}]</span>
                  <span>{{ log }}</span>
                </div>
                <div v-if="jobStatus === 'running'" class="animate-pulse text-black font-bold">
                  _ Waiting for agent response...
                </div>
              </div>

              <!-- Result View -->
              <div class="flex flex-col justify-center items-center text-center p-6 border-2 border-dashed border-neutral-200 rounded-2xl bg-white/50">
                <div v-if="jobStatus === 'running'" class="space-y-4">
                  <div class="w-20 h-20 bg-neutral-100 rounded-full flex items-center justify-center mx-auto animate-bounce">
                    <Rocket class="w-10 h-10 text-black" />
                  </div>
                  <h3 class="text-xl font-bold">Swarm Orchestration in Progress</h3>
                  <p class="text-neutral-500 text-sm">Agents are compiling sections and generating logic.</p>
                </div>

                <div v-if="jobStatus === 'completed'" class="success-state space-y-6">
                  <div class="w-20 h-20 bg-green-500 rounded-full flex items-center justify-center mx-auto text-white">
                    <ShieldCheck class="w-10 h-10" />
                  </div>
                  <div>
                    <h3 class="text-2xl font-black mb-2">{{ blogTitle }}</h3>
                    <p class="text-neutral-500 mb-6">Article compiled and verified. PDF is ready.</p>
                  </div>
                  <a 
                    :href="pdfUrl!" 
                    target="_blank"
                    class="inline-flex items-center gap-3 px-8 py-4 bg-black text-white rounded-xl font-bold hover:bg-neutral-800 transition-all uppercase tracking-widest text-xs"
                  >
                    <Download class="w-4 h-4" />
                    Download PDF Document
                  </a>
                </div>

                <div v-if="jobStatus === 'error'" class="space-y-4 text-red-600">
                  <AlertCircle class="w-12 h-12 mx-auto" />
                  <h3 class="text-xl font-bold">Deployment Failed</h3>
                  <p class="text-sm">Check the logs for detailed agent error reports.</p>
                  <button @click="jobStatus = 'idle'" class="text-black font-bold underline">Try Again</button>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Feature Bento Grid -->
        <section v-if="jobStatus === 'idle'" class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="feat in features" :key="feat.title" class="bento-card rounded-2xl p-8 group">
            <div class="w-12 h-12 bg-black rounded-xl flex items-center justify-center mb-6 text-white group-hover:scale-110 transition-transform">
              <component :is="feat.icon" class="w-6 h-6" />
            </div>
            <h3 class="text-xl font-bold mb-3">{{ feat.title }}</h3>
            <p class="text-neutral-500 text-sm leading-relaxed mb-6">{{ feat.desc }}</p>
            <div class="flex items-center gap-2 text-xs font-bold uppercase tracking-widest opacity-0 group-hover:opacity-100 transition-opacity">
              <span>Learn more</span>
              <ChevronRight class="w-3 h-3" />
            </div>
          </div>
        </section>
      </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-black/5 py-10 mt-20">
      <div class="max-w-[1100px] mx-auto px-4 flex flex-col md:row justify-between items-center gap-6">
        <div class="flex items-center gap-2">
          <div class="w-5 h-5 bg-black rounded-md flex items-center justify-center">
            <Rocket class="w-3 h-3 text-white" />
          </div>
          <span class="font-bold text-xs uppercase tracking-widest">Swarm Intelligence</span>
        </div>
        <p class="text-[10px] uppercase font-bold tracking-[0.2em] text-neutral-400">
          Built for the future of automated technical writing.
        </p>
        <div class="flex gap-6 text-[10px] font-bold uppercase tracking-widest text-neutral-600">
          <a href="#" class="hover:text-black">Privacy</a>
          <a href="#" class="hover:text-black">Terms</a>
          <a href="#" class="hover:text-black">Github</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.success-state {
  animation: slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideUp {
  from { transform: translateY(20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}
</style>
