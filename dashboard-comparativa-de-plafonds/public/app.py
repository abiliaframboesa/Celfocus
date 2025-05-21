import streamlit as st
import pandas as pd
from huggingface_hub import InferenceClient

def compare_plans(user_invoice, all_plans):
    user_plan = user_invoice.iloc[0]
    user_price = user_plan['Price']
    user_internet = user_plan['Internet Speed (GB)']
    user_tv = user_plan['TV Usage (hours)']
    user_mobile = user_plan['Mobile Data (GB)']

    # Garantir que os dados dos planos também estão limpos
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
    st.title("Home Page")
    st.write("Simple UI with clean design")

    # File uploader
    uploaded_file = st.file_uploader("Upload your CSV invoice", type="csv")

    # Add a second file uploader for the plans CSV
    plans_file = st.file_uploader("Upload the CSV with all plans", type="csv", key="plans")

    if st.button("Submit"):
        if uploaded_file is not None and plans_file is not None:
            try:
                # Read the uploaded CSV files
                user_invoice = pd.read_csv(uploaded_file)
                all_plans = pd.read_csv(plans_file)

                # Ensure required columns exist in both CSVs
                required_invoice_columns = ['Price', 'Internet Usage (GB)', 'TV Usage (hours)', 'Mobile Data Usage (GB)']
                required_plans_columns = ['Price', 'Internet Speed (GB)', 'TV Channels', 'Mobile Data (GB)']

                if not all(col in user_invoice.columns for col in required_invoice_columns):
                    st.error("The uploaded invoice CSV is missing required columns. Please check the file format.")
                    return

                if not all(col in all_plans.columns for col in required_plans_columns):
                    st.error("The uploaded plans CSV is missing required columns. Please check the file format.")
                    return

                # Align column names for compatibility
                user_invoice.rename(columns={
                    'Internet Usage (GB)': 'Internet Speed (GB)',
                    'Mobile Data Usage (GB)': 'Mobile Data (GB)'
                }, inplace=True)

                st.success("Files uploaded successfully!")
                st.write("Preview of your invoice data:")
                st.dataframe(user_invoice.head())

                st.write("Preview of all plans data:")
                st.dataframe(all_plans.head())

                # Compare plans
                best_plan = compare_plans(user_invoice, all_plans)

                if best_plan is not None:
                    st.write("The best plan for you is:")
                    st.dataframe(best_plan)

                    # Geração de explicação com LLM
                    descricao = gerar_descricao_plano(user_invoice.iloc[0], best_plan)
                    st.markdown("### Explicação do plano recomendado:")
                    st.write(descricao)

                else:
                    st.write("No suitable plan found that matches or exceeds your current benefits.")


            except Exception as e:
                st.error(f"An error occurred while processing the files: {e}")
        else:
            st.error("Please upload both the invoice and plans CSV files before submitting.")

def gerar_descricao_plano(plano_atual, melhor_plano):
    client = InferenceClient(
        provider="together",
        api_key="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",
    )

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
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content



if __name__ == "__main__":
    main()
