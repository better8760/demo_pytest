import pytest

@pytest.fixture(scope="module")
def set_up_module():
    print("\n--- Test module start run ---")
    yield
    print("\n--- Test module end run ---")

