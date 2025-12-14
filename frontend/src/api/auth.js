import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});

export async function loginUser(credentials) {
  const response = await api.post("/api/auth/login", credentials);
  return response.data;
}
