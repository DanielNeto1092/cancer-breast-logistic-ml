# Imagem enxuta e estável
FROM python:3.11-slim

# Evita prompts e melhora logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Define a pasta de trabalho
WORKDIR /app

# Dependências do sistema (opcional, mas ajuda com builds de wheels)
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential \
 && rm -rf /var/lib/apt/lists/*

# Instala dependências Python primeiro (melhora cache de build)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . .

# Porta padrão do Jupyter
EXPOSE 8888

# Por padrão, sobe o JupyterLab
# - Sem token/senha por padrão (use apenas em rede local) 
# - Para produção, prefira configurar token/senha/https
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=", "--NotebookApp.password="]
