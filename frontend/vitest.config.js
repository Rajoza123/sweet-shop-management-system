import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    globals: true,          // enables describe, test, expect
    environment: "jsdom",
    setupFiles: "./src/testSetup.js",
  },
});
