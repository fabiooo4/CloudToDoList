<script>
  import { isLogged } from "../controller/store";
  import { login } from "../controller/fetchApi";

  let username = '';
  let password = '';

const handleLogin = () => {
  login(username, password)
    .then((response) => {
      if (response.exists) {
        isLogged.set(true);
      } else {
        alert("Wrong username or password");
      }
    })
};

</script>

<h1 class="font-extrabold text-8xl text-center mt-16 mb-16">Login</h1>

<div class="flex justify-center items-start w-screen  ">
  <div class="flex flex-col justify-center items-center">
  
    <!-- Username -->
    <label for="username" class="form-control w-full m-2">
      <span class="label-text font-bold text-lg ml-3">Username</span>
      <input type="text" name="username" placeholder="Username" class="input self-center w-full max-w-xs" bind:value={username} />
    </label>
  
    <!-- Password -->
    <label for="password" class="form-control w-full m-2">
      <span class="label-text font-bold text-lg ml-3">Password</span>
      <input type="password" name="password" placeholder="Password" class="input self-center w-full max-w-xs" bind:value={password} />
    </label>

    <!-- Login Button -->
    <button class="btn btn-primary w-1/2 mt-4" on:click={handleLogin}>Login</button>
  
  </div>
</div>