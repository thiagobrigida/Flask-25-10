from flask import Blueprint, render_template, request, redirect, flash
from models import Pizza
from database import db

bp_pizza = Blueprint('pizzas', __name__, template_folder="templates")

@bp_pizza.route('/')
def index():
    dados = Pizza.query.all()
    return render_template('pizza.html', pizzas = dados)

@bp_pizza.route('/add')
def add():
    return render_template('pizza_add.html')

@bp_pizza.route('/save', methods=['POST'])
def save():
    sabor = request.form.get('sabor')
    ingredientes = request.form.get('ingredientes')
    preco = request.form.get('preco')
    if sabor and ingredientes and preco:
        bd_pedido = Pizza(sabor, ingredientes, preco)
        db.session.add(bd_pedido)
        db.session.commit()
        flash('Pizza salva com sucesso!!')
        return redirect('/pizzas')
    else:
        flash('Preencha todos os campos!!')
        return redirect('/pizzas/add')
