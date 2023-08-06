<template>
  <img alt="Vue logo" src="./assets/threeO.png">
  <UnderConstruction msg="Welcome in CV Creator"/>
</template>

<script>
import UnderConstruction from './components/UnderConstruction.vue'

export default {
  name: 'App',
  components: {
    UnderConstruction
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
