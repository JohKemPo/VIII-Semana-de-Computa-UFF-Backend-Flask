from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar as tarefas (em memória)
todo_list = []

# ola mundo!
@app.route('/home')
def home():
    return "Olá, Flask!"

# exibição de informação passada por url
@app.route('/usuario/<nome>')
def ola_usuario(nome):
    return f"Olá, {nome}!"

# exibição de informação passada por url
@app.route('/usuario_args')
def ola_usuario_args():
    nome = request.args.get('nome')
    return f"Olá, {nome}!"


# Página inicial que lista as tarefas
@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

# Rota para adicionar uma nova tarefa
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todo_list.append({'task': task, 'done': False})
    return redirect(url_for('index'))

# Rota para marcar uma tarefa como concluída
@app.route('/complete/<int:task_id>')
def complete(task_id):
    if 0 <= task_id < len(todo_list):
        todo_list[task_id]['done'] = True
    return redirect(url_for('index'))

# Rota para remover uma tarefa
@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(todo_list):
        todo_list.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)
