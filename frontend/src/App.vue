<template>
  <div id="app">
    <PageHeader/>
    <div class="ui container main-box">
    </div>
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
