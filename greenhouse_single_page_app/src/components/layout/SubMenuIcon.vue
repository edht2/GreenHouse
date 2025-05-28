<template>
    <span>
        <!-- login -->

        <leaf-icon v-if="id === 3" :iconwidth="iconwidth"></leaf-icon>
        <!-- sensor -->
        <sensor-icon v-else-if="id === 1" :iconwidth="iconwidth"></sensor-icon>
        <!-- actuator -->
        <act-icon v-else-if="id === 2" :iconwidth="iconwidth"></act-icon>

    </span>
</template>

<script>


export default {



    props: ['id','iconwidth'],
    mounted() {
        console.log('id', this.id);
        console.log('iconwidth', this.iconwidth);
    }
}


</script>

