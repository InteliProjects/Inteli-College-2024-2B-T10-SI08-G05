import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import json
import os
from dotenv import load_dotenv

from utils import (
    get_fluxo_entre_estacoes,
    get_heatmap_pessoas_por_linha,
    get_media_intervalo_operacao_por_dia,
    get_media_tempo_porta_aberta,
    get_movimento_classificado_por_bilhete,
    get_tipos_bilhete_abundantes,
    get_tipos_bilhete_por_dia,
    get_tipos_bilhete_por_semana,
    get_sensores_por_data
)

st.set_page_config(
    page_title="Pérola Negra",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    load_dotenv()
    auth_credentials_json = os.getenv("AUTH_CREDENTIALS_JSON")
    credentials = json.loads(auth_credentials_json) if auth_credentials_json else {}
    
    def check_credentials(username, password):
        if not credentials or "usernames" not in credentials:
            return False
        user_data = credentials["usernames"].get(username)
        if not user_data:
            return False
        stored_password = user_data.get("password")
        if not stored_password:
            return False
        return password == stored_password
    
    if "authentication_status" not in st.session_state:
        st.session_state["authentication_status"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = ""
    if "page" not in st.session_state:
        st.session_state["page"] = "🏠 Home"
    
    def login_screen():
        st.title("Login - Pérola Negra")
        st.markdown("### Por favor, faça login para acessar o sistema.")
        username = st.text_input("Usuário", key="login_username")
        password = st.text_input("Senha", type="password", key="login_password")
        if st.button("Entrar"):
            if check_credentials(username, password):
                st.session_state["authentication_status"] = True
                st.session_state["username"] = username
                st.success("Login bem-sucedido!")
            else:
                st.warning("Credenciais inválidas. Tente novamente.")
    
    def main_app():
        st.markdown(
            """
            <style>
            .sidebar .sidebar-content { 
                background-color: #dbd8e3; 
                padding: 10px; 
            }
            .sidebar-image { 
                display: flex; 
                justify-content: center; 
                align-items: center; 
                margin-bottom: 15px; 
            }
            .btn-container { 
                display: flex; 
                flex-direction: column; 
                gap: 10px; 
            }
            .btn-container .stButton > button { 
                background-color: #0f3d3e; 
                color: white; 
                width: 100%; 
                border-radius: 10px; 
                border: none; 
                height: 50px; 
                font-size: 16px; 
            }
            .btn-container .stButton > button:hover { 
                background-color: #350338; 
                color: white;
            }
            </style>
            """, unsafe_allow_html=True
        )
        logo_url = "https://res.cloudinary.com/dmornatkl/image/upload/v1733406614/perola_negra_sem_fundo__e6sxco.svg"
        st.sidebar.markdown(f"""
        <div class="sidebar-image">
            <img src="{logo_url}" alt="Logo" style="width: 120px;">
        </div>
        """, unsafe_allow_html=True)
        st.sidebar.title("Pérola Negra")
        
        def format_number(value):
            if value >= 1_000_000:
                return f"{value / 1_000_000:.1f}M"
            elif value >= 1_000:
                return f"{value / 1_000:.1f}k"
            return str(value)
        
        def segundos_para_minutos(segundos):
            return round(segundos / 60, 2) 
        
        def switch_page(selected_page):
            st.session_state.page = selected_page
        
        st.sidebar.markdown('<div class="btn-container">', unsafe_allow_html=True)
        button_labels = [
            "🏠 Home",
            "🚉 Fluxo Entre Estações",
            "🌡️ Heatmap",
            "⏱️ Intervalo Médio Operação",
            "🚪 Tempo Porta Aberta",
            "📊 Movimento Classificado",
            "🎟️ Tipos de Bilhete",
            "📟 Sensores por Data",
            "📈 Infográfico"
        ]
        for label in button_labels:
            if st.sidebar.button(label):
                switch_page(label)
        st.sidebar.markdown('</div>', unsafe_allow_html=True)
        
        user_info = credentials["usernames"].get(st.session_state["username"], {})
        user_name = user_info.get("name", st.session_state["username"])
        st.sidebar.write(f"Bem-vindo, *{user_name}*")
        if st.sidebar.button("Sair"):
            st.session_state["authentication_status"] = False
            st.session_state["username"] = ""
            st.session_state["page"] = "🏠 Home"
        
        page = st.session_state.page
        
        if page == "🏠 Home":
            st.title("Visão Estratégica - CPTM 🚅")
            st.markdown("Bem-vindo ao painel estratégico. Explore os dados operacionais e filtre informações relevantes para a tomada de decisão.")
            st.divider()
            col1, col2, col3, col4 = st.columns(4)
            fluxo_data = get_fluxo_entre_estacoes()
            intervalo_data = get_media_intervalo_operacao_por_dia()
            porta_data = get_media_tempo_porta_aberta()
            if fluxo_data:
                df_fluxo = pd.DataFrame(fluxo_data)
                df_fluxo["taxa_retenção"] = df_fluxo["total_entradas"] / df_fluxo["total_saidas"]
                top_fluxo = df_fluxo.loc[df_fluxo["total_entradas"].idxmax()]
                col1.metric(
                    label="💥 Maior Fluxo de Entrada",
                    value=f"{format_number(top_fluxo['total_entradas'])} pessoas",
                    delta=f"Estação {top_fluxo['estacao_inicio']} → {top_fluxo['estacao_fim']}"
                )
            if intervalo_data and porta_data:
                df_intervalo = pd.DataFrame(intervalo_data)
                df_porta = pd.DataFrame(porta_data)
                intervalo_medio = df_intervalo["media_intervalo_operacao_segundos"].mean()
                minutos_int, segundos_int = divmod(intervalo_medio, 60)
                col2.metric(
                    label="⏱ Intervalo Médio Entre Estações",
                    value=f"{int(minutos_int)}m {int(segundos_int)}s"
                )
                porta_media = df_porta["media_tempo_porta_aberta_segundos"].mean()
                minutos_porta, segundos_porta = divmod(porta_media, 60)
                eficiencia_operacional = min(1, 30 / porta_media) * 100
                col3.metric(
                    label="💪 Tempo Médio Porta Aberta",
                    value=f"{int(minutos_porta)}m {int(segundos_porta)}s"
                )
                col4.metric(
                    label="⚙️ Eficiência Operacional (30s)",
                    value=f"{eficiencia_operacional:.2f}%"
                )
            st.divider()
            st.subheader("📊 Gráficos Operacionais")
            if fluxo_data:
                fig_fluxo = px.bar(
                    df_fluxo,
                    x="estacao_inicio",
                    y="total_entradas",
                    color="estacao_fim",
                    title="Fluxo de Pessoas Entre Estações",
                    labels={
                        "estacao_inicio": "Estação de Origem",
                        "total_entradas": "Total de Entradas",
                        "estacao_fim": "Estação de Destino"
                    },
                    text="total_entradas",
                    color_discrete_sequence=px.colors.qualitative.Pastel
                )
                fig_fluxo.update_traces(textposition="inside", textfont_size=10)
                st.plotly_chart(fig_fluxo, use_container_width=True)
            bilhetes_data = get_tipos_bilhete_abundantes() or []
            if isinstance(bilhetes_data, list):
                df_bilhetes = pd.DataFrame(bilhetes_data)
            else:
                df_bilhetes = pd.DataFrame()
            if not df_bilhetes.empty:
                df_bilhetes_top8 = df_bilhetes.sort_values("total_uso", ascending=False).head(8)
                fig_bilhetes = px.bar(
                    df_bilhetes_top8,
                    y="tipo_bilhete",
                    x="total_uso",
                    orientation="h",
                    title="Top 8 Tipos de Bilhetes Mais Utilizados",
                    labels={"tipo_bilhete": "Tipo de Bilhete", "total_uso": "Total de Uso"},
                    text="total_uso",
                    color_discrete_sequence=px.colors.qualitative.Vivid
                )
                fig_bilhetes.update_layout(
                    yaxis_title=None,
                    xaxis_title="Total de Uso",
                    showlegend=False,
                )
                st.plotly_chart(fig_bilhetes, use_container_width=True)
        
        elif page == "🚉 Fluxo Entre Estações":
            st.title("🚉 Fluxo Entre Estações")
            data = get_fluxo_entre_estacoes()
            if data:
                df = pd.DataFrame(data)
                selected_date = "todas as datas"
                if 'data' in df.columns:
                    df['data'] = pd.to_datetime(df['data'])
                    min_date = df['data'].min().date()
                    max_date = df['data'].max().date()
                    selected_date = st.date_input(
                        "Selecione o dia:",
                        value=min_date,
                        min_value=min_date,
                        max_value=max_date
                    )
                    df = df[df['data'].dt.date == selected_date]
                if isinstance(selected_date, pd.Timestamp):
                    title_date = selected_date.strftime("%d/%m/%Y")
                else:
                    title_date = selected_date
                estacoes_origem = df['estacao_inicio'].unique().tolist()
                estacoes_destino = df['estacao_fim'].unique().tolist()
                estacoes = sorted(list(set(estacoes_origem + estacoes_destino)))
                estacoes_options = ["Todos", "Nenhum"] + estacoes
                estacoes_selecionadas = st.multiselect(
                    "Selecione as estações:",
                    options=estacoes_options,
                    default=["Todos"]
                )
                if "Todos" in estacoes_selecionadas:
                    estacoes_filtradas = estacoes
                elif "Nenhum" in estacoes_selecionadas:
                    estacoes_filtradas = []
                else:
                    estacoes_filtradas = estacoes_selecionadas
                if estacoes_filtradas:
                    df = df[(df['estacao_inicio'].isin(estacoes_filtradas)) | (df['estacao_fim'].isin(estacoes_filtradas))]
                else:
                    df = pd.DataFrame(columns=df.columns)
                st.write("### Gráfico de Entradas e Saídas por Estação")
                if not df.empty:
                    fig_bar = px.bar(
                        df,
                        x="estacao_inicio",
                        y=["total_entradas", "total_saidas"],
                        barmode="group",
                        labels={
                            "estacao_inicio": "Estação",
                            "value": "Total de Pessoas",
                            "variable": "Fluxo"
                        },
                        title=f"Comparativo de Entradas e Saídas em {title_date}"
                    )
                    st.plotly_chart(fig_bar, use_container_width=True)
                else:
                    st.warning("Nenhum dado disponível para as estações selecionadas e data escolhida.")
                st.write("### Percentual de Fluxo por Estação de Início")
                if not df.empty:
                    fig_pie = px.pie(
                        df,
                        values="total_entradas",
                        names="estacao_inicio",
                        title="Distribuição Percentual do Fluxo de Entradas"
                    )
                    st.plotly_chart(fig_pie, use_container_width=True)
                else:
                    st.warning("Nenhum dado disponível para as estações selecionadas e data escolhida.")
            else:
                st.warning("Dados de fluxo entre estações não disponíveis no momento.")
        
        elif page == "🌡️ Heatmap":
            st.title("🌡 Heatmap de Movimentação de Pessoas")
            data = get_heatmap_pessoas_por_linha()
            if data:
                df = pd.DataFrame(data)
                df['hora'] = pd.to_numeric(df['hora'], errors='coerce')
                linhas_disponiveis = sorted(df['linha'].unique())
                linhas_selecionadas = st.selectbox("Selecione a linha (ou 'Todas' para todas as linhas):", ["Todas"] + linhas_disponiveis)
                horas_disponiveis = sorted(df['hora'].unique())
                horas_selecionadas = st.slider(
                    "Selecione o intervalo de horários:",
                    min_value=int(min(horas_disponiveis)),
                    max_value=int(max(horas_disponiveis)),
                    value=(int(min(horas_disponiveis)), int(max(horas_disponiveis))),
                    step=1,
                )
                if linhas_selecionadas == "Todas":
                    df_filtrado = df[
                        (df['hora'] >= horas_disponiveis[0]) &
                        (df['hora'] <= horas_disponiveis[1])
                    ]
                else:
                    df_filtrado = df[
                        (df['linha'] == linhas_selecionadas) &
                        (df['hora'] >= horas_selecionadas[0]) &
                        (df['hora'] <= horas_selecionadas[1])
                    ]
                heatmap_data = df_filtrado.pivot_table(
                    index='hora',
                    columns='linha',
                    values='total_movimentacoes',
                    aggfunc='sum',
                    fill_value=0
                )
                if not heatmap_data.empty:
                    st.markdown("### Mapa de Calor - Movimentação por Linha e Horário")
                    fig_heatmap = px.imshow(
                        heatmap_data,
                        labels={"x": "Linha", "y": "Horário", "color": "Movimentações"},
                        color_continuous_scale="Blues",  
                        title="Heatmap - Movimentações por Linha e Horário",
                        aspect="auto"
                    )
                    fig_heatmap.update_layout(
                        title_font_size=20,
                        title_x=0.5,
                        xaxis_title="Linha",
                        yaxis_title="Horário",
                        coloraxis_colorbar=dict(title="Movimentações", tickprefix=" "),
                        margin=dict(l=0, r=0, t=40, b=0),
                        xaxis=dict(tickmode='linear', tick0=0, dtick=1),  
                        yaxis=dict(tickmode='linear', tick0=0, dtick=1),
                        plot_bgcolor='rgba(0,0,0,0)', 
                        paper_bgcolor='rgba(0,0,0,0)'  
                    )
                    st.plotly_chart(fig_heatmap, use_container_width=True)
                    total_movimentacoes = df_filtrado['total_movimentacoes'].sum()
                    linha_mais_movimentada = df_filtrado.groupby("linha")["total_movimentacoes"].sum().idxmax()
                    horario_pico = df_filtrado.groupby("hora")["total_movimentacoes"].sum().idxmax()
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Total Movimentações", f"{total_movimentacoes:,} pessoas")
                    col2.metric("Linha Mais Movimentada", f"Linha {linha_mais_movimentada}")
                    col3.metric("Horário de Pico", f"{horario_pico}h")
                    st.markdown("### Gráfico de Movimentação por Estação")
                    movimentacao_estacao = df_filtrado.groupby("estacao")["total_movimentacoes"].sum().sort_values(ascending=False)
                    fig_estacao = px.bar(movimentacao_estacao, labels={"value": "Movimentações", "estacao": "Estação"}, title="Movimentação por Estação")
                    fig_estacao.update_layout(barmode='stack', xaxis_title="Estação", yaxis_title="Total de Movimentações", title_x=0.5)
                    st.plotly_chart(fig_estacao, use_container_width=True)
                    st.markdown("### Gráfico de Movimentação por Linha")
                    movimentacao_linha = df_filtrado.groupby("linha")["total_movimentacoes"].sum().sort_values(ascending=False)
                    fig_linha = px.bar(movimentacao_linha, labels={"value": "Movimentações", "linha": "Linha"}, title="Movimentação por Linha")
                    fig_linha.update_layout(barmode='stack', xaxis_title="Linha", yaxis_title="Total de Movimentações", title_x=0.5)
                    st.plotly_chart(fig_linha, use_container_width=True)
                else:
                    st.warning("Nenhum dado disponível para os filtros selecionados.")
            else:
                st.warning("Dados para o heatmap não estão disponíveis no momento.")
        
        elif page == "⏱️ Intervalo Médio Operação":
            st.title("⏱ Intervalo Médio de Operação por Dia")
            data = get_media_intervalo_operacao_por_dia()
            if data:
                df = pd.DataFrame(data)
                df['data'] = pd.to_datetime(df['data'])
                st.write("### Variação do Intervalo Médio de Operação ao Longo do Dia")
                fig_line = px.line(
                    df,
                    x="hora",
                    y="media_intervalo_operacao_segundos",
                    labels={
                        "hora": "Hora do Dia",
                        "media_intervalo_operacao_segundos": "Intervalo Médio (s)"
                    },
                    title="Intervalo Médio de Operação por Hora"
                )
                st.plotly_chart(fig_line, use_container_width=True)
            else:
                st.warning("Dados para o Intervalo Médio Operação não estão disponíveis no momento.")
        
        elif page == "🚪 Tempo Porta Aberta":
            st.title("🚪 Tempo Médio de Porta Aberta")
            data = get_media_tempo_porta_aberta()
            if data:
                df = pd.DataFrame(data)
                df['data'] = pd.to_datetime(df['data'])
                min_date = df['data'].min().date()
                max_date = df['data'].max().date()
                col1, col2 = st.columns(2)
                start_date = col1.date_input("Data de início:", value=min_date, min_value=min_date, max_value=max_date)
                end_date = col2.date_input("Data de fim:", value=max_date, min_value=min_date, max_value=max_date)
                if start_date > end_date:
                    st.error("A data de início não pode ser maior que a data de fim.")
                else:
                    df_filtered = df[(df['data'].dt.date >= start_date) & (df['data'].dt.date <= end_date)]
                    if not df_filtered.empty:
                        df_summary = df_filtered.groupby('linha')['media_tempo_porta_aberta_segundos'].mean().reset_index()
                        df_summary['media_tempo_porta_aberta_minutos'] = df_summary['media_tempo_porta_aberta_segundos'].apply(segundos_para_minutos)
                        media_geral = df_summary['media_tempo_porta_aberta_minutos'].mean()
                        st.write("### Resumo do Tempo Médio de Porta Aberta por Linha")
                        num_linhas = len(df_summary)
                        cols = st.columns(num_linhas)  
                        for i, (index, row) in enumerate(df_summary.iterrows()):
                            delta = row['media_tempo_porta_aberta_minutos'] - media_geral 
                            delta_color = "off" 
                            cols[i].metric(
                                label=f"Linha {row['linha']}",
                                value=f"{row['media_tempo_porta_aberta_minutos']} min",
                                delta=f"{round(abs(delta), 2)} min",
                                delta_color=delta_color,
                                help="Tempo médio de porta aberta"
                            )
                        df_monthly = df_filtered.groupby([df_filtered['data'].dt.to_period('M').rename("data_period"), 'linha']).mean().reset_index()
                        df_monthly['data'] = df_monthly['data_period'].astype(str)
                        df_monthly.drop(columns=["data_period"], inplace=True)
                        st.write("### Variação Mensal do Tempo Médio de Porta Aberta por Linha")
                        fig_line_monthly = px.line(
                            df_monthly,
                            x="data",
                            y="media_tempo_porta_aberta_segundos",
                            color="linha",
                            markers=True,
                            labels={
                                "data": "Mês",
                                "media_tempo_porta_aberta_segundos": "Tempo Médio (s)",
                                "linha": "Linha"
                            },
                            title="Variação Mensal do Tempo Médio de Porta Aberta"
                        )
                        st.plotly_chart(fig_line_monthly, use_container_width=True)
                    else:
                        st.warning("Nenhum dado encontrado para o intervalo de datas selecionado.")
            else:
                st.warning("Dados para o Tempo Porta Aberta não estão disponíveis no momento.")
        
        elif page == "📊 Movimento Classificado":
            st.title("📊 Movimento Classificado por Bilhete")
            data = get_movimento_classificado_por_bilhete()
            if data:
                df = pd.DataFrame(data)
                tipos_disponiveis = sorted(df['tipo_bilhete'].unique())
                tipos_options = ["Todos", "Nenhum"] + tipos_disponiveis
                tipos_selecionados = st.multiselect(
                    "Selecione os tipos de bilhete:",
                    options=tipos_options,
                    default=["Todos"]
                )
                if "Todos" in tipos_selecionados:
                    tipos_filtrados = tipos_disponiveis
                elif "Nenhum" in tipos_selecionados:
                    tipos_filtrados = []
                else:
                    tipos_filtrados = tipos_selecionados
                if tipos_filtrados:
                    df_filtrado = df[df['tipo_bilhete'].isin(tipos_filtrados)]
                else:
                    df_filtrado = pd.DataFrame(columns=df.columns)
                if not df_filtrado.empty:
                    total_movimentos = df_filtrado["total_movimentos"].sum()
                    tipo_mais_utilizado = df_filtrado.groupby("tipo_bilhete")["total_movimentos"].sum().idxmax()
                    classificacao_mais_comum = df_filtrado.groupby("classificacao_lancamento")["total_movimentos"].sum().idxmax()
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Total de Movimentos", f"{total_movimentos:,}")
                    col2.metric("Tipo de Bilhete Mais Usado", tipo_mais_utilizado)
                    col3.metric("Classificação Mais Comum", classificacao_mais_comum)
                    st.markdown("### Movimentos por Tipo de Bilhete e Classificação")
                    fig_barras = px.bar(
                        df_filtrado,
                        x="tipo_bilhete",
                        y="total_movimentos",
                        color="classificacao_lancamento",
                        labels={
                            "tipo_bilhete": "Tipo de Bilhete",
                            "total_movimentos": "Total de Movimentos",
                            "classificacao_lancamento": "Classificação"
                        },
                        title="Movimentos Classificados por Tipo de Bilhete",
                        text="total_movimentos",
                    )
                    fig_barras.update_layout(
                        xaxis_title="Tipo de Bilhete",
                        yaxis_title="Total de Movimentos",
                        legend_title="Classificação",
                        barmode="stack",
                        margin=dict(l=0, r=0, t=30, b=0),
                    )
                    st.plotly_chart(fig_barras, use_container_width=True)
                    st.markdown("### Distribuição Percentual por Classificação de Lançamento")
                    fig_rosca = px.pie(
                        df_filtrado,
                        values="total_movimentos",
                        names="classificacao_lancamento",
                        title="Distribuição de Movimentos por Classificação",
                        hole=0.5,
                    )
                    fig_rosca.update_traces(textinfo="percent+label")
                    fig_rosca.update_layout(
                        margin=dict(l=0, r=0, t=30, b=0),
                    )
                    st.plotly_chart(fig_rosca, use_container_width=True)
                else:
                    st.warning("Nenhum dado disponível para os tipos de bilhetes selecionados.")
            else:
                st.warning("Dados de movimento classificado não estão disponíveis no momento.")
        
        elif page == "🎟️ Tipos de Bilhete":
            st.title("🎟 Análise de Tipos de Bilhete")
            data_abundantes = get_tipos_bilhete_abundantes()
            data_por_dia = get_tipos_bilhete_por_dia()
            data_por_semana = get_tipos_bilhete_por_semana()
            tipos_selecionados = []
            if data_abundantes:
                df_abundantes = pd.DataFrame(data_abundantes)
                tipos_disponiveis = sorted(df_abundantes["tipo_bilhete"].unique())
                tipos_options = ["Todos", "Nenhum"] + tipos_disponiveis
                tipos_selecionados = st.multiselect(
                    "Selecione os tipos de bilhete:",
                    options=tipos_options,
                    default=["Todos"]
                )
                if "Todos" in tipos_selecionados:
                    tipos_filtrados = tipos_disponiveis
                elif "Nenhum" in tipos_selecionados:
                    tipos_filtrados = []
                else:
                    tipos_filtrados = tipos_selecionados
                if tipos_filtrados:
                    df_abundantes = df_abundantes[df_abundantes["tipo_bilhete"].isin(tipos_filtrados)]
                else:
                    df_abundantes = pd.DataFrame(columns=df_abundantes.columns)
                if not df_abundantes.empty:
                    st.write("## Tipos de Bilhete Mais Usados")
                    fig_abundantes = px.bar(
                        df_abundantes,
                        x="tipo_bilhete",
                        y="total_uso",
                        labels={"tipo_bilhete": "Tipo de Bilhete", "total_uso": "Total de Uso"},
                        title="Distribuição dos Tipos de Bilhete",
                        color="tipo_bilhete"
                    )
                    fig_abundantes.update_layout(
                        xaxis_tickangle=-45,
                        xaxis_title="Tipo de Bilhete",
                        yaxis_title="Total de Uso",
                        font=dict(size=12)
                    )
                    st.plotly_chart(fig_abundantes, use_container_width=True)
                else:
                    st.warning("Nenhum dado disponível para os tipos de bilhetes selecionados.")
            if data_por_dia and tipos_selecionados:
                df_por_dia = pd.DataFrame(data_por_dia)
                if 'tipo_bilhete' in df_por_dia.columns:
                    df_por_dia = df_por_dia[df_por_dia["tipo_bilhete"].isin(tipos_filtrados)]
                if not df_por_dia.empty:
                    df_por_dia['data'] = pd.to_datetime(df_por_dia['data'])
                    df_por_dia['mes'] = df_por_dia['data'].dt.to_period('M')
                    df_por_mes = df_por_dia.groupby(['mes', 'tipo_bilhete']).agg({'total_uso': 'sum'}).reset_index()
                    df_por_mes['mes'] = df_por_mes['mes'].astype(str)
                    top_bilhetes = df_por_dia.groupby('tipo_bilhete')['total_uso'].sum().nlargest(10).index
                    df_filtrado = df_por_mes[df_por_mes['tipo_bilhete'].isin(top_bilhetes)]
                    fig_por_mes = px.bar(
                        df_filtrado,
                        x="mes",
                        y="total_uso",
                        color="tipo_bilhete",
                        labels={
                            "mes": "Mês",
                            "total_uso": "Total de Uso",
                            "tipo_bilhete": "Tipo de Bilhete"
                        },
                        title="Tipos de Bilhete Mais Usados por Mês (Top 10)",
                        barmode="stack"
                    )
                    st.plotly_chart(fig_por_mes, use_container_width=True)
            if data_por_semana and tipos_selecionados:
                df_por_semana = pd.DataFrame(data_por_semana)
                if 'tipo_bilhete' in df_por_semana.columns:
                    df_por_semana = df_por_semana[df_por_semana["tipo_bilhete"].isin(tipos_filtrados)]
                if not df_por_semana.empty:
                    fig_por_semana = px.bar(
                        df_por_semana,
                        x="data",
                        y="total_uso",
                        color="tipo_dia",
                        labels={"data": "Semana", "total_uso": "Total de Uso", "tipo_dia": "Tipo de Dia"},
                        title="Uso de Tipos de Bilhete por Semana",
                        barmode="stack"
                    )
                    fig_por_semana.update_layout(
                        xaxis_title="Semana",
                        yaxis_title="Total de Uso",
                        font=dict(size=12)
                    )
                    st.plotly_chart(fig_por_semana, use_container_width=True)
        
        elif page == "📟 Sensores por Data":
            st.title("📟 Sensores por Data")
            dados = get_sensores_por_data()
            if dados:
                df = pd.DataFrame(dados)
                df["data"] = pd.to_datetime(df["data"])
                status_mapping = {0: "OK", 3: "Warning", 255: "Crítico"}
                df["status_label"] = df["sensor_status"].map(status_mapping)
                linhas_disponiveis = list(df['line_id'].unique())
                linhas_disponiveis.insert(0, "Todos")  
                linha_selecionada = st.selectbox("Selecione uma Linha:", options=linhas_disponiveis)
                if linha_selecionada != "Todos":
                    df_filtrado = df[df['line_id'] == linha_selecionada]
                else:
                    df_filtrado = df
                status_count = df_filtrado['status_label'].value_counts()
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"<h3 style='text-align: center;'>OK</h3>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='text-align: center; color: green;'>{status_count.get('OK', 0)}</h1>", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"<h3 style='text-align: center;'>Warning</h3>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='text-align: center; color: orange;'>{status_count.get('Warning', 0)}</h1>", unsafe_allow_html=True)
                with col3:
                    st.markdown(f"<h3 style='text-align: center;'>Crítico</h3>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='text-align: center; color: red;'>{status_count.get('Crítico', 0)}</h1>", unsafe_allow_html=True)
                st.write("### Total de Eventos por Data (Linha Selecionada)")
                data_min1, data_max1 = st.slider(
                    "Intervalo de datas para o Gráfico 1",
                    min_value=df_filtrado["data"].min().date(),
                    max_value=df_filtrado["data"].max().date(),
                    value=(df_filtrado["data"].min().date(), df_filtrado["data"].max().date()),
                    key="slider_grafico_1"
                )
                df_grafico1 = df_filtrado[
                    (df_filtrado["data"] >= pd.Timestamp(data_min1)) & 
                    (df_filtrado["data"] <= pd.Timestamp(data_max1))
                ]
                fig1 = px.bar(
                    df_grafico1,
                    x="data",
                    y="total_eventos",
                    color="status_label",
                    barmode="group",
                    title=f"Eventos por Status - Linha {linha_selecionada}"
                )
                st.plotly_chart(fig1, use_container_width=True)
                st.write("### Proporção de Status dos Sensores")
                data_min2, data_max2 = st.slider(
                    "Intervalo de datas para o Gráfico 2",
                    min_value=df_filtrado["data"].min().date(),
                    max_value=df_filtrado["data"].max().date(),
                    value=(df_filtrado["data"].min().date(), df_filtrado["data"].max().date()),
                    key="slider_grafico_2"
                )
                df_grafico2 = df_filtrado[
                    (df_filtrado["data"] >= pd.Timestamp(data_min2)) & 
                    (df_filtrado["data"] <= pd.Timestamp(data_max2))
                ]
                proporcao_status = df_grafico2["status_label"].value_counts(normalize=True) * 100
                fig2 = px.pie(
                    names=proporcao_status.index,
                    values=proporcao_status.values,
                    title="Distribuição Percentual dos Status"
                )
                st.plotly_chart(fig2, use_container_width=True)
                st.write("### Tendência de Eventos ao Longo do Tempo")
                data_min3, data_max3 = st.slider(
                    "Intervalo de datas para o Gráfico 3",
                    min_value=df_filtrado["data"].min().date(),
                    max_value=df_filtrado["data"].max().date(),
                    value=(df_filtrado["data"].min().date(), df_filtrado["data"].max().date()),
                    key="slider_grafico_3"
                )
                df_grafico3 = df_filtrado[
                    (df_filtrado["data"] >= pd.Timestamp(data_min3)) & 
                    (df_filtrado["data"] <= pd.Timestamp(data_max3))
                ]
                tendencia = df_grafico3.groupby(["data", "status_label"])["total_eventos"].sum().reset_index()
                fig3 = px.line(
                    tendencia,
                    x="data",
                    y="total_eventos",
                    color="status_label",
                    title="Tendência de Eventos por Status"
                )
                st.plotly_chart(fig3, use_container_width=True)
                st.write("### Eventos Críticos por Data")
                data_min4, data_max4 = st.slider(
                    "Intervalo de datas para o Gráfico 4",
                    min_value=df_filtrado["data"].min().date(),
                    max_value=df_filtrado["data"].max().date(),
                    value=(df_filtrado["data"].min().date(), df_filtrado["data"].max().date()),
                    key="slider_grafico_4"
                )
                df_grafico4 = df_filtrado[
                    (df_filtrado["data"] >= pd.Timestamp(data_min4)) & 
                    (df_filtrado["data"] <= pd.Timestamp(data_max4))
                ]
                eventos_criticos = df_grafico4[df_grafico4["status_label"] == "Crítico"].groupby("data")["total_eventos"].sum().reset_index()
                fig4 = px.bar(
                    eventos_criticos,
                    x="data",
                    y="total_eventos",
                    title="Eventos Críticos por Data",
                    labels={"total_eventos": "Eventos Críticos"}
                )
                st.plotly_chart(fig4, use_container_width=True)
            else:
                st.error("Erro ao carregar dados de sensores.")
        
        elif page == "📈 Infográfico":
            st.title("📈 Infográfico")
            st.markdown("### Aqui está o infográfico feito pelo grupo.")
            texto_descritivo = """
            &emsp;&emsp;Ao aplicarmos o princípio da Gestalt da Simplicidade no design do infográfico, nosso objetivo é otimizar a experiência do usuário. 
            Isso garante que as informações mais relevantes sobre a evolução dos trens como meio de transporte sejam compreendidas de forma rápida. 
            Ao eliminar elementos visuais desnecessários e organizar os dados de maneira intuitiva, facilitamos a leitura e a interpretação do infográfico.
        
            &emsp;&emsp;A heurística da Visibilidade do Status do Sistema assegura que o usuário esteja sempre ciente do estado atual do sistema. No contexto do nosso infográfico, 
            isso significa que o usuário deve compreender facilmente a evolução histórica do transporte ferroviário e seu impacto na vida das pessoas. 
            Para alcançar isso, simplificamos os gráficos, reduzindo o número de categorias e utilizando tipos de gráficos mais intuitivos, o que permite transmitir 
            essa informação de forma mais eficaz. A combinação da Simplicidade com a Visibilidade do Status do Sistema foi fundamental para criar um infográfico 
            mais conciso e informativo. Agrupamos elementos relacionados, como os diferentes tipos de bilhetes, e utilizamos uma linha do tempo para visualizar 
            a evolução histórica. Essa abordagem não só facilita a compreensão das relações entre os dados, mas também promove uma experiência sincrética, onde 
            diferentes informações se conectam harmoniosamente.
        
            &emsp;&emsp;Optamos por um layout bem espaçado e organizado, aproveitando as margens para dar respiro ao design. Essa escolha é crucial para evitar a sobrecarga visual 
            e permitir que o usuário absorva as informações de maneira mais eficaz. A escolha de uma paleta de cores e fontes legíveis também contribui para uma 
            experiência visual agradável, tornando o infográfico não apenas informativo, mas também esteticamente atraente. Ao seguir esses princípios de design, 
            conseguimos criar um infográfico que auxilia o usuário a entender a importância do transporte ferroviário com informações-chave. A integração dos princípios 
            da Gestalt com as heurísticas de usabilidade resulta em uma interface que valoriza tanto a simplicidade quanto a clareza na comunicação das informações.
            """
            st.markdown(texto_descritivo)
            infografico_url = "https://res.cloudinary.com/dmornatkl/image/upload/v1733432055/A_Revolu%C3%A7%C3%A3o_Industrial_e_os_Trilhos_kjuhge.png"
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="{infografico_url}" alt="Infográfico" style="width: 100%; max-width: 100%;">
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown("[Clique aqui para editar o infográfico no Canva](https://www.canva.com/design/DAGYWdq1lHw/VQKadpMG6SUPr1g7rqSClg/edit)", unsafe_allow_html=True)
        
        def format_number_report(value):
            if value >= 1_000_000:
                return f"{value / 1_000_000:.1f}M"
            elif value >= 1_000:
                return f"{value / 1_000:.1f}k"
            return str(value)
        
        page_to_filename = {
            "🏠 Home": "relatorio_home.txt",
            "🚉 Fluxo Entre Estações": "relatorio_fluxo_entre_estacoes.txt",
            "🌡️ Heatmap": "relatorio_heatmap.txt",
            "⏱️ Intervalo Médio Operação": "relatorio_intervalo_medio_operacao.txt",
            "🚪 Tempo Porta Aberta": "relatorio_tempo_porta_aberta.txt",
            "📊 Movimento Classificado": "relatorio_movimento_classificado.txt",
            "🎟️ Tipos de Bilhete": "relatorio_tipos_de_bilhete.txt",
            "📟 Sensores por Data": "relatorio_sensores_por_data.txt",
            "📈 Infográfico": "relatorio_infografico.txt",
        }

        def get_report_filename(page):
            return page_to_filename.get(page, "relatorio_analise_dados.txt")

        def generate_report(page):
            report = "Relatório de Análise de Dados\n"
            report += "="*30 + "\n\n"
            
            if page == "🏠 Home":
                report += "Página: 🏠 Home\n"
                report += "-"*20 + "\n"
                
                fluxo_data = get_fluxo_entre_estacoes()
                intervalo_data = get_media_intervalo_operacao_por_dia()
                porta_data = get_media_tempo_porta_aberta()
                
                if fluxo_data:
                    df_fluxo = pd.DataFrame(fluxo_data)
                    df_fluxo["taxa_retenção"] = df_fluxo["total_entradas"] / df_fluxo["total_saidas"]
                    top_fluxo = df_fluxo.loc[df_fluxo["total_entradas"].idxmax()]
                    report += f"💥 Maior Fluxo de Entrada: {format_number_report(top_fluxo['total_entradas'])} pessoas na Estação {top_fluxo['estacao_inicio']} → {top_fluxo['estacao_fim']}\n"
                
                if intervalo_data and porta_data:
                    df_intervalo = pd.DataFrame(intervalo_data)
                    df_porta = pd.DataFrame(porta_data)
                
                    intervalo_medio = df_intervalo["media_intervalo_operacao_segundos"].mean()
                    minutos_int, segundos_int = divmod(intervalo_medio, 60)
                    report += f"⏱ Intervalo Médio Entre Estações: {int(minutos_int)}m {int(segundos_int)}s\n"
                
                    porta_media = df_porta["media_tempo_porta_aberta_segundos"].mean()
                    minutos_porta, segundos_porta = divmod(porta_media, 60)
                    eficiencia_operacional = min(1, 30 / porta_media) * 100
                    report += f"💪 Tempo Médio Porta Aberta: {int(minutos_porta)}m {int(segundos_porta)}s\n"
                    report += f"⚙️ Eficiência Operacional (30s): {eficiencia_operacional:.2f}%\n"
                
                report += "\n"
            
            elif page == "🚉 Fluxo Entre Estações":
                report += "Página: 🚉 Fluxo Entre Estações\n"
                report += "-"*30 + "\n"
                
                data = get_fluxo_entre_estacoes()
                if data:
                    df = pd.DataFrame(data)
                    total_entradas = df["total_entradas"].sum()
                    total_saidas = df["total_saidas"].sum()
                    report += f"Total de Entradas: {format_number_report(total_entradas)}\n"
                    report += f"Total de Saídas: {format_number_report(total_saidas)}\n"
                else:
                    report += "Dados de fluxo entre estações não disponíveis.\n"
                
                report += "\n"
            
            elif page == "🌡️ Heatmap":
                report += "Página: 🌡️ Heatmap\n"
                report += "-"*20 + "\n"
                
                data = get_heatmap_pessoas_por_linha()
                if data:
                    df = pd.DataFrame(data)
                    total_movimentacoes = df['total_movimentacoes'].sum()
                    linha_mais_movimentada = df.groupby("linha")["total_movimentacoes"].sum().idxmax()
                    horario_pico = df.groupby("hora")["total_movimentacoes"].sum().idxmax()
                    report += f"Total de Movimentações: {total_movimentacoes:,} pessoas\n"
                    report += f"Linha Mais Movimentada: Linha {linha_mais_movimentada}\n"
                    report += f"Horário de Pico: {horario_pico}h\n"
                else:
                    report += "Dados para o heatmap não estão disponíveis.\n"
                
                report += "\n"
            
            elif page == "⏱️ Intervalo Médio Operação":
                report += "Página: ⏱️ Intervalo Médio Operação\n"
                report += "-"*30 + "\n"
                
                data = get_media_intervalo_operacao_por_dia()
                if data:
                    df = pd.DataFrame(data)
                    intervalo_medio = df["media_intervalo_operacao_segundos"].mean()
                    minutos_int, segundos_int = divmod(intervalo_medio, 60)
                    report += f"Intervalo Médio de Operação: {int(minutos_int)}m {int(segundos_int)}s\n"
                else:
                    report += "Dados para o Intervalo Médio Operação não estão disponíveis.\n"
                
                report += "\n"
            
            elif page == "🚪 Tempo Porta Aberta":
                report += "Página: 🚪 Tempo Porta Aberta\n"
                report += "-"*30 + "\n"
                
                data = get_media_tempo_porta_aberta()
                if data:
                    df = pd.DataFrame(data)
                    porta_media = df["media_tempo_porta_aberta_segundos"].mean()
                    minutos_porta, segundos_porta = divmod(porta_media, 60)
                    eficiencia_operacional = min(1, 30 / porta_media) * 100
                    report += f"Tempo Médio Porta Aberta: {int(minutos_porta)}m {int(segundos_porta)}s\n"
                    report += f"Eficiência Operacional (30s): {eficiencia_operacional:.2f}%\n"
                else:
                    report += "Dados para o Tempo Porta Aberta não estão disponíveis.\n"
                
                report += "\n"
            
            elif page == "📊 Movimento Classificado":
                report += "Página: 📊 Movimento Classificado\n"
                report += "-"*30 + "\n"
                
                data = get_movimento_classificado_por_bilhete()
                if data:
                    df = pd.DataFrame(data)
                    total_movimentos = df["total_movimentos"].sum()
                    tipo_mais_utilizado = df.groupby("tipo_bilhete")["total_movimentos"].sum().idxmax()
                    classificacao_mais_comum = df.groupby("classificacao_lancamento")["total_movimentos"].sum().idxmax()
                    report += f"Total de Movimentos: {total_movimentos:,}\n"
                    report += f"Tipo de Bilhete Mais Usado: {tipo_mais_utilizado}\n"
                    report += f"Classificação Mais Comum: {classificacao_mais_comum}\n"
                else:
                    report += "Dados de movimento classificado não estão disponíveis.\n"
                
                report += "\n"
            
            elif page == "🎟️ Tipos de Bilhete":
                report += "Página: 🎟️ Tipos de Bilhete\n"
                report += "-"*30 + "\n"
                
                data_abundantes = get_tipos_bilhete_abundantes()
                if data_abundantes:
                    df_abundantes = pd.DataFrame(data_abundantes)
                    total_uso = df_abundantes["total_uso"].sum()
                    top_tipo = df_abundantes.sort_values("total_uso", ascending=False).head(1)["tipo_bilhete"].values[0]
                    report += f"Total de Uso de Bilhetes: {format_number_report(total_uso)}\n"
                    report += f"Tipo de Bilhete Mais Usado: {top_tipo}\n"
                else:
                    report += "Dados de tipos de bilhete abundantes não estão disponíveis.\n"
                
                report += "\n"
            
            elif page == "📟 Sensores por Data":
                report += "Página: 📟 Sensores por Data\n"
                report += "-"*30 + "\n"
                
                dados = get_sensores_por_data()
                if dados:
                    df = pd.DataFrame(dados)
                    status_count = df['sensor_status'].value_counts()
                    ok = status_count.get(0, 0)
                    warning = status_count.get(3, 0)
                    critico = status_count.get(255, 0)
                    report += f"Status OK: {ok}\n"
                    report += f"Status Warning: {warning}\n"
                    report += f"Status Crítico: {critico}\n"
                else:
                    report += "Dados de sensores por data não estão disponíveis.\n"
                
                report += "\n"
            
            elif page == "📈 Infográfico":
                report += "Página: 📈 Infográfico\n"
                report += "-"*30 + "\n"
                report += "Infográfico exibido na aplicação.\n"
                
                report += "\n"
            
            else:
                report += "Página: Outras Seções\n"
                report += "-"*20 + "\n"
                report += "Detalhes do relatório para outras seções podem ser adicionados aqui.\n\n"
            
            report += "Relatório gerado em: " + pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            return report

        st.header("📄 Relatório de Análise de Dados")

        if st.button("Gerar Relatório"):
            report_content = generate_report(st.session_state["page"])
            report_filename = get_report_filename(st.session_state["page"])

            st.download_button(
                label="📥 Baixar Relatório",
                data=report_content,
                file_name=report_filename,
                mime="text/plain"
            )
    
    if not st.session_state.get("authentication_status"):
        login_screen()
    else:
        main_app()

if __name__ == "__main__":
    main()