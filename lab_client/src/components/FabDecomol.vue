<template>
    <div class="decomol-container">
        <div class="columns">
                <div class="column is-one-third" v-if="decomol1.regenerando">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/Regenerando.svg" alt="sla" width="275" y="-15%" x="3%"/>
                        </svg>
                        <!-- colocar um ONFOCUS mostrando os resultados da ultima analise -->
                        <p><router-link class="historico" v-bind:to="'/fab/historico/decomol1'"><b>Decomol 1</b></router-link></p>
                        <div class="spec">
                            <p>Início Regeneração: {{formatData(decomol1.data_liberacao)}}</p>
                            <p><b>{{decomolStatus(decomol1.liberado)}}</b></p>
                        </div>
                        <button class="button" @click="concluirDecomol(decomol1, id=1)">Concluir Regeneração</button>
                    </div>
                    <div class="column is-one-third" v-else-if="decomol1.liberado">
                        <div v-if="decomol1.produzindo">
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Produzindo.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p><router-link class="historico" v-bind:to="'/fab/historico/decomol1'"><b>Decomol 1</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                            </div>
                            <div class="field is-grouped" id="maior">
                                <p class="control">
                                    <button class="button is-warning" @click="produzirDecomol(decomol1)">
                                        Finalizar Produção
                                    </button>
                                </p>
                                <p class="control">
                                    <button class="button is-danger" @click="trocarDecomol(decomol1, id=1)">
                                        Regenerar Decomol
                                    </button>
                                </p>
                            </div>
                        </div>
                        <div v-else>
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Standby.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p><router-link class="historico" v-bind:to="'/fab/historico/decomol1'"><b>Decomol 1</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                            </div>
                            <!-- <button class="button" @click="trocarDecomol(decomol1)">Regenerar Decomol</button> -->
                            <div class="field is-grouped">
                                <p class="control">
                                    <button class="button is-success" @click="produzirDecomol(decomol1)">
                                        Iniciar Produção
                                    </button>
                                </p>
                                <p class="control">
                                    <button class="button is-danger" @click="trocarDecomol(decomol1, id=1)">
                                        Regenerar Decomol
                                    </button>
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="column is-one-third" v-else>
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/V.svg" alt="sla" width="135" y="0%" x="26%"/>
                        </svg>
                        <p><router-link class="historico" v-bind:to="'/fab/historico/decomol1'"><b>Decomol 1</b></router-link></p>
                        <div class="spec">
                            Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                        </div>
                        <button class="button" @click="trocarDecomol(decomol1, id=1)">Regenerar Decomol</button>
                    </div>
                
                    <div class="column" v-if="decomol2.regenerando">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/Regenerando.svg" alt="sla" width="275" y="-15%" x="3%"/>
                        </svg>  
                        <!-- colocar um ONFOCUS mostrando os resultados da ultima analise -->
                        <p><router-link class="historico" v-bind:to="'/fab/historico/decomol2'"><b>Decomol 2</b></router-link></p>
                        <div class="spec">
                            <p>Início Regeneração: {{formatData(decomol2.data_liberacao)}}</p>
                            <p><b>{{decomolStatus(decomol2.liberado)}}</b></p>
                        </div>
                        <button class="button" @click="concluirDecomol(decomol2, id=2)">Concluir Regeneração</button>
                    </div>
                    <div class="column is-one-third" v-else-if="decomol2.liberado">
                        <div v-if="decomol2.produzindo">
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Produzindo.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p><router-link class="historico" v-bind:to="'/fab/historico/decomol2'"><b>Decomol 2</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol2.data_liberacao)}} <br>
                            </div>
                            <div class="field is-grouped" id="maior">
                                <p class="control">
                                    <button class="button is-warning" @click="produzirDecomol(decomol2)">
                                        Finalizar Produção
                                    </button>
                                </p>
                                <p class="control">
                                    <button class="button is-danger" @click="trocarDecomol(decomol2, id=2)">
                                        Regenerar Decomol
                                    </button>
                                </p>
                            </div>
                        </div>
                        <div v-else>
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Standby.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p><router-link class="historico" v-bind:to="'/fab/historico/decomol2'"><b>Decomol 2</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol2.data_liberacao)}} <br>
                            </div>
                            <div class="field is-grouped">
                                <p class="control">
                                    <button class="button is-success" @click="produzirDecomol(decomol2)">
                                        Iniciar Produção
                                    </button>
                                </p>
                                <p class="control">
                                    <button class="button is-danger" @click="trocarDecomol(decomol2, id=2)">
                                        Regenerar Decomol
                                    </button>
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="column is-one-third" v-else>
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/V.svg" alt="sla" width="135" y="0%" x="26%"/>
                        </svg>
                        <p><router-link class="historico" v-bind:to="'/fab/historico/decomol2'"><b>Decomol 2</b></router-link></p>
                        <div class="spec">
                            Última Análise: {{formatData(decomol2.data_liberacao)}} <br>
                        </div>
                        <button class="button" @click="trocarDecomol(decomol2, id=2)">Regenerar Decomol</button>
                    </div>

                    <div class="column" v-if="decomol3.regenerando">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/Regenerando.svg" alt="sla" width="275" y="-15%" x="3%"/>
                        </svg>
                        <!-- colocar um ONFOCUS mostrando os resultados da ultima analise -->
                        <p><router-link class="historico" v-bind:to="'/fab/historico/decomol3'"><b>Decomol 3</b></router-link></p>
                        <div class="spec">
                            <p>Início Regeneração: {{formatData(decomol3.data_liberacao)}}</p>
                            <p><b>{{decomolStatus(decomol3.liberado)}}</b></p>
                        </div>
                        <button class="button" @click="concluirDecomol(decomol3, id=3)">Concluir Regeneração</button>
                    </div>
                    <div class="column is-one-third" v-else-if="decomol3.liberado">
                        <div v-if="decomol3.produzindo">
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Produzindo.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p><router-link class="historico" v-bind:to="'/fab/historico/decomol3'"><b>Decomol 3</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol3.data_liberacao)}} <br>
                            </div>
                            <div class="field is-grouped" id="maior">
                                <p class="control">
                                    <button class="button is-warning" @click="produzirDecomol(decomol3)">
                                        Finalizar Produção
                                    </button>
                                </p>
                                <p class="control">
                                    <button class="button is-danger" @click="trocarDecomol(decomol3, id=3)">
                                        Regenerar Decomol
                                    </button>
                                </p>
                            </div>
                        </div>
                        <div v-else>
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Standby.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p><router-link class="historico" v-bind:to="'/fab/historico/decomol3'"><b>Decomol 3</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol3.data_liberacao)}} <br>
                            </div>
                            <div class="field is-grouped">
                                <p class="control">
                                    <button class="button is-success" >
                                        Iniciar Produção
                                    </button>
                                </p>
                                <p class="control">
                                    <button class="button is-danger" @click="trocarDecomol(decomol3, id=3)">
                                        Regenerar Decomol
                                    </button>
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="column is-one-third" v-else>
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/V.svg" alt="sla" width="135" y="0%" x="26%"/>
                        </svg>
                        <p><router-link class="historico" v-bind:to="'/fab/historico/decomol3'"><b>Decomol 3</b></router-link></p>
                        <div class="spec">
                            Última Análise: {{formatData(decomol3.data_liberacao)}} <br>
                        </div>
                        <button class="button" @click="trocarDecomol(decomol3, id=3)">Regenerar Decomol</button>
                    </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import moment from 'moment'

    export default {
        name: 'FabDecomolView',
        data() {
            return{
                decomol1: [],
                decomol2: [],
                decomol3: [],
                id1: 0,
                id2: 0,
                id3: 0
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
                }) .then (response => {
                    this.decomol1 = response.data})
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
                }) .then (response => {
                    this.decomol3 = response.data,
                    this.status3 = response.data.regenerando
                    })
                setTimeout(this.getDecomol3, 2000)
            },

            decomolStatus(status){
                 if (status == true){
                    return 'Liberado'
                }
                else if (status == false){
                    return 'Não Liberado'
                }
            },

            trocarDecomol(decomol, id){
                const c = confirm("Deseja regenerar o " + decomol.producao+"?")
                if (c) {
                    axios.post(process.env.VUE_APP_ROOT_URL_TROCA, {
                        decomol_troca: decomol.producao
                    }) .then(response => {
                        if(id==1){
                            this.id1 = response.data.id
                        }
                        else if(id==2){
                            this.id2 = response.data.id
                        }
                        else{
                            this.id3 = response.data.id
                        }
                    })

                    axios.put(process.env.VUE_APP_ROOT_URL + decomol.id + '/', {
                        resultado_cor: "",
                        sensorial: "",
                        ph: "",
                        brix: "",
                        producao: decomol.producao,
                        regenerando: true,
                        produzindo: false,
                        liberado: false,
                    })
                }
                    
                    //  .then(response => {
                    //     console.log(response.data)
                    // })
            },

            concluirDecomol(decomol, id){
                const c = confirm("Deseja finalizar a regeneração do " + decomol.producao+"?")
                if(c){
                    axios.put(process.env.VUE_APP_ROOT_URL + decomol.id + '/', {
                        producao: decomol.producao,
                        regenerando: false,
                    })
                    if(id==1){
                        axios.put(process.env.VUE_APP_ROOT_URL_TROCA +  this.id1 + '/', {
                            decomol_troca: decomol.producao
                        })
                    }
                    else if(id==2){
                        axios.put(process.env.VUE_APP_ROOT_URL_TROCA +  this.id2 + '/', {
                            decomol_troca: decomol.producao
                        })
                    }
                    else{
                        axios.put(process.env.VUE_APP_ROOT_URL_TROCA +  this.id3 + '/', {
                            decomol_troca: decomol.producao
                        })
                    }
                }
            },

            produzirDecomol(decomol){

                if(decomol.produzindo == true){
                    const c = confirm("Deseja finalizar a produção do " + decomol.producao+"?")
                    if(c){
                        axios.put(process.env.VUE_APP_ROOT_URL + decomol.id + '/', {
                            producao: decomol.producao,
                            produzindo: false,
                    })
                    }
                }
                
                else{
                    const c = confirm("Deseja iniciar a produção do " + decomol.producao+"?")
                    if(c){
                        axios.put(process.env.VUE_APP_ROOT_URL + decomol.id + '/', {
                            producao: decomol.producao,
                            produzindo: true,
                    })
                    }
               }
            },

            formatData(data) {
            return moment(data).format('DD/MM/YY [-] HH:mm:ss')
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

    #maior{
        margin-left: 3.0rem;
    }

    .field{
        display: flex;
        padding: auto;  
        margin-top: 1.0rem;
        margin-left: 3.75rem;
    }

</style>