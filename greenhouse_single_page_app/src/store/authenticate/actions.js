import Cookies from 'js-cookie';

export default {
    loginUser({ commit }, userData) {
        commit('setGreenhouseUser', userData);
        console.log('User data stored in Vuex after login:', userData);
        console.log('First Name:', userData.first_name);
        console.log('Last Name:', userData.last_name);
        console.log('Role:', userData.role);
    },
    async logoutUser({ commit }, router) { // Receive the router instance as the second argument
        try {
            const response = await fetch('http://192.168.1.228:5000/logout', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
            });
    
            if (response.ok) {
                console.log('Logout successful on the server (optional)');
            } else {
                console.error('Error during server-side logout (optional)');
            }
        } catch (error) {
            console.error('Error during logout API call:', error);
        } finally {
            console.log('logoutUser: About to remove jwt_token cookie');
            Cookies.remove('jwt_token', { path: '/' });
            console.log('logoutUser: jwt_token cookie removed');
            console.log('logoutUser: About to remove csrf_access_token cookie');
            Cookies.remove('csrf_access_token', { path: '/' });
            console.log('logoutUser: csrf_access_token cookie removed');
            commit('clearGreenhouseUser');
            router.push('/login');
        }
    },
    async loadUserFromToken({ commit }) {
        try {
          const csrfToken = Cookies.get('csrf_access_token'); // Get the CSRF token cookie
          console.log('csrf token' , csrfToken)
      
          const response = await fetch('http://192.168.1.228:5000/verify-token', {
            method: 'POST',
            credentials: 'include', // To send the httpOnly jwt_token cookie
            headers: {
              'Content-Type': 'application/json',
              'X-CSRF-TOKEN': csrfToken, // Include the CSRF token in the header
            },
            // No body needed for this verification request
          });
      
          if (!response.ok) {
            console.error(`Token verification failed with status: ${response.status}`);
            commit('setGreenhouseUser', null);
            commit('setAuthStatus', false);
            return;
          }
      
          const data = await response.json();
          
          commit('setGreenhouseUser', {
            firstName: data.firstName,
            lastName: data.lastName,
            role: data.role,
          });
          console.log('greenhouse user is being set... ', data.firstName, data.lastName, data.role);
          commit('setAuthStatus', true);
          
        } catch (error) {
          console.error('Error verifying token:', error);
          commit('setGreenhouseUser', null);
          commit('setAuthStatus', false);
        }
      },
};
