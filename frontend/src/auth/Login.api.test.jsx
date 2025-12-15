import React from "react";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import Login from "../pages/Login";
import axios from "axios";
import { vi } from "vitest";

vi.mock("axios");

describe("Login API integration", () => {
  const renderLogin = () =>
    render(
      <BrowserRouter>
        <Login />
      </BrowserRouter>
    );

  test("submits login form and calls login API", async () => {
    axios.post.mockResolvedValueOnce({
      data: {
        id: 1,
        username: "admin",
      },
    });

    renderLogin();

    fireEvent.change(screen.getByPlaceholderText(/username/i), {
      target: { value: "admin" },
    });

    fireEvent.change(screen.getByPlaceholderText(/password/i), {
      target: { value: "password123" },
    });

    fireEvent.click(screen.getByRole("button", { name: /login/i }));

    await waitFor(() => {
      expect(axios.post).toHaveBeenCalledWith(
        "http://127.0.0.1:8000/api/auth/login/",
        {
          username: "admin",
          password: "password123",
        }
      );
    });
  });
});
