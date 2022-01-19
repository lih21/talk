<template>

    <div class="box">
        <div id="theCanvas"></div>
        <ul>

            <li v-for="(item,key) in list" :key="key"><el-tag style="height:50px; line-height:50px">{{"管理员xiaoT:"+"   "+item.msg}}</el-tag></li>
        </ul>
        
    </div>
</template>

<script>
import $ from 'jquery'
    export default {
        data(){
            return{
                list:[]
            }
        },
        mounted(){
            window.list = this.list
            $.ajax({
                url:'http://127.0.0.1:5000/getadm',
                method:"post",
                dataType:'text',
                success:(data)=>{
                    this.list = eval(data)
                }
            })
            console.log(this.list);
        }
    }
</script>

<style scoped>
*{
    margin: 0;
    padding: 0;
}
.box{
    width: 102%;
    height: 850px;
    margin-top: -60px;
    /* background-color: pink; */
    margin-left: -8px;
    background: url('/image/xy.jpg');
    background-size: 100% 100%;
}
ul li{
    list-style: none;
    
}
li{
    padding-top:20px ;
}
ul{
    
    display: flex;
    flex-flow:column;
    justify-content: space-around;
    align-items: flex-start;
    
}
</style>