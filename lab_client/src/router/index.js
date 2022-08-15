import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DecomolView from '../components/Decomol.vue'
import AdicionarView from '../components/AdicionarDecomol.vue'
import EditView from '../components/EditarDecomol.vue'
import FabricacaoView from '../views/Fabricacao.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

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
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
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
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
