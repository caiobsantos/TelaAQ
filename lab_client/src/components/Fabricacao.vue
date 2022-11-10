<template>
    <div class="decomol-container">
        <div class="columns">
                <div class="column is-one-third" v-if="checker('DECOMOL_1_PRODUCAO', decomol1.troca_decomol) == 'StandBy'">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/A.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p>Decomol 1</p>
                    <router-link v-bind:to="'/fabricacao/detalhes/' + decomol1.id"><span class='tag is-link'>Detalhes</span></router-link> <br>
                    <button class="button" @click="trocarDecomol(decomol1)">Trocar Decomol</button>
                </div>
                <div class="column is-one-third" v-else-if="checker('DECOMOL_1_PRODUCAO', decomol1.troca_decomol) == 'Produzindo'">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/VD.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p>Decomol 1</p>
                    <router-link v-bind:to="'/fabricacao/detalhes/' + decomol1.id"><span class='tag is-link'>Detalhes</span></router-link> <br>
                    <button class="button" @click="trocarDecomol(decomol1)">Trocar Decomol</button>
                </div>
                <div class="column is-one-third" v-else>
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/V.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p>Decomol 1</p>
                    <router-link v-bind:to="'/fabricacao/detalhes/' + decomol1.id"><span class='tag is-link'>Detalhes</span></router-link> <br>
                    <button class="button" @click="trocarDecomol(decomol1)">Trocar Decomol</button>
                </div>

                <div class="column" v-if="decomol2.troca_decomol==true">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/A.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p>Decomol 2</p>
                    <router-link v-bind:to="'/fabricacao/detalhes/' + decomol2.id"><span class='tag is-link'>Detalhes</span></router-link> <br>
                    <button class="button" @click="trocarDecomol(decomol2)">Trocar Decomol</button>
                </div>
                <div class="column" v-else-if="decomol2.liberado==true">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/VD.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p>Decomol 2</p>
                    <router-link v-bind:to="'/fabricacao/detalhes/' + decomol2.id"><span class='tag is-link'>Detalhes</span></router-link> <br>
                    <button class="button" @click="trocarDecomol(decomol2)">Trocar Decomol</button>
                </div>
                <div class="column" v-else>
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/V.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p>Decomol 2</p>
                    <router-link v-bind:to="'/fabricacao/detalhes/' + decomol2.id"><span class='tag is-link'>Detalhes</span></router-link> <br>
                    <button class="button" @click="trocarDecomol(decomol2)">Trocar Decomol</button>
                </div>

                <div class="column" v-if="decomol3.troca_decomol==true">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/A.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p>Decomol 3</p>
                    <router-link v-bind:to="'/fabricacao/detalhes/' + decomol3.id"><span class='tag is-link'>Detalhes</span></router-link> <br>
                    <button class="button" @click="trocarDecomol(decomol3)">Trocar Decomol</button>
                </div>
                <div class="column" v-else-if="decomol3.liberado==true">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/VD.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p>Decomol 3</p>
                    <router-link v-bind:to="'/fabricacao/detalhes/' + decomol3.id"><span class='tag is-link'>Detalhes</span></router-link> <br>
                    <button class="button" @click="trocarDecomol(decomol3)">Trocar Decomol</button>
                </div>
                <div class="column" v-else>
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/V.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
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
                status3: null,
                sinal: []
            } 
        },
        created() {
            this.getDecomol1()
            this.getDecomol1Status()
            this.getDecomol2()
            this.getDecomol2Status()
            this.getDecomol3()
            this.getDecomol3Status()
            this.getSignalDecomol()
        },
        methods: {
            getDecomol1() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '1',
                }) .then (response => {
                    this.decomol1 = response.data})
                setTimeout(this.getDecomol1, 2000)
            },

            getDecomol1Status() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '1',
                }) .then (response => {
                    this.status1 = response.data.troca_decomol})
            },

            getDecomol2() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '2',
                }) .then (response => this.decomol2 = response.data)
                setTimeout(this.getDecomol2, 2000)
            },

            getDecomol2Status() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '2',
                }) .then (response => {
                    this.status2 = response.data.troca_decomol})
            },

            getDecomol3() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '3',
                }) .then (response => {
                    this.decomol3 = response.data,
                    this.status3 = response.data.troca_decomol
                    })
                setTimeout(this.getDecomol3, 2000)
            },

            getDecomol3Status() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '3',
                }) .then (response => {
                    this.status3 = response.data.troca_decomol})
            },

            getSignalDecomol(){
                var axios = require('axios');
                var data = JSON.stringify("DECOMOL");

                var config = {
                method: 'post',
                url: 'http://10.15.100.110:50000/api/ObterValores',
                headers: { 
                    'Content-Type': 'application/json'
                },
                data : data
                };

                axios(config)
                .then(response =>
                    this.sinal = response.data
                )
                .catch(function (error) {
                console.log(error);
                });
            },


            getProducao(nome){ 
                for(let i = 0; i < this.sinal.length; i++){
                    if (this.sinal[i].nome == nome){
                        if(this.sinal[i].valor == 1){
                            return true
                        }
                        else{
                            return false
                        }
                    }
                }
            },

            checker(nomeProd, troca){
                var a = troca
                var b = this.getProducao(nomeProd)
                

                if(!a && b){
                    return "Regenerando"
                }
                else if(a && b){
                    return "StandBy"
                }
                else{
                    return "Produzindo"
                }
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
                const c = confirm("Deseja trocar o " + decomol.producao+"?")
                if (c) {
                    axios.post(process.env.VUE_APP_ROOT_URL_TROCA, {
                        decomol_troca: decomol.producao
                    })

                    axios.put(process.env.VUE_APP_ROOT_URL + decomol.id + '/', {
                        resultado_cor: "",
                        sensorial: "",
                        ph: "",
                        brix: "",
                        producao: decomol.producao,
                        liberado: false,
                        troca_decomol: true,
                        data_liberacao: null
                    })
                }
                    
                    //  .then(response => {
                    //     console.log(response.data)
                    // })
            }

        },

        ready() {
            this.getDecomol1()
            this.getDecomol2()
            this.getDecomol3()
            this.getSignalDecomol()
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
        /* margin-top: 40vh; */
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