from flask import Flask, render_template
app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True


posts = []


@app.route('/')
def index():
    return render_template('index.html', nums_posts=len(posts))


@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template('show_post.html', slug_title=slug)


@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template('admin/post_form.html', post_id=post_id)


@app.route("/signup/")
def show_signup_form():
    return render_template('signup_form.html')
