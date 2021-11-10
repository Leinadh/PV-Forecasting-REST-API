from sqlalchemy import Column, Table, ForeignKey 
from sqlalchemy.sql.sqltypes import Integer, Numeric, DateTime
from config.db import meta, engine

location_observations = Table(
    "location_observations",
    meta,
    Column("location_observation_id", Integer, primary_key=True),
    Column("location_id", Integer, ForeignKey("locations.location_id"), nullable=False),
    Column("datetime", DateTime),
    Column("irradiance", Numeric(10, 4)),
    Column("t_amb", Numeric(10, 4)),
    Column("humidity_relative", Numeric(10, 4)),
    Column("humidity_absolute", Numeric(10, 4)),
    Column("wind_speed", Numeric(10, 4)),
    Column("wind_direction", Numeric(10, 4)),
    Column("air_density", Numeric(10, 4)),
    Column("pressure_relative", Numeric(10, 4)),
    Column("pressure_absolute", Numeric(10, 4)),
)

meta.create_all(engine)