from flask import Flask, render_template, request
import requests
import smtplib

my_email = 'hoanghuyen.hh20897@gmail.com'
password = 'vxcm rxhy oavm hsap'

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

@app.route("/contact",methods=["POST","GET"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        with smtplib.SMTP("smtp.gmail.com",port = 587) as con:
            con.starttls()
            con.login(my_email,password)
            con.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject: Thank you for contact! \n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}"
            )
        return render_template('contact.html',sent = True, name = name, email=email,phone=phone,message=message)
    return render_template("contact.html", sent = False)

    
if __name__ == "__main__":
    app.run(debug=True)