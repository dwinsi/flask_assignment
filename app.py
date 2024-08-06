# Import libraries
from flask import Flask, redirect, request, render_template, url_for

# Instantiate Flask functionality

app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation: List all transactions
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation: Display add transaction form
# Route to handle the creation of a new transaction
@app.route("/add", methods = ['GET', 'POST'])
def add_transactions():
    # check if the request method is POST (form submission)
    if request.method == 'POST':
        # create a new transaction object using form fiels values
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }

        # Append the new transaction to the transactions list
        transactions.append(transaction)

        # Redirect to the transaction list page after adding the new transaction
        return redirect(url_for("get_transactions"))
    
    # if the request method is GET, render the form template to display the add transacton form
    return render_template("form.html")


# Update operation: Display edit transaction dorm
#  Route to handle the editing of an existing transaction
@app.route("/edit/<int:transaction_id", methods = ['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'GET':
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                return render_template("edit.html", transaction = transaction)

    if request.method == 'POST':
        # Extract the updated values from the form fields
        date = request.form['date']
        amount = float(request.form[amount])

        # Find the transaction with the matching ID and update its value
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break
        
        # Redirect to the transactions list page after updating the transactions
        return redirect(url_for("get_transactions"))

    return {"message": "Transaction not found"}, 404

# Delete operation: Delete a transaction
# Route to handle the deletion of an existing transaction
@app.route("/delete/<int:transaction_id>", methods = ['DELETE'])
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break

    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for("get_transactions"))


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
    