<script setup lang="ts">
import { Send } from 'lucide-vue-next';
import { ref } from 'vue';

const props = defineProps<{
  modelValue: string;
  loading: boolean;
}>();

const emit = defineEmits(['update:modelValue', 'submit']);

const onInput = (e: Event) => {
  emit('update:modelValue', (e.target as HTMLInputElement).value);
};
</script>

<template>
  <section id="workspace" class="py-24 px-4 max-w-5xl mx-auto text-center">
    <div class="scroll-reveal mb-16">
      <h2 class="text-4xl md:text-6xl font-black tracking-tighter text-black mb-4">Workspace.</h2>
      <p class="text-black/40 font-bold text-base">Initialize the swarm with your directive.</p>
    </div>

    <div
      id="workspace-anchor"
      class="scroll-reveal relative max-w-3xl mx-auto group px-2 md:px-0"
    >
      <div class="flex flex-col md:flex-row items-center bg-white border-2 border-black/15 rounded-[2rem] md:rounded-full shadow-[0_0_0_4px_rgba(0,0,0,0.03),0_20px_60px_-10px_rgba(0,0,0,0.12)] transition-all duration-300 focus-within:border-black focus-within:shadow-[0_0_0_4px_rgba(0,0,0,0.06),0_20px_60px_-10px_rgba(0,0,0,0.18)] overflow-hidden">
        <input
          :value="modelValue"
          @input="onInput"
          @keyup.enter="$emit('submit')"
          class="w-full md:flex-1 h-16 md:h-20 px-8 bg-transparent border-none focus:outline-none text-base font-medium placeholder:text-black/20 text-black text-center md:text-left"
          placeholder="The Role of AI in Cybersecurity: Opportunities and Risks"
          :disabled="loading"
        />
        <div class="w-full md:w-auto p-2 md:p-3 md:pr-3">
          <button
            @click="$emit('submit')"
            :disabled="loading"
            class="w-full md:w-auto group/btn relative overflow-hidden h-12 md:h-14 bg-black text-white px-8 rounded-full flex items-center justify-center gap-3 font-bold text-sm hover:bg-neutral-800 disabled:opacity-40 transition-all active:scale-95 shadow-lg"
          >
            <span class="absolute inset-0 bg-brand-orange scale-x-0 origin-left group-hover/btn:scale-x-100 transition-transform duration-300 rounded-full"></span>
            <Send v-if="!loading" class="w-4 h-4 relative z-10 group-hover/btn:translate-x-0.5 group-hover/btn:-translate-y-0.5 transition-transform duration-300" />
            <span class="relative z-10">{{ loading ? 'Deploying...' : 'Generate Blog' }}</span>
          </button>
        </div>
      </div>
    </div>
  </section>
</template>
