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
  <section class="py-24 px-4 max-w-5xl mx-auto text-center">
    <h2 class="text-4xl md:text-6xl font-black mb-6 tracking-tight">Workspace.</h2>
    <p class="text-lg text-brand-gray mb-16 font-medium tracking-tight">Initialize the swarm with your directive.</p>

    <div class="relative max-w-3xl mx-auto group" id="workspace-anchor">
      <input 
        :value="modelValue"
        @input="onInput"
        @keyup.enter="$emit('submit')"
        class="w-full h-20 pl-10 pr-52 rounded-full bg-white border border-brand-border shadow-[0_15px_40px_-10px_rgba(0,0,0,0.08)] focus:outline-none focus:ring-4 focus:ring-black/5 text-lg font-medium placeholder:text-neutral-300 transition-all"
        placeholder="The Role of AI in Cybersecurity: Opportunities and Risks"
      />
      <div class="absolute right-2 top-2 bottom-2">
        <button 
          @click="$emit('submit')"
          :disabled="loading"
          class="h-full bg-black text-white px-8 rounded-full flex items-center gap-3 font-bold hover:bg-neutral-800 disabled:opacity-50 transition-all active:scale-95 shadow-lg group"
        >
          <Send v-if="!loading" class="w-5 h-5 group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" />
          <span v-if="!loading">Initialize Swarm</span>
          <span v-else class="animate-pulse">Deploying...</span>
        </button>
      </div>
    </div>
  </section>
</template>
