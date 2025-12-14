import React from "react";
import { describe, test, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import Login from "../pages/Login";

describe("Login Page", () => {
  test("renders login heading", () => {
    render(<Login />);
    expect(
      screen.getByRole("heading", { name: /login/i })
    ).toBeInTheDocument();
  });

  test("renders username and password inputs", () => {
    render(<Login />);
    expect(screen.getByPlaceholderText(/username/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/password/i)).toBeInTheDocument();
  });

  test("renders login button", () => {
    render(<Login />);
    expect(
      screen.getByRole("button", { name: /login/i })
    ).toBeInTheDocument();
  });
});
