from flask import Blueprint, request, render_template
import pandas as pd

leitura_faturas_bp = Blueprint('leitura_faturas', __name__)

@leitura_faturas_bp.route('/leitura_faturas', methods=['GET', 'POST'])
def leitura_faturas():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            df = pd.read_csv(file)
            # Process the invoice data as needed
            # For example, you can extract relevant columns or perform calculations
            return render_template('leitura_faturas.html', data=df.to_html())
    return render_template('leitura_faturas.html', data=None)