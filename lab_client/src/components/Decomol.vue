<template>
    <div class="decomol-container">
        <div class="columns">
                    <div class="column is-one-third" v-if="checker('DECOMOL_1_PRODUCAO', decomol1.regenerando) == 'StandBy'">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/A.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                        </svg>
                        <!-- colocar um ONFOCUS mostrando os resultados da ultima analise -->
                        <p><b>Decomol 1</b></p>
                        <div class="spec">
                            Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                        </div>
                        <router-link class="links" to='/historico/decomol1'><span class="historico">Ver Mais</span></router-link> <br>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol1.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>
                    <div class="column is-one-third" v-else-if="checker('DECOMOL_1_PRODUCAO', decomol1.regenerando) == 'Produzindo'">
                        <!-- <button :class= " corAtual(decomol1.liberado, decomol1.regenerando) ">
                            {{ decomolStatus(decomol1.liberado, decomol1.regenerando) }}
                        </button> -->
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/VD.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                        </svg>
                        <p><b>Decomol 1</b></p>
                        <div class="spec">
                            Última Análise: {{formatData(decomol1.data_liberacao)}} <br>
                        </div>
                        <router-link class="links" to='/historico/decomol1'><span class="historico">Ver Mais</span></router-link> <br>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol1.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>
                    <div class="column is-one-third" v-else>
                        <!-- <button :class= " corAtual(decomol1.liberado, decomol1.regenerando) ">
                            {{ decomolStatus(decomol1.liberado, decomol1.regenerando) }}
                        </button> -->
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/V.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                        </svg>
                        <p><b>Decomol 1</b></p>
                        <div class="spec">
                            Início Regeneração: {{formatData(decomol1.data_liberacao)}} <br>
                            
                        </div>
                        <router-link class="links" to='/historico/decomol1'><span class="historico">Ver Mais</span></router-link> <br>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol1.id"><span class='tag is-link'>Registrar Análise</span></router-link>
                    </div>
                <div class="column" v-if="checker('DECOMOL_2_PRODUCAO', decomol2.regenerando, decomol2.liberado) == 'StandBy'">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/A.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><b>Decomol 2</b></p> 
                    <router-link class="links" v-bind:to="'/decomol/' + decomol2.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                    <router-link class="links" to='/historico/decomol2'><span class='tag is-link'>Histórico</span></router-link>
                </div>
                <div class="column" v-else-if="checker('DECOMOL_2_PRODUCAO', decomol2.regenerando, decomol2.liberado) == 'Produzindo'">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/VD.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><b>Decomol 2</b></p>
                    <div class="spec">
                            Data da Liberação: {{formatData(decomol2.data_liberacao)}} <br>
                            Resultado cor: {{decomol2.resultado_cor}}<br>
                            Sensorial: {{decomol2.sensorial}}<br>
                            Brix: {{decomol2.brix}}<br>
                            Ph: {{decomol2.ph}}<br>
                        </div>
                    <router-link class="links" to='/historico/decomol2'><span class='tag is-link'>Histórico</span></router-link>
                </div>
                <div class="column" v-else>
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/V.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><b>Decomol 2</b></p>
                    <div class="spec">
                            Data da Liberação: {{formatData(decomol2.data_liberacao)}} <br>
                            Resultado cor: {{decomol2.resultado_cor}}<br>
                            Sensorial: {{decomol2.sensorial}}<br>
                            Brix: {{decomol2.brix}}<br>
                            Ph: {{decomol2.ph}}<br>
                        </div>
                    <router-link class="links" to='/historico/decomol2'><span class='tag is-link'>Histórico</span></router-link>
                </div>
                <div class="column" v-if="checker('DECOMOL_3_PRODUCAO', decomol3.regenerando, decomol3.liberado) == 'StandBy'">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/A.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><b>Decomol 3</b></p>
                    <router-link class="links" v-bind:to="'/decomol/' + decomol3.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                    <router-link class="links" to='/historico/decomol3'><span class='tag is-link'>Histórico</span></router-link> 
                </div>
                <div class="column" v-else-if="checker('DECOMOL_3_PRODUCAO', decomol3.regenerando, decomol3.liberado) == 'Produzindo'">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/VD.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><b>Decomol 3</b></p>
                    
                    <div class="spec">
                            Data da Liberação: {{formatData(decomol3.data_liberacao)}} <br>
                            Resultado cor: {{decomol3.resultado_cor}}<br>
                            Sensorial: {{decomol3.sensorial}}<br>
                            Brix: {{decomol3.brix}}<br>
                            Ph: {{decomol3.ph}}<br>
                        </div>
                    <router-link class="links" to='/historico/decomol3'><span class='tag is-link'>Histórico</span></router-link> 
                </div>
                <div class="column" v-else>
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/V.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><b>Decomol 3</b></p>
                    
                    <div class="spec">
                            Data da Liberação: {{formatData(decomol3.data_liberacao)}} <br>
                            Resultado cor: {{decomol3.resultado_cor}}<br>
                            Sensorial: {{decomol3.sensorial}}<br>
                            Brix: {{decomol3.brix}}<br>
                            Ph: {{decomol3.ph}}<br>
                        </div>
                    <router-link class="links" to='/historico/decomol3'><span class='tag is-link'>Histórico</span></router-link> 
                </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import moment from 'moment'

    // criar funcionalidade para a pagina atualizar apenas quando houver alguma alteracao nos elementos

    export default {
        name: 'DecomolView',
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
            this.getSignalDecomol()
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