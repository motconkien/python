from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired
import csv
import os

#create an instance
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

#Initialize Bootstrap 5 for this app
Bootstrap(app)

rating_source = ['☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️']
wifi_source =['x','💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪']
socket_source = ['🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌']
#create class for form
class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = URLField("Cafe Location", validators=[DataRequired()])
    opentime = StringField("Open Time",validators=[DataRequired()])
    closetime = StringField("Close Time",validators=[DataRequired()])
    rating = SelectField("Coffee Rating",choices=rating_source)
    wifistrength = SelectField("Wifi Strength Rating",choices=wifi_source)
    powersocket = SelectField("Power Socket Avaibality",choices=socket_source)
    submit = SubmitField('Submit')

#home page
@app.route('/')
def home():
    return render_template("index.html")

#add page
@app.route('/add', methods =['GET', 'POST'])
def add():
    #create instance from class cafeform
    form = CafeForm()
    if form.validate_on_submit():
        input_cafe = form.cafe.data
        input_location = form.location.data
        input_opentime = form.opentime.data
        input_closetime = form.closetime.data
        selected_rating = form.rating.data
        selected_wifi = form.wifistrength.data
        selected_socket = form.powersocket.data

        file = "Day62/cafe-data.csv"
        headers = ['Cafe Name','Location','Open','Close','Coffee','Wifi','Power']
        data= [input_cafe,
                input_location,
                input_opentime,
                input_closetime,
                selected_rating,
                selected_wifi,
                selected_socket]
        write_to_csv(file,headers,data)

    return render_template('add.html', form = form)

def write_to_csv(file_path,headers,data):
    file_exists = os.path.isfile(file_path)
    existing_headers = []

    if file_exists:
        with open(file_path,mode='r') as file:
            reader = csv.reader(file)
            existing_headers = next(reader,None)
    
    with open(file_path,'a',newline='') as file:
        writer = csv.writer(file)
        if not file_exists or existing_headers != headers:
            writer.writerow(headers)
        
        writer.writerow(data)
#info page
@app.route('/cafes')
def cafes():
    with open('Day62/cafe-data.csv','r') as file:
        csv_data = csv.reader(file, delimiter=',')
        next(csv_data)
        list_of_rows =[row for row in csv_data]
        
    return render_template('cafes.html', cafes = list_of_rows)

if __name__ == '__main__':
    app.run(debug=True)