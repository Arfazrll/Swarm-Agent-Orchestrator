<script setup lang="ts">
import { Layout, Search, FileText, ShieldCheck } from 'lucide-vue-next';

const agents = [
  { name: 'PLANNER', desc: 'Architects structural backbone and thematic consistency.', icon: Layout },
  { name: 'RESEARCHER', desc: 'Scours the digital graph to provide factual depth.', icon: Search },
  { name: 'WRITER', desc: 'Forges the professional narrative from validated logs.', icon: FileText },
  { name: 'EDITOR', desc: 'Enforces professional standards and grammar.', icon: ShieldCheck },
];
</script>

<template>
  <section class="py-32 px-4 max-w-7xl mx-auto relative overflow-hidden">
    <div class="mb-20">
      <h2 class="text-5xl md:text-6xl font-black mb-6 tracking-tight">The Swarm Intelligence.</h2>
      <p class="text-xl text-neutral-500 font-medium">Four specialized agents, one unified mission.</p>
    </div>
    
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
      <div v-for="agent in agents" :key="agent.name" 
           class="bg-white border border-brand-border p-10 rounded-[32px] flex flex-col justify-between hover:-translate-y-2 transition-all duration-300 group shadow-sm hover:shadow-premium">
        <div class="w-12 h-12 rounded-2xl bg-neutral-50 border border-brand-border flex items-center justify-center mb-8 group-hover:bg-black group-hover:text-white transition-colors duration-300">
          <component :is="agent.icon" class="w-6 h-6" />
        </div>
        <div>
          <h3 class="text-xs font-black tracking-[0.2em] mb-4 uppercase text-black">{{ agent.name }}</h3>
          <p class="text-neutral-500 font-medium leading-relaxed text-sm">
            {{ agent.desc }}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>
