# 🍷 Desafio DataLab: Primeiros Passos na Análise de Dados com Polars

## 🎯 Objetivo
Realizar uma **Análise Exploratória de Dados (EDA)** inicial utilizando a **biblioteca Polars**.

---

## 📌 Regra de Ouro

> Para **CADA etapa abaixo**, você deve escrever um comentário no código explicando:
>
> - O que o código está fazendo;
> - Por que essa etapa é importante para um Cientista de Dados.

---

# 🚀 Etapa 1: Conhecendo o Terreno (Importação e Inspeção)

### ✅ Atividades

- [ ] Importe a biblioteca `polars`.
- [ ] Carregue o arquivo **winemag-data_first150k.csv** em um DataFrame.
- [ ] Imprima as **5 primeiras linhas** do DataFrame para vermos a "cara" dos dados.
- [ ] Descubra e imprima a quantidade total de **linhas** e **colunas** do DataFrame.
- [ ] Descubra quais são os **tipos de dados** de cada coluna.

### 🎯 O que você deve responder
- Quantas linhas existem?
- Quantas colunas existem?
- Quais são os tipos de dados presentes?

---

# 🧹 Etapa 2: A Arte da Limpeza (Lidando com Valores Nulos)

Na vida real, os dados raramente vêm perfeitos. Precisamos saber onde estão os "buracos".

### ✅ Atividades

- [ ] Verifique quantas informações nulas (ausentes) existem em cada coluna.
- [ ] A coluna `price` (preço) é muito importante para nós.
- [ ] Crie um novo DataFrame que exclua todas as linhas onde o preço seja nulo.

### 🎯 O que você deve responder
- Quais colunas possuem valores nulos?
- Quantos valores nulos existem em cada uma?
- Quantas linhas restaram após remover os preços nulos?

---

# 🔎 Etapa 3: Respondendo a Perguntas com Filtros

O time de negócios quer saber sobre vinhos específicos.

### ✅ Atividades

- [ ] Filtre o DataFrame para mostrar apenas os vinhos do país (`country`) **"Brazil"**.
- [ ] Filtre os vinhos que:
  - [ ] Possuem pontuação (`points`) maior ou igual a **90**;
  - [ ] Possuem preço (`price`) menor que **20 dólares**.

### 🎯 O que você deve responder
- Quantos vinhos brasileiros existem na base?
- Quantos vinhos atendem aos critérios de alta qualidade e baixo custo?

---

# 📊 Etapa 4: Agrupamento e Insights (O poder do groupby)

Vamos encontrar os padrões gerais dos nossos dados.

### ✅ Atividades

#### 1️⃣ Países e preço médio

- [ ] Agrupe os dados por país (`country`).
- [ ] Calcule a média de preço (`price`) dos vinhos de cada país.
- [ ] Ordene o resultado do maior para o menor preço médio.

#### 2️⃣ Melhor Chardonnay da base

- [ ] Descubra qual é a pontuação máxima (`points`) recebida pelos vinhos da variedade (`variety`) **"Chardonnay"**.

### 🎯 O que você deve responder
- Qual país possui o maior preço médio?
- Qual foi a maior pontuação obtida por um Chardonnay?

---

# ⚙️ Etapa 5: Engenharia de Recursos (Criando novas colunas)

Um bom cientista de dados cria suas próprias métricas.

### ✅ Atividades

- [ ] Crie uma nova coluna chamada `custo_beneficio`.
- [ ] Essa coluna deve ser calculada pela divisão:

```text
points / price
