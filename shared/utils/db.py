"""
Database connection utilities for PostgreSQL.
"""

import os
from pathlib import Path
from contextlib import contextmanager

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

# Load .env from project root
_project_root = Path(__file__).parent.parent.parent
load_dotenv(_project_root / ".env")


def get_connection_string() -> str:
    """Build PostgreSQL connection string from environment variables."""
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    name = os.getenv("DB_NAME", "grocery")
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASSWORD", "")
    
    return f"postgresql://{user}:{password}@{host}:{port}/{name}"


def get_engine(echo: bool = False) -> Engine:
    """
    Create SQLAlchemy engine for PostgreSQL.
    
    Args:
        echo: If True, log all SQL statements
        
    Returns:
        SQLAlchemy Engine instance
    """
    conn_string = get_connection_string()
    return create_engine(conn_string, echo=echo, pool_pre_ping=True)


@contextmanager
def get_connection():
    """
    Context manager for database connections.
    
    Usage:
        with get_connection() as conn:
            result = conn.execute(text("SELECT * FROM table"))
    """
    engine = get_engine()
    connection = engine.connect()
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def execute_query(query: str, params: dict = None):
    """
    Execute a SQL query and return results.
    
    Args:
        query: SQL query string
        params: Optional dict of query parameters
        
    Returns:
        List of result rows
    """
    with get_connection() as conn:
        result = conn.execute(text(query), params or {})
        return result.fetchall()


def execute_script(filepath: str) -> None:
    """
    Execute a SQL script file.
    
    Args:
        filepath: Path to .sql file
    """
    with open(filepath, "r") as f:
        script = f.read()
    
    with get_connection() as conn:
        # Split on semicolons and execute each statement
        for statement in script.split(";"):
            statement = statement.strip()
            if statement:
                conn.execute(text(statement))
