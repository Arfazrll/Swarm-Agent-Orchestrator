<script setup lang="ts">
import { ref, onMounted, onUnmounted, reactive } from 'vue'
import axios from 'axios'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { 
  Send, 
  Loader2, 
  CheckCircle2, 
  Download, 
  Terminal, 
  Sparkles,
  ArrowRight,
  Zap,
  Shield,
  Layout,
  Github,
  Search,
  PenTool,
  Code2,
  Cpu,
  Layers,
  Globe,
  Database,
  Briefcase,
  ZapOff,
  ChevronRight
} from 'lucide-vue-next'

gsap.registerPlugin(ScrollTrigger)

// State
const topic = ref('')
const isLoading = ref(false)
const jobId = ref<string | null>(null)
const status = ref('idle')
const logs = ref<string[]>([])
const pdfUrl = ref<string | null>(null)
const blogTitle = ref('')

let pollInterval: any = null

onMounted(() => {
  // Entrance Animation
  const tl = gsap.timeline()
  tl.from('.nav-pill', { y: -50, opacity: 0, duration: 1, ease: 'power4.out' })
    .from('.hero-content > *', { y: 40, opacity: 0, duration: 1, stagger: 0.15, ease: 'power3.out' }, '-=0.5')

  // Scroll Trigger Revealing
  gsap.utils.toArray('.reveal').forEach((el: any) => {
    gsap.from(el, {
      scrollTrigger: {
        trigger: el,
        start: 'top 85%',
        toggleActions: 'play none none reverse'
      },
      y: 40,
      opacity: 0,
      duration: 1,
      ease: 'power3.out'
    })
  })
})

const startGeneration = async () => {
  if (!topic.value.trim()) return
  isLoading.value = true
  status.value = 'running'
  logs.value = ['Initializing Intelligence Swarm...']
  
  try {
    const response = await axios.post('/api/run', { topic: topic.value })
    jobId.value = response.data.job_id
    startPolling()
    document.getElementById('workspace')?.scrollIntoView({ behavior: 'smooth' })
  } catch (error) {
    status.value = 'error'
    logs.value.push('Error: Connection failed')
    isLoading.value = false
  }
}

const startPolling = () => {
  pollInterval = setInterval(async () => {
    if (!jobId.value) return
    try {
      const response = await axios.get(`/api/status/${jobId.value}`)
      const data = response.data
      logs.value = data.logs
      status.value = data.status
      if (data.status === 'completed') {
        pdfUrl.value = data.pdf_url
        blogTitle.value = data.title
        stopPolling()
        isLoading.value = false
      } else if (data.status === 'error' || data.status === 'failed') {
        stopPolling()
        isLoading.value = false
      }
    } catch (e) {
      console.error(e)
    }
  }, 2000)
}

const stopPolling = () => {
  if (pollInterval) {
    clearInterval(pollInterval)
    pollInterval = null
  }
}

const scrollToWorkspace = () => {
  document.getElementById('workspace')?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <div class="min-h-screen relative bg-white overflow-hidden">
    <div class="grid-bg"></div>

    <!-- Pill Navigation -->
    <div class="nav-pill-container">
      <nav class="nav-pill">
        <div class="flex items-center space-x-2 mr-4 text-black">
          <Zap class="w-5 h-5 fill-black" />
          <span class="font-black tracking-tighter text-lg">Swarm AI</span>
        </div>
        <div class="hidden md:flex items-center space-x-8 text-sm font-black text-black">
          <a href="#technology" class="hover:text-accent transition-colors">Technology</a>
          <a href="#architecture" class="hover:text-accent transition-colors">Architecture</a>
          <a href="https://github.com" class="hover:text-accent transition-colors flex items-center space-x-1">
            <Github class="w-4 h-4" />
            <span>GitHub</span>
          </a>
        </div>
        <button @click="scrollToWorkspace" class="btn-saas-primary !py-2 !px-5 text-sm shadow-xl">
          Get Started
        </button>
      </nav>
    </div>

    <!-- Hero Section -->
    <section class="section-padding pt-48 flex flex-col items-center text-center">
      <div class="hero-content">
        <div class="inline-flex items-center space-x-2 px-6 py-2 rounded-full border border-black/20 bg-black/[0.04] text-[10px] font-black uppercase tracking-[0.3em] mb-12 text-black">
          <Sparkles class="w-3.5 h-3.5 text-accent" />
          <span>Agents Content Orchestration</span>
        </div>
        
        <h1 class="text-title-large mb-10">
          The future of writing<br />is <span class="text-accent">autonomous.</span>
        </h1>
        
        <p class="text-subtitle mx-auto mb-16 text-black font-bold">
          Leverage a collective of Pydantic AI agents to research, outline, and write 
          high-performance long-form content for production-grade environments.
        </p>
        
        <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
          <button @click="scrollToWorkspace" class="btn-saas-primary !py-4 !px-10 text-lg">
            <span>Start Generating</span>
            <ChevronRight class="w-5 h-5" />
          </button>
          <a href="#architecture" class="btn-saas-secondary !py-4 !px-10 text-lg">
            View Architecture
          </a>
        </div>
      </div>
    </section>

    <!-- Technology Bento (Reference Image 3 style) -->
    <section id="technology" class="section-padding bg-gray-50/50">
      <div class="max-w-7xl mx-auto">
        <div class="reveal mb-24 text-center">
          <h2 class="text-5xl md:text-6xl mb-8 font-black tracking-tighter text-black">Built for Reliability.</h2>
          <p class="text-black max-w-2xl mx-auto text-xl font-bold">
            Enterprise-grade infrastructure ensuring every draft is accurate, validated, and secure.
          </p>
        </div>

        <div class="bento-grid">
          <!-- Main Tech Card -->
          <div class="bento-card col-span-12 md:col-span-8 group reveal !border-black/10 shadow-md">
            <div class="flex items-start justify-between">
              <div>
                <Database class="w-12 h-12 mb-8 text-black/20 group-hover:text-accent transition-colors" />
                <h3 class="text-4xl mb-6 font-black text-black">Pydantic Validation</h3>
                <p class="text-black text-xl leading-relaxed max-w-md font-bold">
                  Every section, fact, and draft is validated against strict Pydantic schemas, 
                  ensuring 100% data integrity.
                </p>
              </div>
              <div class="hidden lg:block">
                <div class="p-8 bg-gray-50 rounded-3xl border border-black/5">
                  <div class="flex items-center space-x-4 mb-4">
                    <div class="w-3 h-3 bg-emerald-500 rounded-full"></div>
                    <span class="text-xs font-black uppercase tracking-widest text-black/60">Strict Schema V2</span>
                  </div>
                  <pre class="font-mono text-[10px] text-black/60">class Blog(BaseModel):
  title: str
  content: List[Section]
  status: str = "validated"</pre>
                </div>
              </div>
            </div>
          </div>

          <div class="bento-card col-span-12 md:col-span-4 group reveal bg-black text-white shadow-2xl">
            <Cpu class="w-12 h-12 mb-8 text-white/30 group-hover:text-accent transition-colors" />
            <h3 class="text-3xl mb-6 font-black tracking-tighter">Groq 70B Engine</h3>
            <p class="text-white/80 text-base leading-relaxed font-bold">
              Ultra-fast inference rates powered by Llama 3.3 for near-instant 
              intelligence handoffs.
            </p>
          </div>

          <div class="bento-card col-span-12 md:col-span-4 group reveal !border-black/10 shadow-md">
            <Globe class="w-10 h-10 mb-8 text-black/20 group-hover:text-accent transition-colors" />
            <h3 class="text-2xl mb-4 font-black text-black">Deep Research</h3>
            <p class="text-black text-base font-bold">
              Autonomous search across knowledge graphs to provide verified depth to every article.
            </p>
          </div>

          <div class="bento-card col-span-12 md:col-span-8 group reveal !border-black/10 shadow-md">
            <div class="flex items-center space-x-12">
              <Shield class="w-14 h-14 text-black/20 group-hover:text-accent transition-colors" />
              <div>
                <h3 class="text-3xl mb-4 font-black text-black">Production Ready</h3>
                <p class="text-black text-lg max-w-sm font-bold">
                  Battle-tested agent logic ready for integration into high-scale content marketing workflows.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Architecture Section (Bento Agents) -->
    <section id="architecture" class="section-padding">
      <div class="max-w-7xl mx-auto">
        <div class="reveal mb-20">
          <h2 class="text-5xl md:text-6xl mb-4 font-black text-black">The Swarm Intelligence.</h2>
          <div class="w-20 h-2 bg-accent rounded-full mb-8"></div>
          <p class="text-black text-2xl font-black">Four specialized agents, one unified mission.</p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div v-for="agent in [
            { name: 'Planner', icon: Layout, desc: 'Architects structural backbone and thematic consistency.' },
            { name: 'Researcher', icon: Search, desc: 'Scours the digital graph to provide factual depth.' },
            { name: 'Writer', icon: PenTool, desc: 'Forges the professional narrative from validated logs.' },
            { id: 'Editor', name: 'Editor', icon: Shield, desc: 'Enforces professional standards and grammar.' }
          ]" :key="agent.name" class="bento-card group reveal !border-black/10 shadow-md">
            <component :is="agent.icon" class="w-10 h-10 mb-10 text-black/20 group-hover:text-accent transition-colors" />
            <h3 class="text-2xl mb-4 font-black uppercase tracking-tighter text-black">{{ agent.name }}</h3>
            <p class="text-black text-base leading-relaxed font-bold">
              {{ agent.desc }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Workspace (Refined Light Theme) -->
    <main id="workspace" class="section-padding relative">
      <div class="max-w-5xl mx-auto">
        <div class="reveal text-center mb-20">
          <h2 class="text-title-large mb-6 !text-6xl !font-black text-black">Workspace.</h2>
          <p class="text-black font-bold">Initialize the swarm with your directive.</p>
        </div>

        <div class="space-y-12">
          <!-- Input Container -->
          <div class="bg-white border border-black/10 rounded-[2.5rem] p-4 flex flex-col md:flex-row gap-4 reveal shadow-xl">
            <input 
              v-model="topic"
              @keyup.enter="startGeneration"
              placeholder="Topic: The Evolution of Decentralized Finance..."
              class="flex-1 bg-transparent border-none px-8 py-5 text-xl focus:outline-none placeholder-black/20 text-black"
              :disabled="isLoading"
            />
            <button 
              @click="startGeneration"
              :disabled="isLoading || !topic.trim()"
              class="bg-black text-white px-10 py-5 rounded-[2rem] font-bold text-lg hover:bg-gray-800 transition-all flex items-center justify-center gap-3 active:scale-95 shadow-xl"
            >
              <Loader2 v-if="isLoading" class="w-6 h-6 animate-spin" />
              <Send v-else class="w-6 h-6" />
              <span>Initialize Swarm</span>
            </button>
          </div>

          <!-- Logs -->
          <div v-if="status !== 'idle'" class="reveal">
            <div class="bg-gray-50 border border-black/10 rounded-[2.5rem] overflow-hidden">
              <div class="px-10 py-6 border-b border-black/5 flex justify-between items-center text-xs font-black uppercase tracking-widest text-black/40">
                <div class="flex items-center gap-3">
                  <Terminal class="w-4 h-4" />
                  <span>Execution Logs</span>
                </div>
                <div class="flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full" :class="status === 'running' ? 'bg-black animate-pulse' : (status === 'completed' ? 'bg-emerald-500' : 'bg-red-500')"></span>
                  <span class="text-black">{{ status }}</span>
                </div>
              </div>
              <div class="p-12 h-[400px] overflow-y-auto font-mono text-sm text-black space-y-4">
                <div v-for="(log, i) in logs" :key="i" class="flex items-start gap-6 border-b border-black/5 pb-4 last:border-none">
                  <span class="text-black/20">{{ i + 1 }}</span>
                  <span class="uppercase tracking-tight font-bold">{{ log }}</span>
                </div>
                <div v-if="status === 'running'" class="flex items-center gap-4 text-emerald-600 pt-4">
                  <Loader2 class="w-4 h-4 animate-spin" />
                  <span class="text-xs uppercase font-black tracking-[0.2em]">Synthesizing Neural Data...</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Final Result -->
          <div v-if="status === 'completed'" class="reveal bg-white text-black p-12 rounded-[3rem] shadow-2xl flex flex-col md:flex-row items-center justify-between gap-8 animate-in slide-in-from-bottom duration-700">
            <div class="flex items-center gap-8">
              <div class="bg-emerald-100 p-6 rounded-[2rem]">
                <CheckCircle2 class="w-12 h-12 text-emerald-600" />
              </div>
              <div>
                <h3 class="text-3xl font-bold mb-2">{{ blogTitle }}</h3>
                <p class="text-gray-500 font-medium">Draft finalized and validated as production-ready PDF.</p>
              </div>
            </div>
            <a :href="pdfUrl || '#'" download class="bg-black text-white px-10 py-6 rounded-[2rem] font-bold text-xl hover:bg-gray-800 transition-all flex items-center gap-4 shadow-xl active:scale-95">
              <Download class="w-6 h-6" />
              <span>Download PDF</span>
            </a>
          </div>
        </div>
      </div>
    </main>

    <!-- Footer -->
    <footer class="py-20 border-t border-black/10 bg-white">
      <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center space-y-8 md:space-y-0 text-black font-black">
        <div class="flex items-center space-x-2">
          <Zap class="w-5 h-5 text-accent fill-accent" />
          <span class="tracking-tighter">Swarm AI</span>
        </div>
        <p class="text-[10px] uppercase tracking-widest">
          © 2026 Content Intelligence Systems. Developed by Syahril Arfian Almazril.
        </p>
        <div class="flex items-center space-x-8 text-[10px] uppercase tracking-widest">
          <a href="#" class="hover:text-accent transition-colors">Privacy</a>
          <a href="#architecture" class="hover:text-accent transition-colors">Architecture</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.animate-in {
  animation-fill-mode: forwards;
}
</style>
