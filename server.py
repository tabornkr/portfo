from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import csv

app = Flask(__name__)
print(app)

def write_to_csv(filename, data):
    hdr = 'timestamp, email, name, message'
    timestamp = str(datetime.now()).split('.')[0]
    with open(filename, mode='a',newline='') as db:
        csv_writer = csv.writer(db, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([timestamp, data["email"], data["subject"], data["message"]])



@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # return render_template('submit_form.html', error=error)
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv('database.csv', data)
            return redirect('/thankyou.html')
        except:
            return "did not save to database"
    else:
        return 'something went wrong. Try again!'



# @app.route("/index.html")
# def index():
#     return render_template("index.html")
#
#
# # this is a decorator
# @app.route("/about.html")
# def about():
#     return render_template('about.html')
#     # return "this is about"
#
# @app.route("/works.html")
# def works():
#     return render_template("works.html")
#
# @app.route("/work.html")
# def work():
#     return render_template("work.html")
#
# @app.route("/thankyou.html")
# def thankyou():
#     return "thankyou.html"
#
# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')
#
# @app.route("/components.html")
# def components():
#     return render_template('components.html')

