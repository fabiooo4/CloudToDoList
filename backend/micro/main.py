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

  
#! Login user
@app.route('/login', methods=["POST"])
def login():
  users = deta.Base('users')
  body = getBody()
  
  out = users.fetch({"username": body["username"], "password": body["password"]}).items
  
  if len(out) == 0:
    return {
      "exists": False
    }
  else:
    return {
      "exists": True,
      "data": out[0]
    }
  
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
  
#! Edit task
@app.route('/tasks/<string:id>', methods=["PUT"])
def editTask(id):
  tasks = deta.Base('tasks')
  body = getBody()
  
  tasks.update({
    "title": body["title"],
    "content": body["content"],
    "date": body["date"]
  }, id)
  
  return {
    "updated": True,
  }

#! Delete task
@app.route('/tasks/<string:id>' , methods=["DELETE"])
def taskDelete(id):
  tasks = deta.Base('tasks')
  tasks.delete(id)
  
  return {
    "deleted": True
  }

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