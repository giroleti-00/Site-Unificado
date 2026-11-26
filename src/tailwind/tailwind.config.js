// Mesma configuração que o site usava no CDN do Tailwind (3.4.17): só a fonte Figtree.
// O conteúdo a varrer é passado pelo build2.py (--content), pois depende da pasta de saída.
module.exports = {
  content: [],
  theme: { extend: { fontFamily: {
    sans: ['Figtree', 'ui-sans-serif', 'system-ui', 'sans-serif'],
    serif: ['Figtree', 'ui-sans-serif', 'system-ui', 'sans-serif'],
  } } },
}
