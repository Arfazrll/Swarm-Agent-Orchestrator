<script setup lang="ts">
import { ChevronRight, ArrowRight } from 'lucide-vue-next';
defineEmits(['start']);

const scrollTo = (id: string) => {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
};
</script>

<template>
  <section class="hero-section pt-40 pb-24 text-center px-4 relative overflow-hidden">
    <!-- Subtle radial glow background -->
    <div class="absolute inset-0 pointer-events-none">
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[700px] rounded-full bg-gradient-radial from-neutral-100/80 to-transparent opacity-60"></div>
    </div>

    <div class="hero-content relative z-10 w-full max-w-6xl mx-auto">
      <!-- Animated badge -->
      <div class="scroll-reveal inline-flex items-center gap-2 px-6 py-2.5 rounded-full bg-neutral-50 border-2 border-black/10 mb-10">
        <div class="w-1.5 h-1.5 bg-brand-orange rounded-full animate-pulse"></div>
        <span class="text-[10px] uppercase font-black tracking-[0.3em] text-black/50">Agents Content Orchestration</span>
      </div>

      <!-- Headline -->
      <h1 class="scroll-reveal text-[clamp(3.5rem,10vw,8rem)] font-black leading-[0.9] tracking-[-0.04em] text-black mb-10">
        The future of writing<br />is <span class="text-brand-orange">autonomous.</span>
      </h1>

      <!-- Subtitle -->
      <p class="scroll-reveal text-lg md:text-xl text-black/50 max-w-2xl mx-auto mb-16 font-medium leading-relaxed">
        Leverage a collective of Pydantic AI agents to research, outline, and write
        high-performance long-form content for production-grade environments.
      </p>

      <!-- CTAs -->
      <div class="scroll-reveal flex flex-col sm:flex-row items-center justify-center gap-4">
        <!-- Primary: glow + scale on hover -->
        <button
          @click="$emit('start')"
          class="group relative bg-black text-white px-10 py-5 rounded-full font-black text-base flex items-center gap-2 transition-all duration-300 hover:scale-105 hover:shadow-[0_0_40px_rgba(0,0,0,0.3)] active:scale-95 overflow-hidden"
        >
          <span class="absolute inset-0 bg-gradient-to-r from-neutral-800 to-black opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-full"></span>
          <span class="relative z-10 flex items-center gap-2">
            Start Generating
            <ChevronRight class="w-5 h-5 group-hover:translate-x-1 transition-transform duration-300" />
          </span>
        </button>

        <!-- Secondary: border fill + underline animation -->
        <button
          @click="scrollTo('architecture')"
          class="group relative px-10 py-5 rounded-full font-black text-base border-2 border-black/20 bg-white text-black transition-all duration-300 hover:border-black hover:shadow-md active:scale-95 overflow-hidden"
        >
          <span class="absolute inset-0 bg-black scale-y-0 origin-bottom transition-transform duration-300 group-hover:scale-y-100 rounded-full"></span>
          <span class="relative z-10 group-hover:text-white transition-colors duration-300">View Architecture</span>
        </button>
      </div>
    </div>
  </section>
</template>
