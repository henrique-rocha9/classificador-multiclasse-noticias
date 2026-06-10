# 📰 Classificador de Notícias — Desafio 18

**Grupo 18 | NLP | Classificação Multiclasse | UNIMAR 2026**

---

## 🔗 Aplicação Publicada

👉 **[Acessar o app aqui](https://SEU-LINK-STREAMLIT.streamlit.app)** ← *substitua pelo link após o deploy*

---

## 👥 Integrantes

| Nome | RA |
|------|----|
| *Henrique Giaxa da Rocha* | *2030402* |
| *Gabriel Tomazela Rodrigues* | *2028807* |
| *Pedro Boschetti Servidoni* | *2039519* |

---

## 📋 Descrição do Problema

Plataformas de notícias precisam organizar e recomendar conteúdo para milhões de usuários diariamente. A categorização manual é inviável nessa escala, tornando a classificação automática de manchetes uma solução essencial.

## 🎯 Objetivo

Desenvolver um modelo de Machine Learning capaz de classificar automaticamente manchetes de notícias em 5 categorias predefinidas, utilizando técnicas clássicas de NLP com TF-IDF.

---

## 📊 Dataset

- **Nome:** News Category Dataset
- **Fonte:** [Kaggle — rmisra/news-category-dataset](https://www.kaggle.com/datasets/rmisra/news-category-dataset)
- **Origem:** HuffPost
- **Total original:** ~200.000 manchetes com mais de 40 categorias
- **Utilizado:** 5 categorias mais frequentes (~87.000 manchetes)

### Categorias selecionadas

| Categoria | Aprox. manchetes |
|-----------|-----------------|
| POLITICS | ~35.000 |
| WELLNESS | ~17.000 |
| ENTERTAINMENT | ~17.000 |
| TRAVEL | ~9.000 |
| STYLE & BEAUTY | ~9.000 |

> ⚠️ O dataset não está versionado neste repositório por ser grande (~100MB).
> Para obtê-lo: acesse o link acima no Kaggle e baixe o arquivo `News_Category_Dataset_v3.json`.
> Coloque o arquivo na pasta `data/` antes de rodar o notebook.

---

## 🤖 Tipo de Problema de ML

**Classificação Multiclasse Supervisionada** — cada manchete recebe exatamente uma das 5 categorias.

---

## 🔬 Metodologia

1. **Análise Exploratória (EDA):** distribuição das categorias, tamanho médio das manchetes, palavras mais frequentes por categoria (frequência bruta)
2. **Pré-processamento:** remoção de pontuação e conversão para lowercase via regex
3. **Divisão dos dados:** 80% treino / 20% teste com `stratify=y`
4. **Vetorização:** TF-IDF com `ngram_range=(1,2)` e `max_features=50.000`
5. **Validação:** StratifiedKFold com k=3 aplicado **somente sobre o treino**
6. **Treinamento:** 3 classificadores em Pipeline
7. **Tratamento de desbalanceamento:** `class_weight='balanced'` nos modelos lineares
8. **Feature importance:** análise dos coeficientes do LinearSVC

---

## 🏋️ Modelos Treinados

| Modelo | Configuração |
|--------|-------------|
| MultinomialNB | padrão |
| LogisticRegression | `max_iter=1000`, `class_weight='balanced'` |
| LinearSVC | `max_iter=2000`, `class_weight='balanced'` |

Todos dentro de um **Pipeline sklearn** (TF-IDF + classificador).

---

## 🏆 Modelo Final Escolhido

**LinearSVC** — apresentou o melhor F1-Score Macro na validação cruzada e no conjunto de teste. Modelos SVM lineares são reconhecidamente eficazes para classificação de texto em alta dimensionalidade.

---

## 📈 Métricas de Avaliação

- **Acurácia** — proporção de predições corretas
- **Precisão Macro** — média da precisão por classe (sem ponderação por tamanho)
- **Recall Macro** — média do recall por classe
- **F1-Score Macro** — média harmônica de precisão e recall por classe

> O F1-Score **Macro** foi escolhido como métrica principal por ser mais adequado em cenários com desbalanceamento entre classes.

---

## 📊 Principais Resultados


| Modelo | Acurácia | F1-Score Macro |
|--------|----------|----------------|
| MultinomialNB | 0.8520 | 0.8308 |
| LogisticRegression | 0.8840 | 0.8712 |
| LinearSVC | 0.8943  | 0.8802 |

---

## 📁 Estrutura dos Arquivos

```
desafio18-classificacao-noticias/
├── app.py                          # Aplicação Streamlit
├── requirements.txt                # Dependências do projeto
├── README.md                       # Documentação
│
├── notebooks/
│   └── notebook_atualizado.ipynb   # Notebook revisado (P2)
│
├── model/
│   └── modelo_final.joblib         # Pipeline completo salvo
│
├── reports/
│   └── relatorio_atualizado.pdf    # Relatório final
│
└── data/
    └── README_dados.md             # Instruções para obter o dataset
```

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- scikit-learn (Pipeline, TF-IDF, LinearSVC, StratifiedKFold)
- pandas / numpy
- matplotlib / seaborn
- joblib
- Streamlit

---

## ▶️ Como Executar o Notebook

```bash
# 1. Clone o repositório
git clone https://github.com/SEU-USUARIO/desafio18-classificacao-noticias.git
cd desafio18-classificacao-noticias

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Coloque o dataset em data/News_Category_Dataset_v3.json

# 4. Abra o notebook
jupyter notebook notebooks/notebook_atualizado.ipynb
```

Ou no **Google Colab**: faça upload do `.ipynb` e do dataset, ajuste o caminho do arquivo na célula 2.

---

## ▶️ Como Executar o App Streamlit

```bash
# Certifique-se de que model/modelo_final.joblib existe (rode o notebook antes)
streamlit run app.py
```

O app abre automaticamente em `http://localhost:8501`.

---

## ⚠️ Limitações

- O modelo foi treinado em manchetes do HuffPost (inglês) — pode ter desempenho reduzido em outros veículos
- O desbalanceamento entre POLITICS (~35k) e TRAVEL/STYLE & BEAUTY (~9k) foi tratado com `class_weight='balanced'`, mas ainda impacta a performance nas classes menores
- Algumas categorias do dataset original são muito similares (ex: TASTE e FOOD & DRINK) — a seleção das top 5 minimizou esse problema
- Bigramas melhoram a captura de contexto, mas modelos de linguagem pré-treinados (BERT) poderiam capturar semântica mais profunda

---

## 🏁 Conclusão

O LinearSVC com TF-IDF demonstrou ser a melhor abordagem para este problema, combinando alto desempenho com eficiência computacional. A adição de `class_weight='balanced'` melhorou especialmente o F1-Score das classes minoritárias. O Pipeline sklearn garante que todo o pré-processamento seja aplicado de forma consistente tanto no treino quanto na inferência do app.

---

*Desafio 18 — Curso A.I. Classificadores | Grupo 18 | UNIMAR 2026*
