/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: ['./main/templates/*.html','./main/templates/partials/*.html'],
  theme: {
    extend: {
      keyframes: {        
        bgmove: {
           "0%": { backgroundPosition: "0 0" },
          "100%": { backgroundPosition: "0 100%" }
        },
      },
      animation: {
        bgmove: 'bgmove 360s infinite',
      }
    }
  },
  plugins: [],
}

