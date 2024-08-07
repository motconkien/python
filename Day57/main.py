from flask import Flask, render_template
from post import Post
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts_raw = response.json()
all_posts=[]
for post in all_posts_raw:
    new = Post(post["id"], post["title"], post["subtitle"], post["body"])
    all_posts.append(new)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",blogs = all_posts)

@app.route("/blog/<int:index>")
def get_body(index):
    title = all_posts[1].title if index == 2 else all_posts[0].title
    body = all_posts[1].body if index == 2 else all_posts[0].body
    return render_template("post.html", body=body, title = title)

if __name__ == "__main__":
    app.run(debug=True)
