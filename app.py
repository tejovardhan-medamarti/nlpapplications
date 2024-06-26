from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(200), nullable=True)
    category = db.Column(db.String, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Product Id: %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        
        product_master = request.form  # Use .get() to avoid BadRequestKeyError
        
        if product_master:  # Check if product_master is not None or empty
            new_product = Todo(
                product = product_master['product'],
                category = product_master['category']
                )
            try:
                db.session.add(new_product)
                db.session.commit()
                print('Product added successfully for {}'.format(product_master))
            except:
                return 'There was an issue adding your product.'
        else:
            return 'No product content provided.'  # Handle the case where 'content' is not provided
        return redirect('/')
    else:
        products = Todo.query.order_by(Todo.date_created).all()
        print(products)
        return render_template('index.html', products=products)


@app.route('/delete/<int:id>')
def delete(id):
    product_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(product_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that product.'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    product = Todo.query.get_or_404(id)
    if request.method == 'POST':
        product.product = request.form['product']
        product.category = request.form['category']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your product.'
    else:
        return render_template('update.html', product=product)

def read_data():
    data = pd.read_csv('data/ratings_Beauty.csv')
    return data

@app.route('/get_count')
def get_count():
    data = read_data()
    return data.head()

if __name__ == '__main__':
    app.run(debug=True)