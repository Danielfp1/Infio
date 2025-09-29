import pandas as pd 


#importando dataframes

df1=pd.read_excel('./datasets/Afastamento - PBI - 29-09-25.xlsx')
df2=pd.read_excel('./datasets/Servidores com direito a licença - Cargo e Data.xlsx')

#Tratamento dos dados

# remove espaços extras
df1.columns = df1.columns.str.strip()        
df2.columns = df2.columns.str.strip()

# remove acentos
# df2.columns = df2.columns.str.normalize("NFKD").str.encode("ascii", errors="ignore").str.decode("utf-8")  
# df1.columns = df1.columns.str.normalize("NFKD").str.encode("ascii", errors="ignore").str.decode("utf-8")  


print(df2.columns)

print(df1)

print(df2)

# print(df1.iloc[1])
# print(df2.iloc[1])


#Filtrando por vículo coincidênte

df1Process = df1[df1['Vínculo coincidênte'] == 1]

df1Process

cpfServidoresVinculoCoincidente = df1Process['CPF com pontos'].unique().tolist()

cpfsCoincidentes = len(cpfServidoresVinculoCoincidente)


df_merged = df2.merge(
    df1[["CPF com pontos", "Data Inicio Ocorrencia"]],
    left_on="cpf",
    right_on="CPF com pontos",
    how="inner"
)

df_filtroDataInicioMaiorQCargo = df_merged[df_merged["data_inicio"] < df_merged["Data Inicio Ocorrencia"]]
df_filtroDataInicioMenorQCargo = df_merged[df_merged["data_inicio"] > df_merged["Data Inicio Ocorrencia"]]

df_filtroDataInicioMaiorQCargo.loc[:, "Verificação"] = "Incluir"
df_filtroDataInicioMenorQCargo.loc[:, "Verificação"] = ""

df_resultado = pd.concat([df_filtroDataInicioMaiorQCargo, df_filtroDataInicioMenorQCargo])

df_resultado.to_excel("./datasets/resultados/resultado.xlsx", index=False)