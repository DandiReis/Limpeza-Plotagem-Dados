# Pipeline de ETL - Tratamento de Dados Salariais de TI 🧹⚙️

Este repositório contém o pipeline de **ETL (Extract, Transform, Load)** desenvolvido para extrair, limpar, traduzir e estruturar dados brutos sobre salários na área de tecnologia. O objetivo principal deste projeto é garantir a qualidade e a consistência dos dados que alimentam a camada de visualização em produção.

---

## 🛠️ Arquitetura do Projeto & Boas Práticas

Seguindo padrões de arquitetura de dados e separação de conceitos (*Separation of Concerns*), este projeto foi desacoplado do aplicativo de visualização. 

**Por que manter o ETL isolado?**
- **Performance:** Evita que a aplicação de visualização consuma processamento limpando dados repetidamente a cada interação do usuário.
- **Escalabilidade:** O pipeline pode ser agendado para rodar periodicamente (ex: via Apache Airflow ou GitHub Actions) de forma totalmente independente da interface de usuário.

O fluxo consome uma base bruta com milhares de registros e gera como saída o arquivo tratado `Dado-Final.csv`, pronto para consumo.

---

## 🔄 Detalhes do Processo de ETL

O script principal `Limpeza.py` executa as seguintes etapas estruturadas:

1. **Extração:** Leitura do dataset bruto contendo informações demográficas e financeiras de profissionais de TI globalmente.
2. **Transformação (Tratamento de Dados):**
   - Tradução e padronização das colunas de cargos (ex: convertendo `"Data Scientist"` para `"Cientista de Dados"`).
   - Conversão e padronização monetária de salários anuais para a moeda de referência (`USD`).
   - Mapeamento e enriquecimento geográfico, convertendo códigos de países de 2 letras (ISO-2) para 3 letras (ISO-3) para garantir a compatibilidade com renderizadores de mapas globais.
   - Tratamento de valores ausentes (*nulls*) e remoção de duplicatas.
3. **Carga:** Exportação da base higienizada de alta fidelidade para o arquivo final `Dado-Final.csv`.

---

## 💻 Tecnologias Utilizadas

- **Python** (Core do script de tratamento)
- **Pandas** (Engenharia de features, manipulação de DataFrames e limpeza)
- **Git/GitHub** (Versionamento de dados e controle de código)

---

## 🚀 Como Executar o Script Localmente

1. Clone o repositório:
   ```bash
   git clone [https://github.com/DandiReis/Limpeza-Plotagem-Dados.git](https://github.com/DandiReis/Limpeza-Plotagem-Dados.git)
   cd Limpeza-Plotagem-Dados

2. Instale as dependencias:]
   pip install pandas numpy matplotlib seaborn plotly pycountry

3. Execute o pipeline de limpeza:
   python Limpeza.py
