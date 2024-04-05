import pytest
import json
from pathlib import Path
from save_data import save_variable, load_variable
from save_data import save_variables, load_variables

def test_save_variable():
    save_variable("test", "var1")
    path = Path('save_data/var1_data.json')
    assert path.read_text() == json.dumps("test")

def test_load_variable():
    save_variable("test", "var1")
    assert load_variable("var1") == "test"

def test_save_variables():
    var1 = "test_string"
    var2 = 42
    var3 = ["list1", "list2", "list3"]
    save_variables(var1,var2, var3)
    path = Path('save_data.json')
    data_list = json.loads(path.read_text())
    assert data_list == [
        {"var1": "test_string"},
        {"var2": 42},
        {"var3": ["list1", "list2", "list3"]},
        ]

def test_load_variables():
    var1 = "test_string"
    var2 = 42
    var3 = ["list1", "list2", "list3"]
    save_variables(var1,var2, var3)
    variables = load_variables()
    assert variables == {
        'var1': 'test_string',
        'var2': 42,
        'var3': ['list1', 'list2', 'list3'],
    }
