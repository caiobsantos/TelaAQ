<template>
    <div class="home-container">
        <nav>
            <router-link to="/aq/decomol">AQ</router-link> |
            <router-link to="/fab/decomol">Fab</router-link>
        </nav>
        <div class="content">
            
        </div>
    </div>
</template>

<script>
    export default{
        name: 'HomeView',
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

    .home-container { 
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        background-color: lightgray;
        color: black;
    }

    .content{
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        color: black;   
        min-height: 90vh;
    } 
</style>