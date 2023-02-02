<script>
  let username = '';
  let password = '';
</script>

<div class="flex justify-center items-center w-screen h-screen">
  <div class="flex flex-col justify-center items-center">
    <h1 class="font-extrabold text-8xl text-center mb-8">Login</h1>
  
    <!-- Username -->
    <label for="username" class="form-control w-full m-0 sm:m-2">
      <span class="label-text font-bold text-lg">Username</span>
      <input type="text" name="username" placeholder="Username" class="input self-center w-full max-w-xs" bind:value={username} />
    </label>
  
    <!-- Password -->
    <label for="password" class="form-control w-full m-0 sm:m-2">
      <span class="label-text font-bold text-lg">Password</span>
      <input type="password" name="password" placeholder="Password" class="input self-center w-full max-w-xs" bind:value={password} />
    </label>
  
  </div>
</div>