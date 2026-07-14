from sqlalchemy import Column, Integer, String, Boolean
from database import Base

# This maps directly to a physical table named "tasks" in SQLite
class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True) # Unique ID for each task
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False)
    priority = Column(Integer, default=1)