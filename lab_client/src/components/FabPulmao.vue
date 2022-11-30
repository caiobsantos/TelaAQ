<template>
    <div class="pulmao">
        <div class="columns">
            <div class="column is-half">
                <p><b>{{pulmao1.tanque}}</b></p>
                <p>Resultado Cor: {{pulmao1.resultado_cor}}</p>
                <p>Última Ánalise: {{formatData(pulmao1.data_analise)}}</p>
                <div class="historico">
                    <router-link class="links" to='/pulmao/historico/1'>Ver Mais</router-link>
                </div>
            </div>
            <div class="column">
                <p><b>{{pulmao2.tanque}}</b></p> 
                <p>Resultado Cor: {{pulmao2.resultado_cor}}</p>
                <p>Última Ánalise: {{formatData(pulmao2.data_analise)}}</p>
                <div class="historico">
                    <router-link class="links" to='/pulmao/historico/2'>Ver Mais</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import moment from 'moment'

    // criar funcionalidade para a pagina atualizar apenas quando houver alguma alteracao nos elementos

    export default {
        name: 'FabPulmaoView',
        data() {
            return{
                pulmao1: [],
                pulmao2: [],
                i: true,
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
                    url: 'http://172.16.19.182:8000/pulmao/' + '1',
                }) .then(response => this.pulmao1 = response.data) 
            },

            getPulmao2(){
                axios({
                    method: 'get',
                    url: 'http://172.16.19.182:8000/pulmao/' + '2',
                }) .then(response => this.pulmao2 = response.data) 
            },

            formatData(data){
                return moment(data).format('DD/MM/YY [-] HH:mm:ss')
            }

        },
    }
</script>

<style scoped>
     .pulmao {
        margin-top: 1.5rem;
    }
    
    .historico{
        margin-top: 1.0rem;
    }

</style>