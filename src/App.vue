<template>
	<nav-bar />
	<router-view />
</template>


<script setup>
import NavBar from "../src/components/NavBar.vue";
</script>


<style>
html, body {
  margin: 0;
  padding: 0;
  background: gray;
}

.test-header {
	font-size: 25px;
}

</style>