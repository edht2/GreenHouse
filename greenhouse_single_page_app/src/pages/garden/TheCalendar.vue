<template>
    <div>
        <base-card>
        <h3><base-button><cal-icon iconwidth="20" class="icon"></cal-icon>Calendar</base-button></h3>
        </base-card>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  computed: {
    ...mapGetters('authenticate', [ // 'authenticate' is the first argument
      'greenhouseUser',
      'isLoggedIn',
      'firstName',
      'lastName',
      'roles',
    ]),
  },
  mounted() {
    console.log('Vuex Getters:');
    console.log('greenhouseUser:', this.greenhouseUser);
    console.log('isLoggedIn:', this.isLoggedIn);
    console.log('firstName:', this.firstName);
    console.log('lastName:', this.lastName);
    console.log('roles:', this.roles);

    //Or if you want to log the getters directly from the store:
    console.log("Directly from store.getters:")
    console.log('greenhouseUser:', this.$store.getters['authenticate/greenhouseUser']);
    console.log('isLoggedIn:', this.$store.getters['authenticate/isLoggedIn']);
    console.log('firstName:', this.$store.getters['authenticate/firstName']);
    console.log('lastName:', this.$store.getters['authenticate/lastName']);
    console.log('roles:', this.$store.getters['authenticate/roles']);

  },
};
</script>

<style scoped>
.icon {
  margin-right: 10px;
}
</style>