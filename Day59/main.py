from flask import Flask, render_template, url_for
import requests

response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
all_posts_raw = response.json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", all_posts = all_posts_raw)

@app.route("/post/<int:index>")
def show_post(index):
    request_post = None
    for post in all_posts_raw:
        if post['id'] == index:
            request_post = post
    return render_template("post.html", post=request_post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)