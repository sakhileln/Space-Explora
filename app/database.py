"""
Module for setting up the database connection and ORM configuration.

This module establishes the connection to the database, configures the
SQLAlchemy session, and sets up the base class for ORM models. It provides
a session maker for creating database sessions and an engine for database
interaction.

Configuration:
    - DATABASE_URL: The URL for connecting to the database (SQLite in this case).
    - engine: The SQLAlchemy engine used for connecting to the database.
    - SessionLocal: A session maker used to create session instances for database operations.
    - Base: The base class used for defining ORM models.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bird=engine)
Base = declarative_base()
