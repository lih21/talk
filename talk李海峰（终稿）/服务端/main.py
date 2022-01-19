import json
from logging import log
from os import stat
from re import M
from flask import request
from flask import Flask, jsonify
app = Flask(__name__)
from flask_cors import CORS
CORS(app, resources={r"/*": {"origins":"*"}}, send_wildcard=True)
list = {"talking":[]}
users ={"users":[]}
@app.route('/')
def index():
    print('请求来了')
    # data = json.loads(request.form.get('data'))
    # print(data)
    with open('talking.json', mode='rt', encoding='utf-8') as f:
        dic = json.load(f)
    res = jsonify(dic)
    
    return res

@app.route('/send',methods=['POST'])
def index1():
    print("ff")
    #接收前端的数据
    list['talking']=[]
    data = request.get_data()
    data = json.loads(data)
    print(data)
    with open('talking.json', mode='rt', encoding='utf-8') as f:
        dic = json.load(f)
    res = jsonify(dic)
    print(dic["talking"])

    for i in dic["talking"]:
        list["talking"].append(i)
    list["talking"].append(data)

    with open('talking.json', 'w') as f:
        json.dump(list,f)
        print("加载完成")
    f.close()
    return res

@app.route('/login',methods=["GET"])
def login():
    print("登录请求")
    with open('users.json', mode = "r", encoding="utf-8") as f:
        dic = json.load(f)
    res = jsonify(dic)
    res.headers['Access-Control-Allow-Origin'] = "*"
    return res

@app.route('/register',methods=["POST","GET"])
def register():
    users["users"]=[]
    x=0
    y=0
    newf={

    }
    obj=[{
        "friendId":1,
        "friendname":"xiaoT",
        "FriendAvatar":"null"
    }]
    msg="!"
    print("注册请求")
    data =str(request.get_data(),"utf-8")
    data = eval(data)
    uname = data['username']
    print(data)
    with open('users.json',mode="rt",encoding="utf-8") as f:
        dic = json.load(f)
    res = dic["users"]
    for i in range(0,len(res)):
        users["users"].append(res[i])
        if res[i]["username"] == data["username"]:
            msg = "该用户名已存在"
        elif i == len(res)-1:
            users["users"].append(data)
            with open("users.json", mode="w") as u:
                u = json.dump(users,u)
            with open('friends.json',mode="r") as fp:
                friends = json.load(fp)
            x =len(friends)
            for key in friends:
                # print(friends[key])
                y+=1
                if y == x:
                    newf[uname] = obj
                    newf[key] = friends[key]
                else:
                    newf[key] = friends[key]
            with open('friends.json',mode="w") as wr:
                json.dump(newf,wr)
            
            msg = "注册成功"
    print(msg)
    return msg


@app.route('/addfirend',methods=["POST"])
def addfirend():
    print("发送好友请求")   
    flag=1
    x = 0
    y = 0
    msg = "1" 
    data = request.get_data()
    data = eval(str(data,"utf-8"))
    username = data[0]
    myname = data[1]
    obj = {}
    newrep=[]
    print(username)
    with open('users.json',encoding="utf-8",mode="r") as f:
        dic = json.load(f)
    res = dic["users"]
    print(res)
    for i in res:
        x+=1
        # 判断添加的用户是否存在users中
        if i["username"] == username:
            msg = "用户存在"
            with open("friends.json",mode="r",encoding="utf-8") as p:
                dic = json.load(p)
            rep = dic[myname]
            newrep = []
            print(type(rep))
            for j in rep:
                y+=1
                newrep.append(j)
                if j["friendname"] ==username:
                    msg = "该用户以是好友"
                    break
                elif y==len(rep) and j["friendname"] !=username:
                    msg="可以添加"
                    obj['friendID'] = len(rep)+1
                    obj['friendname']=username
                    obj['FriendAvatar'] ="null"
                    newrep.append(obj)
                    flag=2
                    break          
            break
        elif x ==len(res) and i["username"] != username :
            msg = "用户不存咋"
    if flag==2:
        newdic = {}
        for key in dic:
            print("---------"+key)
            if key == myname:
                dic[key]=newrep
            newdic[key] = dic[key]

        with open('friends.json',mode="w") as k:
            k = json.dump(newdic,k)
            msg="添加成功"
    return msg


@app.route("/friendlist",methods=["POST"])
def friendlist():
    list =[]
    data =str(request.get_data(),"utf-8")
    with open("friends.json",mode="r",encoding="utf-8") as f:
        dic = json.load(f)
    list = dic[data]
    print(list)
    print(data)
    return str(list)
    
@app.route('/dlmsg',methods=['POST','GET'])
def dlmsg():
    list["talking"]=[]
    print("管理员删除信息请求")
    data = request.get_data()
    data = str(data,"utf-8")
    print(data)
    with open("talking.json",encoding="utf-8",mode="r") as f:
        dic = json.load(f)
    res = dic['talking']
    for i in res:
        if str(i['dtime'])==str(data):
            print("找到信息")
            continue
        else:
            list["talking"].append(i)
    print(list)
    with open('talking.json',encoding='utf-8',mode="w") as p:
        json.dump(list,p)
    return "删除消息成功，另外随意删除他人留言是不好的哦！"

@app.route('/alluser',methods=['POST','GET'])
def alluser():
    print("请求所有用户")
    with open('users.json',encoding='utf-8',mode="r") as f:
        dic = json.load(f)
    print(dic)
    return dic    

@app.route('/gb',methods=['POST','GET'])
def gb():
    users["users"]=[]
    print("拉黑请求")
    data = request.get_data()
    data = str(data,"utf-8")
    print(data)
    with open('users.json',encoding='utf-8',mode="r") as f:
        dic = json.load(f)
    for i in dic['users']:
        if i['username'] == data:
            i['state'] =2
            users["users"].append(i)
        else:
            users["users"].append(i)
    print(users)
    with open('users.json',encoding='utf-8',mode='w') as w:
        json.dump(users,w)
    msg = "拉黑了"
    return str(msg)

@app.route('/gw',methods=['POST','GET'])
def gw():
    users["users"]=[]
    print("白名单请求")
    data = request.get_data()
    data = str(data,"utf-8")
    print(data)
    with open('users.json',encoding='utf-8',mode="r") as f:
        dic = json.load(f)
    for i in dic['users']:
        if i['username'] == data:
            i['state'] = 1
            users["users"].append(i)
        else:
            users["users"].append(i)
    print(users)
    with open('users.json',encoding='utf-8',mode='w') as w:
        json.dump(users,w)
    msg = "恢复了"
    return str(msg)

@app.route('/adm',methods=['POST','GET'])
def adm():
    print("发布请求")
    newdic = {"msg":[]}
    data = request.get_data()
    data =eval(str(data,"utf-8"))
    print(data)
    with open("adminmsg.json",encoding='utf-8',mode="r") as f:
        dic = json.load(f)
    res = dic['msg']
    for i in res:
        newdic["msg"].append(i)

    newdic["msg"].append(data)
    print(newdic)    
    with open("adminmsg.json",encoding='utf-8',mode="w") as w:
        json.dump(newdic,w)       
    return "123"

@app.route('/getadm',methods=['POST','GET'])
def getadm():
    print("拿管理员消息")
    with open('adminmsg.json',encoding='utf-8',mode='r') as f:
        dic = json.load(f)
    res = dic['msg']
    print(res)
    return str(res)

if __name__ == '__main__':
    app.run()
