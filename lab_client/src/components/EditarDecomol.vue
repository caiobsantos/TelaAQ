<template>
    <div class="all">
        <form class="box">
            <div class="column">
                <div class="field">
                    <label class="label">Resultado Cor</label>
                        <div class="control">
                            <input class="input" type="text" v-model="resultado_cor" required>
                        </div>
                </div>
                <div class="field">
                    <label class="label">Sensorial</label>
                        <div class="control">
                            <input class="input" type="text" v-model="sensorial" required>
                        </div>
                </div>
                <div class="columns">
                    <div class="column">
                        <div class="field">
                            <label class="label">PH</label>
                                <div class="control">
                                    <input class="input" type="number" min="0" max="14" v-model="ph" placeholder="0.00" required>
                                </div>
                        </div>
                    </div>
                    <div class="column">
                        <div class="field">
                            <label class="label">Brix</label>
                                <div class="control">
                                    <input class="input" type="number" v-model="brix" required>
                                </div>
                        </div>
                    </div>
                </div>
            </div>
                <div class="StatusDecomol">  
                        <label class="radio">
                            <input type="radio" name="answer" value="true" v-model="liberado" required>
                            Liberado
                        </label>
                        <label class="radio">
                            <input type="radio" name="answer" value="false" v-model="liberado">
                            Não Liberado
                        </label>
                </div>
                <div class="box-button">
                    <button class="button is-link" @click="editDecomol()">Salvar</button>
                </div>
        </form>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'EditView',
        data() {
            return{
                id: this.$route.params.id,
                resultado_cor: '',
                sensorial: '',
                ph: '',
                brix: '',
                liberado: null,
            }
        },
        methods: {
            editDecomol() {
                if(this.resultado_cor ==null || this.sensorial ==null || this.ph ==null || this.brix==null || this.liberado==null || this.resultado_cor =="" || this.sensorial == "" || this.ph =="" || this.brix==""){
                    return 0
                }
                
                else{
                    if(this.liberado=='true'){
                        this.liberado = true
                    }
                    else{
                        this.liberado = false
                    }
                    try {
                    axios.put(process.env.VUE_APP_ROOT_URL + this.id + '/',{
                        resultado_cor: this.resultado_cor,
                        sensorial: this.sensorial,
                        ph: this.ph,
                        brix: this.brix,
                        producao: 'Decomol' + this.id,
                        liberado: this.liberado,
                    }) 

                        axios.post(process.env.VUE_APP_ROOT_URL_HISTORICO,{
                        decomol: 'Decomol' + this.id,
                        resultado_cor: this.resultado_cor,
                        sensorial: this.sensorial,
                        ph: this.ph,
                        brix: this.brix,
                        resultado_analise: this.liberado,
                })
                this.$router.push('/aq/decomol')
                        
                    } catch (error) {
                        console("Não foi possível")
                        
                    }
                }
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