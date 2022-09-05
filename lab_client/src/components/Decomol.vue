<template>
    <div class="decomol-container">
        <div class="columns">
                    <div class="column is-one-third" v-if="decomol1.troca_decomol==true">
                        <button :class= " corAtual(decomol1.liberado, decomol1.troca_decomol) ">
                            {{ decomolStatus(decomol1.liberado, decomol1.troca_decomol) }}
                        </button>
                        <!-- colocar um ONFOCUS mostrando os resultados da ultima analise -->
                        <p>Decomol 1</p>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol1.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                        <router-link class="links" to='/historico/decomol1'><span class='tag is-link'>Histórico</span></router-link>
                    </div>
                    <div class="column is-one-third" v-else>
                        <button :class= " corAtual(decomol1.liberado, decomol1.troca_decomol) ">
                            {{ decomolStatus(decomol1.liberado, decomol1.troca_decomol) }}
                        </button>
                        <p>Decomol 1</p>
                        <router-link class="links" to='/historico/decomol1'><span class='tag is-link'>Histórico</span></router-link>
                    </div>
                <div class="column" v-if="decomol2.troca_decomol == true">
                    <button :class= " corAtual(decomol2.liberado, decomol2.troca_decomol) ">
                        {{ decomolStatus(decomol2.liberado, decomol2.troca_decomol) }}
                    </button>
                    <p>Decomol 2</p>
                    <router-link class="links" v-bind:to="'/decomol/' + decomol2.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                    <router-link class="links" to='/historico/decomol2'><span class='tag is-link'>Histórico</span></router-link>
                </div>
                <div class="column" v-else>
                    <button :class= " corAtual(decomol2.liberado, decomol2.troca_decomol) ">
                        {{ decomolStatus(decomol2.liberado, decomol2.troca_decomol) }}
                    </button>
                    <p>Decomol 2</p>
                    <router-link class="links" to='/historico/decomol2'><span class='tag is-link'>Histórico</span></router-link>
                </div>
                <div class="column" v-if="decomol3.troca_decomol == true">
                    <button :class= " corAtual(decomol3.liberado, decomol3.troca_decomol) ">
                        {{ decomolStatus(decomol3.liberado, decomol3.troca_decomol) }}
                    </button>
                    <p>Decomol 3</p>
                    <router-link class="links" v-bind:to="'/decomol/' + decomol3.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                    <router-link class="links" to='/historico/decomol3'><span class='tag is-link'>Histórico</span></router-link> 
                </div>
                <div class="column" v-else>
                    <button :class= " corAtual(decomol3.liberado, decomol3.troca_decomol) ">
                        {{ decomolStatus(decomol3.liberado, decomol3.troca_decomol) }}
                    </button>
                    <p>Decomol 3</p>
                    <router-link class="links" to='/historico/decomol3'><span class='tag is-link'>Histórico</span></router-link> 
                </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    // criar funcionalidade para a pagina atualizar apenas quando houver alguma alteracao nos elementos

    export default {
        name: 'DecomolView',
        data() {
            return{
                decomol1: [],
                decomol2: [],
                decomol3: [],
            } 
        },
        created() {
            this.getDecomol1()
            this.getDecomol2()
            this.getDecomol3()
        },
        methods: {
            getDecomol1() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '1',
                }) .then (response => this.decomol1 = response.data)
                setTimeout(this.getDecomol1, 2000)
            },

            getDecomol2() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '2',
                }) .then (response => this.decomol2 = response.data)
                setTimeout(this.getDecomol2, 2000)
            },

            getDecomol3() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '3',
                }) .then (response => this.decomol3 = response.data)
                setTimeout(this.getDecomol3, 2000)
            },

            async deleteDecomol(id) {
                 const c = confirm("Do you really want to delete it? You will not be able to restore this data again!")
                if (c) {
                    await this.deletar(id)
                    // window.location.reload()
                }
            },

            deletar(id){
                 axios({
                    method: 'delete',
                    url: process.env.VUE_APP_ROOT_URL + id + '/'
                }) .then (response => console.log(response.data))
            },

            corAtual(status, troca){
                if (status == true){
                    return 'button is-success'
                }
                else if (status == false){
                    if(troca == false){
                        return 'button is-danger'
                    }
                    else{
                        return 'button is-warning'
                    }
                }
                else{
                    return 'button is-warning'
                }
            },

            decomolStatus(status, troca){
                 if (status == true){
                    return 'Liberado'
                }
                else if (status == false){
                    if(troca == false){
                        return 'Não Liberado'
                    }
                    else{
                        return 'A ser analisado'
                    }
                }
                else{
                    return 'Em Análise'
                }
            },
        },
        ready() {
        this.getDecomol1()
        this.getDecomol2()
        this.getDecomol3()
        }
    }
</script>

<style scoped>
    .block:not(:last-child) {
        margin-bottom: 1.5rem;
}
    .decomol-container { 
        position: relative;
        margin-top: 1.5rem;
    }

    .columns {
        position: relative;
        margin-top: 40vh;
    }

    button {
        margin-bottom: 1.0rem;
    }

    .tag {
        position: relative;
        margin-top: 1.0rem;
        
    }
</style>