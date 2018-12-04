from flask import Flask,url_for,redirect,render_template,request
import pymongo
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
# 数据库实例
connect = pymongo.MongoClient('127.0.0.1',27017)
db=connect.todo
# mongo todo文档结构
class Todo(object):
    """
    一行待办事项数据结构。添加
    字段：事项内容，添加创建时间，状态（未完成、已完成），完成时间
    """
    @staticmethod
    def create_doc(self,content):
        return {
            'content':content,
            'create_time':datetime.now(),
            'status':0,        # 0未完成 1已经文成
            'finish_time':None
        }


@app.route('/')
def index():
    return redirect(url_for('get'))

@app.route('/get')
def get():
    """展示一条todo"""
    todo_list = db.todo.find({})
    print(todo_list)
    return render_template('index.html',todo_list=todo_list)

@app.route('/add',methods=['POST'])
def add():
    """增加一条todo"""
    form = request.form
    content = form['content']
    print(content)
    new_id = db.todo.insert( {'content':content,
            'create_time':datetime.now(),
            'status':0,        # 0未完成 1已经文成
            'finish_time':None})
    print(new_id)
    if new_id:
       return redirect(url_for('index'))
@app.route('/finish')
def finish():
    """更新状态已完成"""
    args=request.args
    _id = args['_id']
    affect = db.todo.update(
        {"_id":ObjectId(_id)},
        {"$set":{
        "status":1,
        "finish_time":datetime.now()}
        }
    )
    return redirect(url_for('index'))
@app.route('/delete')
def delete():

   args = request.args
   _id = args['_id']
   newid=db.todo.remove({
       '_id':ObjectId(_id)
   })
   print(newid)
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
