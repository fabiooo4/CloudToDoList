from flask import Flask, request
from flask_cors import CORS
from deta import Deta

deta = Deta()

app = Flask(__name__)
CORS(app)


def getBody():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    return request.json
  else:
    return 'Content-Type not supported!'

@app.route('/')
def index():
  out = [{"msg": "index"}]
  return out

  
# #! User list
# @app.route('/user', methods=["GET"])
# def userList():
#   users = deta.Base('users')
#   out = users.fetch().items
  
#   return {
#     "data": out,
#     "size": len(out)
#   }
  
#! Task list
@app.route('/tasks', methods=["GET"])
def taskList():
	tasks = deta.Base('tasks')
	out = tasks.fetch().items
	
	return {
		"data": out,
		"size": len(out)
	}
	
#! Single task
@app.route('/tasks/<string:id>', methods=["GET"])
def taskDetails(id):
  tasks = deta.Base('tasks')
  out = tasks.fetch({"key": id}).items
  
  return {
    "data": out,
    "exists": len(out) > 0
  }
    
#! Toggle state
@app.route('/tasks/<string:id>', methods=["PATCH"])
def toggleState(id):
  tasks = deta.Base('tasks')
  state = tasks.fetch({"key": id}).items[0].get("state")
  tasks.update({"state": not state}, id)
  
  return {
    "updated": True,
  }
  
# #! Edit task
# @app.route('/tasks/<string:id>', methods=["PUT"])
# def editTask(id):
#   database = connect(taskdb)
#   body = getBody()
  
#   database.get("cursor").execute(f"""
#   UPDATE tasks
#     SET date = ?, title = ?, content = ?
#     WHERE id = ?
#   """, (body["date"], body["title"], body["content"], id))
#   database.get("db").commit()
  
#   return {
#     "updated": True,
#   }

# #! Delete task
# @app.route('/tasks/<string:id>' , methods=["DELETE"])
# def taskDelete(id):
#   database = connect(taskdb)
#   database.get("cursor").execute(f"""
#   DELETE FROM tasks
#     WHERE id = {id}
#   """)
#   database.get("db").commit()
#   return {
#     "deleted": True
#   }

#! Add task
@app.route('/tasks', methods=["POST"])
def addTask():  
  tasks = deta.Base('tasks')
  body = getBody()
  
  tasks.put({
    "title": body["title"],
    "content": body["content"],
    "date": body["date"],
    "state": False
  })
  
  return {
    "added": True,
  }

print("Server started")