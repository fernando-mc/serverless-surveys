<template>
  <div v-if="!$auth.loading" class="ui top fixed horizontal menu">
    <div class="item">
      <h2>The Survey Union</h2>
    </div>
    <!-- Check that the SDK client is not currently loading before accessing is methods -->
    <div v-if="!$auth.loading">
      <router-link to="/home" class="ui primary button">Home</router-link>
      <router-link to="/create-survey" class="ui primary button"  > Create Survey</router-link>
      <router-link v-if="$auth.isAuthenticated" to="/profile" class="ui primary button" >Profile</router-link>
      <button @click="login()" v-if="!$auth.isAuthenticated" class="ui primary button">Login</button>
      <button @click="logout()" v-if="$auth.isAuthenticated" class="ui primary button">Logout</button>
      <div id="avatar-img-div" v-show="profileImageVisibility">
        <img :src="profileUrl" class="ui avatar image"/>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PageHeader',
  methods: {
    login() {
      this.$auth.loginWithRedirect();
    },
    logout() {
      this.$auth.logout({
        returnTo: window.location.origin
      });
    },
  },
  data () {
    return {
      profileImageVisibility: false,
      profileUrl: '',
    }
  }
}
</script>

<style scoped>
.ui.top.fixed {
  background: rgb(225, 212, 168);
  margin-bottom: 100px;
}

.ui.modal {
  top: 10%;
}

.close.icon {
  color: black;
  top: 0;
  right: 0;
}

.hidden {
  display: none;
}

label {
  margin-bottom: 10px;
  display: block;
}

body {
  background: #1B1C1D;
}


</style>
