# Site-Unificado

Site do Convivus

Site institucional em português (Porto Alegre) — www.convivus.com.br.
Marca Convivus (portal de gestão condominial). A página Comunicação (materiais para moradores) fica só como link no rodapé; o e-mail de contato é convivus@convivus.com.br e o portal fica em portal.convivus.com.br.

## Estrutura

- Raiz: site pronto para publicar (HTML estático + `assets/`, `config.js`, `sitemap.xml`, `robots.txt`, `llms.txt` e `_headers`, que a Cloudflare Pages lê para aplicar os cabeçalhos de segurança).
- `src/build2.py`: gerador das páginas (Python 3). O CSS (Tailwind) é compilado no build com Node/npm.
- `src/tailwind/`: `package.json` com as versões exatas do Tailwind CSS e do Lucide, configuração e `package-lock.json`.
- `src/assets_src/`: imagens e logos usados pelo gerador.

## Publicar

Hospede a raiz do repositório em qualquer hospedagem estática (GitHub Pages, Netlify, Cloudflare Pages ou a hospedagem do domínio).
Detalhes e configuração do formulário de contato: `LEIA-ME.txt`.

## Regenerar as páginas

```bash
CF_FULL=1 CF_OUT=_build python3 src/build2.py
```

O resultado fica em `_build/` (não versionado). Copie para a raiz para atualizar o site publicado.
Na primeira execução o gerador roda `npm ci` em `src/tailwind` (precisa de Node 18 ou mais novo e acesso ao registro npm). O CSS compilado (`assets/tailwind.css`), o Lucide (`assets/lucide.min.js`) e os scripts do site (`assets/site.js`, `consent.js`, `js-flag.js`) saem em `assets/`; nenhum script de terceiros é carregado, exceto o Google Tag, que só roda depois do aceite de cookies. Só o Google Fonts continua externo.

Política de segurança de conteúdo (CSP): o `_headers` sai com ela aplicada; com `CF_CSP=report-only` ela só registra violações no console (útil para testar mudanças).

## Formulário de contato

O envio por e-mail do formulário de contato está ativo via Web3Forms (`config.js`, e-mail de destino condofluxo@gmail.com). Para trocar de serviço ou de chave, edite `config.js`; deixando `provider` em branco, o botão Enviar abre o WhatsApp e o programa de e-mail do visitante.
