# ==========================================
# Importação, Exploração e Tradução
# ==========================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pycountry


# Carrega a base de dados de salários diretamente de um arquivo CSV no GitHub
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Exibe as primeiras 5 linhas do DataFrame para inspeção visual rápida
df.head()

# Mostra informações gerais do DataFrame: colunas, tipos de dados e memória utilizada
df.info()

# Exibe estatísticas descritivas (média, desvio padrão, mínimos, máximos) das colunas numéricas
df.describe()

# Retorna uma tupla contendo a quantidade de (linhas, colunas) do DataFrame
df.shape

# Guarda e exibe explicitamente o total de linhas e colunas
linhas, colunas = df.shape[0], df.shape[1]
print("linhas:", linhas)
print("colunas:", colunas)

# Mostra os nomes originais de todas as colunas
df.columns

# Renomeia as colunas para o português para facilitar a manipulação e entendimento
df.columns = ['ano', 'senioridade', 'contrato', 'cargo',
              'salario', 'moeda', 'usd', 'residencia',
              'remoto', 'empresa', 'tamanho_empresa']
display = (df.columns)

# Conta quantos registros existem para cada nível de senioridade (valores originais)
df["senioridade"].value_counts()

# Conta os registros para cada tipo de contrato (valores originais)
df["contrato"].value_counts()

# Conta os registros para cada tipo de modelo de trabalho (remoto, híbrido ou presencial)
df["remoto"].value_counts()

# Conta os registros de acordo com o tamanho da empresa (M, L, S)
df["tamanho_empresa"].value_counts()

# Dicionário de mapeamento para traduzir as siglas de senioridade
senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}

# Substitui as siglas de senioridade pelos nomes traduzidos no DataFrame
df['senioridade'] = df['senioridade'].replace(senioridade)

# Verifica a contagem após a tradução das senioridades
df['senioridade'].value_counts()

# Dicionário de mapeamento para traduzir as siglas de tipo de contrato
contrato = {
    'FT': 'Tempo Integral',
    'CT': 'Contrato',
    'PT': 'Tempo Parcial',
    'FL': 'Freelancer'
}

# Substitui as siglas de contrato pelos nomes traduzidos
df['contrato'] = df['contrato'].replace(contrato)

# Verifica a contagem após a tradução dos contratos
df['contrato'].value_counts()

# Dicionário de mapeamento para traduzir o tamanho das empresas
tamanho_empresa = {
    'M': 'Médio',
    'L': 'Grande',
    'S': 'Pequeno'
}

# Substitui as siglas do tamanho da empresa pelos nomes traduzidos
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)

# Verifica a contagem após a tradução dos tamanhos de empresa
df['tamanho_empresa'].value_counts()

# Dicionário de mapeamento para traduzir as categorias de trabalho remoto (codificadas em números)
remoto = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
}

# Substitui os valores numéricos de remoto pelas strings traduzidas
df['remoto'] = df['remoto'].replace(remoto)

# Verifica a contagem após a tradução do tipo de trabalho
df['remoto'].value_counts()

# Visualiza o DataFrame com as primeiras colunas e dados traduzidos
df.head()

# Dicionário para traduzir os cargos mais comuns da área de dados
cargos = {
    'Solutions Engineer': 'Engenheiro de Soluções',
    'Data Engineer': 'Engenheiro de Dados',
    'Data Scientist': 'Cientista de Dados',
    'Machine Learning Engineer': 'Engenheiro de Machine Learning',
    'Data Analyst': 'Analista de Dados',
    'Data Architect': 'Arquiteto de Dados',
    'Engineer': 'Engenheiro',
    'Software Engineer': 'Engenheiro de Software',
    'Product Manager': 'Gerente de Produtos',
    'Data Engineer Intern': 'Engenheiro de Dados Intern',
    'Data Manager': 'Gerente de Dados',
    'Data Analytics Mananger': 'Gerente de Análise de Dados',
    'Data Warehouse Engineer': 'Engenheiro de Data Warehouse',
}

# Substitui os nomes dos cargos em inglês para o português
df['cargo'] = df['cargo'].replace(cargos)

# Exibe os 5 cargos mais frequentes após a tradução
df['cargo'].value_counts().head()

# Mostra estatísticas descritivas básicas focado apenas nas colunas de texto (categóricas)
df.describe(include='object')

# ==========================================
# Tratamento de Dados Nulos/Faltantes
# ==========================================

# Retorna um DataFrame booleano (True onde o valor for nulo/vazio)
df.isnull()

# Soma a quantidade de valores nulos em cada uma das colunas do DataFrame
df.isnull().sum()

# Lista todos os valores únicos na coluna de anos
df['ano'].unique()

# Filtra e exibe qualquer linha que possua ao menos um valor nulo em qualquer coluna
df[df.isnull().any(axis=1)]


# Criação de um mini DataFrame de teste para simular dados de salários com valores nulos (np.nan)
df_salarios = pd.DataFrame({
    'nome': ["Ana", "Bruno", "Carlos", "Daniela", "Val"],
    'salario': [4000, np.nan, 5000, np.nan, 100000]
})

# fillna(): preenche os nulos do salário usando a MÉDIA geral dos salários (arredondada em 2 casas decimais)
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

# fillna(): preenche os nulos do salário utilizando a MEDIANA (valor central que não sofre influência de discrepantes/outliers)
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
df_salarios

# Criação de um DataFrame de teste de temperaturas com valores faltantes consecutivos
df_temperaturas = pd.DataFrame({
    'Dias': ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
    'Temperatura': [38, np.nan, np.nan, 28, 27]
})

# ffill() (forward fill): preenche os nulos propagando o último valor válido conhecido para frente
df_temperaturas["Preenchido_ffill"] = df_temperaturas["Temperatura"].ffill()
df_temperaturas

# Recria o mesmo DataFrame de temperaturas para testar o bfill
df_temperaturas = pd.DataFrame({
    'Dias': ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
    'Temperatura': [38, np.nan, np.nan, 28, 27]
})

# bfill() (backward fill): preenche os nulos propagando o próximo valor válido para trás
df_temperaturas["Preenchido_bfill"] = df_temperaturas["Temperatura"].bfill()
df_temperaturas

# Criação de DataFrame de teste de cidades com dados de texto nulos
df_cidades = pd.DataFrame({
    'nome': ["Ana", "Bruno", "Carlos", "Daniela", "Val"],
    'cidades': ["São Paulo", np.nan, "Curitiba", np.nan, "Belém"]
})

# Substitui nulos categóricos por um texto fixo ("Não Informado")
df_cidades["cidade_preenchidade"] = df_cidades["cidades"].fillna("Não Informado")
df_cidades

# dropna(): remove todas as linhas da base principal que contenham qualquer valor nulo
df_limpo = df.dropna()

# Confirma se todos os nulos foram removidos com sucesso da base final
df_limpo.isnull().sum()

# Visualiza o topo da base limpa
df_limpo.head()

# Exibe estrutura de tipos da base limpa
df_limpo.info()

# Altera explicitamente o tipo de dado da coluna 'ano' para inteiro de 64 bits usando assign
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))


# ==========================================
# Análise Estatística e Visualizações
# ==========================================

df_limpo.head()

# Plota um gráfico de barras simples usando a biblioteca nativa do Pandas para ver a distribuição da senioridade
df_limpo['senioridade'].value_counts().plot(kind='bar', title="Distribuição De Senioridade")


# Gera um gráfico de barras comparando a senioridade com a média salarial em dólares (USD) usando Seaborn
sns.barplot(data=df_limpo, x='senioridade', y="usd")

# Customização do gráfico anterior: define tamanho da figura, rótulos de eixos e título explicativo
plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='senioridade', y="usd")
plt.title("Salario Medio por Senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salario Medio Anual (USD)")
#plt.show()

# Agrupa a base por senioridade e calcula o salário médio anual em USD ordenado do maior para o menor
df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False)

# Captura a ordem correta (índices) das senioridades ordenadas de forma ascendente pela média salarial
ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index
ordem

# Plota o gráfico de barras do Seaborn forçando a ordem lógica dos salários definida na variável 'ordem'
plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='senioridade', y="usd", order=ordem)
plt.title("Salario Medio por Senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salario Medio Anual (USD)")
#plt.show()

# Plota um histograma para visualizar a frequência da distribuição de faixas salariais em 50 colunas (bins)
plt.figure(figsize=(10,5))
sns.histplot(df_limpo['usd'], bins=50, kde=False)
plt.title("Distribuição dos Salarios Anuais")
plt.xlabel("Salario (USD)")
plt.ylabel("Frequencia")
#plt.show()

# Plota um gráfico de Boxplot para identificar a distribuição estatística do salário e a presença de valores extremos (outliers)
plt.figure(figsize=(8,5))
sns.boxplot(x=df_limpo['usd'])
plt.title("BoxPlot Salario")
plt.xlabel("Salario (USD)")
#plt.show()

# Plota boxplots de salário divididos por senioridade, ordenados de forma hierárquica (Junior -> Executivo)
ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
plt.figure(figsize=(8,5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade)
plt.title("BoxPlot da distribuição Salarial por senioridade")
plt.xlabel("Salario (USD)")
#plt.show()

# Boxplot customizado por senioridade, colorindo cada nível de acordo com a paleta 'Set2'
ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
plt.figure(figsize=(8,5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade')
plt.title("BoxPlot da distribuição Salarial por senioridade")
plt.xlabel("Salario (USD)")
#plt.show()

# Agrupa e calcula a média de salário por senioridade criando um novo dataframe limpo para plotagem interativa
media_salario_por_senioridade = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

# Gera um gráfico de barras interativo usando Plotly Express
fig = px.bar(media_salario_por_senioridade,
             x='senioridade',
             y='usd',
             title="media salarial por senioridade",
             labels={'senioridade': 'Nivel de Senioridade', 'usd': 'media salarial anual (USD)'})
#fig.show()

# Agrupa e conta a quantidade de profissionais por tipo de regime (remoto, híbrido, presencial)
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

# Gera um gráfico de pizza interativo (Donut Chart com furo de 50%) para ver a proporção do trabalho remoto
fig = px.pie(remoto_contagem,
             values='quantidade',
             names='tipo_trabalho',
             title='proporção do tipo de trabalho remoto',
             hole=0.5)
#fig.show()

# Recria a contagem de trabalho remoto para fins de demonstração
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

# Configura o mesmo gráfico de rosca, mas adiciona rótulos de porcentagem e nomes nas fatias diretamente na tela
fig = px.pie(remoto_contagem,
             values='quantidade',
             names='tipo_trabalho',
             title='proporção do tipo de trabalho remoto',
             hole=0.5)

fig.update_traces(textinfo='percent+label')
#fig.show()

# --- Desafio Prático ---
# Filtra apenas registros de "Cientista de Dados"
cientista_dados = df_limpo[df_limpo['cargo'] == 'Cientista de Dados']
# Calcula a média salarial desses profissionais agrupados pelo país de residência (código de 2 letras)
media_salario_cientista_dados_por_pais = cientista_dados.groupby('residencia')['usd'].mean().sort_values(ascending=False).reset_index()

# Plota as médias salariais dos cientistas de dados por país
fig = px.bar(media_salario_cientista_dados_por_pais,
             x='residencia',
             y='usd',
             title="Media Salarial para Cientistas de Dados por País",
             labels={'residencia': 'País de Residencia', 'usd': 'Média Salarial Anual (USD)'})
#fig.show()


# ==========================================
# Mapas Globais e Exportação de Dados
# ==========================================

df.head()

# Executa comando para instalar a biblioteca pycountry diretamente do notebook
# %pip install pycountry

# Função utilitária que converte códigos ISO de 2 letras (ex: 'BR') para ISO de 3 letras (ex: 'BRA')
def iso2_to_iso3(code):
    try:
        return pycountry.countries.get(alpha_2=code).alpha_3
    except:
        return None

# Aplica a função de conversão na coluna 'residencia' para criar a nova coluna 'residencia_iso3'
df_limpo['residencia_iso3'] = df_limpo['residencia'].apply(iso2_to_iso3)

# Filtra novamente apenas cientistas de dados
df_ds = df_limpo[df_limpo['cargo'] == 'Cientista de Dados']

# Agrupa a média salarial dos cientistas de dados usando o novo formato ISO de 3 letras
media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()

# Plota um mapa coroplético (mapa do mundo interativo) pintando cada país baseado no salário médio em USD
fig = px.choropleth(media_ds_pais,
                    locations='residencia_iso3',
                    color='usd',
                    color_continuous_scale='rdylgn', # Paleta de cores do Vermelho (baixo) ao Verde (alto)
                    title='Salario médio de Cientista de Dados por País',
                    labels={'usd': 'Salario Médio (USD)', 'residencia_iso3': 'País'})
#fig.show()

# Exporta todo o DataFrame limpo, traduzido e estruturado para um arquivo CSV local sem incluir os índices do Pandas
df_limpo.to_csv('Dado-Final.csv', index=False)