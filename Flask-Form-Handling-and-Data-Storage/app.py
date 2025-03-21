from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy
import csv
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.Text, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        age = request.form.get('age')
        gender = request.form.get('gender')
        address = request.form.get('address')

        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "Error: Email already exists!", 400

        if not name or not email or not phone or not age or not gender or not address:
            return "All fields are required", 400

        new_user = User(name=name, email=email, phone=phone, age=int(age), gender=gender, address=address)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users'))
    return render_template('index.html')

@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

@app.route('/download_csv')
def download_csv():
    users = User.query.all()
    file_path = 'users.csv'
    
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['ID', 'Name', 'Email', 'Phone', 'Age', 'Gender', 'Address'])
        for user in users:
            csv_writer.writerow([user.id, user.name, user.email, user.phone, user.age, user.gender, user.address])
    
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)