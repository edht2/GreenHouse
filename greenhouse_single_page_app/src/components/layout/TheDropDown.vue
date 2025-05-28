<template>
    <div class="menu-item" @click="isOpen = !isOpen">
        <set-icon class="icon" iconwidth="17"></set-icon>
        <a href="#">
            {{ title }}
        </a>

        <transition name="slide-down">
            <div class="sub-menu" v-if="isOpen">
                <div v-for="(item, i) in items" :key="i" class="menu-item" >
                    <template v-if="item.link">
                        <router-link :to="item.link">
                            <sub-menu-icon
                            :id="item.id"
                            :iconwidth="item.width"
                            >
                            </sub-menu-icon>
                            {{ item.title }}
                        </router-link>
                    </template>
                    <template v-else-if="item.handler">
                        <button @click="item.handler" class="logout-button">
                            <sub-menu-icon
                            :id="item.id"
                            :iconwidth="item.width"
                            >
                            </sub-menu-icon>
                            {{ item.title }}
                        </button>
                    </template>
                    <template v-else>
                        <div class="non-link-item">
                            <sub-menu-icon
                            :id="item.id"
                            :iconwidth="item.width"
                            >
                            </sub-menu-icon>
                            {{ item.title }}
                        </div>
                    </template>
                </div>
            </div>
        </transition>

    </div>
</template>

<script>

import SubMenuIcon from './SubMenuIcon.vue';
export default {
    components: {SubMenuIcon},
    name: 'TheDropDown',
    props: ['title', 'items', 'id'],
    data() {
        return {
            isOpen: false
        }
    }
}
</script>

<style scoped>


.sub-menu {
    position: absolute;
    background-color: #74ad7d;
    top: calc(100% + 1px);
    left: 0;
    margin-left: 46px;
    transform: translateX(-50%);
    width: max-content;
    border-radius: 0px 0px 5px 5px;
    z-index: 10; /* Ensure it appears above other elements */
}

/* Transition styles */
.slide-down-enter-from {
    opacity: 0;
    transform: translateX(-50%) translateY(-40px);
}

.slide-down-enter-active {
    transition: opacity 0.3s ease-in-out, transform 0.3s ease-in-out;
}

.slide-down-enter-to {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
}

.slide-down-leave-from {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
}

.slide-down-leave-active {
    transition: opacity 0.3s ease-in-out, transform 0.3s ease-in-out;
    position: absolute; /* Important for smooth leaving transitions sometimes */
}

.slide-down-leave-to {
    opacity: 0;
    transform: translateX(-50%) translateY(-50px);
}
.sub-menu-icon {
    width: 20px; /* Or any size you prefer */
    height: auto; /* Maintain aspect ratio */
    margin-right: 5px; /* Add some spacing between the icon and text */
    vertical-align: middle; /* Align vertically with the text */
}

.sub-menu .menu-item a,
.sub-menu .menu-item .non-link-item,
.sub-menu .menu-item .logout-button {
    display: flex;
    align-items: center;
    padding: 8px 16px;
    text-decoration: none;
    color: #fff; /* Set the text color to white */
    width: 100%;
    text-align: left;
}

.logout-button {
    background: none;
    border: none;
    cursor: pointer;
    font-size: inherit;
}

.logout-button:focus {
    outline: none; /* Remove default focus outline */
}

.logout-button sub-menu-icon {
    margin-right: 5px;
}

.sub-menu .menu-item a:hover,
.sub-menu .menu-item .non-link-item:hover,
.sub-menu .menu-item .logout-button:hover {
    background-color: #5e8d65; /* Match the hover color of the router-links */
}
</style>