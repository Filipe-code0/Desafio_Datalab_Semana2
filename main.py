import polars as pl
import matplotlib.pyplot as mpl

#mostra todas as linhas no terminal 
pl.Config.set_tbl_cols(-1)
pl.Config.set_tbl_rows(100)

#Lê o arquvo csv
data = pl.read_csv('winemag-data_first150k.csv')

#conta os dados nulos da coluna price
print(f'numero de linhas nulas na coluna price: {data["price"].null_count()}')

#agrupar por pais e uva
df_pais_uva = data.group_by(["country","variety"], maintain_order=True).agg(pl.col("price").median().alias("mediana"))

#faz juncao dos dois df e substitui preco por mediana aonde NULL e deleta a coluna mediana
df_pais_uva = data.join(df_pais_uva, on=["country","variety"]).with_columns(pl.col("price").fill_null(pl.col("mediana"))).drop("mediana")
print(df_pais_uva)
print(f'numero de linhas nulas na coluna price: {df_pais_uva["price"].null_count()}')

# OU

#usando a funcao over
dado_limpo = data.with_columns(
    pl.col("price").fill_null(
        pl.col("price").median().over(["country", "variety"])
    )
)

print(dado_limpo)
print(f'numero de linhas nulas na coluna price: {dado_limpo["price"].null_count()}')

#filtra vinhos dos US
dado_US = dado_limpo.filter(pl.col("country") == 'US')
Q1 = dado_US.select(pl.col("price").quantile(0.25)).item() 
Q3 = dado_US.select(pl.col("price").quantile(0.75)).item()
IQR = Q3 - Q1
Limite_superior = Q3 + 1.5 * IQR
print(Q1, Q3, IQR, Limite_superior)
