import json

def test_hello(app, client):
    res = client.get('/hello/student')
    assert res.status_code == 200
    expected = {'message': 'Hello student'}
    assert expected == json.loads(res.get_data(as_text=True))

def test_students(app, client):
    res = client.get('/students')
    assert res.status_code == 200
    expected = {}
    assert expected == json.loads(res.get_data(as_text=True))

def test_students_id(app, client):
    res = client.get('/students/1')
    assert res.status_code == 200
    expected = {}
    assert expected == json.loads(res.get_data(as_text=True))