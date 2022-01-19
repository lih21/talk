<template>
    <div class="box">
        <div class="main-left">
            <div class="left-top">
                <span class="s1">欢迎你！------{{username}}</span><br>
                <span class="s2">---虚争空言不如思而试之</span>
            </div> 
            
            <div class="flist">
                <ul>
                    <li v-for="(item,id) in friendname" :key ="id"  @click="ltk($event)" >{{item}}</li>
                    <li @click="addfirend">添加好友</li>
                    <li @click="adminmsg">管理员消息</li>
                </ul>
            </div>
        </div>
        <div class="addf">
            搜索id <button @click="closeadd">X</button><br>
            <input type="text" style="height:20px" v-model="addname" >
            <br>
            <button @click="sendadd">发送添加</button>
            
        </div>
        <div class="main-right">
            <!-- {{this.$store.state.name}} -->
            <div class="dqyh"><h3>当前聊天对象：{{dqyh}}</h3><br><p>人如江鲫逐功名</p><span><button class="btnX" @click="closebox">X</button></span></div>
            <div class="outbox">
            
            </div>
            <textarea name="" id="" cols="30" rows="10" class="inbox"></textarea>
            <button @click="sendmsg" class="btn">发送</button>
            
        </div>
    </div>
</template>

<script>
import $ from "jquery"
    export default {

        data(){
            return{
                username : this.$store.state.name,
                friendname:[],
                dqyh:"",
                myText:'',
                msg:{},
                addname:"",
                addmsg:""
            }
        },
        mounted(){
            let x =""
            $.ajax({
                url:"http://127.0.0.1:5000/friendlist",
                method:"post",
                data:this.username,
                dataType:"text",
                success:(data)=>{
                    x = eval(data)                   
                }
            })
                         
            for(let i in x){
                console.log(x[i]);
                this.friendname.push(x[i].friendname)
            }
        },
        methods:{
            adminmsg(){
                this.$router.push('/adminmsg')
            },
            sendadd(){
                $.ajax({
                    url:"http://127.0.0.1:5000/addfirend",
                    method:"post",
                    dataType:"text",
                    data:JSON.stringify([this.addname,this.username]),
                    success:(msg)=>{
                        this.addmsg = msg
                    }
                    
                })
                alert(this.addmsg)
            },
            closeadd(){
                $(".addf").hide()
            },
            addfirend(){
                $(".addf").show()
            },
            ltk(e){
                $(".main-right").show();
                $('.outbox').empty();
                this.dqyh = e.target.innerText;
                $.ajax({
                    url: 'http://127.0.0.1:5000/',
                    method: 'get',
                    // Headers:
                    success: (data) => {
                        console.log(data)
                        this.myText = data.talking
                    }
                })
                for(let i = 0; i<this.myText.length-1;i++){
                    for(let j = 0; j<this.myText.length-1-i;j++){
                        if(this.myText[j].dtime>this.myText[j+1].dtime){
                            [this.myText[j],this.myText[j+1]]= [this.myText[j+1],this.myText[j]]
                        }
                    }
                };
                    for(let i = 0 ; i<this.myText.length;i++){
                    if(this.myText[i].other == this.dqyh && this.myText[i].my ==this.username){
                        $('.outbox').append(
                            `
                            <div class = "my" style="border:2px solid green;color:black;height:40px;line-height:40px;margin-bottom:10px;text-align: right; float: right;width: 400px; background:white;">我：${this.myText[i].msg}</div>
                            `
                        )
                    }else if(this.myText[i].other == this.username && this.myText[i].my==this.dqyh){
                        $('.outbox').append(                 
                            `
                            <div class = "other" style="border:2px solid red;color:black;height:40px;line-height:40px;margin-bottom:10px;text-align: left; float: left;width: 400px;background:white;">zhangsan：${this.myText[i].msg}</div>
                            `
                        )
                    }
                
               }
            },
            closebox(){
                $(".main-right").hide();
            },
            sendmsg(){
                
                let smsg = $(".inbox").val();
                if(smsg==""){
                    alert("没说话你发你🐎呢！")
                }else{
                     $('.outbox').append(
                    `
                    <div class = "my" style="border:2px solid green;color:black;height:40px;line-height:40px;margin-bottom:10px;text-align: right; float: right;width: 400px; background:white;">我：${smsg}</div>
                   `
                )
                $(".inbox").val("")
                
                this.msg["my"] = this.username
                this.msg["other"]= this.dqyh
                this.msg["msg"]= smsg
                this.msg["dtime"] = new Date().getTime()
                this.msg['state'] = 1
                console.log(this.msg);
                $.ajax({
                    url:'http://127.0.0.1:5000/send',
                    method:"post",
                    dataType:"json",
                    data:JSON.stringify(this.msg),
                    success:()=>{
                        console.log("成功");
                    }
                })
                }
               
               
            }
        }
    }
</script>

<style scoped>
.addf{
    overflow: hidden;
    width: 400px;
    height: 100px;
    background-color: red;
    position: relative;
    left: 30%;
    transform: translateX(-50%);
    top: 40%;
    display: none;
}   
.box{
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    overflow-y: auto;
    background: url('/image/talk.jpg') 0 -200px;
    background-size: cover;
    color: rgb(255,255,255,.6);
}
.main-left{
    width: 300px;
    height: 800px;
    /* background: cyan; */
    float: left;
    margin-top: 15px;
    margin-left: 40px;
}
.s1{
    margin-top: 20px;
    line-height: 46px;
    font-size: 20px;
}
.s2{
    padding-top: 26px;
    margin-left: 88px;
    line-height: 100px;
}
.flist{
    position: relative;
    left: -40px;
}
.flist ul li{
    width: 116%;
    height: 50px;
    background: #d9d6c3;
    list-style: none;
    margin-top: 30px;
    line-height: 50px;
    margin-right: 10px;
}
.main-right{
    width: 800px;
    height:500px ;
    background: #fab27b;
    float: right;
    margin-top:200px ;
    margin-right: 400px;
    display: none;
}
.btnX{
    position: relative;
    height: 25px;
    top: -61px;
    left: 387px;
}
.outbox{
    background-color: white;
    width: 800px;
    height: 400px;
    overflow-y:scroll;
    
}
.inbox{
    border: 0;
    background-color: #f6f5ec;
    margin: 0px;
    width: 747px;
    height: 74px;
    font-size: 24px;
    resize: none;
    margin-left: -3px;
}
.inbox:focus{
    outline: none;
    width: 743px;
    border:2px solid #00ae9d;
}
.other{
    float: left;
    width: 800px;
    text-align: left;
}
.my{
    float: right;
    width: 800px;
    text-align: right;
}
.left-top{
    height: 15%;
    widows: 100%;
    background-color:#bb505d;
}
.btn{
    height: 81px;
    width: 52px;
    position: relative;
    top: -34px;
    background-color: #1d953f;
    color: white;
    border: none;
}
  .outbox::-webkit-scrollbar {
  /*滚动条整体样式*/
  width : 15px;  /*高宽分别对应横竖滚动条的尺寸*/
  height: 1px;
  }
  .outbox::-webkit-scrollbar-thumb {
  /*滚动条里面小方块*/
  border-radius: 10px;
  box-shadow   : inset 0 0 5px rgba(0, 0, 0, 0.2);
  background   : #535353;
  }
  .outbox::webkit-scrollbar-track {
  /*滚动条里面轨道*/
  box-shadow   : inset 0 0 5px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  background   : #ededed;
  }
li:hover{
    cursor: pointer;
}
</style>