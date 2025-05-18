
from flask import Flask, render_template,request

app =Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/calculator",methods=["GET","POST"])
def calculator():
    result=None
    if request.method=="POST":
        try:
             
            num1=float(request.form["num1"])
            num2=float(request.form["num2"])
            operation=request.form["operation"]

            if operation=="add":
                result=num1+num2
            
            elif operation=="subtract":
                result=num1-num2       

            elif operation =="multiply":
                result = num1 * num2   

            elif operation == "divide":
                result = num1 /num2 if num2 != 0 else "Cannot divide by zero"

        except ValueError:
             result="Invalid input"   
    return render_template("calculator.html", result=result)
             

         

if __name__=="__main__":
    app.run(debug=True)


#http://localhost:5000/
