<template>
    <div class="login-container">
      <div class="login-form">
        <h2>Login</h2>
        <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
        <form @submit.prevent="handleLogin">
          <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="loginForm.email" required />
          </div>
          <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="loginForm.password" required />
          </div>
          <button type="submit" :disabled="loading">
            <span v-if="loading">Loading...</span>
            <span v-else>Login</span>
          </button>
        </form>
        <p>
          Don't have an account? <router-link to="/register">Register</router-link>
        </p>
      </div>
    </div>
  </template>
  
  <script>
  import { mapActions } from 'vuex';

  
  export default {
    data() {
      return {
        loginForm: {
          email: '',
          password: '',
        },
        errorMessage: '',
        loading: false,
      };
    },
    methods: {
      ...mapActions('authenticate', ['loginUser']),
      async handleLogin() {
        this.loading = true;
        this.errorMessage = ''; // Clear previous errors
        try {
          const response = await fetch('http://192.168.1.228:5000/login', { //ensure this is the correct address.
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.loginForm),
            credentials: 'include', // Crucial line for sending cookies
          });
  
          const data = await response.json();
  
          if (response.ok) {
            const userData = {
              firstName: data.first_name,
              lastName: data.last_name,
              role: data.role,
            };
            this.loginUser(userData);
            this.$router.push('/greenhouse');
          } else {
            this.errorMessage = data.message || 'Login failed. Please check your credentials.';
          }
        } catch (error) {
          this.errorMessage = 'Network error. Please try again laterzz.';
          console.error('Login error:', error);
        } finally {
          this.loading = false;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f4f4f4;
  }
  
  .login-form {
    width: 300px;
    padding: 20px;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  
  .error-message {
    color: red;
    margin-bottom: 10px;
  }
  
  p {
    text-align: center;
    margin-top: 15px;
  }
  </style>