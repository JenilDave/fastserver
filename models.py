from sqlalchemy import Column, Integer, String, BINARY, BigInteger,schema,create_engine, text
from sqlalchemy.orm import declarative_base,sessionmaker
import constants as const

Base = declarative_base()

# Define ORM Type Schema for Users TABLE
class UsersModel(Base):
    '''
    Inherit the Base class to get SQLAlchemy Model,
    for table.
    '''   

    __tablename__ = 'users'
    __table_args__ = {"schema" : const.GLOBAL_SCHEMA}

    id = Column(Integer, primary_key= True, autoincrement= True, nullable= False)
    name = Column(String, nullable= False)
    username = Column(String, nullable= False,) # unique= True) # didnot work
    password = Column(String, nullable= False)
    admin = Column(Integer,schema.CheckConstraint('admin IN (0,1)'),nullable=False)


# Define ORM Type Schema for Products TABLE
class ProductsModel(Base):
    '''
    Inherit the Base class to get SQLAlchemy Model,
    for table.
    '''   

    __tablename__ = 'products'
    __table_args__ = {"schema" : const.GLOBAL_SCHEMA}

    id = Column(Integer, primary_key= True, autoincrement= True, nullable= False)
    name = Column(String, nullable= False)
    price = Column(BigInteger, nullable= False)
    category = Column(String, schema.CheckConstraint("category IN ('Accessories', 'Clothing', 'Electronics','Fitness')"), nullable= False, )
    rating = Column(Integer, schema.CheckConstraint("rating IN (1,2,3,4,5)"), nullable= False, )
    quantity = Column(Integer, nullable= False)
    description = Column(String)


# move then into separate files, no need of class....


'''
if __name__ == "__main__":
    print("Populating Users Table......")
    UsersTableUtility.populate_users_table()
    print("\n-------------- Printing users --------------\n")
    UsersTableUtility.read_users_table()
    print("**********************************************************")
    print("Populating Products Table......")
    ProductsTableUtility.populate_products_table()
    print("\n-------------- Printing users --------------\n")
    ProductsTableUtility.read_products_table()
'''