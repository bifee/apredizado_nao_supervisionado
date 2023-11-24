import pandas as pd

alunos_df = pd.read_csv('alunos_engcomp-2023.csv')

# Codificação one-hot para o campo "Sexo"
alunos_df = pd.get_dummies(alunos_df, columns=['Sexo'])

# Normalização para os campos "Coeficiente" e "Nota no ENEM"
alunos_df['Coeficiente'] = (alunos_df['Coeficiente'] - alunos_df['Coeficiente'].min()) / (alunos_df['Coeficiente'].max() - alunos_df['Coeficiente'].min())
alunos_df['Enem'] = (alunos_df['Enem'] - alunos_df['Enem'].min()) / (alunos_df['Enem'].max() - alunos_df['Enem'].min())

# Codificação numérica para o campo "Escola"
alunos_df['Escola'] = alunos_df['Escola'].map({'Pública': 0, 'Particular': 1})

print(alunos_df)
