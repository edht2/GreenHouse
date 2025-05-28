<template>
  <span>
    <button v-if="!link" :class="mode">
        <slot></slot>
    </button>
    <router-link v-else :to="to" :class="mode">
        <slot></slot>
    </router-link>
  </span>
</template>

<script>

export default {
    props: {
        mode: {
            type: String,
            required: false,
            default: null
        },
        link: {
            type: Boolean,
            required: false,
            default: false
        },
        to: {
            type: String,
            required: false,
            default: '/'
        }
    }
}
</script>

<style scoped>

button,
a {
  text-decoration: none;
  padding: 0.75rem 1.5rem;
  font: inherit;
  background-color: #74ad7d;
  border: 1px solid #74ad7d;
  color: white;
  cursor: pointer;
  border-radius: 30px;
  margin-right: 0.5rem;
  display: inline-block;
  display: flex; /* Change to flex */
  align-items: center; /* Vertically center the content */
  justify-content: center; /* Optionally, horizontally center as well */
}

a:hover,
a:active,
button:hover,
button:active {
  background-color: #5e8d65;
  border-color: #5e8d65;
}

.flat {
  background-color: transparent;
  color: #5e8d65;
  border: none;
}

.outline {
  background-color: transparent;
  border-color: #74ad7d;
  color: #74ad7d;
}

.flat:hover,
.flat:active,
.outline:hover,
.outline:active {
  background-color: #edd2ff;
}

</style>
