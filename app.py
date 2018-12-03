from flask import Flask,url_for,redirect,render_template,request
import pymongo
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
    return render_template('index.html')

@app.route('/get')
def get():
    """展示一条todo"""
    pass


@app.route('/add',methods=['POST'])
def add():
    """增加一条todo"""
    form = request.form
    content = form['content']
    print(content)
    new_id=db.todo.insert( {'content':content,
            'create_time':datetime.now(),
            'status':0,        # 0未完成 1已经文成
            'finish_time':None})
    print(new_id)
    if new_id:
       return redirect(url_for('index'))
@app.route('/finish')
def finish():
    """更新状态已完成"""
    pass

@app.route('/delete')
def delete():
    """删除无用todo"""

    pass

if __name__ == '__main__':
    app.run()
