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
            <tr v-bind:key="decomol.id"> 
                <td>{{ formatBlankSpace(decomol.producao) }}</td>
                <td>{{ formatBlankSpace(decomol.resultado_cor) }}</td>
                <td>{{ formatBlankSpace(decomol.sensorial) }}</td>
                <td>{{ formatBlankSpace(decomol.ph) }}</td>
                <td>{{ formatBlankSpace(decomol.brix) }}</td>
                <td>{{ formatData(decomol.data_liberacao) }}</td>
                <td>{{ formatStatus(decomol.liberado, decomol.troca_decomol) }}</td>
            </tr>
        </table>
    </div> 
    <div class="sla">
        <div v-if="id==1">
            <router-link to="/historico/decomol1" >
                <button class="button is-info is-inverted">
                    Ver Mais
                </button>
            </router-link>
        </div>
        <div v-else-if="id==2">
            <router-link to="/historico/decomol2" >
                <button class="button is-info is-inverted">
                    Ver Mais
                </button>
            </router-link>
        </div> 
        <div v-else>
            <router-link to="/historico/decomol3" >
                <button class="button is-info is-inverted">
                    Ver Mais
                </button>
            </router-link>
        </div>  
    </div>
    <br>
        
</template>

<script>
    import axios from 'axios'
    import moment from 'moment'

    const request = axios.CancelToken.source();

    export default {
        name: 'DetalheView',
        data () {
            return {
                id: this.$route.params.id,
                decomol: [],
                router: this.$router,
            }
        },

         mounted() {
            this.getDecomol()
        },

    methods: {
        getDecomol() {
            axios({
                method: 'get',
                url: process.env.VUE_APP_ROOT_URL + this.id,
                cancelToken: request.token
            }) .then(response => this.decomol = response.data)

                .catch(err => {
                    console.log(err)
                    request.cancel()
                    this.router.push({path: '/fabricacao'})
                })

            setTimeout(this.getDecomol, 2000)
        },

        formatData(data) {
            return moment(data).format('DD/MM/YY [] HH:mm')
        },

        formatStatus(status, troca) {
            if (status == true){
                return 'Liberado'
            }
            else if (status == false && troca == false){
                return 'Não Liberado'
            }
            else{
                return 'Em Análise'
            }
        },

        formatBlankSpace(data){
            if (data == null || data == ""){
                return '-'
            }
            else{
                return data
            }
        }
    },

    ready() {
        this.getDecomol()
        }
    }
</script>

<style scoped>
    table{
        margin-left: auto;
        margin-right: auto;
    }

    .sla{
        align-items: center;
        margin-top: 1.5rem;
    }

    .volta{
        position: inherit;
        text-align: left;
        margin-left: 15rem;
        margin-bottom: 2rem
    }
</style>