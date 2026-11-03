# Site-Unificado

Site do Condofluxo e Convivus

Site institucional em português (Porto Alegre) — www.condofluxo.com.br.
Marca CondoFluxo (site) + Convivus (portal de gestão condominial).

## Estrutura

- Raiz: site pronto para publicar (HTML estático + `assets/`, `config.js`, `sitemap.xml`, `robots.txt`, `llms.txt`).
- `src/build2.py`: gerador das páginas (Python 3, sem dependências externas).
- `src/assets_src/`: imagens e logos usados pelo gerador.

## Publicar

Hospede a raiz do repositório em qualquer hospedagem estática (GitHub Pages, Netlify, Cloudflare Pages ou a hospedagem do domínio).
Detalhes e configuração do formulário de contato: `LEIA-ME.txt`.

## Regenerar as páginas

```bash
CF_FULL=1 CF_OUT=_build python3 src/build2.py
```

O resultado fica em `_build/` (não versionado). Copie para a raiz para atualizar o site publicado.
Tailwind CSS, Lucide e Google Fonts são carregados por CDN.

## Formulário de contato

Edite `config.js` (Formspree ou Web3Forms) para o e-mail chegar sozinho. Sem configuração, o botão Enviar abre o WhatsApp e o programa de e-mail do visitante.
