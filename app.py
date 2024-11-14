from flask import Flask, request

app = Flask(__name__)

@app.route('/calculate')
def calculate():
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    match op:
        case 'sum':
            result = arg1 + arg2
            operator = '+'
        case 'sub':
            result = arg1 - arg2
            operator = '-'
        case 'mul':
            result = arg1 * arg2
            operator = '*'
        case 'div':
            if arg2 != 0:
                result = arg1 / arg2
                operator = '/'
            else:
                return "Błąd: dzielenie przez zero!", 400
        case _:
            return "Błąd: nieznana operacja!", 400

    return f"{arg1} {operator} {arg2} = {result}"

if __name__ == '__main__':
    app.run(debug=True)
