<script setup lang="ts">
import { ChevronRight } from 'lucide-vue-next';

defineEmits(['start']);
</script>

<template>
  <section class="pt-28 pb-20 text-center px-4">
    <div class="inline-flex items-center gap-2 px-6 py-2.5 rounded-full bg-neutral-50 border border-brand-border mb-8">
      <div class="w-1.5 h-1.5 bg-brand-orange rounded-full animate-pulse"></div>
      <span class="text-[10px] uppercase font-bold tracking-[0.25em] text-neutral-400">Agents Content Orchestration</span>
    </div>
    
    <h1 class="text-6xl md:text-[120px] font-black tracking-[-0.04em] leading-[0.85] mb-12 max-w-6xl mx-auto text-black">
      The future of writing <br class="hidden md:block"/> is <span class="text-brand-orange">autonomous.</span>
    </h1>
    
    <p class="text-lg md:text-xl text-neutral-500 max-w-2xl mx-auto mb-16 font-medium leading-relaxed">
      Leverage a collective of Pydantic AI agents to research, outline, and write high-performance long-form content for production-grade environments.
    </p>

    <div class="flex flex-col md:flex-row items-center justify-center gap-4">
      <button @click="$emit('start')" class="bg-black text-white px-10 py-5 rounded-full font-bold flex items-center gap-2 hover:bg-neutral-800 transition-all active:scale-95 shadow-xl">
        Start Generating <ChevronRight class="w-5 h-5" />
      </button>
      <button class="px-10 py-5 rounded-full font-bold border border-brand-border bg-white hover:bg-neutral-50 transition-all active:scale-95">
        View Architecture
      </button>
    </div>
  </section>
</template>
