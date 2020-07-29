<template>
  <div id="app">
    <PageHeader/>
    <div class="ui container main-box">
    </div>
    <router-link to="/home">Home</router-link>
    <router-link to="/surveys">Surveys</router-link>
    <router-view></router-view>
  </div>
</template>