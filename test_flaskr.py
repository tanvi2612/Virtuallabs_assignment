import os
import tempfile

import pytest

import app


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    yield client

def test_1(client):
    response=client.get("/")
    assert response.status_code == 200

def test_2(client):
    response=client.get("/Introduction.html")
    assert response.status_code == 200

def test_3(client):
    response=client.get("/Experiment.html")
    assert response.status_code == 200

def test_4(client):
    response=client.get("/Further Readings.html")
    assert response.status_code == 200

def test_5(client):
    response=client.get("/Quizzes.html")
    assert response.status_code == 200

def test_6(client):
    response=client.get("/Theory.html")
    assert response.status_code == 200

def test_7(client):
    response=client.get("/Objective.html")
    assert response.status_code == 200

def test_8(client):
    response=client.get("/Procedure.html")
    assert response.status_code == 200