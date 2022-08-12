from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, login_required, current_user, logout_user
from app import app, bcrypt, db
from app.forms import RegisterForm, LoginForm, PasswordResetRequestForm, ResetPasswordForm, PostTweetForm
from app.email import send_reset_password_mail
from app.models import User, Post
from sqlalchemy import exc
    
@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    title = 'TodoList App'
    form = PostTweetForm()
    if form.validate_on_submit():
        name=form.name.data
        description=form.description.data
        currency=form.currency.data
        post = Post(name=name,description=description,currency=currency)
        current_user.posts.append(post)
        db.session.commit()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page, 2, False)
    return render_template('index.html',title=title, form = form, posts = posts)

@app.route('/post_content/<username>')
@login_required
def user_page(username):
    user = User.query.filter_by(username=username).first()
    if user:
        page = request.args.get('page', 1, type=int)
        posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).paginate(page, 2, False)
        return render_template('post_content.html', user=user, posts=posts)
    else:
        return '404'

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=username,email=email,password=password)
        try:
            db.session.add(user)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
        flash('congrats', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember=form.remember.data
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user,remember=remember)
            flash('Login success',category='info')
            if request.args.get('next'):
                next_page=request.args.get('next')
                return redirect(next_page)
            return redirect(url_for('index'))
        flash('User not exists or password not match', category='danger')
    return render_template('login.html', form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/send_password_reset_request', methods=['GET', 'POST'])
def send_password_reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=PasswordResetRequestForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        token = user.generate_reset_password_token()
        send_reset_password_mail(user, token)
    return render_template('send_password_reset_request.html', form = form)

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=ResetPasswordForm()
    return render_template('reset_password.html', form = form)

'''
@app.route("/todos", methods=["GET", "POST"])
def todos():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM todo")
        todos = [
            dict(id=row[0], name=row[1], description=row[2], currency=row[3])
            for row in cursor.fetchall()
        ]
        if todos is not None:
            return jsonify(todos)

    if request.method == "POST":
        new_name = request.form["name"]
        new_description = request.form["description"]
        new_currency = request.form["currency"]
        sql = """INSERT INTO todo (name, description, currency)
                VALUES (?, ?, ?)"""
        cursor = cursor.execute(sql, (new_name, new_description, new_currency))
        conn.commit()
        return f"Todo with the id: {cursor.lastrowid} created successfully", 201


@app.route("/todo/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_todo(id):
    conn = db_connection()
    cursor = conn.cursor()
    todo = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM todo WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            todo = r
        if todo is not None:
            return jsonify(todo), 200
        else:
            return "Something wrong", 404

    if request.method == "PUT":
        sql = """UPDATE todo
                SET name=?,
                    description=?,
                    currency=?
                WHERE id=? """

        name = request.form["name"]
        description = request.form["description"]
        currency = request.form["currency"]
        updated_todo = {
            "id": id,
            "name": name,
            "description": description,
            "currency": currency,
        }
        conn.execute(sql, (name, description, currency, id))
        conn.commit()
        return jsonify(updated_todo)

    if request.method == "DELETE":
        sql = """ DELETE FROM todo WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The todo with id: {} has been deleted.".format(id), 200
'''