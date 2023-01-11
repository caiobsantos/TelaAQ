<template>
  <nav>
    <button @click="selDecomol()">Decomol</button> |
    <button @click="selPulmao()">Pulmão</button>
  </nav>
  <component v-bind:is="component"></component>
</template>

<script>
  import AQPulmaoView from './components/Pulmao.vue'
  import AQDecomolView from './components/Decomol.vue'
  import axios from 'axios'
  import moment from 'moment'

  export default{
    name: 'App',
    
    components: {
      AQDecomolView,
      AQPulmaoView
    },

    data (){
      return {
        component: 'AQDecomolView',
        decomol1: [],
        decomol2: [],
        decomol3: [],
    }
  },
    created() {
      this.getDecomol1()
      this.getDecomol2()
      this.getDecomol3()
        },
        methods: {
          selDecomol(){
            this.component = 'AQDecomolView'
          },

          selPulmao(){
            this.component='AQPulmaoView'
          },

          getDecomol1() {
              axios({
                  method: 'get',
                  url: process.env.VUE_APP_ROOT_URL + '1',
              }) .then (response => this.decomol1 = response.data)
              setTimeout(this.getDecomol1, 2000)
          },

          getDecomol2() {
              axios({
                  method: 'get',
                  url: process.env.VUE_APP_ROOT_URL + '2',
              }) .then (response => this.decomol2 = response.data)
              setTimeout(this.getDecomol2, 2000)
          },

          getDecomol3() {
              axios({
                  method: 'get',
                  url: process.env.VUE_APP_ROOT_URL + '3',
              }) .then (response => this.decomol3 = response.data)
              setTimeout(this.getDecomol3, 2000)
          },

          corAtual(status, troca){
              if (status == true){
                  return 'button is-success'
              }
              else if (status == false){
                  if(troca == false){
                      return 'button is-danger'
                  }
                  else{
                      return 'button is-warning'
                  }
              }
              else{
                  return 'button is-warning'
              }
          },

          decomolStatus(status){
                if (status == true){
                  return 'Liberado'
              }
              else if (status == false){
                  return 'Não Liberado'               
              }
          },

          formatData(data) {
          return moment(data).format('DD/MM/YY [-] HH:mm:ss')
          },

        },
        ready() {
        this.getDecomol1()
        this.getDecomol2()
        this.getDecomol3()
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

.block:not(:last-child) {
        margin-bottom: 1.5rem;
}
    .decomol-container { 
        position: relative;
        margin-top: 1.5rem;
    }

    .columns {
        position: relative;
        /* margin-top: 20vh; */
    }

    button {
        margin-bottom: 1.0rem;
    }

    .tag {
        position: relative;
        margin-top: 1.0rem;
        
    }

    .spec{
        position: inherit;
        text-align: center;
        margin-top: 5px;
        margin-bottom: 0.5rem;
    }

   .svg{
        position: relative;
   }
</style>
