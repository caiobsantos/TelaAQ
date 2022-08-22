<template>
    <div class="decomol_container">
        <div class="column is-2 is-offset-9">
            <router-link to="/adicionar"><button class="button is-dark">Adicionar Decomol</button></router-link>
        </div>
        <!-- se o status:liberado não estiver blank, o decomol pode sumir (depois fazer um historico) -->
        <div class="decomol_content" v-for="decomol in decs" v-bind:key="decomol.id">            
            <div v-if="decomol.liberado == null">
                <h1 class="title is-4">{{ decomol.producao }}</h1>
                <button :class= " corAtual(decomol.liberado) ">{{ decomolStatus(decomol.liberado) }}</button>
                <router-link v-bind:to="'/decomol/' + decomol.id"><button class='button is-info is-light'>Enviar Resultado</button></router-link>
                <button class='button is-danger is-light' @click="deleteDecomol(decomol.id)">Deletar</button> <br>
                <br><br><br>
            </div>
            <div v-else>
                <h1 class="title is-4">{{ decomol.producao }}</h1>
                <button :class= " corAtual(decomol.liberado) ">{{ decomolStatus(decomol.liberado) }}</button>
                <router-link v-bind:to="'/decomol/' + decomol.id"><button class='button is-info is-light'>Editar Resultado</button></router-link>
                <button class='button is-danger is-light' @click="deleteDecomol(decomol.id)">Deletar</button> <br>
                <br><br><br>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    

    export default {
        name: 'DecomolView',
        data() {
            return{
                decs: [],
                baseUrl: 'http://172.16.19.116:8000/decomol/'
            } 
        },
        mounted() {
            this.getDecomol()
        },
        methods: {
            getDecomol() {
                axios({
                    method: 'get',
                    url: this.baseUrl,
                }) .then (response => this.decs = response.data)


                setTimeout(this.getDecomol, 2000)
            },


            async deleteDecomol(id) {
                 const c = confirm("Do you really want to delete it? You will not be able to restore this data again!")
                if (c) {
                    await this.deletar(id)
                    window.location.reload()
                }
            },

            deletar(id){
                 axios({
                    method: 'delete',
                    url: this.baseUrl + id + '/'
                }) .then (response => console.log(response.data))
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
            },
        },
        ready() {
        this.getDecomol()
        }
    }
</script>