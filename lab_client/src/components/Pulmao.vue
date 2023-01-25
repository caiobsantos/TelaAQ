<template>
    <div class="pulmao-container">
        <navbar></navbar>
        <div class="pulmoes">
            <div class="pulmao">
                <svg class="svg" width="300" height="300">
                    <image href="../assets/tanques/PULMÃO1.svg" alt="sla" width="275" y="-15%" x="3%"/>
                </svg>
                <p class="historico"><b><router-link class="historico" v-bind:to="'/pulmao/historico/' + pulmao1.id">Tanque 1</router-link></b></p>
                <p>Última Ánalise: {{formatData(pulmao1.data_analise)}}</p>
                <!-- <p>
                    <router-link class="links" to='/pulmao/historico/1'><span class="historico">Ver Mais</span></router-link>
                </p> -->
                <router-link class="links" v-bind:to="'/pulmao/' + pulmao1.id"><span class='tag is-link'>Registrar Análise</span></router-link>
            </div>
            <div class="pulmao">
                <svg class="svg" width="300" height="300">
                    <image href="../assets/tanques/PULMÃO2.svg" alt="sla" width="275" y="-15%" x="3%"/>
                </svg>
                <p class="historico"><b><router-link class="historico" v-bind:to="'/pulmao/historico/' + pulmao2.id">Tanque 2</router-link></b></p>
                <p>Última Ánalise: {{formatData(pulmao2.data_analise)}}</p>
                <router-link class="links" v-bind:to="'/pulmao/' + pulmao2.id"><span class='tag is-link'>Registrar Análise</span></router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import moment from 'moment'
    import navbar from '@/components/NavBarLab.vue'

    // criar funcionalidade para a pagina atualizar apenas quando houver alguma alteracao nos elementos

    export default {
        name: 'AQPulmaoView',
        components: {navbar},
        data() {
            return{
                pulmao1: [],
                pulmao2: [],
            } 
        },
        
        created(){
            this.getPulmao1()
            this.getPulmao2()
        },

        methods: {
            getPulmao1(){
                axios({
                    method: 'get',
                    url: 'http://10.15.100.110:50003/pulmao/' + '1',
                }) .then(response => this.pulmao1 = response.data) 
            },

            getPulmao2(){
                axios({
                    method: 'get',
                    url: 'http://10.15.100.110:50003/pulmao/' + '2',
                }) .then(response => this.pulmao2 = response.data) 
            },

            formatData(data){
                return moment(data).format('DD/MM/YY [-] HH:mm:ss')
            }

        },
    }
</script>

<style scoped>
    *{
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
    }
    .pulmao-container { 
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        background-color: lightgray;
        color: black;
    }

    .pulmoes{
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        justify-content: space-around;
        min-height: 90vh;
        padding-top: 50px;
        padding-bottom: 50px;
    }

    .pulmao{
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .historico{
        padding-top: 5px;
        font-size: 16px;
        color: black;
    }

    .tag {
        position: relative;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }

    @media (max-width: 800px){
        .pulmoes{
        display: flex;
        flex-direction: column;
        align-items: center;
        flex-wrap: wrap;
        justify-content: space-around;
        min-height: 90vh;
        padding-top: 50px;
        padding-bottom: 50px;
        gap: 50px;
    }
    .tag {
        position: relative;
        margin-top: 0.75rem;
        margin-bottom: 0.75rem;
    }
    }

</style>