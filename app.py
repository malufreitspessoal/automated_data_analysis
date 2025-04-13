import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_iris
import os

# titulo da minha página
st.title("📊 Análise automática dos dados")
st.markdown('### Esta ferramenta permite que você carregue um conjunto de dados (.xls ou .csv) e realiza automaticamente uma análise exploratória. Ela oferece uma visão geral dos dados com estatísticas descritivas e visualizações interativas, como histogramas, gráficos de dispersão e boxplots, ajudando você a identificar padrões e insights de forma simples.')

def verificar_extensao(nome_arquivo, extensao_arquivo):
    _, extensao = os.path.splitext(nome_arquivo)
    return extensao.lower() in extensao_arquivo    

data_set = st.file_uploader('Selecione o seu arquivo: ', type=['.xls', '.csv', '.xlsx'])

if data_set is not None:
    nome_arquivo = data_set.name
    extensoes_validas = ['.xls', '.csv', '.xlsx'] 
    
    if verificar_extensao(nome_arquivo, extensoes_validas):
        st.success(f'Arquivo {nome_arquivo} recebido com sucesso')

        try: 
            data_set = pd.read_csv(data_set)

        except:
            data_set = pd.read_excel(data_set)
    else:
        st.error('Erro no formato do seu arquivo ')

if data_set is not None:
    # visualização dos dados
    st.markdown("### 🔍 Visualização dos dados")
    st.markdown('### Esta ferramenta permite que você carregue um conjunto de dados (.xls ou .csv) e realiza automaticamente uma análise exploratória. Ela oferece uma visão geral dos dados com estatísticas descritivas e visualizações interativas, como histogramas, gráficos de dispersão e boxplots, ajudando você a identificar padrões e insights de forma simples.')
    
    st.dataframe(data_set)

    st.markdown("### 📈 Estatísticas Descritivas")
    st.dataframe(data_set.describe())

    st.markdown("### 📊 Visualizações gráficas")

    #escolhe a coluna pra filtragem
    colunas_numericas = data_set.select_dtypes(include=['float64', 'int64']).columns.tolist()

    # se nao colocar uma key, ele usa apenas 1 coluna de infos
    
    if len(colunas_numericas) > 0:
        # histograma
        st.subheader("Histograma") #titulo
        st.markdown('### Mostra a distribuição dos dados dividindo-os em intervalos (bins). Útil para visualizar padrões e a frequência dos valores.')
        coluna_histograma = st.selectbox("Escolha uma coluna para o Histograma", colunas_numericas, key="histograma")
        grafico_histograma = px.histogram(data_set, x = coluna_histograma, nbins=50, title=f' Distribuição de {coluna_histograma}')
        st.plotly_chart(grafico_histograma)

        # Scatter Plot
        st.subheader("Scatter Plot") #titulo
        st.markdown('### Exibe a relação entre duas variáveis numéricas. Ideal para identificar correlações e tendências nos dados.')
        coluna_x = st.selectbox("Escolha a coluna para o eixo X:", colunas_numericas, key= "coluna_x")
        coluna_y = st.selectbox("Escolha a coluna para o eixo y:", colunas_numericas, key= "coluna_y")
        grafico_sp = px.scatter(data_set, x =coluna_x, y = coluna_y, title= f"Relação entre coluna {coluna_x} e {coluna_y}")
        st.plotly_chart(grafico_sp)

        # Boxplot
        st.subheader("Boxplot") #titulo
        st.markdown('### Apresenta a distribuição dos dados e destaca outliers. Bom para entender a dispersão e os valores extremos.')
        
        coluna_box = st.selectbox("Escolha uma coluna para o boxplot:", colunas_numericas, key="box")
        grafico_box = px.box(data_set, y = coluna_box, title=f"Distribuição de {coluna_box}")
        st.plotly_chart(grafico_box)
