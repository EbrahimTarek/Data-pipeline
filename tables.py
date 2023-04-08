from sqlalchemy import cast,Column,Integer,String,Date
from sqlalchemy.orm import column_property
from Base import Base,engine

class PprRawAll(Base):
    __tablename__ = "ppr_raw_all"
    id = Column(Integer,primary_key=True)
    date_of_sale = Column(String(55))
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(String(55))
    description = Column(String(255))
    transaction_id = column_property(date_of_sale + "_" + address + "_" + county + "_" + price)

class PprCleanAll(Base):
    __tablename__ = "ppr_clean_all"
    id = Column(Integer, primary_key=True)
    date_of_sale = Column(Date)
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(Integer)
    description = Column(String(255))
    transaction_id = column_property(cast(date_of_sale, String)+ "_" + address+ "_" + county + "_" + cast(price, String))


#Create Table PprRawAll,PprCleanAll in postgresql
Base.metadata.create_all(engine)

