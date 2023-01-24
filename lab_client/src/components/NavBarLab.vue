<template>
    <nav>
        <router-link to="/aq/decomol">Decomol </router-link> |
        <router-link to="/aq/pulmao">Pulmão</router-link>
    </nav>
</template>

<script>
    export default{
        name: 'NavBarLab'
    }
</script>

<style>
    nav {
  display: flex;
  padding: 15px;
  height: 10vh;
  border-bottom: 3px white solid;
  justify-content: center;
  align-items: center;
  background-color: #282A35;
  gap: 5px;
  color: white;
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

nav a.router-link-active {
  color: lightgreen;
}
</style>