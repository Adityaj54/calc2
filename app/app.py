"""A simple flask web app"""
from flask import Flask, request, flash
from flask import render_template
from calc.calculator import Calculator
from calc.calculations.writeresults import Results

app = Flask(__name__)
app.secret_key = 'f3cfe9ed8fae309f02079dbf'

@app.route("/")
def index():
    """index  Route Response"""
    return render_template('index.html')

@app.route("/basicform", methods=['GET', 'POST'])
def basicform():
    """Post Request Handling"""
    if request.method == 'POST':
        #get the values out of the form
        value1 = request.form['value1']
        value2 = request.form['value2']
        if value1 is '' or value2 is '':
            flash(f'Enter the Values')
            return render_template('basicform.html')
        operation = request.form['operation']
        #make the tuple
        my_tuple = (value1, value2)

        #this will call the correct operation
        getattr(Calculator, operation)(my_tuple)
        result = str(Calculator.get_last_result_value())
        flash(f'Operation {operation} Successfull ')
        Results.write_results(value1,value2,result,operation)
        return render_template('result.html',value1=value1, value2=value2, operation=operation, result=result)
    # Displays the form because if it isn't a post it is a get request
    else:
        return render_template('basicform.html')


@app.route("/bad/<value1>/<value2>")
def bad_calc(value1,value2):
    """bad calc Route Response"""
    result = value1 + value2
    response = "The result of the calculation is: " + result + '<a href="/"> back</a>'
    return response

@app.route("/good/<float:value1>/<float:value2>")
def good_calc(value1,value2):
    """good calc Route Response"""
    my_tuple = (value1,value2)
    Calculator.addition(my_tuple)
    response = "The result of the calculation is: " + str(Calculator.get_last_result_value()) + '<a href="/"> back</a>'
    return response

@app.route("/results")
def display_results():
    """bad calc Route Response"""
    return render_template('table.html',values = Results.display_results())

@app.route("/g")
def glossary():
    return render_template('glossary.html')

@app.route("/aaa")
def AAA():
    return render_template('AAA.html')
@app.route("/arpanet")
def arpanet():
    return render_template('arpanet.html')
@app.route("/oops")
def oops():
    return render_template('oop.html')

@app.route("/tcp")
def tcp():
    return render_template('tcpip.html')
@app.route("/sep")
def sep():
    return render_template('seperation.html')



@app.route("/clear")
def clear():
    Results.clear_results()
    return render_template('table.html')



