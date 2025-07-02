import { createRouter, createWebHistory } from 'vue-router';

import Home from '../views/Home.vue';
import ExperiencePage from '../views/Experience.vue';
import ProjectPage from '../views/Projects.vue';
import SkillPage from '../views/skills.vue';
import ContactPage from '../views/Contact.vue';

const routes = [
	{
		path: '/',
		component: Home
	},
	{
		path: '/experience',
		component: ExperiencePage
	},
	{
		path: '/projects',
		component: ProjectPage
	},
	{
		path: '/skills',
		component: SkillPage
	},
	{
		path: '/contact',
		component: ContactPage
	},
]

const router = createRouter({
	history: createWebHistory('/'),
	routes
});

export default router;