# 📊 DataPilot AI

### Assistente inteligente para análise de dados com Inteligência Artificial

O **DataPilot AI** é um projeto em desenvolvimento que busca transformar planilhas e arquivos de dados em informações úteis para a tomada de decisões.

A proposta é permitir que usuários enviem arquivos CSV ou Excel e façam perguntas em linguagem natural sobre seus dados. Por meio de ferramentas de análise, processamento de dados e agentes de Inteligência Artificial, o sistema deverá interpretar solicitações, executar análises e apresentar resultados de maneira clara e visual.

> 🚧 **Status:** MVP em desenvolvimento — módulo inicial de análise de dados implementado.

---

## 🎯 Objetivo

Facilitar a análise de dados de vendas e operações, permitindo que usuários obtenham informações estratégicas sem precisar construir manualmente fórmulas complexas, consultas ou tabelas dinâmicas.

O projeto também tem como objetivo explorar a integração entre agentes de IA, processamento de dados e automação de tarefas, tornando a análise de informações mais acessível e intuitiva.

## 🚀 Funcionalidades

### Implementado
- [x] Estrutura inicial do projeto.
- [x] Configuração do ambiente Python.
- [x] Interface interativa utilizando Streamlit.
- [x] Carregamento de arquivos CSV.
- [x] Validação das colunas necessárias.
- [x] Pré-visualização dos dados carregados.
- [x] Processamento e análise de dados utilizando Pandas.
- [x] Cálculo do faturamento total.
- [x] Identificação do produto mais vendido por quantidade.
- [x] Identificação do vendedor com maior faturamento.
- [x] Cálculo da quantidade total de unidades vendidas.
- [x] Análise de faturamento por categoria.
- [x] Cálculo da participação percentual de cada categoria no faturamento.
- [x] Visualização de dados com gráficos interativos utilizando Plotly.

### Em desenvolvimento
- [ ] Aprimoramento da validação e do tratamento de dados.
- [ ] Implementação de novos indicadores e ferramentas de análise.
- [ ] Melhorias na interface e experiência do usuário.
- [ ] Organização e expansão dos módulos de processamento.

### Planejado
- [ ] Suporte ao carregamento e processamento de arquivos Excel (.xlsx).
- [ ] Integração com API de modelos de Inteligência Artificial.
- [ ] Desenvolvimento de um agente inteligente com Tool Calling / Function Calling.
- [ ] Consultas aos dados utilizando linguagem natural.
- [ ] Geração de relatórios executivos.
- [ ] Exportação dos resultados das análises.
- [ ] Expansão do suporte a diferentes formatos de arquivos e fontes de dados.

## 🛠️ Tecnologias

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal |
| Streamlit | Interface da aplicação |
| Pandas | Processamento e análise de dados |
| Plotly | Criação de gráficos interativos |
| Git e GitHub | Versionamento e documentação |
| Gemini API | Integração com modelos de IA (planejada) |

## 📂 Estrutura do projeto

```text
datapilot-ai/
│
├── .agents/
├── .claude/
├── data/
│   └── exemplo_vendas.csv
│
├── src/
│   └── data_processor.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

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

O desenvolvimento será realizado de maneira incremental, priorizando a construção de um MVP funcional e a evolução gradual de suas capacidades.

As próximas etapas incluem:

1. Aprimorar as ferramentas de processamento e análise de dados.
2. Expandir o suporte para arquivos Excel e outros formatos de planilhas.
3. Desenvolver novas funcionalidades e indicadores de análise.
4. Integrar um modelo de Inteligência Artificial ao sistema.
5. Desenvolver um agente capaz de interpretar solicitações e utilizar ferramentas de análise por meio de Tool Calling.
6. Implementar consultas em linguagem natural e geração de relatórios.

## 👨‍💻 Autor

**Caio Guilherme Araújo Sousa**

Estudante de Bacharelado em Ciência da Computação — Instituto Federal do Maranhão (IFMA), Campus Imperatriz.

- [GitHub](https://github.com/CaioAraujoSousa)
- [LinkedIn](https://www.linkedin.com/in/caioaraújosousa)

---

*Projeto acadêmico e experimental desenvolvido com o objetivo de explorar aplicações práticas de Inteligência Artificial, análise de dados e desenvolvimento de soluções digitais.*
