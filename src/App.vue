<template>
  <EasyForm />
</template>

<script>
import EasyForm from './components/EasyForm.vue'

export default {
  name: 'App',
  components: {
    EasyForm
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

html {
  background-image: linear-gradient(180deg, #26a0da, #314755);
  background-repeat: no-repeat;
  background-size: cover;
  height: 100%;
}
</style>
