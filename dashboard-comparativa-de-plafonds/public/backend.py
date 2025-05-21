from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from huggingface_hub import InferenceClient

app = FastAPI()

# Permitir que o frontend (Streamlit) aceda à API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, defina o domínio correto
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar CSV dos planos uma vez
ALL_PLANS = pd.read_csv("plafonds_examples.csv")  # <-- ajuste o caminho

# Função para comparar planos
def compare(user_invoice: pd.DataFrame):
    user_plan = user_invoice.iloc[0]
    user_price = user_plan['Price']
    user_internet = user_plan['Internet Speed (GB)']
    user_tv = user_plan['TV Usage (hours)']
    user_mobile = user_plan['Mobile Data (GB)']

    suitable_plans = ALL_PLANS[
        (ALL_PLANS['Internet Speed (GB)'] >= user_internet) &
        (ALL_PLANS['TV Channels'] >= user_tv) &
        (ALL_PLANS['Mobile Data (GB)'] >= user_mobile)
    ]

    best_plan = suitable_plans.loc[suitable_plans['Price'].idxmin()] if not suitable_plans.empty else None
    return best_plan


# Gerar explicação com LLM
def gerar_descricao(plano_atual, melhor_plano):
    client = InferenceClient(provider="together", api_key="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")
    prompt = f"""
Plano atual:
- Preço: {plano_atual['Price']}€
- Internet: {plano_atual['Internet Speed (GB)']} GB
- TV: {plano_atual['TV Usage (hours)']}h
- Dados móveis: {plano_atual['Mobile Data (GB)']} GB

Plano recomendado:
- {melhor_plano['Provider']}
- {melhor_plano['Price']}€
- {melhor_plano['Internet Speed (GB)']} GB internet
- {melhor_plano['TV Channels']} canais
- {melhor_plano['Mobile Data (GB)']} GB móveis

Explica por que o plano recomendado é melhor.
"""
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


@app.post("/analisar/")
async def analisar_fatura(file: UploadFile = File(...)):
    try:
        user_invoice = pd.read_csv(file.file)
        user_invoice.rename(columns={
            'Internet Usage (GB)': 'Internet Speed (GB)',
            'Mobile Data Usage (GB)': 'Mobile Data (GB)'
        }, inplace=True)

        best_plan = compare(user_invoice)
        if best_plan is None:
            return {"success": False, "message": "Nenhum plano adequado foi encontrado."}

        descricao = gerar_descricao(user_invoice.iloc[0], best_plan)
        return {
            "success": True,
            "melhor_plano": best_plan.to_dict(),
            "explicacao": descricao
        }

    except Exception as e:
        return {"success": False, "error": str(e)}
