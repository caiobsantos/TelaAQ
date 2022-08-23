<template>
    <div class="decomol_content" v-for="decomol in decs" v-bind:key="decomol.id">            
        <br> <h1 class="title is-4">{{decomol.producao}}</h1>
        <button :class= " corAtual(decomol.liberado) ">{{ decomolStatus(decomol.liberado) }}</button>
        <router-link v-bind:to="'/fabricacao/detalhes/' + decomol.id"><button class='button is-info is-light'>Detalhes</button></router-link>
        <br> <br>
        </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: 'FabricacaoView',
        data() {
            return{
                decs: [],
            }
        },
        mounted() {
            this.isReady()
        },
        methods: {
            isReady(){
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL,
                }) .then (response => this.decs = response.data)

                    .catch(err => {
                    console.log(err)
                })

                setTimeout(this.isReady, 2000)
            },

            corAtual(status){
                if (status == true){
                    return 'button is-success'
                }
                else if (status == false){
                    return 'button is-danger'
                }
                else{
                    return 'button is-warning'
                }
            },

            decomolStatus(status){
                 if (status == true){
                    return 'Liberado'
                }
                else if (status == false){
                    return 'Não Liberado'
                }
                else{
                    return 'Em Análise'
                }
            }
        },

        ready() {
            this.isReady()
        }
    }
</script>