# TUTORIAL PARA INICIAR OS SEUS ESTUDOS

## Informações importantes:
> Buscamos padronizar nossas atividades através de softwares, bibliotecas, e outros para que possamos sempre estar avançando em conjunto com o grupo que fazem parte do Núcleo de Ciência de Dados. Nossos encontros ocorrerão de forma __Híbrida__, sendo 1 vez ao mês (todo primeiro sábado do mês) com o Orientador Pablo de forma __oneline__, o restante dos encontros será feito de forma __presencial__ no __Laboratório de Estatística no 1J - 1J110 às 10:00.__

## Padronização
+ Software [Visual Studio Code](https://code.visualstudio.com/Download)<br>
+ Linguagem de Programação [Python](https://www.python.org/downloads/)<br>
  - Baixe o Instaladdor mais recente do Python<br>
    - Execute o Instalador e marque a opção: Add Python to PATH<br>
  - Para a instalação no Linux:
    - `sudo apt update
       sudo apt install python3 python3-pip -y`
+ Utilizando o VSCODE, navegue pelas extenções e instale o __Pacote Jupyter__
  - Utilizeramos o Jupyter Notebook integrado ao VSCODE para nossas atividades, não sendo obrigatório, caso deseja.

## Instalação das bibliotecas necessárias, sendo elas: kaggle, kagglehub, polars
Após clonar este repositório em sua maquina, instale as bibliotecas através do terminal pelo comando `pip install -r requirements.txt`
 
## Dataset utilizado nos encontros
Para que você possa baixar e utilizar o dataset, é necessário fazer a autenticação no Kaggle.
Dataset disponível em: [IEEE Fraud Detection](https://www.kaggle.com/competitions/ieee-fraud-detection/data)<br>
Crie sua conta, é possível também logar com a sua conta Google.<br>
Autenticação é feita via número de celular, não vai funcionar se não fizer.<br>
A inscrição na competição é necessária para ter acesso aos dados, na aba dados vai aparecer um botão indicando que você se inscreva, é só clicar nele.

### Criar um API Token de autenticação
No site, vá em configurações, novo API Token e crie o seu próprio, guarde o bem porque só vai ser possível ver uma vez, copie o comando similar ao abaixo que aparecer nessa hora.<br>
`mkdir -p ~/.kaggle && echo SEU_API_TOKEN > ~/.kaggle/access_token && chmod 600 ~/.kaggle/access_token`<br>
Rodar o comando copiado, para vincular o seu token a sua máquina.

### Para baixar o dataset, cole este comando no terminal:
`kaggle competitions download -c ieee-fraud-detection`

### Extrair a base: 
`unzip ieee-fraud-detection.zip`

### Carregar os datasets e começar a inspecionar os dados
O código base está em `view_data.py`<br>
Para rodar o comando é: `python3 view_data.py --data_path=path_do_dataset

##  Fazer os joinds das bases de dados
O código para fazer o join está em `build_data.py`<br>
Para executar o comando é: `python3 build_data.py --input=path_do_dataset --output=path_onde_deve_ser_salvo_o_joined`<br>
O script aceita tanto o transaction como o identity como input e lida internamente para fazer o join.
Tanto o input quanto o output precisa conter a extensão .csv para ser salvo, o código não tem suporte para outras extensões.
