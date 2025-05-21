import streamlit as st
import pandas as pd
from huggingface_hub import InferenceClient

# --- Estilização com CSS ---
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .title {
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            color: #f0f2f6;
            margin-bottom: 0;
        }
        .slogan {
            font-size: 1.2em;
            text-align: center;
            color: #888;
            font-style: italic;
            margin-bottom: 2em;
        }
        .upload-section {
            margin-top: 2em;
        }
        .stButton>button {
            background-color: #0D3B66;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1.5em;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

def compare_plans(user_invoice, all_plans):
    user_plan = user_invoice.iloc[0]
    user_price = user_plan['Price']
    user_internet = user_plan['Internet Speed (GB)']
    user_tv = user_plan['TV Usage (hours)']
    user_mobile = user_plan['Mobile Data (GB)']

    all_plans['Price'] = pd.to_numeric(all_plans['Price'], errors='coerce')
    all_plans['Internet Speed (GB)'] = pd.to_numeric(all_plans['Internet Speed (GB)'], errors='coerce')
    all_plans['TV Channels'] = pd.to_numeric(all_plans['TV Channels'], errors='coerce')
    all_plans['Mobile Data (GB)'] = pd.to_numeric(all_plans['Mobile Data (GB)'], errors='coerce')

    suitable_plans = all_plans[
        (all_plans['Internet Speed (GB)'] >= user_internet) &
        (all_plans['TV Channels'] >= user_tv) &
        (all_plans['Mobile Data (GB)'] >= user_mobile)
    ]

    best_plan = suitable_plans.loc[suitable_plans['Price'].idxmin()] if not suitable_plans.empty else None
    return best_plan


def main():
    # Título e slogan
    st.markdown('<div class="title">TelePlan</div>', unsafe_allow_html=True)
    st.markdown('<div class="slogan">stop over paying, find the perfect plan!</div>', unsafe_allow_html=True)

    # Upload de arquivos
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("📄 Upload your **invoice CSV**", type="csv")
    plans_file = st.file_uploader("📑 Upload the **available plans CSV**", type="csv", key="plans")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔍 Submit"):
        if uploaded_file is not None and plans_file is not None:
            try:
                user_invoice = pd.read_csv(uploaded_file)
                all_plans = pd.read_csv(plans_file)

                required_invoice_columns = ['Price', 'Internet Usage (GB)', 'TV Usage (hours)', 'Mobile Data Usage (GB)']
                required_plans_columns = ['Price', 'Internet Speed (GB)', 'TV Channels', 'Mobile Data (GB)']

                if not all(col in user_invoice.columns for col in required_invoice_columns):
                    st.error("❌ The invoice CSV is missing required columns.")
                    return
                if not all(col in all_plans.columns for col in required_plans_columns):
                    st.error("❌ The plans CSV is missing required columns.")
                    return

                user_invoice.rename(columns={
                    'Internet Usage (GB)': 'Internet Speed (GB)',
                    'Mobile Data Usage (GB)': 'Mobile Data (GB)'
                }, inplace=True)

                st.success("✅ Files uploaded successfully!")
                st.subheader("Your current invoice")
                st.dataframe(user_invoice.head())

                st.subheader("Available plans")
                st.dataframe(all_plans.head())

                best_plan = compare_plans(user_invoice, all_plans)

                if best_plan is not None:
                    st.success("🎯 Best matching plan:")
                    st.dataframe(best_plan.to_frame().T)

                    descricao = gerar_descricao_plano(user_invoice.iloc[0], best_plan)
                    st.markdown("### 📝 Why we recommend this plan:")
                    st.write(descricao)
                else:
                    st.warning("😕 No suitable plan found.")
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
        else:
            st.warning("📌 Please upload both files before submitting.")


def gerar_descricao_plano(plano_atual, melhor_plano):
    client = InferenceClient(provider="together", api_key="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")

    prompt = f"""
Sou um assistente que ajuda clientes a escolher o melhor plano de telecomunicações.

Plano atual do cliente:
- Preço: {plano_atual['Price']}€
- Internet: {plano_atual['Internet Speed (GB)']} GB
- TV: {plano_atual['TV Usage (hours)']} horas
- Dados móveis: {plano_atual['Mobile Data (GB)']} GB

Plano recomendado:
- Provedor: {melhor_plano['Provider']}
- Preço: {melhor_plano['Price']}€
- Internet: {melhor_plano['Internet Speed (GB)']} GB
- Canais de TV: {melhor_plano['TV Channels']}
- Dados móveis: {melhor_plano['Mobile Data (GB)']} GB

Escreve uma explicação clara e amigável sobre por que o plano recomendado é melhor.
"""

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    main()
