from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('Website_code\ICV_study.csv')  # data.xlsx
columns = data.columns.tolist()

@app.route('/')
def index():
    return render_template('index.html', columns=columns)

@app.route('/generate_table', methods=['POST'])
def generate_table():
    selected_columns = request.json.get('columns')
    if len(selected_columns) != 2:
        return jsonify(error="Please select exactly two columns."), 400
    try:
        # print(selected_columns[1].size())
        pivot_table = pd.pivot_table(data, 
                                     index=[selected_columns[0]],
                                     values=[selected_columns[1]], 
                                     aggfunc='count',
                                     fill_value=0,
                                     margins=1)
        
        pivot_table_data = pivot_table.reset_index().values.tolist()
        columns = pivot_table.reset_index().columns.tolist()
        return jsonify(table_data=pivot_table_data, columns=columns)

    except KeyError:
        return jsonify(error="Invalid column names."), 400

if __name__ == '__main__':
    app.run(debug=True)