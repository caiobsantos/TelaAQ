<template>
    <div class="decomol-container">
        <navbar></navbar>
        <div class="decs">
                    <div class="dec" v-if="decomol1.regenerando">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/Regenerando.svg" alt="sla" width="275" y="-15%" x="3%"/>
                        </svg>
                        <!-- colocar um ONFOCUS mostrando os resultados da ultima analise -->
                        <p class="historico"><router-link class="historico" v-bind:to="'/historico/decomol1'"><b>Decomol 1</b></router-link></p>
                        <div class="spec">
                            Início Regeneração: {{formatData(decomol1.data_liberacao)}} <br>
                        </div>
                        <!-- <router-link class="links" to='/historico/decomol1'><span class="historico">Ver Mais</span></router-link> <br> -->
                        <router-link class="links" v-bind:to="'/decomol/' + decomol1.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>
                    <div class="dec" v-else-if="decomol1.liberado">
                        <div v-if="decomol1.produzindo">
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Produzindo.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p class="historico"><router-link class="historico" v-bind:to="'/historico/decomol1'"><b>Decomol 1</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                            </div>
                            <router-link class="links" v-bind:to="'/decomol/' + decomol1.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                        </div>
                        <div v-else>
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Standby.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p class="historico"><router-link class="historico" v-bind:to="'/historico/decomol1'"><b>Decomol 1</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                            </div>
                            <router-link class="links" v-bind:to="'/decomol/' + decomol1.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                        </div>
                    </div>
                    <div class="dec" v-else>
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/V.svg" alt="sla" width="135" y="0%" x="26%"/>
                        </svg>
                        <p class="historico"><router-link class="historico" v-bind:to="'/historico/decomol1'"><b>Decomol 1</b></router-link></p>
                        <div class="spec">
                                Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                        </div>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol1.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>
                
                    <div class="dec" v-if="decomol2.regenerando">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/Regenerando.svg" alt="sla" width="275" y="-15%" x="3%"/>
                        </svg>  
                        <!-- colocar um ONFOCUS mostrando os resultados da ultima analise -->
                        <p class="historico"><router-link class="historico" v-bind:to="'/historico/decomol2'"><b>Decomol 2</b></router-link></p>
                        <div class="spec">
                            Início Regeneração: {{formatData(decomol2.data_liberacao)}} <br>
                        </div>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol2.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>
                    <div class="dec" v-else-if="decomol2.liberado">
                        <div v-if="decomol2.produzindo">
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Produzindo.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p class="historico"><router-link class="historico" v-bind:to="'/historico/decomol2'"><b>Decomol 2</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol2.data_liberacao)}} <br>
                            </div>
                            <router-link class="links" v-bind:to="'/decomol/' + decomol2.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                        </div>
                        <div v-else>
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Standby.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p class="historico"><router-link class="historico" v-bind:to="'/historico/decomol2'"><b>Decomol 2</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol2.data_liberacao)}} <br>
                            </div>
                            <router-link class="links" v-bind:to="'/decomol/' + decomol2.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                        </div>
                    </div>
                    <div class="dec" v-else>
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/V.svg" alt="sla" width="135" y="0%" x="26%"/>
                        </svg>
                        <p class="historico"><router-link class="historico" v-bind:to="'/historico/decomol2'"><b>Decomol 2</b></router-link></p>
                        <div class="spec">
                            Última Análise: {{formatData(decomol2.data_liberacao)}} <br>
                        </div>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol2.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>

                    <div class="dec" v-if="decomol3.regenerando">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/Regenerando.svg" alt="sla" width="275" y="-15%" x="3%"/>
                        </svg>
                        <!-- colocar um ONFOCUS mostrando os resultados da ultima analise -->
                        <p class="historico"><router-link class="historico" v-bind:to="'/historico/decomol3'"><b>Decomol 3</b></router-link></p>
                        <div class="spec">
                            Início Regeneração: {{formatData(decomol3.data_liberacao)}} <br>
                        </div>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol3.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>
                    <div class="dec" v-else-if="decomol3.liberado">
                        <div v-if="decomol3.produzindo">
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Produzindo.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p class="historico"><router-link class="historico" v-bind:to="'/historico/decomol3'"><b>Decomol 3</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol3.data_liberacao)}} <br>
                            </div>
                            <router-link class="links" v-bind:to="'/decomol/' + decomol3.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                        </div>
                        <div v-else>
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Standby.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p class="historico"><router-link class="historico" v-bind:to="'/historico/decomol3'"><b>Decomol 3</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol3.data_liberacao)}} <br>
                            </div>
                            <router-link class="links" v-bind:to="'/decomol/' + decomol3.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                        </div>
                    </div>
                    <div class="dec" v-else>
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/V.svg" alt="sla" width="135" y="0%" x="26%"/>
                        </svg>
                        <p class="historico"><router-link class="historico" v-bind:to="'/historico/decomol3'"><b>Decomol 3</b></router-link></p>
                        <div class="spec">
                            Última Análise: {{formatData(decomol3.data_liberacao)}} <br>
                        </div>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol3.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import moment from 'moment'
    import navbar from '@/components/NavBarLab.vue'

    // criar funcionalidade para a pagina atualizar apenas quando houver alguma alteracao nos elementos

    export default {
        name: 'AQDecomolView',
        components: {navbar},
        data() {
            return{
                decomol1: [],
                decomol2: [],
                decomol3: [],
                sinal: [],
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

<style>
    *{
        margin: 0px;
        padding: 0px;
        box-sizing: border-box; 
    }

    .decomol-container { 
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        background-color: lightgray;
    }

    .decs{
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        justify-content: space-around;
        min-height: 90vh;
        padding-top: 50px;
        padding-bottom: 50px;
    }

    .dec{
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .historico{
        padding-top: 5px;
        font-size: 18px;
        color: black;
    }

    .historico :hover{
        color: black;
        border-bottom: 1px black solid;
        transition-delay: 50ms;
    }

    .tag {
        position: relative;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }

   .svg{
        position: relative;
   }

   .spec{
    color: black;
   }

   @media(max-width: 1000px){
    .tag {
        position: relative;
        margin-top: 0.75rem;
        margin-bottom: 0.75rem;
    }
   }

   @media (max-width: 1150px){
    .decs{
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        justify-content: space-around;
        min-height: 90vh;
        padding-top: 50px;
        padding-bottom: 50px;
        gap: 50px;
    }
   }

</style>