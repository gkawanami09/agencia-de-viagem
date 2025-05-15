from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    desconto = None
    if request.method == 'POST':
        email = request.form.get('email')
        if email and email.endswith('@gmail.com'):
            desconto = 'Você ganhou 10% de desconto! Confira seu e-mail.'
        else:
            desconto = 'Insira um e-mail válido do Gmail para receber o desconto.'
    return render_template('index.html', desconto=desconto)

@app.route('/serra-do-cipo')
def serra_do_cipo():
    return render_template('/serra-do-cipo.html')

@app.route('/depoimentos')
def depoimentos():
    return render_template('depoimentos.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)