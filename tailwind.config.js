/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        plus: ['"Plus Jakarta Sans"', 'sans-serif'],
        inter: ['Inter', 'sans-serif'],
      },
      colors: {
        'brand-orange': '#FF5C00',
        'brand-gray': '#6C757D',
        'brand-light': '#F8F1E9',
        'brand-border': '#F0F0F0',
      },
      boxShadow: {
        'premium': '0 20px 40px -10px rgba(0,0,0,0.1), 0 10px 20px -10px rgba(0,0,0,0.05)',
        'hyper-premium': '0 60px 100px -20px rgba(0,0,0,0.35), 0 30px 60px -30px rgba(0,0,0,0.4)',
        'pill': '0 15px 40px -5px rgba(0,0,0,0.12)',
      }
    },
  },
  plugins: [],
}
