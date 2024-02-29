import pytest
from pathlib import Path
import tempfile

@pytest.fixture
def temp_path_fixture():
    print("OUTPUT OF FIXTURE: ")
    with tempfile.TemporaryDirectory() as temp_path:
        yield Path(temp_path)
    
def test_some_func_with_custom_fixture(temp_path_fixture):
    print(f"I was provided with {temp_path_fixture}")
    assert temp_path_fixture.exists()

def test_some_func_with_builtin_fixture(tmp_path):
    print(f"I was provided with {tmp_path}")
    assert tmp_path.exists()

