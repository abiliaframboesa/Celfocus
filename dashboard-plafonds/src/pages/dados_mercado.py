from flask import Blueprint, render_template
import requests

dados_mercado_bp = Blueprint('dados_mercado', __name__)

@dados_mercado_bp.route('/dados-mercado')
def dados_mercado():
    # Aqui você pode adicionar a lógica para buscar dados de mercado
    # Exemplo: dados = requests.get('URL_DA_API').json()
    dados = {}  # Substitua por dados reais

    return render_template('dados_mercado.html', dados=dados)