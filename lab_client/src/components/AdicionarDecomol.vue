<template>
    <h1>Olá</h1>
    <br>
    <div class="column is-6 is-offset-3">
        <form class="inputs">
            <input class="input is-danger" type="text" placeholder="Decomol em Produção" v-model="producao">
            <button class="button is-sucess" @click="addDecomol()">Adicionar Decomol</button>
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
                baseUrl: 'http://172.16.19.116:8000/decomol/',
            }
        },
        methods: {
            addDecomol() {
                axios
                    .post(this.baseUrl, {
                        producao: this.producao
                    }) .then (this.$router.push('decomol')
                    )
            }
        }
    }
</script>