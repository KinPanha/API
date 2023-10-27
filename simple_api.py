from flask import Flask, request , jsonify
app = Flask(__name__)
@app.route("/")
def main():
    return "Hello Api"

product_data = [
        {
            "id" : "1",
            "name_product" : "product1",
            "url" : "url 1",
            "price" : "price1",
            "description": "des3",
            "rate" : "rate1",
        },
        {
            "id" : "2",
            "name_product" : "product2",
            "url" : "url 2",
            "price" : "price2",
            "description": "des3",
            "rate" : "rate2",
        },
        {
            "id" : "3",
            "name_product" : "product3",
            "url" : "url 3",
            "price" : "price3",
            "description": "des3",
            "rate" : "rate3",
        },
    ]

@app.route("/products")
def product():
   return jsonify(product_data)


if __name__ == "__main__":
    app.run(debug=True)