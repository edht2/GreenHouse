import { createRouter, createWebHistory } from 'vue-router';
import store from './store/index.js'; // Import your Vuex store

import TheLogin from './pages/authenticate/TheLogin.vue';
console.log('TheLogin:', TheLogin);
import TheRegister from './pages/authenticate/TheRegister.vue';
import TheCalendar from './pages/garden/TheCalendar.vue';
import TheLocations from './pages/garden/TheLocations.vue';
import ToDoList from './pages/garden/ToDoList.vue';
import ActuatorTest from './pages/greenhouse/ActuatorTest.vue';
import GhSummary from './pages/greenhouse/GhSummary.vue';
import GhDrillDown from './pages/greenhouse/GhDrillDown.vue';
import SensorStatus from './pages/greenhouse/SensorStatus.vue';
import HomePage from './pages/HomePage.vue';
import NotFound from './pages/NotFound.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: HomePage },
        {
            path: '/greenhouse',
            component: GhSummary,
            beforeEnter: async (to, from, next) => { // Make it async
                await store.dispatch('authenticate/loadUserFromToken');
                if (store.getters['authenticate/isLoggedIn']) {
                    next();
                } else {
                    next('/login');
                }
            },
        },
        {
            path: '/greenhouse/drilldown/:dataLabel',
            name: 'drilldownDetail',
            component: GhDrillDown,
            props: true,
            beforeEnter: async (to, from, next) => { // Make it async
                await store.dispatch('authenticate/loadUserFromToken');
                if (store.getters['authenticate/isLoggedIn']) {
                    next();
                } else {
                    next('/login');
                }
            },
        },
        { path: '/register', component: TheRegister },
        { path: '/login', component: TheLogin },
        {
            path: '/calendar',
            component: TheCalendar,
            beforeEnter: async (to, from, next) => { // Make it async
                await store.dispatch('authenticate/loadUserFromToken');
                if (store.getters['authenticate/isLoggedIn']) {
                    next();
                } else {
                    next('/login');
                }
            },
        },
        {
            path: '/locations',
            component: TheLocations,
            beforeEnter: async (to, from, next) => { // Make it async
                await store.dispatch('authenticate/loadUserFromToken');
                if (store.getters['authenticate/isLoggedIn']) {
                    next();
                } else {
                    next('/login');
                }
            },
        },
        {
            path: '/todo',
            component: ToDoList,
            beforeEnter: async (to, from, next) => { // Make it async
                await store.dispatch('authenticate/loadUserFromToken');
                if (store.getters['authenticate/isLoggedIn']) {
                    next();
                } else {
                    next('/login');
                }
            },
        },
        {
            path: '/sensorstatus',
            component: SensorStatus,
            beforeEnter: async (to, from, next) => { // Make it async
                await store.dispatch('authenticate/loadUserFromToken');
                if (store.getters['authenticate/isLoggedIn']) {
                    next();
                } else {
                    next('/login');
                }
            },
        },
        {
            path: '/actuatortest',
            component: ActuatorTest,
            beforeEnter: async (to, from, next) => { // Make it async
                await store.dispatch('authenticate/loadUserFromToken');
                if (store.getters['authenticate/isLoggedIn']) {
                    next();
                } else {
                    next('/login');
                }
            },
        },
        { path: '/:notFound(.*)', component: NotFound },
    ],
});

export default router;