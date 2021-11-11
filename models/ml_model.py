from sqlalchemy import Column, Table, ForeignKey 
from sqlalchemy.sql.sqltypes import Integer, String, LargeBinary, Boolean
from config.db import meta, engine

ml_models = Table(
    "ml_models",
    meta,
    Column("ml_model_id", Integer, primary_key=True),
    Column("system_id", Integer, ForeignKey("systems.system_id"), nullable=False),
    Column("model_name", String(100),),
    Column("description", String(500),),
    Column("image", LargeBinary),
    Column("image_path", String(500)),
    Column("is_trasfered", Boolean),
    Column("origin_system", Integer, ForeignKey("systems.system_id"), nullable=True),
)

meta.create_all(engine)