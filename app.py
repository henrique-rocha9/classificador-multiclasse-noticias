import streamlit as st
import joblib
import re
import os

# ── Configuração da página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Classificador de Notícias",
    page_icon="📰",
    layout="centered"
)

# ── Carregamento do modelo ──────────────────────────────────────────────────
@st.cache_resource
def carregar_modelo():
    caminho = os.path.join(os.path.dirname(__file__), "model", "modelo_final.joblib")
    return joblib.load(caminho)

try:
    modelo = carregar_modelo()
    modelo_ok = True
except Exception as e:
    modelo_ok = False
    erro_modelo = str(e)

# ── Pré-processamento (igual ao notebook) ──────────────────────────────────
def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-z\s]', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

# ── Descrições das categorias ──────────────────────────────────────────────
DESCRICOES = {
    "POLITICS":      ("🏛️", "Política", "Notícias sobre governo, eleições, legislação e figuras políticas."),
    "WELLNESS":      ("🧘", "Bem-estar", "Saúde, mente, alimentação, yoga e qualidade de vida."),
    "ENTERTAINMENT": ("🎬", "Entretenimento", "Cinema, música, celebridades, séries e premiações."),
    "TRAVEL":        ("✈️", "Viagens", "Destinos, hotéis, dicas de viagem e turismo."),
    "STYLE & BEAUTY":("💄", "Estilo & Beleza", "Moda, beleza, skincare, cabelo e tendências."),
}

# ── Interface ───────────────────────────────────────────────────────────────
st.title("📰 Classificador de Notícias")
st.markdown(
    "Insira uma manchete em **inglês** para classificá-la automaticamente em uma das 5 categorias."
)
st.markdown("---")

if not modelo_ok:
    st.error(f"⚠️ Erro ao carregar o modelo: {erro_modelo}")
    st.stop()

manchete = st.text_area(
    "Manchete:",
    placeholder="Ex: Trump signs new immigration bill in the Senate",
    height=80
)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    classificar = st.button("🔍 Classificar", use_container_width=True)

st.markdown("---")

if classificar:
    if manchete.strip() == "":
        st.warning("⚠️ Por favor, insira uma manchete antes de classificar.")
    else:
        manchete_limpa = limpar_texto(manchete)
        predicao = modelo.predict([manchete_limpa])[0]

        emoji, nome_pt, descricao = DESCRICOES.get(
            predicao, ("📌", predicao, "Categoria identificada pelo modelo.")
        )

        st.success(f"### {emoji} Categoria: **{nome_pt}** `{predicao}`")
        st.info(f"**Sobre esta categoria:** {descricao}")

        with st.expander("ℹ️ Como funciona?"):
            st.markdown("""
O modelo utiliza um **Pipeline sklearn** composto por:
1. **TF-IDF Vectorizer** — converte o texto em vetores numéricos considerando unigramas e bigramas (`ngram_range=(1,2)`, `max_features=50.000`)
2. **LinearSVC** — classificador de vetores de suporte linear treinado com `class_weight='balanced'` para lidar com o desbalanceamento entre categorias

O modelo foi treinado no **News Category Dataset** do HuffPost com as 5 categorias mais frequentes, validado com **StratifiedKFold (k=3)**.
            """)

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#888; font-size:13px;'>"
    "Desafio 18 — Classificação de Notícias | Grupo 18 | UNIMAR 2026"
    "</p>",
    unsafe_allow_html=True
)
