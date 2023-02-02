import { writable } from "svelte/store";

export const toDoList = writable([]);
export const filteredToDoList = writable([]);
export const isLogged = writable(false);
export const userId = writable("");