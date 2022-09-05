<template>
    <div class="table-column">
        <table class="table is-bordered is-striped">
            <tr>
                <th>Decomol</th>
                <th>Resultado Cor</th>
                <th>Sensorial</th>
                <th>Ph</th>
                <th>Brix</th>
                <th>Data de Liberação</th>
                <th>Status</th>
            </tr>
            <tbody v-for="dec in decs"  v-bind:key="dec.id"> 
                    <tr v-if="comparaDecomol(dec.decomol)">
                        <td>{{ dec.decomol }}</td>
                        <td>{{ dec.resultado_cor }}</td>
                        <td>{{ dec.sensorial }}</td>
                        <td>{{ dec.ph }}</td>
                        <td>{{ dec.brix }}</td>
                        <td>{{ formatData(dec.data_liberacao) }}</td>
                        <td>{{ dec.resultado_analise }}</td>
                    </tr>
            </tbody>
        </table>
    </div> 
    <br>
    <div class="voltar">
        <router-link to="/decomol">
            <button class="button is-info is-inverted">
                Voltar
            </button>
        </router-link>
    </div>
</template>

<script>
  import axios from 'axios'  
  import moment from 'moment'

  export default {
    name: 'HistoricoView',

    data(){
        return {
            decomol_nome: this.$route.params.id,
            decs: [],
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

        comparaDecomol(nome){
            nome = nome.replace(/\W+/g, '').toLowerCase()
            if(nome == this.decomol_nome){
                return true
            }
            
            else{
                return false
            }
        }
    }
  }
</script>

<style scoped>
    table{
        margin-left: auto;
        margin-right: auto;
    }
</style>