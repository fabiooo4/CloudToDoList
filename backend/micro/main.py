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

  
#! User list
@app.route('/user', methods=["GET"])
def userList():
  users = deta.Base('users')
  out = users.fetch().items
  
  return {
    "data": out,
    "size": len(out)
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
	

# #! Single task
# @app.route('/tasks/<int:id>')
# def taskDetails(id):
#   database = connect(taskdb)
  
#   database.get("cursor").execute(f"""
#   SELECT * FROM tasks
#     WHERE id = ?
#   """, (id,))
    
#   out = []
#   for row in database.get("cursor").fetchall():
#     out.append({
#       "id": row[0],
#       "date": row[1],
#       "title": row[2],
#       "content": row[3],
#       "state": row[4]
#     })
  
#   return {
#     "data": out,
#     "exists": len(out) > 0
#   }
    
# #! Toggle state
# @app.route('/tasks/<int:id>', methods=["PATCH"])
# def toggleState(id):
#   database = connect(taskdb)
  
#   database.get("cursor").execute(f"""
#   UPDATE tasks
#     SET state = NOT state
#     WHERE id = ?
#   """, (id,))
#   database.get("db").commit()
  
#   return {
#     "updated": True,
#   }
  
# #! Edit task
# @app.route('/tasks/<int:id>', methods=["PUT"])
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
# @app.route('/tasks/<int:id>' , methods=["DELETE"])
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

# #! Add task
# @app.route('/tasks', methods=["POST"])
# def addTask():  
#   database = connect(taskdb)
#   body = getBody()
  
#   database.get("cursor").execute("""
#   INSERT INTO tasks(date, title, content, state) VALUES(?, ?, ?, ?)
#   """, (body["date"], body["title"], body["content"], False))
#   database.get("db").commit()
  
#   return {
#     "added": True,
#   }

# print("Server started")