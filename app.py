import streamlit as st
from mistralai import Mistral
import os
import re

# 1. DESIGN DE ELITE (TEMA BLACK & NEON)
st.set_page_config(page_title="Focus PRF IAQstron", layout="centered")

st.markdown("""
    <style>
    /* Fundo Total Black */
    .stApp { background-color: #000000; color: #ffffff; }
    
    /* Card de Resposta Estilo Vidro */
    .card { 
        background: #0d0d0d; 
        padding: 30px; 
        border-radius: 15px; 
        border: 1px solid #1f1f1f; 
        line-height: 1.8;
        box-shadow: 0 10px 40px rgba(0,0,0,0.8);
        margin-bottom: 25px;
    }
    
    /* Títulos e Destaques */
    h2 { color: #00ff88; font-family: 'Courier New', monospace; border-bottom: 1px solid #222; padding-bottom: 8px; font-size: 1.1rem; text-transform: uppercase; margin-top: 25px; }
    .verbo { color: #fff; background: #b00; padding: 2px 6px; border-radius: 4px; font-weight: bold; text-transform: uppercase; font-size: 0.9rem; }
    .sumula { color: #ffd700; font-weight: bold; border-bottom: 1px solid #ffd700; }
    b { color: #00ff88; }
    
    /* Limpeza de Interface */
    #MainMenu, footer, header {visibility: hidden;}
    .stTextInput>div>div>input { background-color: #111; color: #00ff88; border: 1px solid #333; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. CONEXÃO NEURAL (CHAVE MISTRAL)
# No Streamlit Cloud, adicione sua chave em Advanced Settings > Secrets
API_KEY = st.secrets.get("MISTRAL_API_KEY", "6Hf8wwQJwEP36FsrNw9m7hY1hYbLAOAF")
client = Mistral(api_key=API_KEY)

# 3. INTERFACE PRINCIPAL
st.markdown("<h1 style='text-align: center; color: #00ff88; font-family: monospace; letter-spacing: 4px;'>FOCUS PRF IAQSTRON</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #444; font-size: 0.8rem;'>SISTEMA DE FATIAMENTO NEURAL v10.0</p>", unsafe_allow_html=True)

query = st.text_input("", placeholder="Qual artigo ou tema vamos triturar agora?")

if query:
    with st.spinner("TRITURANDO BASE LEGAL..."):
        try:
            # PROMPT DE COMANDO PARA A IA (O "GATILHO")
            sys_prompt = """Você é o motor principal do Focus PRF IAQstron.
            Sua missão é dar aulas fatiadas e letais para a PRF.
            
            ESTRUTURA OBRIGATÓRIA (USE APENAS HTML):
            <h2>📜 LEI SECA FATIADA</h2> (Explicação direta do artigo)
            <h2>⚖️ PUNIÇÃO ADM vs CRIMINAL</h2> (Diferencie as esferas)
            <h2>🏛️ JURISPRUDÊNCIA</h2> (Súmulas STF/STJ importantes)
            <h2>📖 PEGADINHAS DE VERBO</h2> (Onde a banca Cebraspe troca as palavras)

            REGRAS DE OURO:
            - Verbos de comando (pode, deve, salvo, etc) em <span class='verbo'>VERBO</span>.
            - Súmulas em <span class='sumula'>Súmula X</span>.
            - PROIBIDO usar asteriscos (*), hashtags (#) ou hifens.
            - Seja direto, técnico e use termos de concurso."""

            resp = client.chat.complete(
                model="mistral-small-latest",
                messages=[{"role": "system", "content": sys_prompt}, {"role": "user", "content": query}]
            )

            # 4. FILTRO ATÔMICO (LIMPEZA DE TEXTO)
            raw_text = resp.choices[0].message.content
            # Remove qualquer lixo de formatação Markdown que a IA insistir em colocar
            clean_text = raw_text.replace('*', '').replace('#', '').replace('---', '').replace('_', '')
            
            st.markdown(f"<div class='card'>{clean_output := clean_text}</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Erro na conexão neural: {e}")

st.markdown("<p style='text-align: center; color: #222; font-size: 0.7rem;'>Balsas/MA - Operação PRF 2026</p>", unsafe_allow_html=True)
