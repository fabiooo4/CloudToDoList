import { toDoList, userId } from "./store";

let url = "https://u6bauy.deta.dev/";

//? Refresh tasks
export const refreshTasks = async () => {
  const tasks = await getTasks();
  toDoList.set(tasks.data);
}

//? Login user
export const login = async (username, password) => {
  const response = await fetch(url + "login", {
    method: "POST",
    headers: {
      'Content-type': 'application/json'
    },
    body: JSON.stringify({ "username": username.toString(), "password": password.toString() })
  });
  const data = await response.json();
  userId.set(data.data["key"]);
  return data;
}

//? Get all tasks from the server
export const getTasks = async () => {
  const response = await fetch(url + "tasks", { method: "GET" });
  const data = await response.json();
  return data;
}

//? Get a single task from the server
export const getSingle = async (index) => {
  const response = await fetch(url + "tasks/" + index, { method: "GET" });
  const data = await response.json();
  return data;
}

//? Toggle state of a task given its index
export const toggleState = async (index) => {
  const response = await fetch(url + "tasks/" + index, { method: "PATCH" });
  const data = await response.json();

  return data;
}

//? Delete a task given its index
export const deleteTask = async (index) => {
  const response = await fetch(url + "tasks/" + index, { method: "DELETE" });
  const data = await response.json();

  refreshTasks();
  return data;
}

//? Add a task to the server
export const addTask = async (task) => {
  const response = await fetch(url + "tasks", {
    method: 'POST',
    headers: {
      'Content-type': 'application/json'
    },
    body: JSON.stringify(task)
  });

  const data = await response.json();
  refreshTasks();
  return data;
}

//? Edit a task on the server
export const editTask = async (task) => {
  const response = await fetch(url + "tasks/" + task.key, {
    method: "PUT",
    headers: {
      'Content-type': 'application/json'
    },
    body: JSON.stringify(task)
  });
  const data = await response.json();
  refreshTasks();
  return data;
}