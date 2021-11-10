from sqlalchemy import Column, Table, ForeignKey 
from sqlalchemy.sql.sqltypes import Integer, Numeric, DateTime
from config.db import meta, engine

system_observations = Table(
    "system_observations",
    meta,
    Column("system_observation_id", Integer, primary_key=True),
    Column("system_id", Integer, ForeignKey("systems.system_id"), nullable=False),
    Column("datetime", DateTime),
    Column("voltage_dc", Numeric(10, 4)),
    Column("current_dc", Numeric(10, 4)),
    Column("power_apparent", Numeric(10, 4)),
    Column("power_dc", Numeric(10, 4)),
    Column("power_dc_t25", Numeric(10, 4)),
    Column("power_ac", Numeric(10, 4)),
    Column("power_ac_t25", Numeric(10, 4)),
    Column("t_mod", Numeric(10, 4)),
    Column("t_noct", Numeric(10, 4)),
)

meta.create_all(engine)