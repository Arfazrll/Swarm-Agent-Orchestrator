<script setup lang="ts">
import { Cpu, Search, ShieldCheck, Database } from 'lucide-vue-next';
</script>

<template>
  <section class="py-32 px-4 max-w-7xl mx-auto relative overflow-hidden">
    <div class="text-center mb-20">
      <h2 class="text-4xl md:text-6xl font-black mb-6 tracking-tight">Built for Reliability.</h2>
      <p class="text-lg text-neutral-500 max-w-2xl mx-auto font-medium leading-relaxed">
        Enterprise-grade infrastructure ensuring every draft is accurate, validated, and secure.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-12 gap-8">
      <!-- Pydantic Validation Card -->
      <div class="md:col-span-8 bento-card p-12 flex flex-col justify-between overflow-hidden relative group">
        <div>
          <Database class="w-8 h-8 mb-10 text-neutral-300" />
          <h3 class="text-3xl font-bold mb-4">Pydantic Validation</h3>
          <p class="text-neutral-500 text-lg max-w-sm font-medium leading-relaxed">
            Every section, fact, and draft is validated against strict Pydantic schemas, ensuring 100% data integrity.
          </p>
        </div>
        
        <!-- Code snippet visual (STRICT SCHEMA V2) -->
        <div class="absolute right-8 top-1/2 -translate-y-1/2 bg-neutral-50 border border-brand-border p-6 rounded-3xl w-72 shadow-sm transform group-hover:scale-105 transition-transform duration-500">
          <div class="flex items-center gap-2 mb-4">
            <div class="w-2.5 h-2.5 rounded-full bg-green-500"></div>
            <span class="text-[10px] uppercase font-bold tracking-widest text-neutral-400">Strict Schema V2</span>
          </div>
          <pre class="text-[11px] font-mono text-neutral-400 leading-relaxed">
class Blog(BaseModel):
    title: str
    content: List[Section]
    status: str = "validated"</pre>
        </div>
      </div>

      <!-- Groq Card -->
      <div class="md:col-span-4 bento-card !bg-black p-12 text-white flex flex-col justify-between group overflow-hidden !shadow-hyper-premium border-none">
        <Cpu class="w-8 h-8 mb-10 text-brand-orange" />
        <div>
          <h3 class="text-3xl font-bold mb-4">Groq 70B Engine</h3>
          <p class="text-neutral-400 text-lg font-medium leading-relaxed">
            Ultra-fast inference rates powered by Llama 3.3 for near-instant intelligence handoffs.
          </p>
        </div>
      </div>

      <!-- Deep Research Card -->
      <div class="md:col-span-4 bento-card p-12 group flex flex-col justify-between">
        <Search class="w-8 h-8 mb-10 text-neutral-300" />
        <div>
          <h3 class="text-3xl font-bold mb-4">Deep Research</h3>
          <p class="text-neutral-500 text-lg font-medium leading-relaxed">
            Autonomous search across knowledge graphs to provide verified depth to every article.
          </p>
        </div>
      </div>

      <!-- Production Ready Card -->
      <div class="md:col-span-8 bento-card p-12 flex flex-col justify-between">
        <ShieldCheck class="w-8 h-8 mb-10 text-neutral-300" />
        <div>
          <h3 class="text-3xl font-bold mb-4">Production Ready</h3>
          <p class="text-neutral-500 text-lg font-medium leading-relaxed">
            Battle-tested agent logic ready for integration into high-scale content marketing workflows.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>
