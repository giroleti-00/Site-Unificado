// Configuração do envio de e-mail do formulário de contato.
// Envio por e-mail ativo via Web3Forms (a chave de acesso é pública por desenho).
// Se ficar em branco, o botão Enviar abre o WhatsApp e o programa de e-mail do visitante.
//
// Opção 1 - Formspree (formspree.io):
//   provider: 'formspree'
//   endpoint: 'https://formspree.io/f/SEU_CODIGO'
// Opção 2 - Web3Forms (web3forms.com):
//   provider: 'web3forms'
//   accessKey: 'SUA_CHAVE_DE_ACESSO'
window.CF_FORM = {
  provider: 'web3forms',
  endpoint: '',
  accessKey: '26e2bc49-3639-4a82-84eb-eab2796f7334'
};

// Google Analytics 4. O código do Google só é carregado depois que o visitante clica em Aceitar
// no aviso de cookies (LGPD). Para trocar a propriedade, altere o id (formato G-XXXXXXXXXX).
// Para desligar o Analytics e o aviso de cookies, deixe o id em branco ('').
window.CF_GA = {
  id: 'G-N91QJF2G98',
  preview: false
};
