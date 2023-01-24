<template>
    <router-view/>
</template>

<script>
  export default{
    name: 'App',
    data (){
      return {
        nome: this.$route.params.name
      }
    }
  }
</script>

<style>
</style>
