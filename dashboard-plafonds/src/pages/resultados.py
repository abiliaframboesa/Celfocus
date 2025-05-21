from flask import Blueprint, render_template, request
import pandas as pd

resultados_bp = Blueprint('resultados', __name__)

@resultados_bp.route('/resultados', methods=['GET', 'POST'])
def resultados():
    if request.method == 'POST':
        # Assuming the comparison results are stored in a DataFrame
        comparison_results = pd.DataFrame()  # Replace with actual comparison logic
        
        # Render the results in a template
        return render_template('resultados.html', results=comparison_results.to_html(classes='table table-striped'))

    return render_template('resultados.html', results=None)