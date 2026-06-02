# 🍷 Desafio DataLab: Primeiros Passos na Análise de Dados com Polars
Objetivo: Realizar uma **Análise Exploratória de Dados (EDA)** inicial utilizando a **biblioteca polars**.

## Regra de Ouro: Para CADA etapa abaixo, você deve escrever um comentário no código explicando o que o código está fazendo e por que essa etapa é importante para um Cientista de Dados.

### Etapa 1: Conhecendo o Terreno (Importação e Inspeção)
Importe a biblioteca polars.

Carregue o arquivo **winemag-data_first150k.csv** em um DataFrame.

Imprima as 5 primeiras linhas do DataFrame para vermos a "cara" dos dados.

Descubra e imprima a quantidade total de linhas e colunas do seu DataFrame. Quais são os tipos de dados de cada coluna?

### Etapa 2: A Arte da Limpeza (Lidando com Valores Nulos)
Na vida real, os dados raramente vêm perfeitos. Precisamos saber onde estão os "buracos".

Verifique quantas informações nulas (ausentes) existem em cada coluna.

A coluna price (preço) é muito importante para nós. Crie um novo DataFrame que exclua todas as linhas onde o preço seja nulo.

### Etapa 3: Respondendo a Perguntas com Filtros
O time de negócios quer saber sobre vinhos específicos.

Filtre o DataFrame para mostrar apenas os vinhos do país (country) "Brazil".

Agora, queremos vinhos de altíssima qualidade e custo acessível: filtre os vinhos que tenham uma pontuação (points) maior ou igual a 90, e que custem (price) menos de 20 dólares.

### Etapa 4: Agrupamento e Insights (O poder do groupby)
Vamos encontrar os padrões gerais dos nossos dados.

Qual país produz os vinhos mais caros em média? Agrupe os dados por país (country) e calcule a média de preço (price) dos vinhos de cada um. Ordene o resultado do maior para o menor.

Qual é a pontuação (points) máxima que os vinhos da uva (variety) "Chardonnay" já receberam?

### Etapa 5: Engenharia de Recursos (Criando novas colunas)
Um bom cientista de dados cria suas próprias métricas.

Crie uma nova coluna chamada custo_beneficio. Essa coluna deve ser o resultado da divisão da pontuação (points) pelo preço (price).

Ordene seu DataFrame para descobrir qual é o vinho com o maior custo-benefício da nossa base!
