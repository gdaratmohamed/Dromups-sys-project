import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    globals: true, // ✅ Pour utiliser test, expect, vi sans import
    environment: 'jsdom', // ✅ Simule le DOM
    setupFiles: './src/setupTests.js', // ✅ Fichier pour jest-dom
    coverage: {
      provider: 'istanbul', // ✅ Pour rapports de couverture
      reporter: ['text', 'lcov'], // ✅ Génère rapport lisible + pour Jenkins
    },
  },
});
