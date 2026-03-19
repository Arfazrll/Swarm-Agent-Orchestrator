<script setup lang="ts">
import { Zap, Github } from 'lucide-vue-next';

const scrollTo = (id: string) => {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
};
</script>

<template>
  <nav class="fixed top-5 left-1/2 -translate-x-1/2 z-50 w-full max-w-[1000px] px-4">
    <div class="bg-white/85 backdrop-blur-2xl border-2 border-black/12 rounded-full px-2 py-2 flex items-center justify-between shadow-[0_8px_32px_rgba(0,0,0,0.1)]">
      <div class="flex items-center gap-2 pl-4">
        <Zap class="w-5 h-5 text-black fill-black" />
        <span class="font-black text-base tracking-tighter">Swarm Agent</span>
      </div>

      <div class="hidden md:flex items-center gap-10 text-[13px] font-bold text-neutral-500">
        <a @click.prevent="scrollTo('technology')" href="#technology"
           class="hover:text-black transition-colors duration-200 cursor-pointer relative group">
          Technology
          <span class="absolute -bottom-0.5 left-0 w-0 h-0.5 bg-black rounded-full transition-all duration-300 group-hover:w-full"></span>
        </a>
        <a @click.prevent="scrollTo('architecture')" href="#architecture"
           class="hover:text-black transition-colors duration-200 cursor-pointer relative group">
          Architecture
          <span class="absolute -bottom-0.5 left-0 w-0 h-0.5 bg-black rounded-full transition-all duration-300 group-hover:w-full"></span>
        </a>
        <a href="https://github.com/Arfazrll/Swarm-Agent-Orchestrator" target="_blank"
           class="hover:text-black transition-colors duration-200 flex items-center gap-1.5 relative group">
          <Github class="w-4 h-4" />
          GitHub
          <span class="absolute -bottom-0.5 left-0 w-0 h-0.5 bg-black rounded-full transition-all duration-300 group-hover:w-full"></span>
        </a>
      </div>

      <button
        @click="scrollTo('workspace-anchor')"
        class="relative overflow-hidden bg-black text-white px-8 py-3 rounded-full text-[13px] font-bold shadow-lg transition-all duration-300 active:scale-95 group">
        <span class="absolute inset-0 bg-brand-orange scale-x-0 origin-left transition-transform duration-300 group-hover:scale-x-100 rounded-full"></span>
        <span class="relative z-10">Get Started</span>
      </button>
    </div>
  </nav>
</template>
