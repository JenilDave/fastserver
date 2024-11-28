from models import ProductsModel
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine, text
import constants as const


def populate_products_table():
    products = [
        ProductsModel(name="Bag", price=1000, category="Accessories", rating=3,quantity=50,description="Good Bag"),
        ProductsModel(name="Shirt", price=700, category="Clothing", rating=4,quantity=500,description="Good Shirt"),
        ProductsModel(name="Dumbell", price=5000, category="Fitness", rating=2,quantity=10,description="Good Dumbell"),
        ProductsModel(name="Laptop", price=100000, category="Electronics", rating=3,quantity=20,description="Good Laptop"),
        ProductsModel(name="Treadmill", price=10000, category="Fitness", rating=3,quantity=5,description="Good Treadmill"),
        ProductsModel(name="Charger", price=1000, category="Electronics", rating=4,quantity=500,description="Fast Charger"),
    ]
    with sessionmaker(bind= create_engine(const.DB_URL))() as session:
        session.execute(text('USE [Jan23TrainingDB16]'))
        for product in products:
            session.add(product)

        # Alembic starts a transaction to populate table. Thus commit is required
        session.commit()
        print("Products table population succesfull")

def read_products_table():
    with sessionmaker(bind= create_engine(const.DB_URL))() as session:
        session.execute(text('USE [Jan23TrainingDB16]'))
        products = session.query(ProductsModel).all()
        products = [product_to_dict(product) for product in products]

        # Alembic starts a transaction to populate table. Thus commit is required
        session.commit()
        print("Products table read completed")
        return products

def product_to_dict(product: ProductsModel):
    ''' 
    @arg: product -> give ProductsModel Type
    '''
    return {
            "name":product.name,
            "price":product.price,
            "category":product.category,
            "rating":product.rating,
            "quantity":product.quantity,
            "description":product.description
        }
