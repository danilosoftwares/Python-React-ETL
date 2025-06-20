# 🧩 Projeto de Importação de CSV em Ambiente Monolítico

Este projeto é uma aplicação monolítica composta por:

- **Backend** em Python (FastAPI, Django ou Flask, conforme o caso)
- **Frontend** em React
- **Banco de Dados** PostgreSQL
- **Mensageria** via RabbitMQ
- **Infraestrutura** orquestrada com Docker Compose
- **CDN** embutido para servir a aplicação frontend

O objetivo principal da aplicação é realizar **importações de arquivos CSV extensos**, com mais de **900 mil linhas**, de forma performática, confiável e integrada.

---

## 🛠️ Tecnologias Utilizadas

### 1. Backend (Python)
- Framework: FastAPI / Django / Flask *(especifique conforme seu caso)*
- Manipulação de arquivos CSV pesados
- Integração com RabbitMQ para processamento assíncrono
- Comunicação com PostgreSQL para persistência dos dados

### 2. Frontend (React)
- Interface de upload e monitoramento de progresso do arquivo
- Feedback em tempo real de status via websocket ou polling
- Aplicação servida via CDN local criada no ambiente dockerizado

### 3. Banco de Dados (PostgreSQL)
- Armazena os dados extraídos do CSV
- Estrutura relacional otimizada para performance de escrita em massa

### 4. Mensageria (RabbitMQ)
- Gerencia as tarefas de importação de forma assíncrona
- Garante escalabilidade no processamento dos dados

### 5. Docker / Docker Compose
- Todo o ambiente é isolado e reproduzível com `docker compose`
- Contêineres definidos:
  - `backend`: API Python
  - `frontend`: Aplicação React
  - `db`: PostgreSQL
  - `rabbitmq`: Servidor de mensagens
  - `cdn`: Servidor estático (ex: nginx) para servir o frontend

---

## 🚀 Como Subir a Aplicação

Subir a stack completa é simples e requer apenas o Docker instalado em sua máquina.

```bash
docker compose up --build
```

## Demo
![](demonstracao.gif)