<script>
  import Login from '../components/view/login.svelte';
  import TaskList from '../components/view/taskList.svelte';

  import { toDoList } from '../components/controller/store.js';
  import { onMount } from 'svelte';
  import { isLogged } from '../components/controller/store.js';

  // Project key: a05juqv9_d4UX8wccxbqnbfXndYUNGNnhjEbsHSxG
  let url = "https://u6bauy.deta.dev/";

  // Load all tasks from the database
  onMount(async () => {
    const response = await fetch(url + "tasks", { method:'GET' });
    let tasks = await response.json();

    toDoList.set(tasks.data);
  });
</script>

{#if $isLogged}
  <TaskList />
{:else}
  <Login />
{/if}