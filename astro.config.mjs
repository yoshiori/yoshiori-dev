import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import react from '@astrojs/react';
import icon from 'astro-icon';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://yoshiori.dev',

  vite: {
    plugins: [tailwindcss()],
  },

  integrations: [react(), icon(), sitemap()],
});