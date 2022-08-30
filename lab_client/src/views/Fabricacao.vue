<template>
    <div class="decomol-container">
        <div class="columns">
                <div class="column is-one-third">
                    <button :class= " corAtual(decomol1.liberado, decomol1.troca_decomol) ">
                        {{ decomolStatus(decomol1.liberado, decomol1.troca_decomol) }}
                    </button>
                    <p>Decomol 1</p>
                    <router-link v-bind:to="'/fabricacao/detalhes/' + decomol1.id"><span class='tag is-link'>Detalhes</span></router-link> <br>
                    <button class="button" @click="trocarDecomol(decomol1)">Trocar Decomol</button>
                </div>
                <div class="column">
                    <button :class= " corAtual(decomol2.liberado, decomol2.troca_decomol) ">
                        {{ decomolStatus(decomol2.liberado, decomol2.troca_decomol) }}
                    </button>
                    <p>Decomol 2</p>
                    <router-link v-bind:to="'/fabricacao/detalhes/' + decomol2.id"><span class='tag is-link'>Detalhes</span></router-link> <br>
                    <button class="button" @click="trocarDecomol(decomol2)">Trocar Decomol</button>
                </div>
                <div class="column">
                    <button :class= " corAtual(decomol3.liberado, decomol3.troca_decomol) ">
                        {{ decomolStatus(decomol3.liberado, decomol3.troca_decomol) }}
                    </button>
                    <p>Decomol 3</p>
                    <router-link v-bind:to="'/fabricacao/detalhes/' + decomol3.id"><span class='tag is-link'>Detalhes</span></router-link> <br>
                    <button class="button" @click="trocarDecomol(decomol3)">Trocar Decomol</button>
                </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

    export default {
        name: 'FabricacaoView',
        data() {
            return{
                decomol1: [],
                decomol2: [],
                decomol3: [],
                status1: null,
                status2: null,
                status3: null
            } 
        },
        created() {
            this.getDecomol1()
            this.getDecomol1Status()
            this.getDecomol2()
            this.getDecomol2Status()
            this.getDecomol3()
            this.getDecomol3Status()
        },
        methods: {
            getDecomol1() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '47',
                }) .then (response => {
                    this.decomol1 = response.data})
                setTimeout(this.getDecomol1, 2000)
            },

            getDecomol1Status() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '47',
                }) .then (response => {
                    this.status1 = response.data.troca_decomol})
            },

            getDecomol2() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '48',
                }) .then (response => this.decomol2 = response.data)
                setTimeout(this.getDecomol2, 2000)
            },

            getDecomol2Status() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '48',
                }) .then (response => {
                    this.status2 = response.data.troca_decomol})
            },

            getDecomol3() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '49',
                }) .then (response => {
                    this.decomol3 = response.data,
                    this.status3 = response.data.troca_decomol
                    })
                setTimeout(this.getDecomol3, 2000)
            },

            getDecomol3Status() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '49',
                }) .then (response => {
                    this.status3 = response.data.troca_decomol})
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

            trocarDecomol(decomol){
                    this.status3 = true
                    axios.put(process.env.VUE_APP_ROOT_URL + decomol.id + '/', {
                        resultado_cor: decomol.resultado_cor,
                        sensorial: decomol.sensorial,
                        ph: decomol.ph,
                        brix: decomol.brix,
                        producao: decomol.producao,
                        liberado: false,
                        troca_decomol: true
                    })
                    //  .then(response => {
                    //     console.log(response.data)
                    // })
            }

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
        margin-bottom: 1.0rem;
    }
</style>