<template>
  <div>
    <div v-if="! $route.meta.hideNavbar" >
      <nav v-if="$route.meta.isLab">
        <router-link to="/aq/decomol">Decomol </router-link> |
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
  color: white;
  min-height: 100vh;
  background-color: lightgray;
}

nav {
  display: flex;
  padding: 15px;
  height: 60px;
  border-bottom: 3px white solid;
  justify-content: center;
  align-items: center;
  background-color: #282A35;
  gap: 5px;
}

nav a {
  font-weight: bold;
  color: white;
  border: 1px solid transparent;
}

nav a:hover{
  color: white;
  border-bottom: 1px solid darkgray;
  transition-delay: 50ms;
}

nav a.router-link-exact-active {
  color: lightgreen;
}
</style>
