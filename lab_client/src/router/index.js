import { createRouter, createWebHistory } from 'vue-router'
import AQDecomolView from '../components/Decomol.vue'
import AQPulmaoView from '../components/Pulmao.vue'
import EditView from '../components/EditarDecomol.vue'
import FabDecomolView from '../components/FabDecomol.vue'
import DetailView from '../components/Detalhes.vue'
import HistoricoView from '../components/Historico.vue'
import HistoricoTrocaView from '../components/HistoricoTrocas.vue'
import EditPulmaoView from '../components/EditarPulmao.vue'
import HistoricoPulmaoView from '../components/HistoricoPulmao.vue'
import FabPulmaoView from '../components/FabPulmao.vue'


const routes = [
  // {
  //   path: '/aq',
  //   name: 'aq',
  //   component: AQView,
  //   meta: {
  //     isLab: true,
  //    }
  // },

  {
    path: '/aq/decomol',
    name: 'AQDecomol',
    component: AQDecomolView,
    meta: {
      isLab: true,
    }
  },

  {
    path: '/aq/pulmao',
    name: 'AQPulmao',
    component: AQPulmaoView,
    meta: {
      isLab: true,
    }
  },

  {
    path: '/decomol/:id',
    name: 'editdecomol',
    component: EditView,
    meta: {
      isLab: true,
    }
  },

  {
    path: '/pulmao/:id',
    name: 'editpulmao',
    component: EditPulmaoView,
    meta: {
      isLab: true,
    }
  },

  // {
  //   path: '/fab',
  //   name: 'fabricacao',
  //   component: FabricacaoView,
  //   meta: {
  //     isLab: false,
  //   }
  // },

  {
    path: '/fab/decomol',
    name: 'FabDecomol',
    component: FabDecomolView,
    meta: {
      isLab: false,
    }
  },

  {
    path: '/fab/pulmao',
    name: 'FabPulmao',
    component: FabPulmaoView,
    meta: {
      isLab: false,
    }
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
    path: '/pulmao/historico/:id',
    name: 'historico',
    component: HistoricoPulmaoView,
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
