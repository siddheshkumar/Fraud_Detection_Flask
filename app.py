from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/detect_fraud', methods=['POST'])
def detect_fraud():
    # Get the transaction details from the form
    amount = float(request.form['amount'])
    old_balance_org = float(request.form['oldbalanceOrg'])
    new_balance_orig = float(request.form['newbalanceOrig'])
    new_balance_dest = float(request.form['newbalanceDest'])
    old_balance_dest = float(request.form['oldbalanceDest'])

    # Perform fraud detection logic
    if is_fraudulent(amount, old_balance_org, new_balance_orig, new_balance_dest, old_balance_dest):
        result = alert('fraud');
    else:
        result = alert('safe');

    # Return the result as JSON
    return jsonify(result)


def is_fraudulent(amount, old_balance_org, new_balance_orig, new_balance_dest, old_balance_dest):
    # Add your fraud detection logic here
    # This is just a placeholder example
    if amount > old_balance_org:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run()
