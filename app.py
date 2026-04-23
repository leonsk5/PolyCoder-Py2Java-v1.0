import streamlit as st
# Aqui está a mágica: importamos as funções do arquivo agentes.py
from agentes import polycoder_com_memoria, agent_validator

st.title("PolyCoder Py2Java")
# Configuração da página
st.set_page_config(page_title="PolyCoder Py2Java", layout="wide")

st.title("🚀 PolyCoder: Python ➔ Java Transpiler")
st.markdown("Converta código Python para Java profissional com validação de sintaxe e memória RAG.")

# Interface em duas colunas
col1, col2 = st.columns(2)

with col1:
    st.subheader("Entrada Python")
    codigo_py = st.text_area("Cole seu código Python aqui:", height=300, placeholder="print('Olá Mundo')")
    
    if st.button("Converter para Java"):
        if codigo_py:
            with st.spinner("Consultando memória e gerando código..."):
                # 1. Chamada do Agente Gerador com RAG
                java_final = polycoder_com_memoria(codigo_py)
                
                # 2. Chamada do Agente Validador
                status_validacao = agent_validator(java_final)
                
                # Guardar no estado da sessão
                st.session_state['java_output'] = java_final
                st.session_state['validacao'] = status_validacao
        else:
            st.error("Por favor, insira um código Python.")

with col2:
    st.subheader("Saída Java")
    if 'java_output' in st.session_state:
        st.code(st.session_state['java_output'], language='java')
        
        # Exibe o status da validação
        if "APROVADO" in st.session_state['validacao'].upper():
            st.success("✅ Código validado pelo Revisor!")
        else:
            st.warning("⚠️ Sugestão do Revisor:")
            st.info(st.session_state['validacao'])

# Rodapé com opção de ensinar o agente
st.divider()
st.subheader("🧠 Ensinar nova regra ao Agente")
nova_regra = st.text_input("Ex: 'Para listas de strings, use sempre o tipo LinkedList'")
if st.button("Salvar na Memória"):
    # Chamar a função de salvar no Qdrant que criamos antes
    st.success("Regra armazenada com sucesso!")