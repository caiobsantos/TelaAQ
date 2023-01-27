<template>
    <div class="historico-container">
        <navbar></navbar>
        <div class="content">
            <div class="voltar">
                <button   @click="$router.go(-1)">
                    Voltar
                </button>
            </div>
            <div class="tabela">
                <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
                    <thead>
                        <tr>
                            <th>Tanque</th>
                            <th>Resultado Cor</th>
                            <th>Sensorial</th>
                            <th>Ph</th>
                            <th>Brix</th>
                            <th>Data da Análise</th>
                        </tr>
                    </thead>
                    <tbody v-for="pulmao in filterPulmao()" :key="pulmao.id">
                            <tr v-if="comparaNome(pulmao)">
                                <td>{{ pulmao.tanque }}</td>
                                <td>{{ pulmao.resultado_cor }}</td>
                                <td>{{ pulmao.sensorial }}</td>
                                <td>{{ pulmao.ph }}</td>
                                <td>{{ pulmao.brix }}</td>
                                <td>{{ formatData(pulmao.data_analise) }}</td>
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
  import navbar from '@/components/NavBarLab.vue'

  export default {
    name: 'HistoricoPulmaoView',
    components: {navbar},
    data(){
        return {
            id: this.$route.params.id,
            pulmoes: [],
            pul: []
        }
    },

    created() {
        this.getPulmao()
    },


    methods: {

        filterPulmao(){
            for (let index = this.pulmoes.length-1; index >=0; index--) {
                this.pul.push(this.pulmoes[index])
                if(index==0){
                    return this.pul
                }
            }
            return 0
        },
        getPulmao(){
            axios.get(process.env.VUE_APP_ROOT_URL_HPULMAO, {
            }) .then (response => this.pulmoes = response.data)
        },


        comparaNome(pulmao){
            if(pulmao.tanque == 'Tanque 1' && this.id == 1){
                return true
            }
            else if(pulmao.tanque == 'Tanque 2' && this.id == 2){
                return true
            }
            else{
                return false
            }
        },

        formatData(data) {
            return moment(data).format('DD/MM/YY [] HH:mm')
        },
    }
  }
</script>

<style scoped>
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


    @media (max-width: 768px){
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
        width: 80vh;
        font-size: 16px;
    }
    }

    @media (max-width: 400px){
        .tabela{
        margin-right: auto;
        margin-left: auto;
        overflow-x: auto;
        width: 66.11vh;
        font-size: 16px;
    }
    }
</style>