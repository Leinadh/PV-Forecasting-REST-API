from sqlalchemy import Column, Table, ForeignKey 
from sqlalchemy.sql.sqltypes import Integer, Date, String, Numeric
from config.db import meta, engine

metrics = Table(
    "metrics",
    meta,
    Column("metric_id", Integer, primary_key=True),
    Column("ml_model_id", Integer, ForeignKey("ml_models.ml_model_id"), nullable=False),
    Column("metric_name", String(100)),
    Column("date", Date),
    Column("value", Numeric(10, 4)),
)

meta.create_all(engine)