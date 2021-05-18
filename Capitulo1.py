import pandas as pd
import numpy as np
from scipy import stats

# Importação de dados e tratamento
dados = pd.read_csv('data/state.csv')
colunas = [
    'Estado',
    'População',
    'Taxa',
    'Abreviação'
]
dados.columns = colunas

# Exercícios
media = dados['População'].mean()
mediana = dados['População'].median()
media_aparada = stats.trim_mean(dados['População'], 0.1)
desvio_padrao = dados['População'].std()
amplitude_interquartil = stats.iqr(dados['População'])
percentis = np.quantile(dados['Taxa'], [.5, .25, .5, .75, .95])

# Respostas
print('Repostas:')
print('Média: ' + '%0.0f' % media)
print('Media aparada: ' + '%0.0f' % media_aparada)
print('Mediana: ' + '%0.0f' % mediana)
print('Amplitude interquartil: ' + '%0.0f' % amplitude_interquartil)
print('Percentis de taxa de homicídio: ' + '\n' + '\n'.join('{} : {}'.format(*k) for k in enumerate(percentis)))
