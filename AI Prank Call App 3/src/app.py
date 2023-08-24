from flask import Flask, render_template, request
import prank_call

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        pricing_plan = request.form.get('pricing_plan')
        voice = request.form.get('voice')
        prank_call.prank_call(phone_number, pricing_plan, voice)
        return 'Prank call made!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)