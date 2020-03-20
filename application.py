import datetime
from flask import Flask, render_template,url_for,request


app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    #new_year = True
    return render_template("index.html", new_year=new_year)

@app.route("/names", methods =["GET","POST"])
def names():
    names = ["Hamza","Arwa","Batul", "Amatullah"]
    if request.method == "POST":
        name = request.form.get("name")
        names.append(name)
    
    return render_template("names.html", names=names)

#@app.route("/add_name", methods=["POST","GET"])
#def add_name():
    #if request.method == "POST":
        #name = request.form.get("name")
        #names.append(name)

    #return render_template("add_name.html", names=names)


if __name__=='__main__':
    app.run(debug=True)


