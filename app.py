from flask import Flask, render_template, request
from Modules import calculation
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return render_template("test.html")


@app.route('/submit', methods=['POST'])
def submit():
    dnd = request.form['dnd'].split(',')
    nsr = request.form['nsr'].split(',')
    b2b = request.form['b2b'].split(',')
    nscl = request.form['nscl'].split(',')
    clean = request.form['clean'].split(',')
    total_co = request.form['total_co']
    total_stay = request.form['total_stay']
    day_use = request.form['day_use'].split(',')

    room_count_file = request.files['room_count_file']
    toga_file = request.files['toga_file']

    result = calculation.calculate(room_count_file,
                                   toga_file,
                                   total_co,
                                   total_stay,
                                   dnd,
                                   nsr,
                                   b2b,
                                   nscl,
                                   clean,
                                   day_use)

    return result


if __name__ == '__main__':
    app.run(debug=True)
