from flask import Flask         # сперва подключим модуль

app = Flask(__name__)           # объявим экземпляр фласка


@app.route('/')
def render_main():
    return 'Здесь будет главная страница'

@app.route('/products/')
def render_products():
    return 'Продукты'

@app.route('/about/')
def render_about():
    return 'Информация о проекте'

'''
@app.route('/profiles/')
@app.route('/contacts/')
def render_under_construction():
    return render_template('')
'''
@app.route('/videos/<video_id>/')       # принимаем один параметр
def render_videos_item(video_id):
    return 'Здесь будет видео ' + video_id

@app.route('/book/<author>/<title>/')   # принимаем несколько параметров
def render_author_title(author, title):
    return 'Здесь будет страница книги ' + title + ' автора ' + author

@app.route('/book/<int:book_id>')
def render_book(book_id):
    print(type(book_id))
    return ''

@app.route('/temp/<float:temp_value>/')
def render_temp(temp_value):
    print(type(temp_value))
    return ''

@app.route('/example/')
def render_example():
    return '<h2>Привет, я функция Example <h2>'

@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!:\n{}".format(error), 404

@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим", 500

app.run()