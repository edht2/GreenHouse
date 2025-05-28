import { createStore } from 'vuex';
import authModule from './authenticate/index.js';
import router from '../router'; // Import your router instance

const store = createStore({
    modules: {
        authenticate: authModule
    },
    state() {
        return {
            userId: 'c4'
        };
    },
    getters: {
        userId(state) {
            return state.userId;
        }
    },
    plugins: [
        (store) => {
            store.$router = router; // Attach the router to the store instance
        }
    ]
});

export default store;