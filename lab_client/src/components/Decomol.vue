<template>
    <div class="decomol-container">
        <div class="columns">
                    <div class="column is-one-third" v-if="decomol1.regenerando">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/Regenerando.svg" alt="sla" width="275" y="-15%" x="3%"/>
                        </svg>
                        <!-- colocar um ONFOCUS mostrando os resultados da ultima analise -->
                        <p><router-link class="historico" v-bind:to="'/historico/decomol1'"><b>Decomol 1</b></router-link></p>
                        <div class="spec">
                            Início Regeneração: {{formatData(decomol1.data_liberacao)}} <br>
                        </div>
                        <!-- <router-link class="links" to='/historico/decomol1'><span class="historico">Ver Mais</span></router-link> <br> -->
                        <router-link class="links" v-bind:to="'/decomol/' + decomol1.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>
                    <div class="column is-one-third" v-else-if="decomol1.liberado">
                        <div v-if="decomol1.produzindo">
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Produzindo.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p><router-link class="historico" v-bind:to="'/historico/decomol1'"><b>Decomol 1</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                            </div>
                            <router-link class="links" v-bind:to="'/decomol/' + decomol1.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                        </div>
                        <div v-else>
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Standby.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p><router-link class="historico" v-bind:to="'/historico/decomol1'"><b>Decomol 1</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                            </div>
                            <router-link class="links" v-bind:to="'/decomol/' + decomol1.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                        </div>
                    </div>
                    <div class="column is-one-third" v-else>
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/V.svg" alt="sla" width="135" y="0%" x="26%"/>
                        </svg>
                        <p><router-link class="historico" v-bind:to="'/historico/decomol1'"><b>Decomol 1</b></router-link></p>
                        <div class="spec">
                            Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                        </div>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol1.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>
                
                    <div class="column" v-if="decomol2.regenerando">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/Regenerando.svg" alt="sla" width="275" y="-15%" x="3%"/>
                        </svg>  
                        <!-- colocar um ONFOCUS mostrando os resultados da ultima analise -->
                        <p><router-link class="historico" v-bind:to="'/historico/decomol2'"><b>Decomol 2</b></router-link></p>
                        <div class="spec">
                            Início Regeneração: {{formatData(decomol2.data_liberacao)}} <br>
                        </div>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol2.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>
                    <div class="column is-one-third" v-else-if="decomol2.liberado">
                        <div v-if="decomol2.produzindo">
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Produzindo.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p><router-link class="historico" v-bind:to="'/historico/decomol2'"><b>Decomol 2</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol2.data_liberacao)}} <br>
                            </div>
                            <router-link class="links" v-bind:to="'/decomol/' + decomol2.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                        </div>
                        <div v-else>
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Standby.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p><router-link class="historico" v-bind:to="'/historico/decomol2'"><b>Decomol 2</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol2.data_liberacao)}} <br>
                            </div>
                            <router-link class="links" v-bind:to="'/decomol/' + decomol2.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                        </div>
                    </div>
                    <div class="column is-one-third" v-else>
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/V.svg" alt="sla" width="135" y="0%" x="26%"/>
                        </svg>
                        <p><router-link class="historico" v-bind:to="'/historico/decomol2'"><b>Decomol 2</b></router-link></p>
                        <div class="spec">
                            Última Análise: {{formatData(decomol2.data_liberacao)}} <br>
                        </div>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol2.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>

                    <div class="column" v-if="decomol3.regenerando">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/Regenerando.svg" alt="sla" width="275" y="-15%" x="3%"/>
                        </svg>
                        <!-- colocar um ONFOCUS mostrando os resultados da ultima analise -->
                        <p><router-link class="historico" v-bind:to="'/historico/decomol3'"><b>Decomol 3</b></router-link></p>
                        <div class="spec">
                            Início Regeneração: {{formatData(decomol3.data_liberacao)}} <br>
                        </div>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol3.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>
                    <div class="column is-one-third" v-else-if="decomol3.liberado">
                        <div v-if="decomol3.produzindo">
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Produzindo.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p><router-link class="historico" v-bind:to="'/historico/decomol3'"><b>Decomol 3</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol3.data_liberacao)}} <br>
                            </div>
                            <router-link class="links" v-bind:to="'/decomol/' + decomol3.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                        </div>
                        <div v-else>
                            <svg class="svg" width="300" height="300">
                                <image href="../assets/tanques/Standby.svg" alt="sla" width="275" y="-15%" x="3%"/>
                            </svg>
                            <p><router-link class="historico" v-bind:to="'/historico/decomol3'"><b>Decomol 3</b></router-link></p>
                            <div class="spec">
                                Última Análise: {{formatData(decomol3.data_liberacao)}} <br>
                            </div>
                            <router-link class="links" v-bind:to="'/decomol/' + decomol3.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                        </div>
                    </div>
                    <div class="column is-one-third" v-else>
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/V.svg" alt="sla" width="135" y="0%" x="26%"/>
                        </svg>
                        <p><router-link class="historico" v-bind:to="'/historico/decomol3'"><b>Decomol 3</b></router-link></p>
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

    // criar funcionalidade para a pagina atualizar apenas quando houver alguma alteracao nos elementos

    export default {
        name: 'AQDecomolView',
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
                    url: 'http://192.168.0.199:8000/' + '1',
                }) .then (response => this.decomol1 = response.data)
                setTimeout(this.getDecomol1, 2000)
            },

            getDecomol2() {
                axios({
                    method: 'get',
                    url: 'http://192.168.0.199:8000/' + '2',
                }) .then (response => this.decomol2 = response.data)
                setTimeout(this.getDecomol2, 2000)
            },

            getDecomol3() {
                axios({
                    method: 'get',
                    url: 'http://192.168.0.199:8000/' + '3',
                }) .then (response => this.decomol3 = response.data)
                setTimeout(this.getDecomol3, 2000)
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
        position: relative;
        margin-top: 1.5rem;
    }

    .columns {
        position: relative;
        /* margin-top: 20vh; */
    }

    button {
        margin-bottom: 1.0rem;
    }

    .tag {
        position: relative;
        margin-top: 1.0rem;
        
    }

    .spec{
        position: inherit;
        text-align: center;
        margin-top: 5px;
        margin-bottom: 0.5rem;
    }

   .svg{
        position: relative;
   }

</style>