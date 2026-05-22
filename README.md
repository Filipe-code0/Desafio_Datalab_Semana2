# 📚 Tutorial para Iniciar seus Estudos

## 📌 Informações Importantes

Buscamos padronizar nossas atividades através de softwares, bibliotecas e metodologias, permitindo que todos os integrantes do Núcleo de Ciência de Dados evoluam em conjunto.

Nossos encontros ocorrerão de forma **híbrida**:

- 📅 **1 vez ao mês** (todo primeiro sábado do mês) com o orientador **Pablo**, de forma **online**;
- 🏫 Os demais encontros serão realizados presencialmente no **Laboratório de Estatística — sala 1J110**, às **10:00**.

---

# ⚙️ Padronização do Ambiente

## 🖥️ Softwares Utilizados

- Editor de código: [Visual Studio Code](https://code.visualstudio.com/Download)
- Linguagem principal: [Python](https://www.python.org/downloads/)

---

## 🐍 Instalando o Python

### Windows

1. Baixe a versão mais recente do Python;
2. Execute o instalador;
3. **IMPORTANTE:** marque a opção:

```bash
Add Python to PATH
```

---

### Linux (Ubuntu/Debian)

Execute os comandos abaixo no terminal:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

---

## 📓 Configurando o VSCode

No VSCode, acesse a aba de extensões e instale o pacote:

- **Jupyter**

Utilizaremos o **Jupyter Notebook integrado ao VSCode** durante as atividades.  
O uso não é obrigatório, mas é altamente recomendado.

---

# 📦 Instalação das Bibliotecas Necessárias

Após clonar este repositório em sua máquina, instale as dependências com:

```bash
pip install -r requirements.txt
```

As principais bibliotecas utilizadas serão:

- `kaggle`
- `kagglehub`
- `polars`

---

# 📊 Dataset Utilizado nos Encontros

O dataset utilizado será o:

- [IEEE Fraud Detection](https://www.kaggle.com/competitions/ieee-fraud-detection/data)

---

## 🔐 Autenticação no Kaggle

Para baixar o dataset, será necessário criar e autenticar sua conta no Kaggle.

### Passos

1. Crie sua conta no Kaggle;
2. É possível entrar utilizando sua conta Google;
3. Faça a verificação via número de celular (**obrigatório**);
4. Inscreva-se na competição para obter acesso aos dados.

Na aba **Data**, aparecerá um botão solicitando sua participação na competição — basta clicar nele.

---

# 🔑 Criando um API Token do Kaggle

1. Acesse:
   - `Profile → Settings → API`
2. Clique em:
   - **Create New API Token**

O Kaggle irá baixar automaticamente um arquivo `.json` contendo seu token.

> ⚠️ Guarde esse arquivo com cuidado — ele só pode ser visualizado uma única vez.

---

## Linux/macOS — Configuração do Token

Execute o comando abaixo substituindo `SEU_API_TOKEN` pelo conteúdo do token:

```bash
mkdir -p ~/.kaggle && echo SEU_API_TOKEN > ~/.kaggle/access_token && chmod 600 ~/.kaggle/access_token
```

---

# ⬇️ Baixando o Dataset

Execute o comando abaixo no terminal:

```bash
kaggle competitions download -c ieee-fraud-detection
```

---

# 📂 Extraindo os Arquivos

```bash
unzip ieee-fraud-detection.zip
```

---

# 🔎 Inspecionando os Dados

O código base para exploração inicial dos dados está em:

```bash
view_data.py
```

Para executar:

```bash
python3 view_data.py --data_path=CAMINHO_DO_DATASET
```

---

# 🔗 Realizando o Join das Bases

O script responsável por realizar o join entre as bases está em:

```bash
build_data.py
```

Para executar:

```bash
python3 build_data.py --input=CAMINHO_DO_DATASET --output=CAMINHO_DO_ARQUIVO_FINAL.csv
```

---

## 📌 Observações Importantes

- O script aceita tanto os arquivos `transaction` quanto `identity` como entrada;
- O join é tratado automaticamente pelo código;
- Tanto o caminho de entrada quanto o de saída devem conter a extensão `.csv`;
- Atualmente o script não possui suporte para outros formatos de arquivo.

---
