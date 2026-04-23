# PolyCoder-Py2Java-v1.0
````markdown
# 🚀 PolyCoder: Python-to-Java Multi-Agent Transpiler

O **PolyCoder** é um sistema avançado de transpilação de código que utiliza uma arquitetura de múltiplos agentes de IA para converter scripts Python em código Java 17+ robusto, tipado e documentado. 

Diferente de tradutores simples, o PolyCoder utiliza **RAG (Retrieval-Augmented Generation)** para consultar regras de memória e um fluxo de **Chain-of-Verification** para garantir que o código gerado seja sintaticamente correto.

---

## 🧠 Arquitetura do Sistema

O projeto é orquestrado por três componentes fundamentais que trabalham em harmonia:

1.  **O Arquiteto (Llama 3.3-70B via Groq):** O agente principal responsável por entender a lógica Pythonic e mapeá-la para as estruturas de Orientação a Objetos do Java.
2.  **O Inspetor (Llama 3.1-8B via Groq):** Um agente especializado em revisão de sintaxe. Ele verifica pontos-e-vírgulas, fechamento de chaves e coerência de tipos antes da entrega final.
3.  **A Memória (Qdrant Vector DB):** Uma base de dados vetorial que armazena regras customizadas. Se você ensinar ao sistema que uma biblioteca específica do Python deve ser traduzida de uma forma X em Java, ele aprenderá e aplicará isso em todas as conversões futuras.



---

## 🛠️ Stack Tecnológico

Este projeto foi construído focando em performance extrema e custo zero (100% Free Tier):

* **Linguagem:** Python 3.10+
* **LLMs:** Llama 3.3 & 3.1 (via **Groq LPU** para latência quase zero)
* **Vector DB:** **Qdrant Cloud** (Memória de longo prazo)
* **Embeddings:** `all-MiniLM-L6-v2` (Hugging Face)
* **Interface:** **Streamlit**

---

## ⚡ Como Rodar o Projeto

### Pré-requisitos
* Python instalado.
* Chaves de API do [Groq](https://console.groq.com/) e [Qdrant](https://cloud.qdrant.io/).

### Instalação
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/polycoder-py2java.git](https://github.com/seu-usuario/polycoder-py2java.git)
   cd polycoder-py2java
````

2.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3.  Configure suas chaves de API no arquivo `agentes.py` (ou via variáveis de ambiente).

4.  Inicie a interface:

    ```bash
    streamlit run app.py
    ```

-----

## ⚠️ Limitações & Observações (O "Porém")

O projeto utiliza planos gratuitos:

  - **Groq:** Possui limites de requisições por minuto (RPM). Se o limite for atingido, aguarde 60 segundos.
  - **Qdrant:** O cluster gratuito entra em repouso após inatividade prolongada.
  - **Contexto:** A IA pode alucinar em bibliotecas Python muito obscuras sem regras de memória prévias.

-----

## 👨‍💻 Sobre o Autor: Leonardo da Silva Melo

Este projeto faz parte do ecossistema de soluções desenvolvidas por **Leonardo da Silva Melo**, focado em IA Generativa, Automação e Engenharia de Dados.

### Outros Projetos de Destaque:

  * **[Assistente\_IANA](https://www.google.com/search?q=https://github.com/seu-user/Assistente_IANA):** Estudo aprofundado sobre Agentes de IA e fluxos de trabalho autônomos.
  * **[Portifolio26](https://www.google.com/search?q=https://github.com/seu-user/portifolio26):** Showcase de tecnologias web e design focado em UX.
  * **[Estudos-Algoritmos-SUPERVISIONADOS](https://www.google.com/search?q=https://github.com/seu-user/Estudos-Algoritmos-SUPERVISIONADOS):** Pesquisa e implementação dos pilares de Machine Learning Supervisionado.
