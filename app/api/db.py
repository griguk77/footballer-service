import os
from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table, create_engine, ARRAY)
from databases import Database

DATABASE_URI = 'postgresql://secUREusER:StrongEnoughPassword)@51.250.26.59:5432/postgres'

engine = create_engine(DATABASE_URI)
metadata = MetaData()

footballers = Table(
    'footballers',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('country', String(250)),
    Column('goals', Integer),
    Column('age', Integer),
    Column('clubs_id', Integer)
)

database = Database(DATABASE_URI)
