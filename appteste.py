import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Configuração da página para utilizar toda a largura disponível da tela
st.set_page_config(layout='wide')

vazio_esq, col1, col2, col3, vazio_dir = st.columns([1.0, 2, 2, 2, 0.5])

with col1:
    # O truque está no width=150: ele limita o tamanho máximo da imagem em pixels
    st.image("ufpel.png", width=100)

with col2:
    st.image("labserg.jpg", width=200)
with col3:
    st.image("ceng.png", width=140)
    
# Dá um espaço antes de começar o cabeçalho azul
st.write("")

# Bloco do Cabeçalho com fundo azul claro personalizado
st.markdown(
    """
    <div style="background-color: #E6F0FA; padding: 20px; border-radius: 8px; margin-bottom: 15px;">
        <h1 style="margin: 0; font-size: 38px; color: #1E1E1E;">📊 Resultados do Questionário PROART</h1>
        <h3 style="margin: 10px 0 0 0; font-size: 24px; color: #4F4F4F; font-weight: normal;">
            Relatório com análises estatísticas 
            <span style="color: #FF0000; font-weight: bold;">(Testes para aplicação no Projeto!)</span>
        </h3>
        <h4 style="margin: 10px 0 0 0; font-size: 18px; color: #4F4F4F; font-weight: normal;">
            Autor: Douglas F. D'avila -- Acadêmico de Engenharia ELetrônica e bolsista deste projeto na UFPel <br>
            Orientadora: Profa. Dra. Renata H. Benvenuti -- Professora de Engenharia de Produção na UFPel e engenheira de SST
        </h4>
        <h4 style="margin: 10px 0 0 0; font-size: 18px; color: #4F4F4F; font-weight: normal;">
            Data de Geração: 22 de maio de 2026
        </h4>

    </div>
    """, 
    unsafe_allow_html=True
)

st.divider()

# ------ Dashboard começa daqui para baixo --------

st.subheader("Contextualização")
st.write("Este trabalho consistiu na aplicação do questionario PROART em uma turma de Saúde e Segurança do Trabalho (SST), disciplina ofertada para os cursos de engenharia na Universidade Federal de Pelotas (UFPEL), como requisito para obtenção do título de bacharel. O questionário PROART foi aplicado em 22 alunos de 5 cursos de engenharia. A aplicação ocorreu durante a aula, de 6 a 10 de abril de 2026. A participação dos alunos ocorreu de forma voluntária.")

st.divider()

# ------ Seção 1: Perfil dos Alunos --------
st.subheader("👥 Dados Sociodemográficos e da Atividade dos Participantes")
st.write("Foi utilizado o Excel, do Microsoft Office para o tratamento e contagem dos dados, bem como a concepção dos gráficos apresentados a seguir. O Google Planilhas foi utilizado para manter formatação em algumas exportações para este documento. Esta página foi gerada por meio de lógica programada em linguagem python, como teste para uma implementação futura mais detalhada de um dashboard interativo com dados referentes a aplicação do questionário PROART em um escritório de advocacia (Projeto de extensão em SST)")

# ==========================================
# FILEIRA 1 (3 Gráficos)
# ==========================================
l1_col1, l1_col2, l1_col3 = st.columns(3)

with l1_col1:
    st.image("idade.svg", use_container_width=True)

with l1_col2:
    st.image("curso.png", use_container_width=True)

with l1_col3:
    st.image("tempo.svg", use_container_width=True)


# Espaço sutil entre as fileiras
st.write("")


# ==========================================
# FILEIRA 2 (3 Gráficos)
# ==========================================
l2_col1, l2_col2, l2_col3 = st.columns(3)

with l2_col1:
    st.image("genero.svg", use_container_width=True)

with l2_col2:
    st.image("escola.png", use_container_width=True)

with l2_col3:
    st.image("horas.svg", use_container_width=True)


# Espaço sutil entre as fileiras
st.write("")


# ==========================================
# FILEIRA 3 (2 Gráficos Centralizados)
# Para centralizar 2 gráficos em uma linha de 3 espaços,
# criamos 3 colunas, mas deixamos a primeira e a última menores como "margem"
# ==========================================
l3_col1, l3_col2, l3_col3, l3_col4 = st.columns([0.5, 2, 2, 0.5])

# Deixamos l3_col1 vazia (funciona como margem esquerda)

with l3_col2:
    st.image("saude.svg", use_container_width=True)

with l3_col3:
    st.image("estagio.svg", use_container_width=True)

# Deixamos l3_col4 vazia (funciona como margem direita)

st.divider() # linha divisória entre as seções

# ------ Seção 2: Mapa de calor das respostas --------

st.subheader("🔥 Mapa de Calor dos Riscos Psicossociais")

st.write("O mapa de calor abaixo apresenta a média das respostas dos alunos para cada item do questionário PROART, organizado por categoria de risco psicossocial. As cores mais quentes (vermelho) indicam maior incidência do risco, enquanto as cores mais frias (verde) indicam menor incidência. Este mapa é uma ferramenta visual importante para identificar áreas de atenção e direcionar ações de intervenção em curto, médio e longo prazo.")

# Centralização da margem por pesos em colunas
col_esq, col_centro, col_dir = st.columns([3, 8, 1])

with col_centro:
    # use_container_width=True faz a imagem expandir até ocupar quase a tela toda (peso 8)
    st.image("mapa.png")
    
st.write("")

st.write("Algumas áreas de risco psicossocial se destacaram com médias mais altas, indicando que os alunos percebem esses fatores como mais presentes em suas experiências acadêmicas. Por exemplo, a existência de um estilo individualista por parte de professores que se acham insubstituiveis, ou então questões de esgotamento mental como o cansaço provocado por atividades acadêmicas e a interferência no sono noturno apresentaram cores vermelhas, sugerindo que esses aspectos podem ser fontes de estresse para os estudantes. No entanto, por mais desgastante que seja a vida acadêmica, foi constatado que não houveram danos físicos e mentais conforme representado em tonalidade verde algumas questoes na escala de danos relacionados ao trabalho (no caso meio acadêmico), além disso os alunos se sentem motivados e veem sentido no que fazem, demonstrando que são extremamente resilientes e encontram prazer em suas atividades, o que é um fator protetor importante para a saúde mental.")
st.write("")

col_esq, col_centro, col_dir = st.columns([1, 8, 1])

with col_centro:
    st.image("intervenção.svg", use_container_width=True)
    
st.write("")
st.divider()
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
    
col1, col2 = st.columns(2)

with col1:
    st.image("dejours.jpg")
    
with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.subheader("*”O trabalho nunca é neutro em relação à saúde mental. Ou ele causa prazer ou ele causa sofrimento”.*")
    st.subheader("*Dejours*")