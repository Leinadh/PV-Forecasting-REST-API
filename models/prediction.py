from sqlalchemy import Column, Table, ForeignKey 
from sqlalchemy.sql.sqltypes import Integer, DateTime, Numeric
from config.db import meta, engine

predictions = Table(
    "predictions",
    meta,
    Column("prediction_id", Integer, primary_key=True),
    Column("ml_model_id", Integer, ForeignKey("ml_models.ml_model_id"), nullable=False),
    Column("datetime", DateTime),
    Column("pred_power_ac", Numeric(10, 4)),
)

meta.create_all(engine)
