from sqlalchemy import create_engine, MetaData

password="yqWFPQRHSxoxjGB2moYz"
engine = create_engine(f"mysql+pymysql://admin:{password}@localhost:3306/DBTesis")

meta = MetaData()

conn = engine.connect()