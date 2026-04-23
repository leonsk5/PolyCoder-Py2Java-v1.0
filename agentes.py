import os
from groq import Groq
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

# --- CONFIGURAÇÕES ---
# Coloque suas chaves aqui ou use variáveis de ambiente
os.environ["GROQ_API_KEY"] = "SUA_API_KEY_GROQ"
client = Groq()

# Inicializa o modelo de memória (Embeddings)
model_embed = SentenceTransformer('all-MiniLM-L6-v2')

# Inicializa o cliente Qdrant
qdrant_client = QdrantClient(
    url="URL_QDRANT", 
    api_key="API_KEY_QDRANT"
)

# --- FUNÇÃO 1: O GERADOR (Cérebro) ---
def agent_generator(prompt_com_contexto):
    system_prompt = """
    Você é o PolyCoder, especialista em Java 17. 
    Converta o Python para Java com tipagem estática e Javadoc. 
    Retorne o código dentro de uma classe 'Main'.
    """
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt_com_contexto}
        ],
        temperature=0.1
    )
    return completion.choices[0].message.content

# --- FUNÇÃO 2: O VALIDADOR (Inspetor) ---
def agent_validator(java_code):
    system_prompt = """
    Você é um Inspetor de Código. Verifique se o Java tem erros de sintaxe (';', '{}', tipos).
    Responda 'APROVADO' ou descreva os erros.
    """
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": java_code}
        ],
        temperature=0.1
    )
    return completion.choices[0].message.content

# --- FUNÇÃO 3: O ORQUESTRADOR (O que o app.py chama) ---
def polycoder_com_memoria(codigo_python):
    try:
        vetor = model_embed.encode(codigo_python).tolist()
        busca = qdrant_client.search(
            collection_name="regras_transpilacao",
            query_vector=vetor,
            limit=1
        )
        # Se achar regra, usa. Se não, apenas diz para seguir o padrão Java.
        contexto = f"Regra específica: {busca[0].payload['regra']}" if busca else "Siga as melhores práticas padrão do Java 17."
    except Exception as e:
        # Se der erro no Qdrant, não assuste a IA. Apenas diga para ela prosseguir normalmente.
        contexto = "Tradução padrão: use a sintaxe nativa do Java 17."

    prompt_final = f"""
    CONTEXTO TÉCNICO: {contexto}
    
    TAREFA: Converta o código abaixo seguindo o contexto acima.
    CÓDIGO PYTHON:
    {codigo_python}
    """
    
    return agent_generator(prompt_final)
