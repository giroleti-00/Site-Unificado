# -*- coding: utf-8 -*-
# Artigos do blog CondoFluxo.
#
# Para publicar um artigo novo: copie um bloco de POSTS, troque os campos e rode
#   CF_FULL=1 CF_OUT=_build python3 src/build2.py
# depois copie o conteúdo de _build/ para a raiz do repositório.
#
# Campos:
#   slug   -> endereço da página (vira blog-<slug>.html e /blog-<slug>)
#   title  -> título do artigo (também usado no <title> e na listagem)
#   desc   -> resumo de 1 ou 2 frases (listagem, Google e redes sociais)
#   date   -> data de publicação, AAAA-MM-DD
#   cat    -> categoria exibida no selo
#   icon   -> ícone Lucide (https://lucide.dev/icons) do cartão (usado se não houver imagem)
#   image  -> (opcional) arquivo em src/assets_src exibido no site (JPG, ~1600 px de largura, 16:9)
#   image_og -> (opcional) versão 1200x630 para redes sociais (se faltar, usa a imagem principal)
#   image_alt -> texto alternativo da imagem
#   read   -> tempo de leitura em minutos
#   body   -> HTML do corpo. Use <h2>, <h3>, <p>, <ul><li>, <ol><li>, <strong>, <a>.
#   faq    -> (opcional) lista de (pergunta, resposta) para a seção de perguntas
#
# Regra editorial do site: texto informativo, sem prometer o que o produto não faz
# e sem substituir orientação técnica ou jurídica.

POSTS = [
    {
        "slug": "manutencao-predial-por-onde-comecar",
        "title": "Manutenção predial no condomínio: por onde o síndico começa",
        "desc": "Um roteiro simples para sair do improviso: levantar os sistemas do prédio, definir responsável e periodicidade e guardar a prova de cada serviço.",
        "date": "2026-11-06",
        "cat": "Manutenção",
        "icon": "wrench",
        "read": 4,
        "image": "blog-manutencao-predial.jpg",
        "image_og": "blog-manutencao-predial-og.jpg",
        "image_alt": "Síndica com prancheta e zelador conversando diante do quadro de medidores de um condomínio residencial",
        "body": """
<p>Quem assume um condomínio costuma receber uma pasta de papéis, um zelador que sabe de cor onde está cada registro e uma lista de coisas que \"sempre se fez assim\". O problema aparece quando o síndico muda, o zelador sai ou alguém pergunta: <em>quando foi a última limpeza da caixa d'água?</em> Sem registro, a resposta vira memória, e memória não comprova nada.</p>

<h2>O que a norma pede, em poucas palavras</h2>
<p>A NBR 5674 trata a manutenção como um <strong>sistema organizado</strong>, e não como uma sequência de consertos. Isso significa ter um programa de atividades com periodicidade, responsáveis definidos, previsão de recursos e registro do que foi feito. A NBR 15575, que trata do desempenho das edificações habitacionais, liga a vida útil dos sistemas do prédio ao cumprimento do manual de uso, operação e manutenção.</p>
<p>Na prática: consertar quando quebra é necessário, mas não basta. O que a norma espera é prevenção com prazo e prova.</p>

<h2>Quatro passos para começar</h2>
<ol>
<li><strong>Levante os sistemas do prédio.</strong> Comece pelo manual entregue pela construtora. Se ele não existir, faça um inventário: elevadores, reservatórios, bombas, quadros elétricos, SPDA, combate a incêndio, portões, cobertura, fachada.</li>
<li><strong>Dê a cada item um responsável e uma periodicidade.</strong> O responsável pode ser o zelador, uma empresa contratada ou um profissional técnico. A frequência vem do manual e das exigências de cada sistema.</li>
<li><strong>Liste os vencimentos legais à parte.</strong> PPCI e AVCB, laudos, seguro obrigatório e inspeção predial têm prazo próprio e precisam de aviso antecipado, porque são os que geram problema quando passam em branco.</li>
<li><strong>Guarde a prova de cada execução.</strong> Data, evidência (laudo, relatório ou foto), responsável e data da próxima vez. Esse histórico é o que você mostra ao conselho, à administradora e ao próximo síndico.</li>
</ol>

<h2>Onde a maioria dos condomínios trava</h2>
<ul>
<li><strong>Tudo na cabeça de uma pessoa.</strong> Quando ela sai, o calendário vai junto.</li>
<li><strong>Planilha que ninguém atualiza.</strong> Funciona por dois meses e depois vira um arquivo desatualizado.</li>
<li><strong>Laudos espalhados.</strong> Estão no e-mail do antigo síndico, numa pasta do WhatsApp ou na gaveta da portaria.</li>
<li><strong>Vencimento sem aviso.</strong> O prazo só é lembrado quando já venceu.</li>
</ul>

<h2>Um sinal simples de que está organizado</h2>
<p>Faça este teste: escolha três sistemas do prédio e responda, sem procurar muito, qual foi a última execução, quem fez e quando é a próxima. Se as três respostas saem em minutos e com documento na mão, a rotina está funcionando. Se não, o primeiro passo é centralizar os registros num só lugar, com prazo e responsável visíveis para quem precisa.</p>

<p>Para ver o detalhe de cada norma e o checklist de sistemas, leia o <a href="manutencao-predial-normativa.html">guia de manutenção predial normativa</a>. Para a licença de incêndio, que tem regras próprias por estado, veja o <a href="ppci-avcb-guia.html">guia de PPCI e AVCB</a>.</p>
""",
        "faq": [
            ("Preciso de um plano de manutenção mesmo em prédio pequeno?",
             "Sim. O tamanho muda a quantidade de itens, mas não a necessidade de ter periodicidade, responsável e registro. Em prédio pequeno o plano costuma ser curto e fácil de manter."),
            ("Quem executa a manutenção, o síndico?",
             "A gestão do condomínio organiza e comprova, e a execução pode ficar com o zelador, uma empresa contratada ou um responsável técnico, conforme o sistema. Em dúvida sobre responsabilidades, consulte um advogado."),
        ],
    },
]
