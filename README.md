# 🧬 Tech Challenge – Fase 1

## Classificação de Câncer de Mama com Machine Learning

Este projeto foi desenvolvido como parte do **Tech Challenge – Fase 1 (FIAP Pós-Tech)**, com o objetivo de aplicar conceitos de **Aprendizado de Máquina** na resolução de um problema de **classificação supervisionada** voltado ao diagnóstico de câncer de mama. A **Regressão Logística** é adotada como **modelo principal**, por sua interpretabilidade e ampla utilização em problemas de saúde, enquanto outros algoritmos são explorados apenas para **comparação de desempenho**.

A aplicação utiliza **Docker** para garantir **padronização do ambiente**, **reprodutibilidade dos resultados** e **facilidade de execução** em diferentes sistemas operacionais.

## 🎯 Objetivo do Projeto

O diagnóstico precoce do câncer de mama é fundamental para aumentar as chances de tratamento eficaz e reduzir a mortalidade.

Neste contexto, o projeto tem como objetivo:

* Construir um **modelo de classificação binária** (Benigno × Maligno);
* Aplicar a **Regressão Logística** como **modelo principal** do projeto;
* Realizar **análise exploratória e pré-processamento dos dados**;
* Avaliar o desempenho do modelo com métricas adequadas ao contexto de saúde, com **ênfase em Recall (Sensibilidade)**.

## 🧠 Abordagem Metodológica

O projeto contempla as seguintes etapas:

1. **Análise exploratória dos dados (EDA)**
2. **Pré-processamento** (limpeza, imputação de valores ausentes e padronização)
3. **Treinamento do modelo de Regressão Logística** como abordagem central
4. **Comparação exploratória com outros algoritmos de classificação** (KNN, Árvore de Decisão e Random Forest), utilizada apenas como apoio analítico
5. **Avaliação do modelo**, com ênfase em métricas adequadas ao contexto clínico, especialmente **Recall (Sensibilidade)**
6. **Inferência em novos dados**

O relatório completo da análise está documentado no notebook disponível na pasta `notebooks/`.

## 🗂 Estrutura do Projeto

```text
cancer-breast-logistic-ml/
├── data/
│   ├── data.csv                 # Dataset do Kaggle (obrigatório)
│   └── entrada_exemplo.csv      # Exemplo de dados para inferência
│
├── notebooks/
│   └── relatorio_tech_challenge_fase1.ipynb
│
├── src/
│   └── train.py                 # Script de treinamento do modelo
│
├── artifacts/
│   └── model.joblib             # Modelo treinado
│
├── main.py                      # Script de inferência
├── requirements.txt
├── Dockerfile
└── README.md
```

## ⚙️ Requisitos

### 🔹 Execução com Docker

* Docker **20.x** ou superior
* Docker Compose (opcional)

### 🔹 Execução sem Docker (opcional)

* Python **3.9+**
* Jupyter Notebook
* Bibliotecas listadas em `requirements.txt`

## 🐳 Como Executar o Projeto com Docker

### 1️⃣ Clonar o repositório

```bash
git clone <url-do-repositorio>
cd cancer-breast-logistic-ml
```

### 2️⃣ Build da imagem Docker

```bash
docker build -t cancer-breast-ml .
```

### 3️⃣ Treinar o modelo

O comando abaixo executa o treinamento e salva o modelo treinado em `artifacts/model.joblib`.

**Windows (PowerShell):**

```bash
docker run --rm -v ${PWD}:/app cancer-breast-ml python src/train.py --out artifacts/model.joblib
```

**Linux / macOS:**

```bash
docker run --rm -v "$(pwd)":/app cancer-breast-ml python src/train.py --out artifacts/model.joblib
```

### 4️⃣ Inferência (uso do modelo treinado)

Gera o arquivo `predicoes.csv` a partir de um conjunto de dados de entrada.

**Windows (PowerShell):**

```bash
docker run --rm -v ${PWD}:/app cancer-breast-ml python main.py \
  --model artifacts/model.joblib \
  --input data/entrada_exemplo.csv \
  --output predicoes.csv
```

**Linux / macOS:**

```bash
docker run --rm -v "$(pwd)":/app cancer-breast-ml python main.py \
  --model artifacts/model.joblib \
  --input data/entrada_exemplo.csv \
  --output predicoes.csv
```

### 5️⃣ Execução do Jupyter Notebook (opcional)

```bash
docker compose up --build
```

Acesse no navegador:
👉 [http://localhost:8888/lab/](http://localhost:8888/lab/)

Abra o notebook:

📘 `relatorio_tech_challenge_fase1.ipynb`
Execute as células **em ordem sequencial**.

## 🧾 Saída Esperada

### 🔹 Treinamento

* Impressão das métricas de avaliação:

    * `classification_report`
    * Recall (Sensibilidade)
    * AUC (quando aplicável)
* Modelo salvo em:

  ```text
  artifacts/model.joblib
  ```

### 🔹 Inferência

* Geração do arquivo:

  ```text
  predicoes.csv
  ```
* Colunas geradas:

    * `pred_maligno` (0 = Benigno | 1 = Maligno)
    * `pred_label` (Benigno / Maligno)
    * `proba_maligno` (probabilidade estimada, se disponível)

## 📚 Referências

* Dataset: *Breast Cancer Wisconsin (Diagnostic) Data Set*
  [https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data)

* James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013).
  *An Introduction to Statistical Learning.*

* Géron, A. (2019).
  *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.*

* Fávero, L. P., & Belfiore, P. (2024).
  *Manual de análise de dados: estatística e machine learning.* Elsevier.
