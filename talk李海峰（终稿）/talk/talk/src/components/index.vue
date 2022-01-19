<template>
  <div class="main">
      <div class="top">
          <h1 style="color:white;font-weight: 500;
    opacity: .8;">{{username}}的空间</h1>
          <p style="margin-top:40px;font-size:20px;">管理员宣言：“我是超级管理员小T,我最大！哼！！”</p>
          <table >
              <tr>
                  <th>用户名</th>
                  <th>权限</th>
              </tr>
              <tr v-for="(item,key) in users" :key="key">
                  <td v-text="item.username" ></td>
                  <td><el-button type="info" size="small"  plain @click="goblack(item)">拉黑</el-button> <el-button type="success" size="small" plain @click="gowhite(item)" class="elbtn">恢复</el-button></td>
              </tr>
          </table>
      </div>

      <div class="center">
          <div class="cetner-main">
              <div class="center-top">
                  <h4>留言板</h4>
                  <input v-model="adminmsg" style="height:80px; font-size:20px">

                  <br/> 
                  <el-button type="success" @click="sendmsg()">发表</el-button>
              </div>
              <p>所有信息管理</p>
                <div class="msg">
                    <div class="msg1" v-for="(index,key) in list" :key="key">
                        <div>
                            <p class="firendname" style="text-align:left">{{index.my+"对"+index.other+"说"}}</p>
                            <p class="firmsg" style="text-align:left">{{index.msg}}------消息来自于{{index.newtime}}</p>
                            <p class="elbtn"><el-button type="danger" @click="delmsg(index)">点击删除信息</el-button></p>
                            <br>
                            <hr/>
                        </div>    
                    </div>
                </div>
          </div>
          
      </div>
  </div>
</template>

<script>

import $ from 'jquery'
    export default {
        data(){
            return{
                username:this.$store.state.name,
                list:[],
                users:[],
                usermsg:[],
                textarea: '',
                adminmsg:''

               
            }
        },
        created(){
             window.usermsg = this.usermsg
            this.getMessage()
            $.ajax({
               url:'http://127.0.0.1:5000/alluser',
               method:'get',
               success:(data)=>{
                   this.users = data.users
               }
            })
            console.log(this.users);
        },
        // mounted(){
        //     window.usermsg = this.usermsg
        //     this.getMessage()
        //     $.ajax({
        //        url:'http://127.0.0.1:5000/alluser',
        //        method:'get',
        //        success:(data)=>{
        //            this.users = data.users
        //        }
        //     })
        //     console.log(this.users);
            
        // },
        methods:{
            sendmsg(){
                console.log(this.adminmsg);
                let obj = {"msg":this.adminmsg}
                $.ajax({
                    url:'http://127.0.0.1:5000/adm',
                    method:'post',
                    data:JSON.stringify(obj),
                    success:(data)=>{
                        console.log(data);
                    }
                })
                alert("消息发布成功")
                this.adminmsg = ""
            },
            gowhite(index){
                let user = index.username
                let msg =""
                $.ajax({
                    url:'http://127.0.0.1:5000/gw',
                    method:'post',
                    data:user,
                    dataType:"text",
                    success:(data)=>{
                        msg = data
                    }
                })
                alert("白了")
            },
            goblack(index){
                let user = index.username
                let msg =""
                $.ajax({
                    url:'http://127.0.0.1:5000/gb',
                    method:'post',
                    data:user,
                    dataType:"text",
                    success:(data)=>{
                        msg = data
                    }
                })
                alert("拉黑了")
            },
            getMessage(){
                $.ajax({
                    url:"http://127.0.0.1:5000/",
                    method:"get",
                  success:(data)=>{
                      console.log(data);
                      this.list = data.talking
                  }
                })
                console.log(this.list);
                // for(let i of this.list){
                //     if(i.other == this.username){
                         
                //         this.usermsg.push(i)
                //     }
                // }
                //  for(let i of this.list){
                //     if(i.my == this.username){
                //         i.other="我"
                //         this.usermsg.push(i)
                //     }
                // }
                for(let i = 0;i<this.list.length-1;i++){
                    for(let j =0 ; j<this.list.length-1-i;j++){
                        if(this.list[j].dtime>this.list[j+1].dtime){
                            [this.list[j],this.list[j+1]]=[this.list[j+1],this.list[j]]
                        }
                    }
                }
                function getLocalTime(nS) {  
                    return new Date(parseInt(nS)).toLocaleString().replace(/:\d{1,2}$/,' ');  
                }
                for(let i of this.list){
                    console.log(i);
                   
                   i.newtime = getLocalTime(parseInt(i.dtime))
                }

            },
            delmsg(index){
                let msg = ""
                console.log(index.dtime)
                $.ajax({
                    url:"http://127.0.0.1:5000/dlmsg",
                    method:"post",
                    data:index.dtime,
                    success:(data)=>{
                      msg = data                    
                  }
                })
                console.log(index);
                let dtime = index.dtime
                let x = 0
                for(let i of this.list){
                    x+=1
                    if(dtime==i.dtime){
                        this.list.splice(x,1)
                    }
                }
                alert("成功")
            }
        }
    }
</script>

<style scoped>
*{
    margin: 0;
    padding: 0;
}

.main{
     width:100%;
     height: 100%;
     
}

.top{
   background:url('/image/mount.jpg')0 1040px;
   margin-top:-50px ;
   position: relative;
   left: -10px;
   top: -10px;
   height: 500px;
   width: 102%;
}
.center{
    background-color:#d3d7d4;
    height: 120%;
    width: 102%;
    position: relative;
    top: -10px;
    left: -10px;
}
.cetner-main{
    padding-top: 10px;
    color: white;
    margin: 0 auto;
    background-color:#a3cf62;
    height: 150%;
    width: 60%;
}
.cetner-main input{
    width: 80%;
    height: 30px;
}

.firmsg{
    text-align: left;
    display: inline-block;
    float: left;
    margin-left: 40px;
    margin-top: 26px;


}
input :focus{
    outline: none;
}
table{
    position: absolute;
    left: 50%;
    transform: translateX(-50%); 
    top: 30%;
    border:1px solid #0094ff;
    background:rgba(144,215,236,.5);
    width: 50%; 
    min-height: 25px;
    line-height: 25px; 
    text-align: center; 
    border-collapse: collapse;
}
tr,th,td{
    border:1px solid #00a6ac;
}
.elbtn{
    /* display: inline-block; */
    text-align: right;
}
p{
    padding-top: 10px;
}
</style>