import Vue from 'vue'

import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)

export default new Vuex.Store({

    state:{
        count:0,
        name:''
    },
    plugins:[
       createPersistedState({
           storage:window.sessionStorage,
           key:'vueX',
           render(state){
               return {...state}
           }
       })
    ],
    mutations:{
        CurrentUser(state,username){
            state.name = username;
        }
    }
})

