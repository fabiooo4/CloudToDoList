<script>
  import { isLogged } from "../controller/store";
  import { login } from "../controller/fetchApi";
  import { register } from "../controller/fetchApi";
  import { userId } from "../controller/store";

  let username = '';
  let password = '';

  const handleLogin = () => {
    login(username, password)
      .then((response) => {
        if (response.exists) {
          userId.set(response.data["key"]);
          isLogged.set(true);
        } else {
          alert("Wrong username or password");
        }
      })
  };

  const handleRegister = () => {
    register(username, password)
      .then((response) => {
        if (response.added) {
          isLogged.set(true);
          alert("Account added and logged in");
        } else {
          alert("Username already exists");
        }
      })
  };
</script>

<h1 class="font-extrabold text-8xl text-center mt-16 mb-16">Log in</h1>

<div class="flex justify-center items-start w-screen  ">
  <div class="flex flex-col justify-center items-center">
  
    <!--! Username -->
    <label for="username" class="form-control w-full m-2">
      <span class="label-text font-bold text-lg ml-3">Username</span>
      <input type="text" name="username" placeholder="Username" class="input self-center w-full max-w-xs" bind:value={username} />
    </label>
  
    <!--! Password -->
    <label for="password" class="form-control w-full m-2">
      <span class="label-text font-bold text-lg ml-3">Password</span>
      <input type="password" name="password" placeholder="Password" class="input self-center w-full max-w-xs" bind:value={password} />
    </label>

    <div class="flex flex-row w-full justify-between">
      <!--! Register button -->
      <button class="btn btn-ghost mt-4" on:click={handleRegister}>Register</button>

      <!--! Login Button -->
      <button class="btn btn-primary mt-4" on:click={handleLogin}>Log in</button>
    </div>
  
  </div>
</div>