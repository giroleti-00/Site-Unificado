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
    {
        "slug": "checklist-manutencao-predial-por-frequencia",
        "title": "Checklist de manutenção predial por frequência: do diário ao quinquenal",
        "desc": "Uma referência para síndicos organizarem as rotinas do condomínio, da conferência diária aos laudos de longo prazo, com os prazos revisados e as normas ABNT de cada item.",
        "date": "2026-11-08",
        "cat": "Manutenção",
        "icon": "list-checks",
        "read": 7,
        "image": "blog-checklist-manutencao.jpg",
        "image_og": "blog-checklist-manutencao-og.jpg",
        "image_alt": "Engenheiro de inspeção com capacete e tablet ao lado do reservatório de água na cobertura de um prédio ao entardecer",
        "body": """
<p>Manter a manutenção predial em dia vai muito além de evitar vazamentos ou desgaste estético. É uma questão de segurança dos moradores, de proteção do patrimônio e de segurança jurídica para quem administra o condomínio. Reunimos as principais rotinas com base nas normas da ABNT, em especial a NBR 5674, que trata da manutenção de edificações.</p>

<h2>Por que seguir um plano de manutenção</h2>
<p>A NBR 5674 define os requisitos para gerir a manutenção como um sistema organizado: atividades com periodicidade, responsáveis definidos, recursos previstos e registro do que foi feito. Manter o plano e a documentação em dia ajuda a:</p>
<ul>
<li><strong>Proteger moradores e funcionários:</strong> a prevenção reduz o risco de acidentes graves.</li>
<li><strong>Preservar o patrimônio:</strong> o prédio bem cuidado mantém seu valor.</li>
<li><strong>Defender a cobertura do seguro:</strong> a seguradora pode questionar um sinistro quando há falta de manutenção comprovada.</li>
<li><strong>Reduzir a exposição do síndico:</strong> em caso de dano causado por negligência, o síndico pode ser chamado a responder, inclusive pessoalmente. O registro das manutenções é sua melhor defesa.</li>
</ul>

<h2>Checklist por frequência</h2>
<p><strong>Importante:</strong> os prazos abaixo são referências gerais. A periodicidade final depende do manual do prédio, do projeto, das instruções do fabricante, da legislação do município e do estado e das exigências do Corpo de Bombeiros.</p>

<h3>1. Diária e semanal (operacional)</h3>
<ul>
<li><strong>Elevadores:</strong> nivelamento das cabines, botões e sinais sonoros e luminosos.</li>
<li><strong>Bombas de água:</strong> inspeção visual de vazamentos e ruídos, e alternância das bombas de recalque.</li>
<li><strong>Extintores e hidrantes:</strong> conferência visual de acesso, sinalização e lacres, feita pelo zelador.</li>
<li><strong>Iluminação de emergência:</strong> teste rápido dos pontos principais, conforme o manual e o projeto.</li>
</ul>

<h3>2. Mensal</h3>
<ul>
<li><strong>Elevadores:</strong> manutenção preventiva por empresa conservadora registrada, com relatório dos serviços. A NBR 16083 trata das instruções de manutenção; o relatório anual e o registro da empresa seguem a lei do município.</li>
<li><strong>Portões automáticos e cancelas:</strong> lubrificação das guias, teste dos sensores antiesmagamento e do travamento.</li>
<li><strong>Geradores:</strong> teste de partida sob carga e conferência de combustível e óleo, conforme o manual do fabricante. É uma boa prática, e o tempo de teste deve seguir o fabricante.</li>
<li><strong>Central de alarme de incêndio (se o prédio tiver):</strong> teste dos acionadores e detectores, conforme o projeto aprovado pelo Corpo de Bombeiros.</li>
</ul>

<h3>3. Semestral</h3>
<ul>
<li><strong>Extintores:</strong> inspeção (manutenção de nível 1) a cada 6 meses, ou a cada 12 meses nos de CO2, conforme a NBR 12962.</li>
<li><strong>Reservatórios de água:</strong> limpeza a cada 6 meses. Em algumas cidades é obrigatória, como em São Paulo.</li>
<li><strong>Análise de potabilidade:</strong> coleta e laudo laboratorial a cada 6 meses.</li>
<li><strong>Portas corta-fogo:</strong> revisão das molas por empresa especializada. Alguns fornecedores recomendam visitas a cada 3 meses.</li>
<li><strong>SPDA (para-raios):</strong> inspeção visual, prática recomendada por seguradoras e empresas do setor.</li>
</ul>

<h3>4. Anual</h3>
<ul>
<li><strong>Extintores:</strong> manutenção de nível 2 e recarga, conforme a NBR 12962.</li>
<li><strong>Hidrantes e mangueiras:</strong> verificação anual por empresa especializada.</li>
<li><strong>Instalações elétricas das áreas comuns:</strong> reaperto de conexões, termografia e verificação de disjuntores.</li>
<li><strong>Elevadores:</strong> relatório de inspeção anual, quando exigido pela lei do município.</li>
</ul>

<h3>5. Periodicidade longa</h3>
<ul>
<li><strong>Extintores:</strong> manutenção de nível 3, com teste hidrostático, a cada 5 anos, ou antes se houver corrosão ou dano.</li>
<li><strong>SPDA:</strong> inspeção completa e laudo por engenheiro habilitado, conforme a NBR 5419. A referência é de até 3 anos para a maioria das estruturas e de 1 ano em ambientes de corrosão severa ou serviços essenciais. Muitos condomínios adotam laudo anual por cautela ou por exigência da seguradora. Confirme com o engenheiro responsável.</li>
<li><strong>Inspeção predial (NBR 16747):</strong> laudo de estrutura, fachadas e instalações. A norma não fixa um prazo: a periodicidade vem da legislação local e da recomendação do engenheiro, que costuma ser menor em prédios mais antigos.</li>
<li><strong>Fachadas e revestimentos:</strong> teste de percussão para localizar pastilhas e rebocos soltos, conforme a inspeção predial.</li>
</ul>

<h2>Boas práticas de gestão</h2>
<ol>
<li><strong>Guarde o registro de manutenção.</strong> Anote intervenções, chamados técnicos, notas fiscais e relatórios das empresas contratadas.</li>
<li><strong>Exija ART ou RRT.</strong> Em serviços técnicos de engenharia ou arquitetura, peça a Anotação ou o Registro de Responsabilidade Técnica.</li>
<li><strong>Automatize o calendário.</strong> Alertas antes do vencimento de laudos e rotinas evitam descobrir o prazo só depois de vencido.</li>
</ol>

<h2>Conclusão</h2>
<p>Seguir a NBR 5674 não é burocracia: é o que transforma a manutenção em prevenção e protege moradores, patrimônio e o próprio síndico. O que sustenta tudo isso é a rotina com <strong>prazo, responsável e prova</strong>. Um laudo emitido que ninguém encontra quando a seguradora, o conselho ou a fiscalização pedem vale quase tanto quanto um laudo que nunca existiu.</p>
<p>Comece pelo básico: levante os sistemas do prédio, defina a periodicidade de cada um, nomeie quem executa e guarde tudo em um só lugar, com histórico, para que a próxima gestão receba o calendário pronto.</p>
<p>Para aprofundar, leia o <a href="manutencao-predial-normativa.html">guia de manutenção predial normativa</a> e o <a href="ppci-avcb-guia.html">guia de PPCI e AVCB</a>. Se quer sair da planilha e da memória do zelador, conheça o <a href="gestao.html">Convivus</a>.</p>
""",
        "faq": [
            ("A NBR 5674 é obrigatória por lei?",
             "As normas da ABNT são referências técnicas e não são lei por si só, mas costumam ser usadas por seguradoras, em perícias e em leis que as citam. Na dúvida sobre responsabilidades, consulte um advogado."),
            ("Com que frequência fazer o laudo do SPDA (para-raios)?",
             "Pela NBR 5419, a referência é de até 3 anos para a maioria das estruturas e de 1 ano em ambientes de corrosão severa ou serviços essenciais. Muitos condomínios adotam laudo anual por cautela ou exigência da seguradora. Confirme com o engenheiro responsável."),
            ("Qual o prazo do teste hidrostático dos extintores?",
             "A NBR 12962 prevê a manutenção de nível 3, com teste hidrostático, a cada 5 anos, ou antes se houver corrosão ou dano no cilindro. A inspeção é semestral e a manutenção de nível 2 é anual."),
            ("A inspeção predial tem prazo fixo?",
             "A NBR 16747 não fixa uma periodicidade. O prazo vem da legislação do município ou do estado e da recomendação do engenheiro responsável, que costuma ser menor em prédios mais antigos."),
        ],
    },
]
