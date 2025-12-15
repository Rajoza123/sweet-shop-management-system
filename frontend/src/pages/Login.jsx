import React from "react";

export default function Login() {
  return (
    <div>
      <h1>Login</h1>

      <form>
        <input
          type="text"
          placeholder="Username"
          aria-label="username"
        />

        <input
          type="password"
          placeholder="Password"
          aria-label="password"
        />

        <button type="submit">Login</button>
      </form>
    </div>
  );
}
