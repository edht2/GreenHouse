export default {
    greenhouseUser(state) {
        return state.greenhouseUser;
    },
    isLoggedIn(state) {
        return !!state.greenhouseUser; // Returns true if greenhouseUser is not null/undefined
    },
    firstName(state) {
        return state.greenhouseUser ? state.greenhouseUser.firstName : null;
    },
    lastName(state) {
        return state.greenhouseUser ? state.greenhouseUser.lastName : null;
    },
    roles(state) {
        return state.greenhouseUser ? state.greenhouseUser.role : [];
    },
};