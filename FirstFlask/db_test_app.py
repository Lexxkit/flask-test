from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


# строчка нужна для первого создания таблицы БД
db.create_all()

user = User(name='Василий')
db.session.add(user)
print(f'ID is {user.id}')
db.session.commit()
print(f'ID is {user.id}')

# Add multiple users to DB
db.session.add_all([User(name='Vlad'), User(name='Oleg'), User(name='Slava')])
db.session.commit()

# Теперь выведем записи из базы
users = db.session.query(User).all()
print(users)