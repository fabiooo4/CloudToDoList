<script>
  import { toDoList } from "../controller/store.js";
  import { filteredToDoList } from "../controller/store.js";
  export let search = "";

  filteredToDoList.set($toDoList);
  $: if (search !== "") {
    filteredToDoList.update((tasks) => {
      return tasks.filter((task) => {
        return task.title.toLowerCase().includes(search.toLowerCase());
      });
    });
    console.log($filteredToDoList)
  } else {
    filteredToDoList.set($toDoList);
    console.log($filteredToDoList)
  }

</script>

<input type="text" name="search" placeholder="Search" class="input input-bordered self-center rounded-full text-lg font-semibold w-fill" bind:value={search} />