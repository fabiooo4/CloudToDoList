<script>
  import Task from './task.svelte';
  import AddTask from './addTask.svelte';
  import Search from './search.svelte';

  import { toDoList } from '../controller/store.js';
  import { userId } from '../controller/store.js';


</script>

<h1 class="text-8xl text-center font-extrabold m-4">ToDo List</h1>

<div class="flex flex-row justify-center flex-wrap">
  <Search />
  <AddTask />
</div>

<div class='flex flex-row flex-wrap justify-center items-center w-screen pb-10'>
  {#if $toDoList.length > 0}
    {#each $toDoList as task}
      {#if task.userId == $userId}
        <Task {task}/>
      {/if}
    {/each}
  {:else}
    <h2 class='text-2xl text-center font-bold m-4'>No tasks found...</h2>
  {/if}
</div>