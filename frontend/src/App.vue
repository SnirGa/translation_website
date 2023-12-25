<template>
  <div id="app">
    <SearchComp/>
  </div>
</template>

<script>
import SearchComp from './components/Searcher.vue'

export default {
  name: 'App',
  components: {
    SearchComp
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
