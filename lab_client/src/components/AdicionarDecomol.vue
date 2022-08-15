<template>
    <h1>Olá</h1>
    <br>
    <div class="column is-6 is-offset-3">
        <form class="inputs" @submit.prevent="addDecomol">
            <input class="input is-danger" type="text" placeholder="Decomol em Produção" v-model="producao">
            <button class="button is-sucess">Adicionar Decomol</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

    export default {
        name: 'AdicionarView',
        
        data() {
            return {
                decs: [],
                producao: "",
            }
        },
        methods: {
            addDecomol() {
                axios
                    .post('http://127.0.0.1:8000/decomol/', {
                        producao: this.producao
                    }) .then ((response) => {
                        let newDecomol = {
                            id: response.data.id,
                            producao: this.producao
                        }
                        this.decs.push(newDecomol),
                        this.producao = ""
                    })
            }
        }
    }
</script>