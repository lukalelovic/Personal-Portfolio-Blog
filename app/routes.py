from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
#from flask_mail import Message
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, PostForm
from app.models import User, Post

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    posts = Post.query.all()
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('dashboard'))
    return render_template('dashboard.html',form=form,posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dashboard')
        return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.filter_by(id=id).first_or_404()
    return render_template('_post.html', post=post)
