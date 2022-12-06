<template>
    <div class="table-column">
        <div class="voltar">
            <button class="button is-info is-inverted" @click="$router.go(-1)">
                Voltar
            </button>
        </div>
        <table class="table is-bordered is-striped">
            <tr>
                <th>Tanque</th>
                <th>Resultado Cor</th>
                <th>Sensorial</th>
                <th>Ph</th>
                <th>Brix</th>
                <th>Data da Análise</th>
            </tr>
            <tbody v-for="pulmao in pulmoes.reverse()"  v-bind:key="pulmao.id"> 
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
    <br>
</template>

<script>
  import axios from 'axios'  
  import moment from 'moment'

  export default {
    name: 'HistoricoPulmaoView',

    data(){
        return {
            id: this.$route.params.id,
            pulmoes: [],
        }
    },

    created() {
        this.getPulmao()
    },

    methods: {
        getPulmao(){
            axios.get('http://172.16.19.182:8000/historico/pulmao', {
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
    table{
        margin-left: auto;
        margin-right: auto;
    }
    .voltar{
        position: inherit;
        text-align: left;
        margin-left: 15rem;
        margin-bottom: 2rem;
        margin-top: 2.5rem
    }
</style>