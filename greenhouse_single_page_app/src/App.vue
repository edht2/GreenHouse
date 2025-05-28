<template>
<div id="app">
  <header>
    <the-nav-bar></the-nav-bar>
  </header>
  <router-view></router-view>
</div>
</template>

<script>
import TheNavBar from './components/layout/TheNavBar.vue';

export default {
  name: 'app',
  components: {
    TheNavBar
  }
}
</script>

<style>

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  }

  body {
    font-family: 'montserrat', sans-serif;
  }

header {
  width: 100vw;
  background-color: #74ad7d;
  padding: 5px
}
</style>
