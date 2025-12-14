import React from "react";
import { describe, test, expect, vi } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import Login from "../pages/Login";
import * as authApi from "../api/auth";

describe("Login API Integration", () => {
  test("logs in user and stores token", async () => {
    vi.spyOn(authApi, "loginUser").mockResolvedValue({
      access: "fake-jwt-token",
    });

    render(
      <BrowserRouter>
        <Login />
      </BrowserRouter>
    );

    fireEvent.change(screen.getByPlaceholderText(/username/i), {
      target: { value: "raj" },
    });

    fireEvent.change(screen.getByPlaceholderText(/password/i), {
      target: { value: "Pass1234!" },
    });

    fireEvent.click(screen.getByRole("button", { name: /login/i }));

    await waitFor(() => {
      expect(localStorage.getItem("accessToken")).toBe("fake-jwt-token");
    });
  });
});
