import { createApp } from 'vue'
import router from './router.js';
import App from './App.vue';
import store from './store/index.js'



import BaseCard from './components/UI/BaseCard.vue';
import BaseButton from './components/UI/BaseButton.vue';
import BaseBadge from './components/UI/BaseBadge.vue';

import GrHsIcon from './components/UI/icons/GrHsIcon.vue';
import ActIcon from './components/UI/icons/ActIcon.vue';
import LeafIcon from './components/UI/icons/LeafIcon.vue';
import SensorIcon from './components/UI/icons/SensorIcon.vue';
import ToDoIcon from './components/UI/icons/ToDoIcon.vue';
import CalIcon from './components/UI/icons/CalIcon.vue';
import SetIcon from './components/UI/icons/setIcon.vue';

const app = createApp(App);

app.component('base-card',BaseCard);
app.component('base-button',BaseButton);
app.component('base-badge',BaseBadge);

app.component('cal-icon', CalIcon);
app.component('gr-hs-icon', GrHsIcon);
app.component('act-icon', ActIcon);
app.component('leaf-icon', LeafIcon);
app.component('sensor-icon', SensorIcon);
app.component('to-do-icon', ToDoIcon);
app.component('set-icon', SetIcon);

app.use(router);
app.use(store);

router.isReady().then(async () => { // Make the callback async
    console.log('router.isReady().then() callback is executing!');
    console.log('About to dispatch authenticate/loadUserFromToken...');
    await store.dispatch('authenticate/loadUserFromToken'); // Await the dispatch
    console.log('loadUserFromToken completed.');
    app.mount('#app');
    console.log('App mounted.');
});
