<script setup lang="ts">
import { Zap, Github } from 'lucide-vue-next';
</script>

<template>
  <nav class="fixed top-6 left-1/2 -translate-x-1/2 z-50 w-full max-w-[1000px] px-4">
    <div class="bg-white/80 backdrop-blur-xl border border-brand-border rounded-full px-2 py-2 flex items-center justify-between shadow-pill">
      <div class="flex items-center gap-2 pl-4">
        <Zap class="w-5 h-5 text-black fill-black" />
        <span class="font-bold text-lg tracking-tight">Swarm AI</span>
      </div>
      
      <div class="hidden md:flex items-center gap-12 text-[13px] font-bold text-neutral-500">
        <a href="#" class="hover:text-black transition-colors">Technology</a>
        <a href="#" class="hover:text-black transition-colors">Architecture</a>
        <a href="#" class="hover:text-black transition-colors flex items-center gap-2">
          <Github class="w-4 h-4" />
          GitHub
        </a>
      </div>

      <button class="bg-black text-white px-8 py-3 rounded-full text-[13px] font-bold shadow-lg hover:bg-neutral-800 transition-all active:scale-95">
        Get Started
      </button>
    </div>
  </nav>
</template>
