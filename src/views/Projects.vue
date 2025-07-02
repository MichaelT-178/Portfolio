<template>
  <div class="project-page">
    <p class="title">PROJECT PAGE</p>
    
    <div class="card-container">
      <ProjectCard 
        v-for="(project, index) in projectData" 
        :key="index"
        :title="project.title"
        :text="project.text"
        :image="project.image"
      />
    </div>
  </div>
</template>


<script setup>
import ProjectCard from '../components/ProjectCard.vue';
import data from '../assets/Data/ProjectData.json';

const projectData = data.projectData;

</script>


<style scoped>
.title {
  color: red;
  font-family: Arial, sans-serif;
  font-size: 2rem;
  text-align: center;
  margin: 2rem 0;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
}

</style>
