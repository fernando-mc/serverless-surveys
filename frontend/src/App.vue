<template>

  <div id="app">
    <PageHeader/>
    <div class="ui container main-box">
    </div>
    <router-link to="/home">Home</router-link>
    <router-link to="/surveys">Surveys</router-link>
    <div id="nav">
      <router-link to="/">Home</router-link>|
      <router-link to="/about">About</router-link>|

      <!-- NEW - add a route to the profile page -->
      <router-link v-if="$auth.isAuthenticated" to="/profile">Profile</router-link>
    </div>
    
    <router-view />
  </div>
</template>

<script>
import PageHeader from './components/PageHeader.vue'

export default {  
  name: 'App',
  components: {
    PageHeader, 
  },
}
</script>

<style>
  .card {
    margin-top: auto;
  }
  body {
    background-color: rgb(164, 199, 230);
  }
  .main-box {
    margin-top: 6rem;
  }
  body>.container {
    padding: 24px;
    background-color: rgb(164, 199, 230);
  }
  .hits-box {
    padding: 1px 14px 12px;
  }

body {    
    padding: 1em;
  }
  
  .ui.action.input input[type="file"] {
    display: none;
  }
  
  .ui.top.fixed {
    background: rgb(225, 212, 168);
  }

  .ui.horizontal.divider {
    color: rgb(225, 212, 168);
  }
</style>
