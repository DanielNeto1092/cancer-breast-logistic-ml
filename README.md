🧬 Tech Challenge – Fase 1
Classificação de Câncer de Mama com Machine Learning

Este projeto foi desenvolvido como parte do Tech Challenge – Fase 1, com o objetivo de aplicar conceitos de Aprendizado de Máquina na resolução de um problema de classificação supervisionada, utilizando Regressão Logística para análise de dados relacionados ao câncer de mama.

O projeto utiliza Docker para garantir padronização do ambiente, reprodutibilidade dos resultados e facilidade de execução em diferentes sistemas operacionais.

🎯 Objetivo do Projeto

🎯 Problema

O diagnóstico precoce do câncer de mama é essencial para aumentar as chances de tratamento eficaz.
Neste contexto, o projeto busca construir e avaliar modelos de classificação capazes de auxiliar a decisão clínica, priorizando métricas adequadas para problemas de saúde, como Recall (Sensibilidade).

🗂 Estrutura do Projeto
Machine-Learning-Classification-blue/
│
├── data/
│   ├── data.csv                # Dataset do Kaggle (obrigatório)
│   └── entrada_exemplo.csv     # Exemplo para inferência
│
├── notebooks/
│   └── relatorio_tech_challenge_fase1.ipynb
│
├── src/
│   └── train.py                # Treinamento do modelo
│
├── artifacts/
│   └── model.joblib            # Modelo treinado
│
├── main.py                     # Inferência (uso do modelo)
├── requirements.txt
├── Dockerfile
└── README.md


⚙️ Requisitos

🔹 Para execução com Docker (recomendado)

Docker 20.x ou superior

Docker Compose (se utilizado)

🔹 Para execução sem Docker (opcional)

Python 3.9+

Jupyter Notebook

Bibliotecas listadas em requirements.txt

🐳 Como Executar o Projeto com Docker (Recomendado)

1️⃣ Clonar ou baixar o projeto
git clone <url-do-repositorio>
cd tech-challenge-fase1

2️⃣ Build da imagem Docker

```bash
    docker build -t tech-challenge-ml .
    docker run --rm -v %cd%/artifacts:/app/artifacts tech-challenge-ml python src/train.py --out artifacts/model.joblib
    docker run --rm -v %cd%:/app tech-challenge-ml python main.py --model artifacts/model.joblib --input data/entrada_exemplo.csv --output data/predicoes.csv
```
> No Linux/Mac troque `%cd%` por `$(pwd)`.

3️⃣ Executar o container

```bash
  docker compose up --build
```


Abra o link http://localhost:8888/lab/tree/ no navegador.

4️⃣ Abrir o notebook

No Jupyter, abra:

📘 relatorio_tech_challenge_fase1.ipynb

Execute as células em ordem sequencial.


👥 Equipe

Este projeto foi desenvolvido pelo Grupo 56 como parte do Tech Challenge FIAP Pós-Tech:

Araguacy Bezerra Pereira
Emerson Vitorio de Oliveira
Robson Carvalho Calixto
Vinicius Fernando M. Costa


📚 Referências

Dataset: [Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data)

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). An Introduction to Statistical Learning

Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow

FÁVERO, Luiz Paulo; BELFIORE, Patrícia. Manual de análise de dados: estatística e machine learning 2. ed. Rio de Janeiro: Elsevier, 2024