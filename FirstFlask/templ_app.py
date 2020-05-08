from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test/')
def template():
    mycart = [{"title": "Курс по Python", "price": 8900}, {"title": "Курс португальского языка", "price": 7000},
              {"title": "Подписка на электронные книги", "price": 2400}]
    output = render_template('test.html', name='Oleg', place='Cabinet',
                             role='admin', a=64.554336, b=20.21, mycart=mycart)
    return output

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

app.run()