import streamlit as st
from mistralai import Mistral
import time

# --- 1. CONFIGURAÇÃO VISUAL DE ELITE (INTERFACE SOURCECAT) ---
st.set_page_config(
    page_title="SourceCat // Neural Intel",
    page_icon="🐱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS OMEGA: Design Glassmorphism, Neon e Tipografia Tática
st.markdown("""
    <style>
    /* Fundo Total Black */
    .stApp { background-color: #050505; }
    
    /* Remove barras padrão do Streamlit */
    header, footer, #MainMenu { visibility: hidden; }
    
    /* Card de Resposta (Vidro Escuro) */
    .neural-card {
        background: rgba(20, 20, 20, 0.9);
        border: 1px solid #333;
        border-left: 4px solid #00ff88;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 0 50px rgba(0, 255, 136, 0.05);
        margin-top: 20px;
        animation: fadeIn 0.5s ease-in-out;
    }
    
    /* Tipografia */
    h1 { color: #fff; font-family: 'Courier New', monospace; letter-spacing: -1px; font-weight: 700; }
    h2 { color: #00ff88; font-family: sans-serif; font-size: 1.1rem; text-transform: uppercase; margin-top: 25px; border-bottom: 1px solid #222; padding-bottom: 5px; }
    p, li { color: #e0e0e0; font-family: sans-serif; line-height: 1.6; font-size: 1rem; }
    
    /* Destaques Táticos */
    .verbo { background-color: rgba(255, 62, 62, 0.15); color: #ff5555; padding: 2px 6px; border-radius: 4px; font-weight: bold; border: 1px solid rgba(255, 62, 62, 0.3); }
    .sumula { color: #ffd700; font-weight: bold; text-decoration: none; border-bottom: 1px dashed #ffd700; }
    .badge { background: #111; color: #666; padding: 4px 10px; border-radius: 20px; font-size: 0.7rem; border: 1px solid #333; margin-bottom: 20px; display: inline-block; }

    /* Input Customizado */
    .stTextInput input {
        background-color: #0a0a0a !important;
        color: #00ff88 !important;
        border: 1px solid #222 !important;
        border-radius: 8px !important;
        padding: 15px !important;
    }
    .stTextInput input:focus { border-color: #00ff88 !important; box-shadow: 0 0 15px rgba(0,255,136,0.1) !important; }
    
    /* Animação */
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
""", unsafe_allow_html=True)

# --- 2. SISTEMA DE SEGURANÇA E CONEXÃO ---
try:
    # A MÁGICA: O código busca a chave no cofre do servidor, não no código exposto
    API_KEY = st.secrets["MISTRAL_KEY"]
except:
    st.error("⛔ ERRO DE SEGURANÇA: Chave API não detectada nos Secrets.")
    st.stop()

client = Mistral(api_key=API_KEY)

# --- 3. INTERFACE DE USUÁRIO (FRONTEND) ---
st.markdown("<div class='badge'>SYSTEM: ONLINE // v12.0</div>", unsafe_allow_html=True)
st.markdown("<h1>SOURCECAT <span style='color:#00ff88'>//</span> OMNI</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#666; font-size: 0.9rem; margin-bottom: 30px;'>INTELIGÊNCIA TÁTICA PARA PRF & CEBRASPE</p>", unsafe_allow_html=True)

query = st.text_input("", placeholder="Digite o comando (Ex: Art 306, Abuso de Autoridade)...")

# --- 4. LÓGICA NEURAL (BACKEND API) ---
if query:
    with st.spinner("PROCESSANDO FATIAMENTO..."):
        try:
            # Prompt de Engenharia Reversa da Banca
            sys_prompt = """
            Você é o SOURCECAT, uma IA Tática.
            Sua missão: Fatiar leis para concursos da PRF (Cebraspe).
            
            REGRAS VISUAIS RÍGIDAS (HTML):
            1. Use <h2>TÍTULO</h2> para separar seções.
            2. Use <p>texto</p> para parágrafos.
            3. Verbos de comando: <span class='verbo'>VERBO</span>.
            4. Súmulas/Jurisprudência: <span class='sumula'>Súmula X</span>.
            5. PROIBIDO: Asteriscos (*), Markdown (#), ou blocos de código.
            
            ESTRUTURA DE RESPOSTA:
            - LEI SECA (O que diz a letra da lei)
            - TRÍPLICE ESFERA (Administrativo, Civil e Penal)
            - GATILHO MENTAL (Como decorar)
            - A PEGADINHA (Como a banca troca as palavras)
            """
            
            # Chamada API
            resp = client.chat.complete(
                model="mistral-small-latest",
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": query}
                ]
            )
            
            # Filtro de Limpeza (Sanitização)
            raw_content = resp.choices[0].message.content
            clean_content = raw_content.replace("```html", "").replace("```", "").replace("*", "").replace("#", "")

            # Renderização Final
            st.markdown(f"<div class='neural-card'>{clean_content}</div>", unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"FALHA NA CONEXÃO NEURAL: {str(e)}")

# Rodapé Discreto
st.markdown("<div style='position:fixed; bottom:10px; right:10px; color:#333; font-size:0.7rem;'>SOURCECAT SYSTEM</div>", unsafe_allow_html=True)
