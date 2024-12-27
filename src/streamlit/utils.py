import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def authenticated_get(endpoint: str):
    base_url = os.getenv("BASE_URL")
    token = os.getenv("STREAMLIT_TOKEN")
    api_key = os.getenv("API_KEY")

    if not base_url or not token or not api_key:
        st.error("Configuração inválida: BASE_URL, STREAMLIT_TOKEN ou API_KEY está ausente.")
        return None

    headers = {
        "Authorization": f"Bearer {token}",
        "X-API-KEY": api_key
    }
    try:
        response = requests.get(f"{base_url}/{endpoint}", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Erro ao buscar os dados: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"Erro durante a requisição: {e}")
        return None


def get_fluxo_entre_estacoes():
    return authenticated_get("dados/view_fluxo_entre_estacoes")

def get_heatmap_pessoas_por_linha():
    return authenticated_get("dados/view_heatmap_pessoas_por_linha")

def get_media_intervalo_operacao_por_dia():
    return authenticated_get("dados/view_media_intervalo_operacao_por_dia")

def get_media_tempo_porta_aberta():
    return authenticated_get("dados/view_media_tempo_porta_aberta")

def get_movimento_classificado_por_bilhete():
    return authenticated_get("dados/view_movimento_classificado_por_bilhete")

def get_tipos_bilhete_abundantes():
    return authenticated_get("dados/view_tipos_bilhete_abundantes")

def get_tipos_bilhete_por_dia():
    return authenticated_get("dados/view_tipos_bilhete_por_dia")

def get_tipos_bilhete_por_semana():
    return authenticated_get("dados/view_tipos_bilhete_por_semana")

def get_tipos_bilhete_por_semana():
    return authenticated_get("dados/view_tipos_bilhete_por_semana")

def get_sensores_por_data():
    return authenticated_get("dados/view-sensores-por-data")

