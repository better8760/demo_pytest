import pytest
import allure

@pytest.fixture(scope="package",autouse="True")
def set_up_package():
    print("\n--- Test package start run ---")
    yield
    print("\n--- Test package end run ---")

