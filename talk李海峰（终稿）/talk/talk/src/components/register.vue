<template>
    <div class="box">
        <div class="main">
            <div class="login-top">
                <p><span>Talk</span>用户注册</p>
            </div>
            <div class="login-mid">
                <p class="users" >用户帐号</p>
                <input type="text" name="" id="" class="tof" v-model="uname">
                <p class="users">用户密码</p>
                <input type="password" name="" id="" class="tof" v-model="fpwd"><br/>
                 <p class="users">用户密码</p>
                <input type="password" name="" id="" class="tof" v-model="spwd"><br/>
               
            </div>
            <div class="main-foot">
                <button @click="registers">注册</button>
                <router-link to="/"><button class="log">登录</button></router-link> 
            </div>
        </div>
    </div>
    
</template>

<script>
import $ from 'jquery'

    export default {
        data(){
            return{
                uname:'',
                fpwd:'',
                spwd:'',
                userlist:{},
                
            }
        },
        methods:{
            registers(){
                let msg = ""
                if(this.uname=="" || this.fpwd=="" || this.spwd==""){
                    alert("不能为空")
                }else if(this.fpwd != this.spwd){
                    alert("两次密码输入不一致")
                }else{
                    this.userlist["username"]=this.uname
                    this.userlist["password"] = this.fpwd
                    $.ajax({
                    url:"http://127.0.0.1:5000/register",
                    method:'POST',
                    // dataType:"json",
                    dataType:"text",
                    data:JSON.stringify(this.userlist),
                    success:(data)=>{
                        msg = data 
                    },
                    error:(err)=>{
                        console.log(err)
                    }
                })
                }
                alert(msg) 
            }
        }
    
    }
</script>

<style  scoped>
.log{
    position: relative;
    top: -39px;
    left: -94px;
}
.box{
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    overflow-y: auto;
    background: url('/image/st.jpg');
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
    margin-top: 10px;
    padding-top: 10px;

}
.main-foot button{
    width: 80px;
    height: 40px;
    border-radius: 15%;
    background:darkgray;
    color: white;
}
</style>