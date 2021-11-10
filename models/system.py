from sqlalchemy import Column, Table, ForeignKey 
from sqlalchemy.sql.sqltypes import Integer, String, Numeric, Date
from config.db import meta, engine

systems = Table(
    "systems",
    meta,
    Column("system_id", Integer, primary_key=True),
    Column("location_id", Integer,ForeignKey("locations.location_id"), nullable=False),
    Column("nominal_power", Numeric(10, 4)),
    Column("area", Numeric(10, 4)),
    Column("technology", String(50)),
    Column("row", Integer),
    Column("parallel", Integer),
    Column("commisioned", Date),
    Column("inclination", Numeric(10, 4)),
    Column("orientation", String(1)),
    Column("azimuth", Numeric(10, 4)),
    Column("gamma", Numeric(10, 4)),
    Column("filename", String(10)),
)

meta.create_all(engine)