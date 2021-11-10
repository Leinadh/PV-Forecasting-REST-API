from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Numeric
from config.db import meta, engine

locations = Table(
    "locations",
    meta,
    Column("location_id", Integer, primary_key=True),
    Column("label", String(10),),
    Column("full_name", String(100)),
    Column("region", String(50)),
    Column("city", String(50)),
    Column("address", String(100)),
    Column("latitud", Numeric(11, 6)),
    Column("longitude", Numeric(11, 6)),
    Column("altitud", Numeric(11, 6)),
)

meta.create_all(engine)