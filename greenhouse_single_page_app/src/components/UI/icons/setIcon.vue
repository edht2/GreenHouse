<template>
    <span>
        <svg viewBox="0 0 122.88 92.62" :width="iconwidth" class="menu-icon">
            <path class="st0" d="M36.91,0h5.78A4.93,4.93,0,0,1,47.6,4.91v5.35A30.73,30.73,0,0,1,55,13.59l4-4a4.93,4.93,0,0,1,7,0L70,13.7a4.92,4.92,0,0,1,0,6.94l-4.27,4.28A30.49,30.49,0,0,1,68.52,32h6.16a4.93,4.93,0,0,1,4.92,4.91v5.78a4.93,4.93,0,0,1-4.92,4.91H68.46a30.38,30.38,0,0,1-2.83,7L70,59a4.93,4.93,0,0,1,0,7L65.9,70a4.93,4.93,0,0,1-7,0l-4.11-4.11a30.48,30.48,0,0,1-7.24,3.25v5.56a4.93,4.93,0,0,1-4.91,4.92H36.91A4.93,4.93,0,0,1,32,74.68v-5a30.61,30.61,0,0,1-8-3L20.64,70a4.92,4.92,0,0,1-6.94,0L9.61,65.9a4.93,4.93,0,0,1,0-7l3.06-3.06A30.67,30.67,0,0,1,9.08,47.6H4.91A4.93,4.93,0,0,1,0,42.69V36.91A4.93,4.93,0,0,1,4.91,32H9a30.74,30.74,0,0,1,3.57-8.38l-3-3a4.92,4.92,0,0,1,0-6.94L13.7,9.61a4.92,4.92,0,0,1,6.94,0l3.22,3.22A30.55,30.55,0,0,1,32,9.72V4.91A4.93,4.93,0,0,1,36.91,0ZM94.2,47.52l3.27-.61a2.83,2.83,0,0,1,3.29,2.27l.56,3a17.77,17.77,0,0,1,4.53,1.11l1.83-2.67a2.84,2.84,0,0,1,3.93-.73l2.74,1.89a2.84,2.84,0,0,1,.73,3.93l-2,2.87a17.07,17.07,0,0,1,2.33,3.71l3.49-.65a2.85,2.85,0,0,1,3.3,2.27l.6,3.27a2.82,2.82,0,0,1-2.26,3.29l-3.53.66a17.51,17.51,0,0,1-.86,4.26l2.91,2a2.84,2.84,0,0,1,.73,3.94l-1.88,2.74a2.83,2.83,0,0,1-3.93.72l-2.76-1.89a17.72,17.72,0,0,1-3.76,2.6l.58,3.15A2.84,2.84,0,0,1,105.81,92l-3.27.61a2.85,2.85,0,0,1-3.3-2.27l-.52-2.85a17.46,17.46,0,0,1-4.85-.87l-1.55,2.25a2.84,2.84,0,0,1-3.93.73l-2.74-1.89a2.84,2.84,0,0,1-.73-3.93l1.41-2a17.77,17.77,0,0,1-2.9-4.32l-2.36.43a2.82,2.82,0,0,1-3.29-2.26l-.61-3.27A2.83,2.83,0,0,1,79.44,69l2.32-.44a17.66,17.66,0,0,1,1.15-5.11l-2-1.37a2.85,2.85,0,0,1-.73-3.94l1.89-2.74A2.83,2.83,0,0,1,86,54.67l2.15,1.48a17.46,17.46,0,0,1,4.29-2.61l-.51-2.73a2.84,2.84,0,0,1,2.27-3.29Zm4.25,13.82a8.55,8.55,0,1,1-6.85,10,8.55,8.55,0,0,1,6.85-10ZM39.8,25A14.85,14.85,0,1,1,25,39.8,14.84,14.84,0,0,1,39.8,25Z" fill="#FFF"></path>
        </svg>
    </span>
</template>

<script>

export default {
  props: ['iconwidth'],
  computed: {
    logIconWidth() {
      return typeof this.iconwidth; // You can also return the value if you need to use it in the template later
    }
  },
  mounted() {
    console.log('Type of iconwidth:', this.logIconWidth);
    console.log('value of iconwidth: ', this.iconwidth);
  }
}
</script>


<style scoped>
svg {
    margin-right: 5px;
  };
</style>
