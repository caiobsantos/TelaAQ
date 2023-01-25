<template>
    <div class="historico-container">
        <div v-if="decomol_nome=='decomol1'">
            <nav>
                <router-link to="/fab/historico/decomol1">Histórico de Análises</router-link> |
                <router-link to="/fab/historico/decomol1/troca">Histórico de Regeneração</router-link>
            </nav>
        </div>
            <div v-else-if="decomol_nome=='decomol2'">
                <nav>
                    <router-link to="/fab/historico/decomol2">Histórico de Análises</router-link> |
                    <router-link to="/fab/historico/decomol2/troca">Histórico de Regeneração</router-link>
                </nav>
            </div>
            <div v-else>
                <nav>
                    <router-link to="/fab/historico/decomol3">Histórico de Análises</router-link> |
                    <router-link to="/fab/historico/decomol3/troca">Histórico de Regeneração</router-link>
                </nav>
            </div>
        
        <div class="content">
            <div class="voltar">
            <router-link to="/fab/decomol">
                <button>
                    Início
                </button>
            </router-link>
            </div>
            <div class="tabela">
                <table class="table table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
                    <tr>
                        <th>Decomol</th>
                        <th>Resultado Cor</th>
                        <th>Sensorial</th>
                        <th>Ph</th>
                        <th>Brix</th>
                        <th>Data da Análise</th>
                        <th>Resultado Análise</th>
                    </tr>
                    <tbody class="reverse" v-for="dec in filterDecomol()"  v-bind:key="dec.id">
                            <tr v-if="comparaDecomol(dec)">
                                <td>{{ dec.decomol }}</td>
                                <td>{{ dec.resultado_cor }}</td>
                                <td>{{ dec.sensorial }}</td>
                                <td>{{ dec.ph }}</td>
                                <td>{{ dec.brix }}</td>
                                <td>{{ formatData(dec.data_liberacao) }}</td>
                                <td>{{ formatResultado(dec.resultado_analise) }}</td>
                            </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'  
  import moment from 'moment'

  export default {
    name: 'FabHistoricoView',
    props: ['origin'],

    data(){
        return {
            decomol_nome: this.$route.params.id,
            decs: [],
            dec: [],
        }
    },

    mounted() {
        this.getDecomol()
    },

    methods: {
        getDecomol(){
            axios.get(process.env.VUE_APP_ROOT_URL_HISTORICO, {
            }) .then (response => this.decs = response.data)
        },

        formatData(data) {
            return moment(data).format('DD/MM/YY [] HH:mm')
        },

        formatResultado(resultado){
            if(resultado){
                return "Liberado"
            }
            else{
                return "Não Liberado"
            }
        },

        comparaDecomol(nome){
            nome = nome.decomol.replace(/\W+/g, '').toLowerCase()
            if(nome == this.decomol_nome){
                return true
            }
            
            else{
                return false
            }
        },

        filterDecomol(){
            for (let index = this.decs.length-1; index >=0; index--) {
                this.dec.push(this.decs[index])
                if(index==0){
                    return this.dec
                }
            }
            return 0
        },
    }
  }
</script>

<style scoped>
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

.historico-container { 
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
        padding-top: 3rem;
        color: black;
        padding-bottom: 1.5rem;   
        min-height: 90vh;
        gap: 50px;
    } 

    .tabela{
        margin-right: auto;
        margin-left: auto;
        overflow-x: auto;
        width: 160vh;
        font-size: 17px;
    }

    button{
        cursor: pointer;
        border: 1px transparent solid;
        background-color: lightgray;
        font-size: 16px;
        color: blue;
    }

    button:hover{
        transition-delay: 50ms;
        border-bottom: 1px blue solid;
    }


    @media (max-width: 800px){
        .tabela{
        margin-right: auto;
        margin-left: auto;
        overflow-x: auto;
        width: 140vh;
        font-size: 16px;
    }
    }

    @media (max-width: 680px){
        .tabela{
        margin-right: auto;
        margin-left: auto;
        overflow-x: auto;
        width: 115vh;
        font-size: 16px;
    }
    }

    @media (max-width: 600px){
        .tabela{
        margin-right: auto;
        margin-left: auto;
        overflow-x: auto;
        width: 100vh;
        font-size: 16px;
    }
    }

    @media (max-width: 500px){
        .tabela{
        margin-right: auto;
        margin-left: auto;
        overflow-x: auto;
        width: 83vh;
        font-size: 16px;
    }
    }

    @media (max-width: 400px){
        .tabela{
        margin-right: auto;
        margin-left: auto;
        overflow-x: auto;
        width: 69.5vh;
        font-size: 16px;
    }
    }
</style>