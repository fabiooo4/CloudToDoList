<script>
  import { isLogged } from '../controller/store.js';
  
  const handleClick = () => {
    isLogged.set(false);
  };
</script>

<div class="m-4">
  <button class="btn btn-ghost" on:click={handleClick}>Logout</button>
</div>