import streamlit as st
import requests

st.set_page_config(page_title="Comparador de Tarifários", layout="centered")
st.title("📡 Comparador Inteligente de Tarifários")
st.write("Faça upload da sua fatura em CSV e descubra o melhor plano disponível para si.")

# Upload do ficheiro
uploaded_file = st.file_uploader("🧾 Envie a sua fatura (formato CSV)", type="csv")

if st.button("🔍 Analisar Plano"):
    if uploaded_file is not None:
        with st.spinner("A analisar o seu plano atual..."):
            try:
                # Enviar o ficheiro para o backend FastAPI
                response = requests.post(
                    "http://localhost:8000/analisar/",
                    files={"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}
                )

                if response.status_code == 200:
                    data = response.json()

                    if data.get("success"):
                        st.success("🎯 Plano ideal encontrado!")

                        st.markdown("### ✅ Plano Recomendado:")
                        st.json(data["melhor_plano"])

                        st.markdown("### 💬 Explicação:")
                        st.write(data["explicacao"])
                    else:
                        st.warning(data.get("message", "Nenhum plano adequado foi encontrado."))
                else:
                    st.error("Erro ao contactar o servidor. Verifique se o backend está ativo.")
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")
    else:
        st.warning("Por favor, envie o ficheiro da fatura.")
