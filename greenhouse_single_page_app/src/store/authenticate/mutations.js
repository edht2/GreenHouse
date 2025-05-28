

// In your mutations.js
export default {
    setGreenhouseUser(state, userData) {
      state.greenhouseUser = userData;
    },
    setAuthStatus(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
      console.log('setAuthStatus mutation called:', isAuthenticated); // Add this line
    },
    clearGreenhouseUser(state){
      state.greenhouseUser = null;
    }
  };