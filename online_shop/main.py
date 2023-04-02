from flask import Flask, render_template, request, flash, Blueprint, session, redirect, url_for, abort
import sqlite3
import re
app = Flask(__name__)
app.config["SECRET_KEY"]="ASDFGHJKL"

# функция для подключения в базу данных 
def connect_to_db():
    connect = sqlite3.connect("store.db")
    connect.row_factory = sqlite3.Row
    return connect


@app.route("/")
def index():
    if not "BBSB232" in session:
        session["BBSB232"] = False


    connect = connect_to_db()
    cursor = connect.cursor()
    cursor.execute("select * from products")
    products = cursor.fetchall()

    return render_template("bootstrp.html", products=products)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login1.html")
    elif request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        connect = connect_to_db()
        cursor = connect.cursor()
        user = cursor.execute("select * from users where email == ?", [email]).fetchall()
        if user:
            for row in user:
                if row[3] == password:

                    session["BBSB232"] = row[0]

                    return redirect(url_for("index"))
                else:
                    flash('Что-то не так(')
        else:
            flash('Пользователя не существует')

        return render_template("login1.html")

@app.route("/testregistr")
def test_registr():

    return render_template("signup.html")


@app.route("/testlogin", methods=["GET", "POST"])
def test_login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        connect = connect_to_db()
        cursor = connect.cursor()
        user = cursor.execute("select * from users where email == ?", [email]).fetchall()
        if user:
            for row in user:
                if row[3] == password:

                    session["BBSB232"] = row[0]

                    return redirect(url_for("index"))
                else:
                    flash('Что-то не так(')
        else:
            flash('Пользователя не существует')

        return render_template("login.html")


@app.route("/database")
def cataloge():
    connect = connect_to_db()
    cursor = connect.cursor()
    cursor.execute("select * from products")
    products = cursor.fetchall()

    return render_template("view_of_database.html", products=products)

@app.route("/user_view")
def user_view():
    if session["BBSB232"]:

        connect = connect_to_db()
        cursor = connect.cursor()
        cursor.execute("select * from users")
        users = cursor.fetchall()
        print(len(users))


        return render_template("view_of_users.html", users=users)

    else:
        print(session['BBSB232'])
        return abort(403)

@app.route("/products")
def function_url():
    if request.method == 'GET':
        id = request.args.get("id")
        connect = connect_to_db()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", [id])
        product = cursor.fetchall()

        return render_template("product.html", product=product)


@app.route("/cabinet")
def personal_area():
    if session["BBSB232"]:

        connect = connect_to_db()
        cursor = connect.cursor()
        cursor.execute("select * from users where id == ?", [session['BBSB232']])
        user = cursor.fetchone()
        print(len(user))


        return render_template("personal.html", user=user)

    else:
        return abort(403)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == 'GET':
        return render_template("sign_up.html")
    elif request.method == 'POST':
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        password = request.form.get("password")
        if not name:
            flash('Введите имя')

        #повторение почты

        elif not surname:
            flash('Введите фамилию')

        elif not email:
            flash('Введите адрес электронной почты')
        elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            flash('Некорректный адрес электронной почты')

        elif not phone_number:
            flash('Введите номер телефона')
        elif not re.match(r'^\+?[0-9]{8,}$', phone_number):
            flash('Некорректный номер телефона')

        elif not password:
            flash('Введите пароль')
        elif len(password) < 4:
            flash('Пароль должен содержать не менее 4 символов')

        else:
            connect = connect_to_db()
            cursor = connect.cursor()
            cursor.execute("INSERT INTO users (name, surname, password, email, phone_number) VALUES (?, ?, ?, ?, ?)", [name, surname, password, email, phone_number])
            connect.commit()

            flash('Пользователь успешно добавлен!')

        print("Имя:", name)
        print("Фамилия:", surname)
        print("Email:", email)
        print("Номер телефона:", phone_number)
        print("Пароль:", password)
        return render_template("sign_up.html")


if __name__ == '__main__':
    app.run(debug=True)


