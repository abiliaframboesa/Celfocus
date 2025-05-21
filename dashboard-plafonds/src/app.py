from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Handle file upload
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            # Process the uploaded CSV file
            return redirect(url_for('leitura_faturas'))
    return render_template('upload.html')

@app.route('/leitura_faturas')
def leitura_faturas():
    # Logic to read invoices from uploaded CSV
    return render_template('leitura_faturas.html')

@app.route('/dados_mercado')
def dados_mercado():
    # Logic to fetch and display market data
    return render_template('dados_mercado.html')

@app.route('/comparacao')
def comparacao():
    # Logic to compare plafonds
    return render_template('comparacao.html')

@app.route('/resultados')
def resultados():
    # Logic to display comparison results
    return render_template('resultados.html')

if __name__ == '__main__':
    app.run(debug=True)