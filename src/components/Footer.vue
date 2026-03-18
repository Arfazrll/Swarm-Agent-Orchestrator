<script setup lang="ts">
import { Rocket } from 'lucide-vue-next';
</script>

<template>
  <footer class="py-16 px-4 border-t border-brand-border">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-8 text-center md:text-left">
      <div class="flex items-center gap-2">
        <Zap class="w-4 h-4 text-brand-orange" />
        <span class="font-bold text-sm tracking-tight text-black">Swarm AI</span>
      </div>

      <p class="text-[10px] font-bold tracking-[0.2em] text-neutral-400 uppercase">
        © 2026 CONTENT INTELLIGENCE SYSTEMS. DEVELOPED BY SYAHRIL ARFIAN ALMAZRIL.
      </p>

      <div class="flex gap-8 text-[10px] uppercase font-bold tracking-widest text-neutral-400">
        <a href="#" class="hover:text-black transition-colors">Privacy</a>
        <a href="#" class="hover:text-black transition-colors">Architecture</a>
        <a href="#" class="hover:text-black transition-colors">GitHub</a>
      </div>
    </div>
  </footer>
</template>
