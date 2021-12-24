from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from app import app, db, limiter
from app.forms import LoginForm, PostForm, EditForm
from app.models import User, Post

@app.route('/', methods=['GET'])
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
       
        f = form.upload.data
        filename = str(Post.query.count()) + '.jpg'
        
        # Save uploaded file (if exists)
        if (f is not None):
            f.save(app.config['UPLOAD_PATH'] + filename)

        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('dashboard'))
    return render_template('dashboard.html',form=form,posts=posts)

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("10/hour")
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

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/post/<int:id>', methods=['GET'])
def post(id):
    post = Post.query.filter_by(id=id).first_or_404()
    return render_template('_post.html', post=post)

@app.route('/delete-post/<int:id>', methods=['GET', 'DELETE'])
@login_required
def delete_post(id):
    p = Post.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/edit-post/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    p = Post.query.filter_by(id=id).first_or_404()
    form = EditForm()
    if form.validate_on_submit():
        p.title = form.title.data
        p.body = form.post.data 
        db.session.commit()
        return redirect(url_for('post', id=p.id))

    form.title.data = p.title
    form.post.data = p.body
    return render_template('_edit-post.html', form=form, post=p)
