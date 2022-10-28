<template>
    <nav>
    <router-link to="/historico/">Histórico de Registros</router-link> |
    <router-link to="/historico/troca">Histórico de Trocas</router-link>
  </nav>
    <div class="table-column">
        <table class="table is-bordered is-striped">
            <tr>
                <th>Decomol</th>
                <th>Data de Liberação</th>
            </tr>
            <tbody v-for="dec in decs.reverse()"  v-bind:key="dec.id"> 
                    <tr v-if="comparaDecomol(dec.decomol_troca)">
                        <td>{{ dec.decomol_troca }}</td>
                        <td>{{ formatData(dec.data_troca) }}</td>
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
    name: 'HistoricoTrocaView',

    data(){
        return {
            decomol_nome: this.$route.params.id,
            decs: [],
        }
    },

    created() {
        this.getTroca()
    },

    methods: {
        getTroca(){
            axios.get(process.env.VUE_APP_ROOT_URL_TROCA, {
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