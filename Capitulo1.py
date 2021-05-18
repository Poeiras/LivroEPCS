import pandas as pd
from scipy import stats
dados = pd.read_csv('data/state.csv')
colunas = [
    'Estado',
    'População',
    'Taxa',
    'Abreviação'
]
dados.columns = colunas

# Exercício 1
media = dados['População'].mean()
mediana = dados['População'].median()
media_aparada = stats.trim_mean(dados['População'], 0.1)
desvio_padrao = dados['População'].std()
amplitude_interquartil = stats.iqr(dados['População'])

# Respostas
print('Repostas:')
print('Média: ' + '%0.0f' % media)
print('Media aparada: ' + '%0.0f' % media_aparada)
print('Mediana: ' + '%0.0f' % mediana)
print('Amplitude interquartil: ' + '%0.0f' % amplitude_interquartil)
