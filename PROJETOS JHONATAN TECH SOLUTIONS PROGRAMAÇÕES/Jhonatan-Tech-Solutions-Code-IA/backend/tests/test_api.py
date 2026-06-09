"""
Test suite for backend API
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture(scope="session")
def test_client():
    """Test client fixture"""
    return client


class TestHealth:
    """Health check tests"""

    def test_health_endpoint(self, test_client):
        """Test health check endpoint"""
        response = test_client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

    def test_ping_endpoint(self, test_client):
        """Test ping endpoint"""
        response = test_client.get("/ping")
        assert response.status_code == 200
        assert response.json()["message"] == "pong"


class TestRoot:
    """Root endpoint tests"""

    def test_root_endpoint(self, test_client):
        """Test root endpoint"""
        response = test_client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()
        assert "version" in response.json()


class TestCodeGeneration:
    """Code generation endpoint tests"""

    def test_list_languages(self, test_client):
        """Test list supported languages"""
        response = test_client.get("/api/code/languages")
        assert response.status_code == 200
        assert "languages" in response.json()
        assert len(response.json()["languages"]) > 0

    def test_generate_code(self, test_client):
        """Test code generation"""
        payload = {
            "prompt": "Create a function to add two numbers",
            "language": "python"
        }
        response = test_client.post("/api/code/generate", json=payload)
        assert response.status_code == 200
        assert "id" in response.json()
        assert "code" in response.json()
        assert response.json()["language"] == "python"

    def test_generate_code_invalid_prompt(self, test_client):
        """Test code generation with invalid prompt"""
        payload = {
            "prompt": "",
            "language": "python"
        }
        response = test_client.post("/api/code/generate", json=payload)
        assert response.status_code == 422


class TestErrorHandling:
    """Error handling tests"""

    def test_404_not_found(self, test_client):
        """Test 404 error handling"""
        response = test_client.get("/api/nonexistent")
        assert response.status_code == 404

    def test_method_not_allowed(self, test_client):
        """Test method not allowed"""
        response = test_client.post("/health")
        assert response.status_code == 405
