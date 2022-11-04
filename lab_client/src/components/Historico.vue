<template>
    <div v-if="decomol_nome=='decomol1'">
        <nav>
            <router-link to="/historico/decomol1">Histórico de Registros</router-link> |
            <router-link to="/historico/decomol1/troca">Histórico de Trocas</router-link>
        </nav>
    </div>
        <div v-else-if="decomol_nome=='decomol2'">
            <nav>
                <router-link to="/historico/decomol2">Histórico de Registros</router-link> |
                <router-link to="/historico/decomol2/troca">Histórico de Trocas</router-link>
            </nav>
        </div> 
        <div v-else>
            <nav>
                <router-link to="/historico/decomol3">Histórico de Registros</router-link> |
                <router-link to="/historico/decomol3/troca">Histórico de Trocas</router-link>
            </nav>
        </div>
    
    <div class="table-column">
        <div class="voltar">
        <router-link to="/decomol">
            <button class="button is-info is-inverted">
                Voltar
            </button>
        </router-link>
        </div>
        <table class="table is-bordered is-striped">
            <tr>
                <th>Decomol</th>
                <th>Resultado Cor</th>
                <th>Sensorial</th>
                <th>Ph</th>
                <th>Brix</th>
                <th>Data de Liberação</th>
                <th>Resultado Análise</th>
            </tr>
            <tbody v-for="dec in decs.reverse()"  v-bind:key="dec.id"> 
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
    <br>
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
        margin-bottom: 2rem
    }
</style>