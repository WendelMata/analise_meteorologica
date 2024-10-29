import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Estabelecer a conexão com o banco de dados
engine = create_engine('mysql+pymysql://root:your_password@localhost/meteorologia')

# Carregar dados da tabela 'dados_meteorologicos' de volta para um DataFrame
dados_sql = pd.read_sql('SELECT * FROM dados_meteorologicos', con=engine)

# Garantir que a coluna 'data' está no formato datetime
dados_sql['data'] = pd.to_datetime(dados_sql['data'])

# Agrupar dados por mês e calcular a média de precipitação
dados_sql['mes'] = dados_sql['data'].dt.to_period('M')
media_precipitacao = dados_sql.groupby('mes')['precipitacao'].mean()

# Plotar
plt.figure(figsize=(10, 5))
media_precipitacao.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Média de Precipitação por Mês')
plt.xlabel('Mês')
plt.ylabel('Precipitação Média (mm)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
