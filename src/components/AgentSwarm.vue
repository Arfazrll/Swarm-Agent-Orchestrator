<script setup lang="ts">
import { Layout, Search, FileText, ShieldCheck } from 'lucide-vue-next';

const agents = [
  { 
    name: 'PLANNER', 
    desc: 'Architects structural backbone and thematic consistency.', 
    icon: Layout,
    color: 'group-hover:bg-blue-600',
    num: '01'
  },
  { 
    name: 'RESEARCHER', 
    desc: 'Scours the digital graph to provide factual depth.', 
    icon: Search,
    color: 'group-hover:bg-violet-600',
    num: '02'
  },
  { 
    name: 'WRITER', 
    desc: 'Forges the professional narrative from validated logs.', 
    icon: FileText,
    color: 'group-hover:bg-emerald-600',
    num: '03'
  },
  { 
    name: 'EDITOR', 
    desc: 'Enforces professional standards and grammar.', 
    icon: ShieldCheck,
    color: 'group-hover:bg-brand-orange',
    num: '04'
  },
];
</script>

<template>
  <section id="architecture" class="py-32 px-4">
    <div class="max-w-7xl mx-auto">

      <!-- Section Header (scroll-reveal) -->
      <div class="scroll-reveal mb-20 flex flex-col md:flex-row md:items-end md:justify-between gap-6 px-4 md:px-2">
        <div class="md:pl-4">
          <p class="text-[10px] font-black uppercase tracking-[0.3em] text-brand-orange mb-4">Architecture</p>
          <h2 class="text-5xl md:text-6xl font-black tracking-tighter text-black leading-none">The Swarm<br/>Intelligence.</h2>
        </div>
        <p class="text-black/40 font-bold text-base max-w-xs md:text-right leading-relaxed md:pr-4">
          Four specialized agents, one unified mission — designed for precision and speed.
        </p>
      </div>

      <!-- Agent Cards (staggered scroll-reveal) -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <div
          v-for="(agent, i) in agents"
          :key="agent.name"
          class="scroll-reveal-stagger group bg-white border-2 border-black/8 p-8 rounded-[2rem] flex flex-col justify-between transition-all duration-500 hover:-translate-y-3 hover:border-black/20 hover:shadow-[0_20px_60px_-10px_rgba(0,0,0,0.18)] cursor-default"
        >
          <!-- Top: number + icon box -->
          <div class="flex items-start justify-between mb-8">
            <div
              :class="['w-12 h-12 rounded-xl bg-neutral-50 border-2 border-black/8 flex items-center justify-center transition-all duration-500 text-black/30', agent.color, 'group-hover:border-transparent group-hover:text-white group-hover:scale-110']"
            >
              <component :is="agent.icon" class="w-5 h-5" />
            </div>
            <span class="text-[10px] font-black text-black/15 tracking-[0.2em]">{{ agent.num }}</span>
          </div>

          <!-- Bottom: text -->
          <div>
            <h3 class="text-[11px] font-black tracking-[0.25em] uppercase text-black mb-3">{{ agent.name }}</h3>
            <!-- Underline animation on h3 -->
            <div class="w-6 h-0.5 bg-brand-orange rounded-full mb-4 transition-all duration-300 group-hover:w-full"></div>
            <p class="text-black/40 font-medium leading-relaxed text-sm">{{ agent.desc }}</p>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>
