from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Email

app = Flask(__name__)
app.secret_key = 'randomstring'


# создаем форму
class OrderForm(FlaskForm):
    name = StringField('Имя', validators=[InputRequired()])
    phone = StringField('Телефон')
    mail = StringField('Email', validators=[Email()])


'''Создание формы и прием данных в разных представлениях
# показываем форму
@app.route('/form/')
def render_form():
    form = OrderForm()
    return render_template('form.html', form=form)


# принимаем форму
@app.route('/save/', methods=['GET', 'POST'])
def render_save():
    # создаем инстанс формы
    form = OrderForm()
    # получаем данные
    name = form.name.data
    phone = form.phone.data
    # выводим данные
    if request.method == 'POST':
        return render_template('save.html', name=name, phone=phone)
    return 'Просто зашли посмотреть'
'''

'''Создание формы и получение данных в одном представлении'''
@app.route('/form/', methods=['GET', 'POST'])
def render_form():
    #create form instance
    form = OrderForm()

    # If data was sent
    # if request.method == 'POST' and form.validate():
    if form.validate_on_submit():
        # get data
        name = form.name.data
        phone = form.phone.data
        mail = form.mail.data

        # render data
        return render_template('save.html', name=name, phone=phone, mail=mail)

    # If no data was sent
    return render_template('form.html', form=form)

app.run(debug=True)
