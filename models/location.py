from decimal import Decimal
from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Decimal
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
    Column("latitud", Decimal(11, 6)),
    Column("longitude", Decimal(11, 6)),
    Column("altitud", Decimal(11, 6)),
)

meta.create_all(engine)