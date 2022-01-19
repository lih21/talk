<template>
    <div class="box">
        <div class="main">
            <div class="login-top">
                <p><span>Talk</span>用户登录</p>
            </div>
            <div class="login-mid">
                <p class="users" >用户帐号</p>
                <input type="text" name="" id="" class="tof" v-model="username">
                <p class="users">用户密码</p>
                <input type="password" name="" id="" class="tof"  v-model="password" @keyup.enter="enterdlu"><br/>
                <div class="state">
                    
                <p><input type="checkbox" name="" class="nots">&nbsp;&nbsp;&nbsp;&nbsp;保持登录状态</p>
                </div>                 
            </div>
            <div class="main-foot">
            <button @click="dlu" >登&nbsp;&nbsp;&nbsp;录</button>
            <button @click="reg">注册</button>
            </div>
        </div>
    </div>
    
</template>

<script>
import $ from 'jquery'

    export default {
        name:"login",
        data(){
            return{
                username:"",
                password:"",
                value:''
            }
        },
        methods:{
            reg(){
                this.$router.push('/register')
            },
            enterdlu(){
                this.dlu()
            },
            dlu(){            
                // this.$axios.get('/test.json').then(res=>{
                //     console.log(res)
                // });
                //因为getJson为异步操作所以即使有返回值，仍然任务getJson没有执行完成故而得不到返回值
                var k = ""
                $.ajax({
                    url:"http://127.0.0.1:5000/login",
                    method:"get",
                    success:(data)=>{
                        k = data.users
                    }
                })
                // let data1 = $.getJSON('/users.json',data=>{
                //     k = data.users
                // })
                console.log(k);
                if(this.username=="xiaoT" && this.password == "xiaoT"){
                    this.$router.push("/index")
                    this.$store.commit('CurrentUser',this.username)
                }else{
                    //2表示密码错误，1表示成功，3表示被拉黑
                var ifuser = 2

                let len = k.length
                for(let i=0; i<len;i++){
                    // console.log(k[i]);
                    for(let j in k[i]){
                        if(this.password == k[i].password && this.username==k[i].username){
                            if(k[i].state==1){
                                ifuser=1
                                this.$store.commit('CurrentUser',this.username)
                            }else if(k[i].state==2){
                                
                                ifuser=3
                            }
                            
                        }
                    }
                }
                if(ifuser==1){
                    this.$router.push("/talk")
                }else if(ifuser==2){
                    alert("用户名或密码错误")
                }else if(ifuser==3){
                    alert("用户已被拉黑，请联系管理员")
                }
                }
                
               
            }   
            
        },
       
    }
</script>

<style  scoped>
.box{
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    overflow-y: auto;
    background: url('/image/sl.jpg');
    background-size: cover;
    color: rgb(255,255,255,.6);
}
.main{
    
	background: rgba(0,0,0,.1);
    box-shadow: 0 15px 25px rgba(0,0,0,.5);
    box-sizing: border-box;
    height: 430px;
    width: 400px;
	position: absolute;
	top:50%;
	left: 50%;
	transform: translate(-50%,-50%);
    /* background: violet; */
    border-radius: 5%;  
}

.login-top{
    width: 100%;
    height: 20%;
    /* background: yellowgreen; */
    font-size: 24px;
    
    
}
.login-top p{
    
    position: relative;
    top: 25px;
    left: -120px;

}
.login-top span{
    font-weight: 800;
}
.login-mid .users{
    margin-left:-250px;
    font-size: 16px;
    
}
.tof{
    height: 30px;
    width: 300px;
    color: white;
    background-color:rgba(255,255,255,.1);
    border:0;
    /* border-bottom: 5px; */
}
.tof:focus{
    background-color:rgba(255,255,255,.5);
}
.nots{
    height: 18px;
    width: 18px;
}
.state{
   margin-left: -170px;
}
.main-foot{
    height: 80px;
    width:80px;
    position: relative;
    left: 271px;

}
.main-foot button{
    width: 80px;
    height: 40px;
    border-radius: 15%;
    background:darkgray;
    color: white;
}
</style>