<template>
    <div class="editar-container">
        <navbar></navbar>
        <div class="all">
            <form class="box">
                <h1 class="title is-5">{{ 'Pulmão '+ id }}</h1>
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
    </div>
</template>

<script>
    import axios from 'axios'
    import navbar from '@/components/NavBarLab.vue'

    export default {
        name: 'EditPulmaoView',
        components: {navbar},
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

    *{
        padding: 0px;
        margin: 0px;
        box-sizing: border-box;    
    }

    .editar-container { 
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        background-color: lightgray;
        color: black;
    }
    .label {
        text-align: left;
        padding-left: 0.25rem;
        font-size: 17px;
        font-weight: bold;
    }

    .field { 
        padding-bottom: 1rem;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }

    .box {
        width: 170vh;
        /* border: 1px #282A35 solid; */
        background-color: white;
    }

    .all{
        display: flex;
        justify-content: center;
        align-items: center;
        padding-top: 1.5rem;
        color: black;
        padding-bottom: 1.5rem;   
        min-height: 90vh;
    }

    .box-button {
        display: flex;
        justify-content: flex-end;
        padding-right: 1.5rem; 
        padding-top: 1rem;
    }
    

    h1{
        padding-top: 0.75rem;
    }

    @media (max-width: 768px){
        .box-button {
        display: flex;
        justify-content: center;
        padding-top: 1rem;
    }
    }

</style>