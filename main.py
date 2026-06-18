import polars as pl

#Missao 1

#mostra todas as linhas no terminal 
pl.Config.set_tbl_cols(-1)

#Lê o arquvo csv
dado = pl.read_csv('winemag-data_first150k.csv')

#conta os dados nulos da coluna price
print('-'*40)
print("Antes de tratar os nulos")
print(f'numero de linhas nulas na coluna price: {dado["price"].null_count()}')

#agrupar por pais e uva
df_pais_uva = dado.group_by(["country","variety"], maintain_order=True).agg(pl.col("price").median().alias("mediana"))

#faz juncao dos dois df e substitui preco por mediana aonde NULL e deleta a coluna mediana
df_pais_uva = dado.join(df_pais_uva, on=["country","variety"]).with_columns(pl.col("price").fill_null(pl.col("mediana"))).drop("mediana")
print('-'*40)
print('Tratando os nulos com juncao')
print(f'numero de linhas nulas na coluna price: {df_pais_uva["price"].null_count()}')

# OU

#usando a funcao over
dado_limpo = dado.with_columns(pl.col("price").fill_null(pl.col("price").median().over(["country", "variety"])))
print('-'*40)
print('tratando os nulos com over')
print(f'numero de linhas nulas na coluna price: {dado_limpo["price"].null_count()}')
dado = dado_limpo

#Missao 2

#filtra vinhos dos US
dado_US = dado_limpo.filter(pl.col("country") == 'US')

#faz os calculos estátisticos
Q1 = dado_US.select(pl.col("price").quantile(0.25)).item() 
Q3 = dado_US.select(pl.col("price").quantile(0.75)).item()
IQR = Q3 - Q1
Limite_superior = Q3 + 1.5 * IQR
print('-'*40)
print(f'Q1 = {Q1}, Q3 = {Q3}, IQR = {IQR}, Limite Superior = {Limite_superior}')

#cria os dataframes
vinhos_normais = dado_US.filter(pl.col("price") <= Limite_superior)
vinhos_luxo = dado_US.filter(pl.col("price") > Limite_superior)

#pega a media de "points" de cada grupo
media_normais = vinhos_normais.select(pl.col("points").mean()).item()
media_luxo = vinhos_luxo.select(pl.col("points").mean()).item()

print('-'*40)
print(f'media da qualidade dos vinhos normais: {media_normais:.2f}')
print(f'media da qualidade dos vinhos de luxo: {media_luxo:.2f}')
print(f'diferenca dos dois (luxo - normal): {media_luxo - media_normais:.2f}')
#Se comparados a qualidade media dos vinhos normais e de luxo não se diferem tanto, é bem possível achar um vinho normal com mais qualidade do que um de luxo. 


#Missao 3

import matplotlib.pyplot as plt

#seleciona a coluna price
prices = dado_US.select(pl.col("price"))

#dropa os nulos
num_nulls = prices.null_count().item()
print('-'*40)
print(f'numero de nulos em price: {num_nulls}')
#por ser somente um numero vou só dropar
prices = prices.drop_nulls()
num_nulls = prices.null_count().item()
print(f'numero de nulos em price apos a limpeza: {num_nulls}')

#transformar em uma lista
prices = prices.to_series().to_list()

#gera o boxplot
fig, ax = plt.subplots()
ax.boxplot(prices)
ax.set_title("preços de vinhos")
ax.set_ylabel("preços")

#Os pontos acima do bigode superior são os outliers, eles são os valores acima do limite superior ou abaixo do limite
#inferior do gráfico, uma das grandes vantagens do boxplot é que análise tira os outliers, o que é benficial já que os
#outliers podem influênciar nas conclusões, pois são valores extremos que não seguem a tendência,
#atrapalhando na análise.

#transforma vinhos_normais em lista
grafico_vinhos = vinhos_normais.select(pl.col("price"))
grafico_vinhos = grafico_vinhos.to_series().to_list()

#gera o boxplot de vinhos_normais
fig, ax = plt.subplots()
ax.boxplot(grafico_vinhos)
ax.set_title("preços de vinhos normais")
ax.set_ylabel("preços")
plt.show()

#Com os dados mais filtrados o com um escopo menor, o gráfico ficou mais claro 



