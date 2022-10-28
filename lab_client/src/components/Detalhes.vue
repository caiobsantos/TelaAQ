<template>
    <div class="table-column">
        <div class="volta">
            <router-link to="/fabricacao">
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
                <th>Status</th>
            </tr>
            <tr v-bind:key="decomol.id"> 
                <td>{{ formatBlankSpace(decomol.producao) }}</td>
                <td>{{ formatBlankSpace(decomol.resultado_cor) }}</td>
                <td>{{ formatBlankSpace(decomol.sensorial) }}</td>
                <td>{{ formatBlankSpace(decomol.ph) }}</td>
                <td>{{ formatBlankSpace(decomol.brix) }}</td>
                <td>{{ formatData(decomol.data_liberacao) }}</td>
                <td>{{ formatStatus(decomol.liberado) }}</td>
            </tr>
        </table>
    </div> 
    <div class="sla">
                <router-link to="/historico/">
                    <button class="button is-info is-inverted">
                        Ver Mais
                    </button>
                </router-link>     
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

        formatStatus(status) {
            if (status == true){
                return 'Liberado'
            }
            else if (status == false){
                return 'Não Liberado'
            }
            else{
                return 'Em Análise'
            }
        },

        formatBlankSpace(data){
            if (data == null){
                return 'Não Especificado'
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
        margin-top: 4px;
    }

    .volta{
        align-items: left;
        margin-bottom: 4px
    }
</style>