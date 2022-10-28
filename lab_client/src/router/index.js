import { createRouter, createWebHistory } from 'vue-router'
import DecomolView from '../components/Decomol.vue'
import AdicionarView from '../components/AdicionarDecomol.vue'
import EditView from '../components/EditarDecomol.vue'
import FabricacaoView from '../components/Fabricacao.vue'
import DetailView from '../components/Detalhes.vue'
import HistoricoView from '../components/Historico.vue'
import HistoricoTrocaView from '../components/HistoricoTrocas.vue'


const routes = [
  {
    path: '/decomol',
    name: 'decomol',
    component: DecomolView
  },

  {
    path: '/decomol/:id',
    name: 'editdecomol',
    component: EditView
  },


  {
    path: '/adicionar',
    name: 'adicionar',
    component: AdicionarView
  },

  {
    path: '/fabricacao',
    name: 'fabricacao',
    component: FabricacaoView
  },

  {
    path: '/fabricacao/detalhes/:id',
    name: 'detalhe',
    component: DetailView
  },

  {
    path: '/historico/:id',
    name: 'historico',
    component: HistoricoView,
    meta: {
      hideNavbar: true,
     }
  },

  {
    path: '/historico/:id/troca',
    name: 'historicoTroca',
    component: HistoricoTrocaView,
    meta: {
      hideNavbar: true,
     }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
