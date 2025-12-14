import React from "react";
import { describe, test, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import Login from "../pages/Login";

describe("Login Page", () => {
  test("renders login heading", () => {
    render(
      <BrowserRouter>
        <Login />
      </BrowserRouter>
    );

    expect(
      screen.getByRole("heading", { name: /login/i })
    ).toBeInTheDocument();
  });

  test("renders username and password inputs", () => {
    render(
      <BrowserRouter>
        <Login />
      </BrowserRouter>
    );

    expect(screen.getByPlaceholderText(/username/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/password/i)).toBeInTheDocument();
  });

  test("renders login button", () => {
    render(
      <BrowserRouter>
        <Login />
      </BrowserRouter>
    );

    expect(
      screen.getByRole("button", { name: /login/i })
    ).toBeInTheDocument();
  });
});
