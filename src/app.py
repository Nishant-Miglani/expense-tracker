from flask import Flask, request


app = Flask(__name__)


@app.route("/add_expense", methods=["POST"])
def add_expense():
    pass

@app.route("/update_expense", methods=["POST"])
def update_expense():
    pass

@app.route("/delete_expense", methods=["DELETE"])
def delete_expense():
    expense_id = request.args.get("expense_id")
    pass

@app.route("/get_expense", methods=["GET"])
def get_expense():
    expense_id = request.args.get("expense_id")
    pass

@app.route("/get_expenses", methods=["GET"])
def get_expenses():
    pass


if __name__ == "__main__":
    app.run(debug=True)