from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "%40Kiliyam6"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "nifty100"

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)