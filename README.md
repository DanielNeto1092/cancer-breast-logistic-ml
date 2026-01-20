🧬 Tech Challenge – Fase 1
Classificação de Câncer de Mama com Machine Learning

Este projeto foi desenvolvido como parte do Tech Challenge – Fase 1, com o objetivo de aplicar conceitos de Aprendizado de Máquina na resolução de um problema de classificação supervisionada, utilizando Regressão Logística para análise de dados relacionados ao câncer de mama.

O projeto utiliza Docker para garantir padronização do ambiente, reprodutibilidade dos resultados e facilidade de execução em diferentes sistemas operacionais.

🎯 Objetivo do Projeto

Aplicar técnicas de Machine Learning em um problema real de classificação

Utilizar boas práticas de pré-processamento de dados

Treinar e avaliar um modelo supervisionado

Garantir reprodutibilidade por meio de ambiente containerizado (Docker)

📂 Estrutura do Projeto

O projeto está organizado da seguinte forma:

Notebook:

tech_challenge_fase1_cancer_mama.ipynb:
Consolida a análise exploratória, o pré-processamento dos dados e a implementação e avaliação de um modelo de machine learning para classificação.

Diretórios:

/data: Contém o dataset utilizado no projeto

/notebook: Armazena o notebook Jupyter utilizado no desenvolvimento do projeto.

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
  docker build -t tech-challenge-fase1 .
  docker run --rm -it -p 8888:8888 tech-challenge-fase1
```


3️⃣ Executar o container

```bash
  docker compose up --build
```

Abra o link http://localhost:8888/lab/tree/ no navegador.

4️⃣ Abrir o notebook

No Jupyter, abra:

📘 tech_challenge_fase1_cancer_mama_corrigido.ipynb

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