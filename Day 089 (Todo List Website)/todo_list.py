from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    todos.append(todo)
    return render_template('index.html', todos=todos)

@app.route('/delete/<int:index>')
def delete_todo(index):
    if index < len(todos):
        del todos[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
