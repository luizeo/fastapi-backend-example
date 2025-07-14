import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import Base, get_db
from app.models.user import User
from fastapi.testclient import TestClient
from main import app

# Cria engine para o banco de testes
TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Cria as tabelas
Base.metadata.create_all(bind=engine)

# Override da dependência de banco no app
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def clean_database():
    # Limpa os dados da tabela antes de cada teste
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
