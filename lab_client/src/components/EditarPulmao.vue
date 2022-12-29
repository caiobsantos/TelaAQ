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
            <div class="box-button">
                    <button class="button is-link" @click="editPulmao()">Salvar</button>
                </div>
        </form>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'EditPulmaoView',
        data() {
            return{
                id: this.$route.params.id,
                resultado_cor: '',
                sensorial: '',
                ph: '',
                brix: '',
                nameTanque: ''
            }
        },
        methods: {
            editPulmao() {
                if(this.resultado_cor ==null || this.sensorial ==null || this.ph ==null || this.brix==null || this.resultado_cor =="" || this.sensorial == "" || this.ph =="" || this.brix==""){
                    return 0
                }
                else{
                    if(this.id == 1){
                        this.nameTanque = 'Tanque 1'
                    }
                    else{
                        this.nameTanque = 'Tanque 2'
                    }
                    try {
                    axios.put(process.env.VUE_APP_ROOT_URL_PULMAO+this.id+'/',{
                        tanque: this.nameTanque,
                        resultado_cor: this.resultado_cor,
                        sensorial: this.sensorial,
                        ph: this.ph,
                        brix: this.brix,
                    })

                    axios.post('http://10.15.100.110:50003/historico/pulmao',{
                    tanque: this.nameTanque,
                    resultado_cor: this.resultado_cor,
                    sensorial: this.sensorial,
                    ph: this.ph,
                    brix: this.brix,
                    })

                    this.$router.push('/aq/pulmao')
                        
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

    

    .Statuspulmao {
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }

</style>