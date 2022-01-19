import Vue from 'vue'
import VueRouter from 'vue-router'

import Talk from "../components/talk.vue"
import Login from "../components/login.vue"
import Index from "../components/index.vue"
import RegisterU from "../components/register.vue"
import Adminmsg from "../components/adminmsg.vue"
Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "login",
    component: Login
  },
  {
    path:"/talk",
    name:"talk",
    component:Talk,
  },
  {
    path:"/index",
    name:"index",
    component:Index,
  },
  {
    path:"/register",
    name:"register",
    component:RegisterU,
  },
  {
    path:"/adminmsg",
    name:"adminmsg",
    component:Adminmsg,
  },
 
 
 
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
