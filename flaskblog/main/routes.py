from flask import render_template, request, Blueprint
from flaskblog.models import Post
from . import main
from ..request import get_quote

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    quote= get_quote()
    return render_template('about.html', title='About',quote=quote)
