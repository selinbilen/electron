from flask import Flask, render_template, request
import pandas as pd
import xlrd
from xlrd import open_workbook
from tablepyxl import tablepyxl

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def index():
    return render_template('index.html')

@app.route('/data', methods = ['GET', 'POST'])
def data():
    if request.method == 'POST':
        f = request.form['upload-file']

        if f:
            book = open_workbook(f)
            sheet = book.sheet_by_index(0)

            keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]

            dict_list = []
            for row_index in range(1, sheet.nrows):
                d = {keys[col_index]: sheet.cell(row_index, col_index).value 
                     for col_index in range(sheet.ncols)}
                dict_list.append(d)

            return render_template('data.html', data=dict_list)
        else:
            return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    