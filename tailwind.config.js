/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './*.html',               // arquivos HTML na raiz
    './src/**/*.{js,ts}',      // arquivos JS/TS da pasta src
    './js/**/*.js',            // arquivos JS na pasta js
    './styles/**/*.css',       // arquivos CSS na pasta styles
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}