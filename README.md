# 📊 DataPilot AI

### Assistente inteligente para análise de dados com Inteligência Artificial

O **DataPilot AI** é um projeto em desenvolvimento que busca transformar planilhas de dados em informações úteis para a tomada de decisões.

A proposta é permitir que usuários enviem arquivos CSV ou Excel e façam perguntas em linguagem natural sobre seus dados. Por meio de ferramentas de análise e agentes de Inteligência Artificial, o sistema deverá interpretar solicitações, executar análises e apresentar resultados de maneira clara e visual.

> 🚧 **Status:** Em desenvolvimento — MVP inicial.

---

## 🎯 Objetivo

Facilitar a análise de dados de vendas e operações, permitindo que usuários obtenham informações estratégicas sem precisar construir manualmente fórmulas complexas, consultas ou tabelas dinâmicas.

O projeto também tem como objetivo explorar a integração entre agentes de IA, processamento de dados e automação de tarefas.

## 🚀 Funcionalidades

### Implementado
- [x] Estrutura inicial do projeto.
- [x] Configuração do ambiente Python.
- [x] Interface inicial utilizando Streamlit.
- [x] Preparação de uma base de dados de exemplo.

### Em desenvolvimento
- [ ] Carregamento e validação de arquivos CSV e Excel.
- [ ] Processamento e análise de dados utilizando Pandas.
- [ ] Cálculo automatizado de indicadores, faturamento, médias e rankings.
- [ ] Integração com API de modelos de Inteligência Artificial.
- [ ] Agente inteligente com Tool Calling / Function Calling.

### Planejado
- [ ] Visualização interativa de dados com Plotly.
- [ ] Consulta aos dados utilizando linguagem natural.
- [ ] Geração de relatórios executivos.
- [ ] Exportação dos resultados das análises.

## 🛠️ Tecnologias

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal |
| Streamlit | Interface da aplicação |
| Pandas | Processamento e análise de dados |
| Plotly | Visualização de dados (planejado) |
| APIs de IA | Integração com modelos de linguagem (planejado) |
| Git e GitHub | Versionamento e documentação |

## 📂 Estrutura do projeto

```text
datapilot-ai/
│
├── .agents/
├── .claude/
├── data/
│   └── exemplo_vendas.csv
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

> O diretório `venv/` é utilizado localmente para o ambiente virtual Python e não deve ser versionado no GitHub.

## ⚙️ Como executar localmente

### 1. Pré-requisitos

- Python 3.11 ou superior.
- Git.
- Editor de código, como VS Code.

### 2. Clonar o repositório

```bash
git clone https://github.com/CaioAraujoSousa/datapilot-ai.git

cd datapilot-ai
```

### 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
venv\Scripts\activate.bat
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a aplicação

```bash
streamlit run app.py
```

A aplicação será disponibilizada localmente pelo Streamlit, normalmente em:

`http://localhost:8501`

## 🗺️ Próximas etapas

O desenvolvimento será realizado de maneira incremental, priorizando a construção de um MVP funcional.

As próximas etapas incluem:

1. Implementar o carregamento e processamento de planilhas.
2. Desenvolver ferramentas de análise de dados com Python.
3. Integrar um agente de IA capaz de utilizar essas ferramentas.
4. Construir um dashboard interativo.
5. Implementar a geração de relatórios.

## 👨‍💻 Autor

**Caio Guilherme Araújo Sousa**

Estudante de Bacharelado em Ciência da Computação — Instituto Federal do Maranhão (IFMA), Campus Imperatriz.

- [GitHub](https://github.com/CaioAraujoSousa)
- [LinkedIn](https://www.linkedin.com/in/caioaraújosousa)

---

*Projeto acadêmico e experimental desenvolvido com o objetivo de explorar aplicações práticas de Inteligência Artificial, análise de dados e desenvolvimento de soluções digitais.*
