<template>
    <div class="pulmao">
        <div class="columns">
            <div class="column is-half">
                <svg class="svg" width="300" height="300">
                    <image href="../assets/tanques/PULMÃO1.svg" alt="sla" width="275" y="-15%" x="3%"/>
                </svg>
                <p><b>{{pulmao1.tanque}}</b></p> <br>
                <p>Última Ánalise: {{formatData(pulmao1.data_analise)}}</p>
                <p>
                    <router-link class="links" to='/pulmao/historico/1'><span class="historico">Ver Mais</span></router-link>
                </p>
                <router-link class="links" v-bind:to="'/pulmao/' + pulmao1.id"><span class='tag is-link'>Registrar Análise</span></router-link>
            </div>
            <div class="column">
                <svg class="svg" width="300" height="300">
                    <image href="../assets/tanques/PULMÃO2.svg" alt="sla" width="275" y="-15%" x="3%"/>
                </svg>
                <p><b>{{pulmao2.tanque}}</b></p> <br>
                <p>Última Ánalise: {{formatData(pulmao2.data_analise)}}</p>
                <p>
                    <router-link class="links" to='/pulmao/historico/2'><span class="historico">Ver Mais</span></router-link>
                </p>
                <router-link class="links" v-bind:to="'/pulmao/' + pulmao2.id"><span class='tag is-link'>Registrar Análise</span></router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import moment from 'moment'

    // criar funcionalidade para a pagina atualizar apenas quando houver alguma alteracao nos elementos

    export default {
        name: 'AQPulmaoView',
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

    .tag {
        position: relative;
        margin-top: 1.0rem;
        
    }

</style>