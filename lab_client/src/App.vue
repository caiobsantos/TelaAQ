<template>
  <div>
    <div v-if="! $route.meta.hideNavbar" >
      <nav v-if="$route.meta.isLab">
        <router-link to="/aq/decomol">Decomol</router-link> |
        <router-link to="/aq/pulmao">Pulmão</router-link>
      </nav>
      <nav v-else>
        <router-link to="/fab/decomol">Decomol</router-link> |
        <router-link to="/fab/pulmao">Pulmão</router-link>
      </nav>
    </div>
    <router-view/>
  </div>
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
