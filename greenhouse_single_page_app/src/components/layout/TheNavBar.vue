<template>
    <nav>
           <div class="menu-item">
            <router-link to="/greenhouse">
                <gr-hs-icon iconwidth="15"></gr-hs-icon>
                Greenhouse
            </router-link>
        </div>
        <div class="menu-item">
            <router-link to="/todo">
                <to-do-icon iconwidth="13"></to-do-icon>
                ToDo
            </router-link>
        </div>
        <div class="menu-item">
            <router-link to="/calendar">
                <cal-icon :items="updatedServices" iconwidth="13"></cal-icon>
                Calendar
            </router-link>
        </div>
        

        <the-drop-down title="Settings" :items="updatedServices"></the-drop-down>
    </nav>
</template>

<script>
import TheDropDown from './TheDropDown.vue';
import { useStore } from 'vuex';
import router from '@/router';


export default {
    name: 'TheNavBar',
    components: {
        TheDropDown
    },
    setup() {
        const store = useStore();


        const handleLogout = () => {
            console.log('handleLogout called');
            console.log('About to dispatch logoutUser action...');
            store.dispatch('authenticate/logoutUser', router);
            console.log('logoutUser action dispatched.');
        };

        const services = [
            {
                id: 1,
                title: 'Sensor Status',
                link: '/sensorstatus',
                width: 12
            },
            {
                id: 2,
                title: 'Actuator Test',
                link: '/actuatortest',
                width: 12
            },
            {
                id: 3,
                title: 'LogOut',
                handler: handleLogout, // Add a handler function instead of a link
                width: 11
            },
        ];

        return {
            updatedServices: services, // Pass the modified services to the dropdown
        };
    }
}

</script>

<style>

nav {
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 20;
}

nav .menu-item {
    color: #fff;
    padding: 10px 6px;
    position: relative;
    text-align: left;
    border-bottom: 3px solid transparent;
    display: flex;
    align-items: center;
    transition: 0.4s;
    font-size: 0.9em;
}

nav .menu-item.active,
nav .menu-item:hover {
    background-color: #5e8d65;
    border-bottom-color: #cce6d0;
}

nav .menu-item a {
    color: inherit;
    text-decoration: none;
    display: flex;
    align-items: center;
    margin-left: 3px; /* Add margin-left to the anchor tag */
}

nav .menu-item a gr-hs-icon,
nav .menu-item a to-do-icon,
nav .menu-item a cal-icon {
    vertical-align: middle;
    margin-right: 8px;
}
</style>
