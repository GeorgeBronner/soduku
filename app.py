from flask import Flask, render_template, redirect, url_for, request, flash
from logic import print_board, solve, string_to_board, valid_board_full
app = Flask(__name__)
app.config['SECRET_KEY'] = '12341234'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

def data_to_string(d):
    s = []
    for i in d.listvalues():
        s.append(i[0])
    
    t = ""
    ans = []
    for i in s:
        if i == "":
            t += '0'
        else:
            t += i

    return t   

@app.route('/solution', methods=['POST'])
def solution():
    data = request.form
    s = data_to_string(data)
    bo = string_to_board(s)
    if not valid_board_full(bo):
        flash('Invalid Sudoku')
        return redirect(url_for('index'))
    else:
        solve(bo)
        return render_template('solution.html', solved_puzzle=bo)


def clean_puzzle(puzzle):
    """
    converts input from request.form to a string format readable by Sudoku
    """
    output = ''
    for val in puzzle.values():
        if val == '':
            output += '.'
        elif int(val) in range(1, 10):
            output += val
    return output



if __name__ == '__main__':
    app.run(debug=True)