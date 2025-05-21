from flask import Blueprint, render_template, request
import pandas as pd
from src.utils.file_reader import read_csv

comparacao_bp = Blueprint('comparacao', __name__)

@comparacao_bp.route('/comparacao', methods=['GET', 'POST'])
def comparacao():
    if request.method == 'POST':
        # Handle file upload
        uploaded_file = request.files['file']
        if uploaded_file and uploaded_file.filename.endswith('.csv'):
            # Read the CSV file
            data = read_csv(uploaded_file)
            # Perform comparison logic here
            comparison_results = perform_comparison(data)
            return render_template('resultados.html', results=comparison_results)
    return render_template('comparacao.html')

def perform_comparison(data):
    # Placeholder for comparison logic
    # This function should implement the logic to compare the invoice data with market data
    return data  # Return the processed comparison results for now