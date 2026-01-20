🧬 Tech Challenge – Fase 1
Classificação de Câncer de Mama com Machine Learning (Ambiente Docker)

Este projeto foi desenvolvido como parte do Tech Challenge – Fase 1, com o objetivo de aplicar conceitos de Aprendizado de Máquina na resolução de um problema de classificação supervisionada, utilizando Regressão Logística para análise de dados relacionados ao câncer de mama.

O projeto utiliza Docker para garantir padronização do ambiente, reprodutibilidade dos resultados e facilidade de execução em diferentes sistemas operacionais.

🎯 Objetivo do Projeto

Aplicar técnicas de Machine Learning em um problema real de classificação

Utilizar boas práticas de pré-processamento de dados

Treinar e avaliar um modelo supervisionado

Garantir reprodutibilidade por meio de ambiente containerizado (Docker)

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

🧠 Metodologia

Separação dos dados em treino e teste

Normalização das variáveis com StandardScaler

Treinamento do modelo de Regressão Logística

Uso de Pipeline para garantir consistência no pré-processamento

Avaliação do desempenho com métricas estatísticas

📊 Avaliação do Modelo

Acurácia

Matriz de confusão

Relatório de classificação

Essas métricas permitem avaliar a qualidade do modelo de classificação.