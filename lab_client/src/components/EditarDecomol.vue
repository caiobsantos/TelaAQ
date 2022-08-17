<template>
    <div id='edit'>
        <form class="inputs" @submit.prevent="getDecomol" v-bind:key="decomol.id">
            <input class="input is-danger" type="text" placeholder="Resultado Cor" v-model="decomol.producao">
            <input class="input is-danger" type="text" placeholder="Resultado Cor" v-model="decomol.resultado_cor">
            <input class="input is-danger" type="text" placeholder="Sensorial" v-model="decomol.sensorial">
            <input class="input is-danger" type="text" placeholder="P.H." v-model="decomol.ph">
            <input class="input is-danger" type="text" placeholder="Brix" v-model="decomol.brix"> <br>
            <div class="StatusDecomol">
                <div v-if="getStatus() == null">
                    <label class="radio">
                        <input type="radio" name="answer" @click="liberaDecomol()">
                        Liberado
                    </label>
                    <label class="radio">
                        <input type="radio" name="answer" @click="cancelaDecomol()">
                        Não Liberado
                    </label>
                    <label class="radio">
                        <input type="radio" name="answer" @click="analisaDecomol()" checked>
                        Em Análise
                    </label>
                </div>

                <div v-else-if="getStatus() == true">
                    <label class="radio">
                        <input type="radio" name="answer" @click="liberaDecomol()" checked>
                        Liberado
                    </label>
                    <label class="radio">
                        <input type="radio" name="answer" @click="cancelaDecomol()">
                        Não Liberado
                    </label>
                     <label class="radio">
                        <input type="radio" name="answer" @click="analisaDecomol()">
                        Em Análise
                    </label>
                </div>

                  <div v-else>
                    <label class="radio">
                        <input type="radio" name="answer" @click="liberaDecomol()">
                        Liberado
                    </label>
                    <label class="radio">
                        <input type="radio" name="answer" @click="cancelaDecomol()" checked>
                        Não Liberado
                    </label>
                     <label class="radio">
                        <input type="radio" name="answer" @click="analisaDecomol()">
                        Em Análise
                    </label>
                </div>
            </div>
            <router-link to="/decomol"><button class="button is-sucess" @click="editDecomol()">Salvar</button></router-link>
        </form>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data() {
            return{
                id: this.$route.params.id,
                decomol: [],
                producao: "",
                resultado_cor: "",
                sensorial: "",
                ph: "",
                brix: "",
                liberado: null
            }
        },
        mounted() {
            this.getDecomol()
        },
        methods: {
            getDecomol() {
                axios({
                    method: 'get',
                    url: 'http://127.0.0.1:8000/decomol/' + this.id,
                }) .then (response => this.decomol = response.data)
            },

            editDecomol() {
                axios.put('http://127.0.0.1:8000/decomol/' + this.id + '/',{
                    resultado_cor: this.decomol.resultado_cor,
                    sensorial: this.decomol.sensorial,
                    ph: this.decomol.ph,
                    brix: this.decomol.brix,
                    producao: this.decomol.producao,
                    liberado: this.liberado
                }) .then(response => {
                    this.refreshData()
                    alert(response.data)
                    })
            },

            liberaDecomol() {
                this.liberado = true
            },

            cancelaDecomol() {
                this.liberado = false
            },

            analisaDecomol() {
                this.liberado = null
            },

            getStatus() {
                this.liberado = this.decomol.liberado
                return this.decomol.liberado
            },
        }
    }
</script>