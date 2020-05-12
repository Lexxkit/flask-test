from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    form = '''
    <form class="search-form" action="/search" method="POST" >
    <input type="text" name="s" />
    <input type="submit" value="Найти" />
    </form>
    '''
    return form


@app.route('/search/', methods=['POST'])
def search():
    s = request.form.get('s')
    return f'<p>Выполняем поиск по {s}</p>'


@app.route('/test2')
def index_test2():
    form = '''
    <h2>Заказать консультацию</h2>
    <form class="request-form" method="POST" action = "/send" >
    <div> <input type="text" name="r_name" /> Имя </div>
    <div> <input type="text" name="r_phone" /> Телефон </div>
    <div> <input type="text" name="r_mail" /> Почта </div>
    <div> <input type="submit" value="Отправить" />  </div>
    </form>
    '''
    return form


@app.route("/send/", methods=['POST'])
def send():
    r_name = request.form.get('r_name')
    r_phone = request.form.get('r_phone')
    r_mail = request.form.get('r_mail')
    return f'Новая заявка от {r_name}, телефон: {r_phone}, почта: {r_mail}'


@app.route('/request')
def index_test3():
    form = '''
    <h2>Платежные данные</h2>
    <form class="card-form" action = "/pay" method="POST">
    <div> <input type="text" name="card_number" /></div>
    <div> 
    <input type="text" name="card_name" />   
    <input type="text" name="card_expires" />  
    </div>
    <div> <input type="text" name="card_cvv2" /></div>
    <div> <input type="submit" value="Оплатить" /></div>
    </form>
    '''
    return form

@app.route('/pay/', methods=['POST'])
def pay():
    card_num = request.form.get('card_number')
    card_name = request.form.get('card_name')
    card_expires = request.form['card_expires']
    card_cvv2 = request.form['card_cvv2']
    return "Карта: {}\nВладелец: {}\nДействует до: {}\nКод безопасности: {}".format(card_num, card_name, card_expires, card_cvv2)


@app.route('/login/')
def index_test4():
    form ='''
    <h2>Авторизация</h2> 
    <form class="auth-form" action="/pay_test4" method="POST">
    <div> Логин <input type="text" name="u_name" />  </div>
    <div> Пароль <input type="password" name="u_pass" /> </div>
    <div> <input type="submit" value="Отправить" />  </div>
    </form>
    '''

    return form


@app.route('/pay_test4/', methods=['POST'])
def pay_test4():
    u_name = request.form.get('u_name')
    u_pass = request.form.get('u_pass')

    if u_name == 'user@stepik.org' and u_pass == '12345':
        return 'OK'
    else:
        return 'ERROR'


form = '''
    <form class="auth-form" action="/signin" method="POST">
    <div> Имя <input type="text" name="u_name" />  </div>
    <div> Фамилия <input type="text" name="u_surname" /> </div>
    <div> Почта <input type="email" name="u_mail" /> </div>
    <div> Пароль <input type="password" name="u_pass" /> </div>
    <div> Еще раз <input type="password" name="u_pass_again" /> </div>
    <div> <input type="submit" value="Зарегистрироваться" />  </div>
    </form>
'''


@app.route('/signin', methods=['POST'])
def registration():
    u_name = request.form.get('u_name')
    u_surname = request.form.get('u_surname')
    u_mail = request.form.get('u_mail')
    u_pass = request.form.get('u_pass')
    u_pass_again = request.form.get('u_pass_again')
    if u_pass == None or len(u_pass) < 1:
        return form
    if '@' in u_mail and u_pass == u_pass_again:
        return f'Пользователь {u_name} {u_surname} с почтой {u_mail} зарегистрирован'
    else:
        return form


app.run()
