# 📊 DataPilot AI — Assistente Inteligente para Análise de Dados

O **DataPilot AI** é um sistema inteligente concebido para transformar planilhas brutas (CSV/Excel) em relatórios estratégicos e respostas claras em linguagem natural. A aplicação utiliza Agentes de IA para interpretar perguntas de negócio, selecionar ferramentas de análise e gerar conclusões visuais automaticamente.

> 🛠️ **Status do Projeto:** Em desenvolvimento (MVP — Dia 01 concluído)

---

## 🎯 Objetivo do Projeto

Permitir que gestores e equipas analisem dados de vendas e operações sem a necessidade de construir fórmulas complexas ou tabelas dinâmicas manuais.

## 🚀 Funcionalidades (Planeadas & Em Implementação)

- [x] Estrutura base da aplicação e interface interativa com Streamlit
- [x] Suporte para carregamento e validação de ficheiros CSV
- [ ] Análise automatizada de dados com Pandas (Faturamento, Rankings e Médias)
- [ ] Agente de IA com *Tool Calling* / *Function Calling*
- [ ] Visualização de dados interativa com Plotly
- [ ] Exportação de relatórios executivos

---

## 💻 Tecnologias Utilizadas

- **Linguagem:** Python 3.11+
- **Interface:** Streamlit
- **Análise de Dados:** Pandas
- **Visualização:** Plotly
- **Orquestração de IA:** API LLM (Gemini / OpenAI)
- **Controlo de Versão:** Git & GitHub

---

## ⚙️ Como Executar o Projeto Localmente

1. **Clona o repositório:**
   ```bash
   git clone [https://github.com/CaioAraujoSousa/datapilot-ai.git](https://github.com/CaioAraujoSousa/datapilot-ai.git)
   cd datapilot-ai
Cria e ativa o ambiente virtual:

Bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
Instala as dependências:

Bash
pip install -r requirements.txt
Executa a aplicação:

Bash
streamlit run app.py
👨‍💻 Autor
Desenvolvido por Caio Guilherme Araújo Sousa

Estudante de Ciência da Computação — IFMA Campus Imperatriz

LinkedIn

GitHub


---

### Passo 2: Enviar o README para o GitHub

Depois de salvar o ficheiro no VS Code, executa estes 3 comandos no terminal:

```bash
git add README.md