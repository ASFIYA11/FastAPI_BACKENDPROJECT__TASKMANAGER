from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Define where the database file will live on your computer
DATABASE_URL = "sqlite:///./todo_app.db"

# 2. Create the engine (the pipeline to the database file)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 3. Create a session factory (to generate active database connections)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Create a Base class that our database blueprints will inherit from
Base = declarative_base()

# 5. The Dependency Injection function we'll use in endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db  # Give the database connection to the endpoint
    finally:
        db.close()  # Always close the connection when the request is done!