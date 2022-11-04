<template>
    <div class="decomol-container">
        <div class="columns">
                    <div class="column is-one-third" v-if="decomol1.troca_decomol==true">
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/A.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                        </svg>
                        <!-- colocar um ONFOCUS mostrando os resultados da ultima analise -->
                        <p><b>Decomol 1</b></p>
                        <router-link class="links" v-bind:to="'/decomol/' + decomol1.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                        <router-link class="links" to='/historico/decomol1'><span class='tag is-link'>Histórico</span></router-link>
                    </div>
                    <div class="column is-one-third" v-else-if="decomol1.liberado==true">
                        <!-- <button :class= " corAtual(decomol1.liberado, decomol1.troca_decomol) ">
                            {{ decomolStatus(decomol1.liberado, decomol1.troca_decomol) }}
                        </button> -->
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/VD.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                        </svg>
                        <p><b>Decomol 1</b></p>
                        <div class="spec">
                            Data da Liberação: {{formatData(decomol1.data_liberacao)}} <br>
                            Resultado cor: {{decomol1.resultado_cor}}<br>
                            Sensorial: {{decomol1.sensorial}}<br>
                            Brix: {{decomol1.brix}}<br>
                            Ph: {{decomol1.ph}}<br>
                        </div>
                        <router-link class="links" to='/historico/decomol1'><span class='tag is-link'>Histórico</span></router-link>
                    </div>
                    <div class="column is-one-third" v-else>
                        <!-- <button :class= " corAtual(decomol1.liberado, decomol1.troca_decomol) ">
                            {{ decomolStatus(decomol1.liberado, decomol1.troca_decomol) }}
                        </button> -->
                        <svg class="svg" width="300" height="300">
                            <image href="../assets/tanques/V.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                        </svg>
                        <p><b>Decomol 1</b></p>
                        <div class="spec">
                            Data da Liberação: {{formatData(decomol1.data_liberacao)}} <br>
                            Resultado cor: {{decomol1.resultado_cor}}<br>
                            Sensorial: {{decomol1.sensorial}}<br>
                            Brix: {{decomol1.brix}}<br>
                            Ph: {{decomol1.ph}}<br>
                        </div>
                        <router-link class="links" to='/historico/decomol1'><span class='tag is-link'>Histórico</span></router-link>
                    </div>
                <div class="column" v-if="decomol2.troca_decomol == true">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/A.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><b>Decomol 2</b></p>
                    <router-link class="links" v-bind:to="'/decomol/' + decomol2.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                    <router-link class="links" to='/historico/decomol2'><span class='tag is-link'>Histórico</span></router-link>
                </div>
                <div class="column" v-else-if="decomol2.liberado==true">
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
                <div class="column" v-if="decomol3.troca_decomol == true">
                    <svg class="svg" width="300" height="300">
                        <image href="../assets/tanques/A.svg" alt="sla" heigth="90" width="130" y="0%" x="27%"/>
                    </svg>
                    <p><b>Decomol 3</b></p>
                    <router-link class="links" v-bind:to="'/decomol/' + decomol3.id"><span class='tag is-link'>Registrar Análise</span></router-link> <br>
                    <router-link class="links" to='/historico/decomol3'><span class='tag is-link'>Histórico</span></router-link> 
                </div>
                <div class="column" v-else-if="decomol3.liberado==true">
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
            } 
        },
        mounted() {
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
    }

   .svg{
    position: relative;
   }


</style>