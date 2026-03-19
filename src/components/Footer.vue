<script setup lang="ts">
import { Zap } from 'lucide-vue-next';
</script>

<template>
  <footer class="py-16 px-6 border-t-2 border-black/8 bg-white">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-8 text-center md:text-left">

      <!-- Brand -->
      <div class="flex items-center gap-2">
        <Zap class="w-4 h-4 text-brand-orange fill-brand-orange" />
        <span class="font-black text-sm tracking-tighter text-black">Swarm Agent</span>
      </div>

      <!-- Copyright -->
      <p class="text-[10px] font-black tracking-[0.2em] text-black uppercase">
        © 2026 CONTENT INTELLIGENCE SYSTEMS. DEVELOPED BY SYAHRIL ARFIAN ALMAZRIL.
      </p>

      <!-- Links -->
      <div class="flex gap-8 text-[10px] uppercase font-black tracking-widest text-black/60">
        <a href="https://github.com/Arfazrll/Swarm-Agent-Orchestrator/blob/main/README.md" class="hover:text-black transition-colors duration-200 relative group">
          Docs
          <span class="absolute -bottom-0.5 left-0 w-0 h-0.5 bg-black rounded-full transition-all duration-300 group-hover:w-full"></span>
        </a>
        <a href="#architecture" class="hover:text-black transition-colors duration-200 relative group">
          Architecture
          <span class="absolute -bottom-0.5 left-0 w-0 h-0.5 bg-black rounded-full transition-all duration-300 group-hover:w-full"></span>
        </a>
        <a href="https://github.com/Arfazrll/Swarm-Agent-Orchestrator" target="_blank" class="hover:text-black transition-colors duration-200 relative group">
          GitHub
          <span class="absolute -bottom-0.5 left-0 w-0 h-0.5 bg-black rounded-full transition-all duration-300 group-hover:w-full"></span>
        </a>
      </div>

    </div>
  </footer>
</template>
