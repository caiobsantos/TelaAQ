<template>
    <div class="all">
        <form class="box">
            <div class="column">
                <div class="field">
                    <label class="label">Resultado Cor</label>
                        <div class="control">
                            <input class="input" type="text" v-model="decomol.resultado_cor">
                        </div>
                </div>
                <div class="field">
                    <label class="label">Sensorial</label>
                        <div class="control">
                            <input class="input" type="text" v-model="decomol.sensorial">
                        </div>
                </div>
                <div class="columns">
                    <div class="column">
                        <div class="field">
                            <label class="label">PH</label>
                                <div class="control">
                                    <input class="input" type="text" v-model="decomol.ph">
                                </div>
                        </div>
                    </div>
                    <div class="column">
                        <div class="field">
                            <label class="label">Brix</label>
                                <div class="control">
                                    <input class="input" type="text" v-model="decomol.brix">
                                </div>
                        </div>
                    </div>
                </div>
            </div>
                <div class="StatusDecomol">
                    <div v-if="getStatus() == true">
                        <label class="radio">
                            <input type="radio" name="answer" @click="liberaDecomol()" checked>
                            Liberado
                        </label>
                        <label class="radio">
                            <input type="radio" name="answer" @click="cancelaDecomol()">
                            Não Liberado
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
                    </div>
                </div>
                <div class="box-button">
                    <router-link to="/decomol"><button class="button is-link" @click="editDecomol()">Salvar</button></router-link>
                </div>
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
                liberado: null,
            }
        },
        mounted() {
            this.getDecomol()
        },
        methods: {
            getDecomol() {
                axios({
                    method: 'get',
                    url: process.env.VUE_APP_ROOT_URL + this.id,
                }) .then (response => this.decomol = response.data)
            },

            editDecomol() {
                axios.put(process.env.VUE_APP_ROOT_URL + this.id + '/',{
                    resultado_cor: this.decomol.resultado_cor,
                    sensorial: this.decomol.sensorial,
                    ph: this.decomol.ph,
                    brix: this.decomol.brix,
                    producao: this.decomol.producao,
                    liberado: this.liberado,
                    troca_decomol: false
                }) //.then(response => {
                //     this.refreshData()
                //     alert(response.data)
                //     })
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

<style scoped>

    .label {
        position: relative;
        text-align: left;
        margin-left: 0.25rem;
    }

    .field {
        margin-top: 1.0rem;
        margin-bottom: 1.0rem;
        margin-left: 1.5rem;
        margin-right: 1.5rem;
    }

    .box {
        margin-left: 150px;
        margin-right: 150px;
        margin-top: 50px;
    }

    .box-button {
        margin-left: 143vh;
    }

    

    .StatusDecomol {
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }

</style>