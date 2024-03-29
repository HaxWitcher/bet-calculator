from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        losses = float(request.form.get('losses'))
        odds = float(request.form.get('odds'))
        profit = float(request.form.get('profit'))
        stake = (losses + profit) / (odds - 1)
        return render_template('index.html', stake=stake)
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
