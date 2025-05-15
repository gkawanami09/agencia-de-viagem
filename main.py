from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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