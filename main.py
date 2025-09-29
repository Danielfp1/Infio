import pandas as pd 


#importando dataframes

df1=pd.read_excel('./datasets/Afastamento - PBI - 29-09-25.xlsx')
df2=pd.read_excel('./datasets/Servidores com direito a licença - Cargo e Data.xlsx')

print ('-----------//------------')

print(df1)

print ('-----------//------------')

print(df2)

print ('-----------//------------')

print(df1.iloc[1])
print(df2.iloc[1])


print ('---------/-FIM-/----------')

