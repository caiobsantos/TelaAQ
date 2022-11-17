<template>
    <div class="decomol-container">
        <div class="columns">
                <div class="column is-one-third" v-if="checker('DECOMOL_1_PRODUCAO', decomol1.regenerando) == 'StandBy'">
                    <div v-if="decomol1.liberado">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/A.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                        </svg>
                        <p><router-link v-bind:to="'/fabricacao/detalhes/' + decomol1.id"><b>Decomol 1</b></router-link></p>
                        <div class="spec">
                            Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                        </div>
                        <button class="button" @click="trocarDecomol(decomol1)">Regenerar Decomol</button>
                    </div>
                    <div v-else>
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/V.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                        </svg>
                        <p><router-link v-bind:to="'/fabricacao/detalhes/' + decomol1.id"><b>Decomol 1</b></router-link></p>
                        <div class="spec">
                            Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                        </div>
                        <button class="button" @click="trocarDecomol(decomol1)">Regenerar Decomol</button>
                    </div>
                </div>
                <div class="column is-one-third" v-else-if="checker('DECOMOL_1_PRODUCAO', decomol1.regenerando) == 'Produzindo'">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/VD.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><router-link v-bind:to="'/fabricacao/detalhes/' + decomol1.id"><b>Decomol 1</b></router-link></p>
                    <div class="spec">
                            Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                    </div>
                    <button class="button" @click="trocarDecomol(decomol1)">Regenerar Decomol</button>
                </div>
                <div class="column is-one-third" v-else>
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/V.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                        </svg>
                        <p><router-link v-bind:to="'/fabricacao/detalhes/' + decomol1.id"><b>Decomol 1</b></router-link></p>
                        <div class="spec">
                            Início Regeneração: {{formatData(decomol1.data_liberacao)}} <br>
                            <b>{{decomolStatus(decomol1.liberado)}}</b> <br>
                        </div>
                        <button class="button" @click="concluirDecomol(decomol1)">Concluir Regeneração</button>
                </div>

                <div class="column" v-if="checker('DECOMOL_2_PRODUCAO', decomol2.regenerando) == 'StandBy'">
                    <div v-if="decomol2.liberado">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/A.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                        </svg>
                        <p><router-link v-bind:to="'/fabricacao/detalhes/' + decomol2.id"><b>Decomol 2</b></router-link></p>
                        <div class="spec">
                            Última Análise: {{formatData(decomol2.data_liberacao)}} <br>
                        </div>
                        <button class="button" @click="trocarDecomol(decomol2)">Regenerar Decomol</button>
                    </div>
                    <div class="column is-one-third" v-else-if="checker('DECOMOL_2_PRODUCAO', decomol2.regenerando) == 'Produzindo'">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/VD.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><router-link v-bind:to="'/fabricacao/detalhes/' + decomol2.id"><b>Decomol 2</b></router-link></p>
                    <div class="spec">
                            Última Análise: {{formatData(decomol2.data_liberacao)}} <br>
                    </div>
                    <button class="button" @click="trocarDecomol(decomol2)">Regenerar Decomol</button>
                </div>
                </div>
                <div class="column" v-else-if="checker('DECOMOL_2_PRODUCAO', decomol2.regenerando) == 'Produzindo'">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/VD.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><router-link v-bind:to="'/fabricacao/detalhes/' + decomol2.id"><b>Decomol 2</b></router-link></p>
                    <div class="spec">
                            Última Análise: {{formatData(decomol2.data_liberacao)}} <br>
                    </div>
                    <button class="button" @click="trocarDecomol(decomol2)">Regenerar Decomol</button>
                </div>
                <div class="column" v-else>
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/V.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><router-link v-bind:to="'/fabricacao/detalhes/' + decomol2.id"><b>Decomol 2</b></router-link></p>
                    <div class="spec">
                            Início Regeneração:{{formatData(decomol2.data_liberacao)}} <br>
                            Última Análise: {{decomolStatus(decomol2.liberado)}}<br>
                    </div>
                    <button class="button" @click="trocarDecomol(decomol2)">Concluir Regeneração</button>
                </div>

                <div class="column" v-if="checker('DECOMOL_3_PRODUCAO', decomol3.regenerando) == 'StandBy'">
                    <div v-if="decomol3.liberado">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/A.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                        </svg>
                        <p><router-link v-bind:to="'/fabricacao/detalhes/' + decomol3.id"><b>Decomol 3</b></router-link></p>
                        <div class="spec">
                            Última Análise: {{formatData(decomol3.data_liberacao)}} <br>
                        </div>
                        <button class="button" @click="trocarDecomol(decomol3)">Regenerar Decomol</button>
                    </div>
                    <div class="column is-one-third" v-else-if="checker('DECOMOL_3_PRODUCAO', decomol3.regenerando) == 'Produzindo'">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/VD.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><router-link v-bind:to="'/fabricacao/detalhes/' + decomol3.id"><b>Decomol 3</b></router-link></p>
                    <div class="spec">
                            Última Análise: {{formatData(decomol3.data_liberacao)}} <br>
                    </div>
                    <button class="button" @click="trocarDecomol(decomol3)">Regenerar Decomol</button>
                </div>
                </div>
                <div class="column" v-else-if="checker('DECOMOL_3_PRODUCAO', decomol3.regenerando) == 'Produzindo'">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/VD.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><router-link v-bind:to="'/fabricacao/detalhes/' + decomol3.id"><b>Decomol 3</b></router-link></p>
                    <div class="spec">
                            Última Análise: {{formatData(decomol3.data_liberacao)}} <br>
                    </div>
                    <button class="button" @click="trocarDecomol(decomol3)">Regenerar Decomol</button>
                </div>
                <div class="column" v-else>
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/V.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><router-link v-bind:to="'/fabricacao/detalhes/' + decomol3.id"><b>Decomol 3</b></router-link></p>
                    <div class="spec">
                            <b>Início Regeneração:</b> {{formatData(decomol3.data_liberacao)}} <br>
                            <b>{{decomolStatus(decomol3.liberado)}}</b> <br>
                    </div>
                    <button class="button" @click="trocarDecomol(decomol3)">Concluir Regeneração</button>
                </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import moment from 'moment'

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
                    this.status1 = response.data.regenerando})
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
                    this.status2 = response.data.regenerando})
            },

            getDecomol3() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '3',
                }) .then (response => {
                    this.decomol3 = response.data,
                    this.status3 = response.data.regenerando
                    })
                setTimeout(this.getDecomol3, 2000)
            },

            getDecomol3Status() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + '3',
                }) .then (response => {
                    this.status3 = response.data.regenerando})
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

            checker(nomeProd, regenerando){
                var a = regenerando
                var b = this.getProducao(nomeProd)
                

                if(a && b){
                    return "Regenerando"
                }
                else if(!a && b){
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

            decomolStatus(status){
                 if (status == true){
                    return 'Liberado'
                }
                else if (status == false){
                    return 'Não Liberado'
                }
            },

            trocarDecomol(decomol){
                const c = confirm("Deseja regenerar o " + decomol.producao+"?")
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
                        regenerando: true,
                    })
                }
                    
                    //  .then(response => {
                    //     console.log(response.data)
                    // })
            },

            concluirDecomol(decomol){
                axios.put(process.env.VUE_APP_ROOT_URL + decomol.id + '/', {
                        producao: decomol.producao,
                        liberado: false,
                        regenerando: false,
                    })
            },

            formatData(data) {
            return moment(data).format('DD/MM/YY [-] HH:mm:ss')
            },

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
        margin-top: 0.5rem;
        margin-bottom: 1.0rem;
    }

    .spec{
        position: inherit;
        text-align: center;
        margin-top: 5px;
        margin-bottom: 0.5rem;
    }
</style>