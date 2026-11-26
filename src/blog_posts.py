# -*- coding: utf-8 -*-
# Artigos do blog Convivus.
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
        "slug": "acidente-falta-manutencao-processo-sindico",
        "title": "Acidente por falta de manutenção pode gerar processo contra o síndico?",
        "desc": "Sim. Além do condomínio, o síndico pode responder na esfera civil e, em casos graves, na criminal. Veja o que diz a lei, quando a responsabilidade é afastada e como se proteger com registros.",
        "date": "2026-11-14",
        "cat": "Responsabilidade",
        "icon": "shield-alert",
        "read": 5,
        "image": "blog-acidente-sindico.jpg",
        "image_og": "blog-acidente-sindico-og.jpg",
        "image_alt": "Síndica de blazer verde consultando o calendário de manutenção em um tablet, no hall de um condomínio com elevadores, extintor e placa de piso molhado",
        "body": """
<p><strong>Sim. Um acidente causado por falta de manutenção pode gerar processo contra o síndico, e não só contra o condomínio.</strong> Dependendo do caso, ele pode responder na esfera civil (indenização) e, nas situações mais graves, até na criminal.</p>
<p>Essa é uma das dúvidas mais comuns entre síndicos, principalmente entre os profissionais que cuidam de vários condomínios ao mesmo tempo. Um portão com mola quebrada, um piso solto na garagem, um elevador sem manutenção: qualquer um desses itens pode virar um acidente. E o acidente pode virar um processo.</p>
<p>Neste artigo, explicamos o que diz a lei, em que situações o síndico pode ser responsabilizado e, principalmente, o que ele pode fazer para se proteger.</p>

<h2>O que diz a lei: a conservação é dever do síndico</h2>
<p>O ponto de partida é o <strong>art. 1.348, inciso V, do Código Civil</strong>. Ele diz que compete ao síndico "diligenciar a conservação e a guarda das partes comuns e zelar pela prestação dos serviços que interessem aos possuidores".</p>
<p>Na prática, tudo o que está na área comum passa pela gestão do síndico: elevadores, bombas, reservatórios, para-raios, extintores e hidrantes, gerador, fachada, piscina, portões. O mesmo artigo também faz do síndico o representante do condomínio, ativa e passivamente. Por isso, quando algo dá errado, ele está na linha de frente.</p>

<h2>Na esfera civil: o dever de indenizar</h2>
<p>Quem sofre um dano por ação ou omissão de outra pessoa tem direito a ser indenizado. A regra está nos <strong>arts. 186 e 927 do Código Civil</strong> e vale tanto para negligência quanto para imprudência ou imperícia.</p>
<p>No caso de um acidente por falta de manutenção, o caminho costuma ser este:</p>
<ol>
<li><strong>O condomínio é acionado primeiro.</strong> Como pessoa jurídica responsável pelas áreas comuns, ele responde perante a vítima quando o dano decorre de falta de manutenção ou de ausência de sinalização.</li>
<li><strong>O síndico pode responder pessoalmente.</strong> Isso acontece quando fica provado que ele agiu com culpa, deixando de cumprir as atribuições que a lei lhe dá.</li>
<li><strong>O condomínio pode cobrar do síndico.</strong> Se o condomínio pagou a indenização e a culpa foi do síndico, pode buscar o ressarcimento contra ele.</li>
</ol>
<p>Ou seja: o fato de a ação ser movida contra o condomínio não significa que o síndico está fora da história.</p>

<h2>Na esfera criminal: quando a omissão vira crime</h2>
<p>Nos casos mais graves, a responsabilidade pode ir além da indenização. O síndico ocupa o que o Direito chama de <strong>posição de garantidor</strong>, prevista no <strong>art. 13, §2º, do Código Penal</strong>: ele tem o dever e a possibilidade de agir para evitar o resultado.</p>
<p>Por isso, se alguém se fere ou morre por causa de uma omissão na manutenção, o síndico pode responder por <strong>lesão corporal</strong> ou <strong>homicídio culposo</strong>, ou seja, sem intenção, mas por negligência.</p>
<p>Isso não é automático. Em geral, é preciso demonstrar que o síndico sabia do risco (ou deveria saber), que podia agir e que não agiu. É exatamente nesse ponto que a documentação da gestão faz toda a diferença.</p>

<h2>"Mas eu contratei uma empresa": terceirizar não basta</h2>
<p>Um engano comum é achar que, ao contratar uma empresa de manutenção, a responsabilidade passa toda para ela. Não é bem assim.</p>
<p>Quando o serviço é terceirizado, a responsabilidade pode ser <strong>compartilhada entre a empresa, o condomínio e o síndico</strong>. O síndico continua podendo responder por:</p>
<ul>
<li><strong>Falha na fiscalização:</strong> não acompanhar se o serviço foi feito, quando e como.</li>
<li><strong>Escolha equivocada do prestador:</strong> contratar uma empresa sem qualificação, sem responsável técnico ou sem a documentação exigida.</li>
</ul>
<p>Contratar é o primeiro passo. Acompanhar, cobrar e registrar é o que efetivamente protege o síndico.</p>

<h2>E quando o condomínio não responde?</h2>
<p>Nem todo acidente gera responsabilidade. Situações de <strong>força maior</strong> ou sem culpa da gestão costumam afastar o dever de indenizar, desde que o condomínio tenha agido e sinalizado o risco. Alguns exemplos:</p>
<ul>
<li><strong>Piso molhado por chuva forte:</strong> em regra, força maior, desde que o local tenha sido sinalizado.</li>
<li><strong>Galho que cai e danifica um carro:</strong> a responsabilidade tende a ser afastada se houver poda regular comprovada.</li>
<li><strong>Criança sozinha no elevador:</strong> as regras de segurança de elevadores costumam vedar o transporte de menores de 12 anos desacompanhados, e a responsabilidade tende a recair sobre os pais ou responsáveis.</li>
</ul>
<p>Repare no padrão: em todos os casos, o que afasta a responsabilidade é o condomínio conseguir mostrar que fez a parte dele.</p>

<h2>A melhor defesa do síndico é a prova</h2>
<p>Se acontecer um acidente, a pergunta central será: <strong>o síndico consegue provar que cumpriu o seu dever?</strong> Sem registro, fica muito difícil demonstrar que não houve omissão. Por isso, todo síndico deveria ter sempre à mão:</p>
<ul>
<li><strong>Plano de manutenção preventiva em dia</strong>, com as periodicidades das normas ABNT (como a NBR 5674). Veja o <a href="blog-checklist-manutencao-predial-por-frequencia.html">checklist de manutenção predial por frequência</a>.</li>
<li><strong>Laudos, notas fiscais e contratos</strong> de cada serviço executado.</li>
<li><strong>PPCI aprovado e licença de incêndio válida</strong> (no RS, o APPCI emitido pelo Corpo de Bombeiros).</li>
<li><strong>Chamados e ocorrências registrados com data</strong>, mostrando quando o problema foi informado e quando foi resolvido.</li>
<li><strong>Fotos e avisos de sinalização</strong> em áreas com risco temporário.</li>
<li><strong>Atas e comunicados</strong> que comprovem que a assembleia e os moradores foram informados sobre riscos e obras necessárias.</li>
</ul>
<p>Esse histórico precisa estar organizado e acessível. Documento perdido em e-mail, pasta física ou WhatsApp do zelador não ajuda na hora em que é preciso comprovar.</p>

<h2>Como o Convivus ajuda o síndico a se proteger</h2>
<p>Cuidar do prédio é obrigação do síndico. Provar que cuidou também. O <a href="gestao.html">Convivus</a> foi criado para que essa prova esteja sempre pronta:</p>
<ul>
<li><strong>Calendário de manutenção preventiva</strong> baseado nas normas ABNT, com semáforo Em dia / A vencer / Vencido e alertas antes do prazo.</li>
<li><strong>Módulo de PPCI</strong> com os prazos de renovação da licença de incêndio (APPCI, no RS).</li>
<li><strong>Repositório de documentos com trilha de auditoria</strong>, para laudos, contratos e notas fiscais.</li>
<li><strong>Livro de Ocorrências</strong> que só recebe novos registros.</li>
<li><strong>Vários condomínios em uma só conta</strong>, para síndicos profissionais e administradoras.</li>
</ul>
<p>Quer ver como funciona na prática? <a href="gestao.html">Conheça o Convivus</a> ou fale com a gente pelo WhatsApp (51) 99611-7922.</p>

<h2>Fontes</h2>
<ul>
<li><a href="https://www.sindiconet.com.br/informese/responsabilidade-por-acidentes-ocorridos-no-condominio-colunistas-rodrigo-karpat/amp" target="_blank" rel="noopener">Responsabilidade por acidentes ocorridos no condomínio, por Rodrigo Karpat (SíndicoNet)</a></li>
<li><a href="https://condominiosc.com.br/jornal-dos-condominios/ponto-de-vista/2980-a-responsabilidade-civil-e-criminal-do-sindico" target="_blank" rel="noopener">A responsabilidade civil e criminal do síndico, Jornal dos Condomínios</a></li>
</ul>
""",
        "faq": [
            ("O síndico pode ser processado por um acidente no condomínio?",
             "Pode. O condomínio costuma ser acionado primeiro, mas o síndico também pode responder, na esfera civil, se ficar provado que agiu com culpa ao deixar de cumprir seus deveres de conservação. Nos casos mais graves, pode haver responsabilização criminal."),
            ("Contratar uma empresa de manutenção livra o síndico da responsabilidade?",
             "Não. A responsabilidade pode ser compartilhada entre a empresa, o condomínio e o síndico. O síndico ainda pode responder por falha na fiscalização do serviço ou por escolher um prestador sem qualificação ou documentação."),
            ("Como o síndico comprova que cumpriu o seu dever?",
             "Com registros: plano de manutenção em dia, laudos, notas fiscais e contratos, PPCI e licença de incêndio válidos, chamados e ocorrências com data, fotos, sinalização e atas que mostrem que moradores e assembleia foram informados."),
        ],
    },
    {
        "slug": "nfse-condominios",
        "title": "Condomínios e a NFS-e: o que muda em 1º de dezembro",
        "desc": "A partir de 1º de dezembro de 2026, o condomínio passa a emitir NFS-e no próprio CNPJ. Entenda a regra, por que isso não é imposto novo, a exceção dos 80% e o que fazer até lá.",
        "date": "2026-11-11",
        "cat": "Legislação",
        "icon": "receipt",
        "read": 6,
        "image": "blog-nfse-condominios.jpg",
        "image_og": "blog-nfse-condominios-og.jpg",
        "image_alt": "Notebook com a tela da NFS-e, calendário marcando 1º de dezembro de 2026 e caderno com checklist sobre a mesa, com um prédio residencial ao fundo",
        "body": """
<p>A Reforma Tributária do consumo chegou ao dia a dia do condomínio. A partir de <strong>1º de dezembro de 2026</strong>, a taxa condominial e as demais receitas do condomínio passam a ser documentadas em Nota Fiscal de Serviços Eletrônica (NFS-e). A nota é emitida no CNPJ do próprio condomínio, e não no da administradora.</p>

<h2>O que diz a nova regra</h2>
<p>A obrigação vem do Ato Conjunto RFB/CGIBS nº 4, de 30 de julho de 2026 (art. 1º, III, "f"). Ele inclui no cronograma da NFS-e a cobrança de taxas e demais valores condominiais pelo condomínio edilício, além das outras receitas do condomínio. O regulamento do IBS (Resolução CGIBS nº 6/2026) confirma que o dever de emitir documento fiscal alcança as operações do condomínio.</p>
<p>O ato define <strong>quando</strong> o documento passa a ser exigido. Quem paga ou não paga tributo é assunto da Lei Complementar 214/2025, explicada mais abaixo.</p>
<table>
<thead><tr><th>Data</th><th>O que acontece</th></tr></thead>
<tbody>
<tr><td><strong>01/10/2026</strong></td><td>Publicada a Nota Técnica SE/CGNFS-e nº 009, que cria o código 99.05.01, Operações Condominiais. A nota da taxa de administração passa a trazer os campos de IBS e CBS.</td></tr>
<tr><td><strong>03/11/2026</strong></td><td>O ambiente nacional da NFS-e entra em produção com o novo leiaute.</td></tr>
<tr><td><strong>01/12/2026</strong></td><td>Cobranças e outras receitas do condomínio passam a exigir NFS-e.</td></tr>
<tr><td><strong>01/01/2027</strong></td><td>Administradoras do Simples Nacional passam a destacar IBS e CBS nas suas notas.</td></tr>
</tbody>
</table>
<p>Em 2026, o IBS e a CBS estão em fase de teste: os campos são preenchidos na nota, mas não há cobrança efetiva dos novos tributos. A transição da Reforma segue até 2033.</p>

<h2>Emitir nota não é pagar imposto</h2>
<p>Pelo art. 26 da LC 214/2025, o condomínio edilício, como regra, <strong>não é contribuinte</strong> do IBS nem da CBS. A cota condominial continua sendo rateio de despesas entre os condôminos. O que muda é que agora ela fica documentada em nota fiscal.</p>
<p>Essa condição muda em dois cenários:</p>
<ul>
<li><strong>Regra dos 80%.</strong> Se as cobranças feitas aos condôminos ficarem abaixo de 80% da receita total, ou seja, se as receitas com terceiros passarem de 20%, o condomínio passa a recolher IBS e CBS sobre essas operações com terceiros.</li>
<li><strong>Opção pelo regime regular.</strong> Qualquer condomínio pode optar por ser contribuinte. Nesse caso, o IBS e a CBS incidem sobre tudo o que ele cobra, inclusive as cotas dos moradores, com direito a créditos. Por isso a opção raramente compensa em prédios residenciais.</li>
</ul>
<p>As receitas que pesam nessa conta são as de exploração das áreas comuns: aluguel do topo do prédio para antenas de telefonia, publicidade em fachada e elevadores, locação do salão de festas a não condôminos e estacionamento para terceiros. Prédios comerciais e mistos tendem a chegar perto do limite antes dos residenciais.</p>
<p>Dois efeitos indiretos valem para todos:</p>
<ul>
<li>O condomínio que não é contribuinte recebe notas de fornecedores já com IBS e CBS, mas não aproveita esses créditos. Serviços de limpeza, portaria e segurança devem pesar mais no orçamento a partir de 2027.</li>
<li>A NFS-e não substitui a declaração, no Imposto de Renda dos proprietários, dos rendimentos obtidos com as áreas comuns. São obrigações distintas.</li>
</ul>

<h2>Como é a nota fiscal do condomínio</h2>
<p>A nota usa o código de tributação nacional <strong>99.05.01, Operações Condominiais</strong>. É um código de IBS e CBS, sem ISS.</p>
<p>Ela não sai pelo sistema da prefeitura. Os códigos do grupo 99 só são emitidos pelos canais nacionais: o Emissor Nacional (web e aplicativo) ou a integração por API com o ambiente nacional da NFS-e. Na prática, cada condomínio precisa de CNPJ ativo e de um meio de acesso ao emissor, como o certificado digital.</p>
<p>O leiaute pede a data de vencimento original e cada cobrança do boleto separada por tipo: condomínio ordinário, condomínio privativo, fundo de promoção e propaganda, impostos e taxas, fundo de reserva e outras cobranças, como a taxa extra. Descontos, como o de pontualidade, aparecem destacados.</p>
<p>Receitas com terceiros não usam o 99.05.01. O aluguel do salão ou de uma vaga a não condôminos, por exemplo, vai nos códigos de locação e cessão de imóveis (99.03.x).</p>

<h2>Nota do condomínio x nota da administradora</h2>
<p>São dois documentos diferentes. A administradora já emite NFS-e pela sua taxa de administração. A novidade é a nota das cobranças, no CNPJ do condomínio. A administradora ou o síndico pode operar a emissão, mas a nota é sempre do condomínio.</p>
<table>
<thead><tr><th></th><th>Nota do condomínio</th><th>Nota da administradora</th></tr></thead>
<tbody>
<tr><td><strong>Emitente</strong></td><td>Condomínio, no CNPJ próprio</td><td>Administradora</td></tr>
<tr><td><strong>O que registra</strong></td><td>Taxas e valores cobrados dos condôminos</td><td>Taxa de administração</td></tr>
<tr><td><strong>Código</strong></td><td>99.05.01</td><td>Serviço de administração, com ISS</td></tr>
<tr><td><strong>Onde emitir</strong></td><td>Só nos emissores nacionais</td><td>Conforme o município da administradora</td></tr>
<tr><td><strong>Campos de IBS e CBS</strong></td><td>A partir de 01/12/2026</td><td>A partir de 01/10/2026 (Simples Nacional: 01/01/2027)</td></tr>
</tbody>
</table>

<h2>Checklist até 1º de dezembro</h2>
<ol>
<li><strong>Confirme o CNPJ.</strong> Cada condomínio precisa estar com o cadastro ativo e regular.</li>
<li><strong>Garanta o acesso ao Emissor Nacional.</strong> Providencie o certificado digital e defina quem opera a emissão: a administradora ou o síndico.</li>
<li><strong>Separe as cobranças por tipo.</strong> Taxa ordinária, fundo de reserva e taxa extra precisam aparecer separadas no rateio e no plano de contas.</li>
<li><strong>Levante as receitas com terceiros.</strong> Antenas, publicidade e locação de espaços: calcule quanto representam da receita total.</li>
<li><strong>Atualize o cadastro de unidades.</strong> Proprietários, coproprietários, inquilinos e inscrição de IPTU de cada unidade.</li>
<li><strong>Alinhe com o contador e com o sistema de cobrança.</strong> Defina o enquadramento tributário e como as notas sairão no fechamento do mês.</li>
<li><strong>Revise o orçamento de 2027.</strong> Considere o aumento de custo dos serviços terceirizados.</li>
<li><strong>Informe síndico, conselho e moradores.</strong> Explique o que muda e, principalmente, o que não muda na cota.</li>
</ol>

<h2>Base legal</h2>
<p>As principais referências são o <a href="https://www.cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf" target="_blank" rel="noopener">Ato Conjunto RFB/CGIBS nº 4/2026</a>, a <a href="https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc/nota-tecnica-009-se-cgnfs-e-v-1-01.pdf" target="_blank" rel="noopener">Nota Técnica SE/CGNFS-e nº 009</a> e a Lei Complementar 214/2025, art. 26. A Reforma ainda terá regulamentações complementares, e a aplicação da regra dos 80% a cada caso depende de interpretação. Valide o enquadramento do seu condomínio com o contador.</p>
<p>Para a rotina de manutenção, que segue valendo independentemente da parte fiscal, veja o <a href="blog-checklist-manutencao-predial-por-frequencia.html">checklist de manutenção predial por frequência</a>.</p>
""",
        "faq": [
            ("A partir de quando o condomínio precisa emitir nota fiscal?",
             "A partir de 1º de dezembro de 2026, conforme o Ato Conjunto RFB/CGIBS nº 4/2026. A obrigação vale para as cobranças feitas aos condôminos e para as outras receitas do condomínio."),
            ("A taxa de condomínio vai ficar mais cara por causa da nota?",
             "A emissão da nota, por si só, não cria imposto sobre a cota. Como regra, o condomínio não é contribuinte de IBS e CBS. O orçamento pode subir por outro motivo: o custo de serviços terceirizados, como limpeza e portaria, tende a aumentar com a Reforma a partir de 2027."),
            ("Dá para emitir a nota do condomínio no sistema da prefeitura?",
             "Não. O código 99.05.01 só é emitido pelo Emissor Nacional (web e aplicativo) ou por integração via API com o ambiente nacional da NFS-e."),
        ],
    },
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
        "date": "2026-11-09",
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
