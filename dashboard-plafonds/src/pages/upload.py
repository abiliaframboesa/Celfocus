from flask import Blueprint, request, render_template, redirect, url_for, flash
import pandas as pd
import os

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join('uploads', filename)
            file.save(file_path)
            # Process the CSV file
            data = pd.read_csv(file_path)
            # Further processing can be done here
            return redirect(url_for('home'))
        else:
            flash('Invalid file format. Please upload a CSV file.')
            return redirect(request.url)
    return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'csv'