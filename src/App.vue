<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
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
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

import Navbar from './components/Navbar.vue';
import Hero from './components/Hero.vue';
import Features from './components/Features.vue';
import AgentSwarm from './components/AgentSwarm.vue';
import Workspace from './components/Workspace.vue';
import Footer from './components/Footer.vue';

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

const startGeneration = async () => {
  if (!topic.value) return;
  
  jobStatus.value = "running";
  logs.value = ["Initiating Swarm Orchestrator..."];
  pdfUrl.value = null;
  currentStep.value = 0;

  const el = document.getElementById('workspace-anchor');
  if (el) el.scrollIntoView({ behavior: 'smooth' });

  try {
    const res = await axios.post("/api/run", { topic: topic.value });
    const jobId = res.data.job_id;
    pollStatus(jobId);
    
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

const scrollToWorkspace = () => {
  const el = document.getElementById('workspace-anchor');
  if (el) el.scrollIntoView({ behavior: 'smooth' });
};

onMounted(() => {
  gsap.from(".hero-content > *", {
    y: 30,
    opacity: 0,
    duration: 1,
    stagger: 0.2,
    ease: "power4.out"
  });

  gsap.utils.toArray<Element>('.scroll-reveal').forEach((el) => {
    gsap.fromTo(el, 
      { y: 50, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 1,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 88%',
          end: 'top 20%',
          toggleActions: 'play none none reverse',
        }
      }
    );
  });

  const staggerGroups = document.querySelectorAll('.scroll-reveal-stagger');
  if (staggerGroups.length > 0) {
    gsap.fromTo(staggerGroups,
      { y: 60, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 0.8,
        stagger: 0.12,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: staggerGroups[0],
          start: 'top 85%',
          toggleActions: 'play none none reverse',
        }
      }
    );
  }

  gsap.to('.hero-section', {
    y: -80,
    ease: 'none',
    scrollTrigger: {
      trigger: '.hero-section',
      start: 'top top',
      end: 'bottom top',
      scrub: 1.5,
    }
  });
});

onUnmounted(() => {
  ScrollTrigger.getAll().forEach(t => t.kill());
});
</script>

<template>
  <div class="min-h-screen bg-white relative font-plus selection:bg-brand-orange selection:text-white">
    <Navbar />

    <main class="relative z-10">
      <Hero @start="scrollToWorkspace" />

      <Features />
      <AgentSwarm />

      <div id="workspace-anchor" class="scroll-mt-32">
        <Workspace v-model="topic" :loading="jobStatus === 'running'" @submit="startGeneration" />
      </div>

      <section v-if="jobStatus !== 'idle'" class="max-w-7xl mx-auto px-4 pb-32">
        <div class="bento-card p-10 relative overflow-hidden bg-white/80 backdrop-blur-md">
          <div class="flex justify-between items-center mb-16 relative z-10 max-w-4xl mx-auto">
            <div v-for="(step, index) in steps" :key="step.id" class="flex flex-col items-center gap-4">
              <div 
                :class="[
                  'w-14 h-14 rounded-full flex items-center justify-center border-2 transition-all duration-700',
                  currentStep >= index ? 'bg-black border-black text-white scale-110 shadow-lg' : 'bg-white border-brand-border text-neutral-300'
                ]"
              >
                <component :is="step.icon" class="w-6 h-6" />
              </div>
              <span :class="['text-[10px] font-black uppercase tracking-widest', currentStep >= index ? 'text-black' : 'text-neutral-300']">
                {{ step.name }}
              </span>
            </div>
            <div class="absolute top-7 left-14 right-14 h-[2px] bg-brand-border -z-10">
              <div 
                class="h-full bg-black transition-all duration-1000"
                :style="{ width: `${(currentStep / 4) * 100}%` }"
              ></div>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 max-w-5xl mx-auto">
            <div class="bg-neutral-50 rounded-3xl p-8 border border-brand-border font-mono text-xs h-96 overflow-y-auto shadow-inner relative">
              <div class="sticky top-0 bg-neutral-50/90 backdrop-blur pb-4 mb-4 border-b border-black/5 flex items-center gap-2">
                <Terminal class="w-4 h-4 text-black" />
                <span class="font-bold uppercase tracking-widest text-[10px]">Orchestrator Logs</span>
              </div>
              <div v-for="(log, index) in logs" :key="index" class="mb-3 text-brand-gray flex gap-4 leading-relaxed">
                <span class="text-neutral-300">{{ String(index + 1).padStart(2, '0') }}</span>
                <span>{{ log }}</span>
              </div>
              <div v-if="jobStatus === 'running'" class="mt-4 flex items-center gap-2 text-black font-black italic">
                <span class="w-2 h-2 bg-brand-orange rounded-full animate-ping"></span>
                <span>Awaiting agent response...</span>
              </div>
            </div>

            <div class="flex flex-col justify-center items-center text-center p-10 border-2 border-dashed border-brand-border rounded-3xl bg-neutral-50/30">
              <div v-if="jobStatus === 'running'" class="space-y-6">
                <div class="w-24 h-24 bg-white shadow-premium rounded-full flex items-center justify-center mx-auto animate-pulse">
                  <Rocket class="w-10 h-10 text-black fill-black" />
                </div>
                <h3 class="text-2xl font-black">Swarm in Action</h3>
                <p class="text-brand-gray font-medium max-w-xs mx-auto">Multi-agent intelligence is active. Neutralizing hallucination risks and validating schemas.</p>
              </div>

              <div v-if="jobStatus === 'completed'" class="success-state space-y-8">
                <div class="w-24 h-24 bg-black rounded-full flex items-center justify-center mx-auto text-white shadow-xl">
                  <ShieldCheck class="w-12 h-12" />
                </div>
                <div>
                  <h3 class="text-3xl font-black mb-3">{{ blogTitle }}</h3>
                  <p class="text-brand-gray font-medium mb-8">Generation verified. High-fidelity report is ready for export.</p>
                </div>
                <a 
                  :href="pdfUrl!" 
                  target="_blank"
                  class="btn-black inline-flex items-center gap-3 uppercase tracking-widest text-xs"
                >
                  <Download class="w-5 h-5" />
                  Download PDF Report
                </a>
              </div>

              <div v-if="jobStatus === 'error'" class="space-y-6 text-red-600">
                <AlertCircle class="w-16 h-16 mx-auto stroke-[2.5]" />
                <h3 class="text-2xl font-black">Orchestration Error</h3>
                <p class="font-medium">System encountered a critical exception during validation.</p>
                <button @click="jobStatus = 'idle'" class="text-black font-black underline uppercase tracking-widest text-xs">Re-Initialize</button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>

    <Footer />
  </div>
</template>

<style scoped>
.success-state {
  animation: slideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideUp {
  from { transform: translateY(30px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}
</style>
