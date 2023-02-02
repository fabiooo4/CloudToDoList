import { writable } from "svelte/store";

export const toDoList = writable([]);
export const isLogged = writable(false);
export const userId = writable("");