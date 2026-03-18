/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        inter: ['Inter', 'sans-serif'],
      },
      colors: {
        brand: {
          primary: '#3b82f6',
          secondary: '#1d4ed8',
          dark: '#0f172a',
          surface: '#1e293b',
        }
      }
    },
  },
  plugins: [],
}
