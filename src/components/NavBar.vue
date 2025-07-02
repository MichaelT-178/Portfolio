<template>
  <div>
    <div class="top-bar">
      <div class="top-bar-inner">

        <!-- Livestream directory and CH logo -->
        <router-link to="/" custom v-slot="{ navigate, href }">
          <div
            class="home-router-btn"
            :href="href"
            @click="navigate"
          >
            <h1 class="site-title">Personal Portfolio</h1>
          </div>
        </router-link>
        
        <div class="nav-links desktop-only">
          <div class="nav-items">
            <router-link to="/experience">Experience</router-link>
            <router-link to="/projects">Projects</router-link>
            <router-link to="/skills">Skills</router-link>
            <router-link to="/contact">Contact</router-link>
          </div>
        </div>

        <!-- Hamburger menu icon for mobile -->
        <div class="mobile-only">
          <font-awesome-icon
            icon="bars"
            @click="toggleMobileMenu"
            class="hamburger-icon"
          />
        </div>
      </div>
    </div>

    <!-- Mobile menu -->
    <div v-if="isMobileMenuOpen" class="mobile-menu">
      <router-link 
        to="/" 
        @click="closeMobileMenu"
      >Home</router-link>
      <router-link to="/experience">Experience</router-link>
      <router-link to="/projects">Projects</router-link>
      <router-link to="/skills">Skills</router-link>
      <router-link to="/contact">Contact</router-link>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const isMobileMenuOpen = ref(false);


const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};

const handleResize = () => {
  if (window.innerWidth >= 750) {
    isMobileMenuOpen.value = false;
  }
};

const closeMobileMenu = () => {
  isMobileMenuOpen.value = false;
};

onMounted(() => {
  window.addEventListener('resize', handleResize);
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', handleResize);
});

</script>


<style scoped>
.top-bar {
  width: 100%;
  border-bottom: 0.5px solid #cbd5e1;
  background-color: transparent;
}

.top-bar-inner {
  margin: 0 auto;
  padding: 16.5px 42px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: white;
}

.home-router-btn {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.ch-logo {
  display: none;
  width: 40px;
  height: 40px;
  object-fit: contain;
  border-radius: 4px;
}

.ch-logo:hover {
  opacity: 0.7;
}

.site-title {
  font-size: 23px;
  margin: 0;
  white-space: nowrap;
}

.site-title:hover {
  color: #cbd5e1;
}

.dark .nav-links a {
  color: #60A5FA;
}

.dark .toggle-btn {
  /* color: #cbd5e1; */
  color: #60A5FA;
}

.dark .top-bar {
  width: 100%;
  border-bottom: 0.5px solid #cbd5e1;
  background-color: transparent;
}

.dark .site-title {
  color: #60A5FA;
}

.dark .site-title:hover {
  color: purple;
}

.dark .hamburger-icon {
  color: #cbd5e1;
}

.dark .mobile-menu {
  background-color: #eef5fd;
  color: red;
}

.dark .mobile-menu a {
  color: #60A5FA;
}

.nav-links a,
.mobile-menu a {
  color: #cbd5e1;
  text-decoration: none;
  margin-left: 20px;
  font-weight: bold;
  font-size: 18.5px;
}

.nav-links a:hover,
.mobile-menu a:hover {
  text-decoration: underline;
}

.mobile-menu {
  display: flex;
  flex-direction: column;
  padding: 20px;
  background-color: #1f2937;
}

.mobile-menu a {
  margin: 10px 0;
}

.desktop-only {
  display: flex;
}

.mobile-only {
  display: none;
}

.hamburger-icon {
  font-size: 24px;
  cursor: pointer;
}


@media (max-width: 750px) {
  .top-bar-inner {
    padding: 17px 17px;
  }

  .mobile-only {
    display: flex;
  }

  .desktop-only {
    display: none;
  }
}

@media (max-width: 600px) {
  .ch-logo {
    display: block;
  }

  .site-title {
    display: none;
  }

  .top-bar-inner {
    padding: 11px 25px;
  }
}

</style>