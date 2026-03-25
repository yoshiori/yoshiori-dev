/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,ts,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"IBM Plex Sans JP"', 'sans-serif'],
        mono: ['"IBM Plex Mono"', 'monospace'],
        display: ['"Bebas Neue"', 'sans-serif'],
      },
      colors: {
        bg:      '#0a0a0a',
        surface: '#111111',
        border:  '#222222',
        muted:   '#555555',
        text:    '#e8e8e8',
        accent:  '#e8ff00',   // electric yellow
      },
    },
  },
  plugins: [],
};
