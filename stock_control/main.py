from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

#SECTION - CONFIGURAÇÃO DO BANCO DE DADOS E LOGIN
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


#SECTION - MODELOS DO BANCO DE DADOS
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

#NOTE - EXECUTAR APENAS UMA VEZ PARA CRIAR O BANCO DE DADOS E AS TABELAS
"""with app.app_context():
    db.create_all()"""

#SECTION - ROTAS
#ANCHOR - CARREGAR USUÁRIO
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#ANCHOR - ROTA DE LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Credenciais inválidas', 'danger')
    return render_template('login.html')


#ANCHOR - ROTA DE LOGOUT
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


#ANCHOR - ROTA DE REGISTRO
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')


#ANCHOR - ROTA PRINCIPAL
@app.route('/')
@login_required
def dashboard():
    return render_template('index.html', username=current_user.username)

#SECTION - EXECUÇÃO DO APP
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
