from flask import Blueprint, request, render_template, app, redirect, url_for

from apps.user.models import User
from apps.article.models import Article
from exts import db

article_bp = Blueprint('article',__name__)
@article_bp.route('/publish', methods=['POST','GET'])
def publish():

    if request.method == 'POST':
        title = request.form.get('title')
        user_id = request.form.get('uid')
        content = request.form.get('content')
        article = Article()
        article.title = title
        article.content = content
        article.user_id = user_id
        print('**************',article)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('article.all_articles'))

    else:
        users = User.query.all()
        return render_template('article/publish.html',users=users)
        # return render_template('user/../../templates/article/publish.html', users=users)

@article_bp.route('/all_articles')
def all_articles():
    articles = Article.query.all()
    return render_template('article/all_articles.html', articles=articles)

@article_bp.route('/all_articles1')
def all_articles1():
    id = 1
    user = User.query.get(id)

    return render_template('article/all_articles1.html', user=user)