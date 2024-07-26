from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

def write2csv(data):
    with open('database.csv','a') as csvfile:
        writer = csv.writer(csvfile, delimiter='-',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        writer.writerow([data['email'], data["subject"], data['message']])
    
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/<string:page>")
def html_page(page='index.html'):
    return render_template(page)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        try:
            data = request.form.to_dict()
            print(data)
            write2csv(data)
            return redirect('thank.html')
        except:
            return 'cannot save data'
    else: 
        return print("something went wrong, try again!")