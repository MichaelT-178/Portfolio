<template>
  <div class="card">
    <img 
      :src="imagePath" 
      alt="Image" 
      class="card-image"
    />
    <h2 class="card-title">{{ title }}</h2>
    <p class="card-text">{{ text }}</p>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  text: {
    type: String,
    required: true
  },
  image: {
    type: String,
    required: true
  },
});

const imagePath = computed(() => {
  return new URL(`../assets/ProjectPics/${props.image}`, import.meta.url).href;
});

</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 1rem;
  text-align: center;
  max-width: 300px;
  background-color: white;
}

.card-image {
  width: 100%;
  height: auto;
  border-radius: 10px;
}

.card-title {
  font-size: 1.2rem;
  margin-top: 0.5rem;
}

.card-text {
  font-size: 1rem;
  margin: 0.5rem 0;
}

.button {
  display: inline-block;
  margin-top: 0.5rem;
  background-color: #007bff;
  color: white;
  padding: 0.5rem 1rem;
  text-decoration: none;
  border-radius: 5px;
}
</style>
