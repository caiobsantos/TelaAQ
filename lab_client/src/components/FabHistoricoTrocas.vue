<template>
    <div v-if="decomol_nome=='decomol1'">
        <nav>
            <router-link to="/fab/historico/decomol1">Histórico de Registros</router-link> |
            <router-link to="/fab/historico/decomol1/troca">Histórico de Trocas</router-link>
        </nav>
    </div>
        <div v-else-if="decomol_nome=='decomol2'">
            <nav>
                <router-link to="/fab/historico/decomol2">Histórico de Registros</router-link> |
                <router-link to="/fab/historico/decomol2/troca">Histórico de Trocas</router-link>
            </nav>
        </div> 
        <div v-else>
            <nav>
                <router-link to="/fab/historico/decomol3">Histórico de Registros</router-link> |
                <router-link to="/fab/historico/decomol3/troca">Histórico de Trocas</router-link>
            </nav>
        </div>
    <div class="table-column">
        <div class="voltar">
        <router-link to="/fab/decomol">
            <button class="button is-info is-inverted">
                Voltar
            </button>
        </router-link>
        </div>
        <table class="table is-bordered is-striped">
            <tr>
                <th>Decomol</th>
                <th>Início da Regeneração</th>
                <th>Fim da Regeneração</th>
            </tr>
            <tbody v-for="dec in decs.reverse()"  v-bind:key="dec.id"> 
                    <tr v-if="comparaDecomol(dec.decomol_troca)">
                        <td>{{ dec.decomol_troca }}</td>
                        <td>{{ formatDataInicio(dec.data_troca) }}</td>
                        <td>{{ formatDataFim(dec.data_fim, dec.data_troca)}}</td>
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
    name: 'FabHistoricoTrocaView',

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

        formatDataInicio(data) {
            return moment(data).format('DD/MM/YY [] HH:mm')
        },

        formatDataFim(datafim, datain){
            var a = moment(datafim)
            var b = moment(datain)
            if (a.diff(b)<=100){
                return '-'
            }
            else{
                return moment(datafim).format('DD/MM/YY [] HH:mm')
            }
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
    .voltar{
        position: inherit;
        text-align: left;
        margin-left: 15rem;
        margin-bottom: 2rem;
        margin-top: 2.5rem;
    }
</style>