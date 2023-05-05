from flask import (render_template, url_for, flash, redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from doobbile_app import db
from doobbile_app.models import Post
from doobbile_app.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_doobbile():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created!", "success")
        return redirect(url_for('main.home'))

    return render_template('create_doobbile.html', title='Create', form=form, legend='Create Doobbile')


@posts.route("/post/<int:post_id>")
def doobbile(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('doobbile.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_doobbile(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your Doobbile has been updated!', 'success')
        return redirect(url_for('posts.doobbile', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_doobbile.html', title='Update Doobbile', form=form, legend='Update Doobbile')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_doobbile(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your Doobbile has been deleted', 'success')
    return redirect(url_for('main.home'))

