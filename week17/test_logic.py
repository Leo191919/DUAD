import pytest
from logic import Finance_manager
import os


@pytest.fixture
def finance_manager_setup():
    filename_movements= "test_movements.json"
    filename_categories= "test_categories.json"
    if os.path.exists(filename_movements):
        os.remove(filename_movements)




    manager = Finance_manager(filename= filename_movements)

    manager.category_manager.add_category("Job")
    manager.category_manager.add_category("Food")
    manager.category_manager.add_category("Other")
    manager.category_manager.add_category("Housing")
    manager.category_manager.add_category("Test")

    yield manager 

    if os.path.exists(filename_movements):
        os.remove(filename_movements)

def test_add_movement_valid(finance_manager_setup):
    manager = finance_manager_setup
    assert manager.add_movement("income", 100, "Salary","2025-10-01", "Job")
    assert len(manager.movements) == 1 


def test_add_movement_invalid_amount(finance_manager_setup):

    manager = finance_manager_setup
    assert not manager.add_movement("expense", -50, "Groceries", "2025-10-02", "Food")
    assert not manager.add_movement("expense", 0, "Groceries", "2025-10-02", "Food")
    assert len(manager.movements) == 0 

def test_add_movement_invalid_date(finance_manager_setup):
    manager = finance_manager_setup
    assert not manager.add_movement("income", 200, "Gift", "2025/10/03", "Other")
    assert len (manager.movements)==0

def test_add_movement_invalid_kind(finance_manager_setup):

    manager = finance_manager_setup
    assert not manager.add_movement("invalid_kind", 10, "Test", "2025-10-01", "Test")
    assert len(manager.movements) == 0 
    

def test_calculate_total_balance(finance_manager_setup):
    
    manager = finance_manager_setup
    manager.add_movement("income", 100, "Salary", "2025-10-01", "Job")
    manager.add_movement("expense", 30, "Groceries", "2025-10-02", "Food")
    manager.add_movement("income", 50, "Gift", "2025-10-03", "Other")
    assert manager.calculate_total_balance() == 120.0


def test_remove_movement(finance_manager_setup):
    manager = finance_manager_setup
    manager.add_movement("income", 100, "Salary", "2025-10-01","Job")
    assert manager.remove_movement(0)
    assert len(manager.movements) == 0 
    assert not manager.remove_movement(0)

def test_edit_movement_valid(finance_manager_setup):
    manager = finance_manager_setup
    manager.add_movement("income", 100, "Salary", "2025-10-01", "Job")
    assert manager.edit_movement(0, "expense", 200, "Rent", "2025-10-05", "Housing")
    assert manager.movements[0].description == "Rent"
    assert manager.movements[0].amount == 200

def test_edit_movement_invalid(finance_manager_setup):
    manager = finance_manager_setup
    manager.add_movement("income", 100, "Salary", "2025-10-01", "Job")
    assert not manager.edit_movement(0, "expense", -50, "Rent", "2025-10-05", "Housing ")
    assert not manager.edit_movement(0, "expense", 50, "Rent", "invalid_date", "Housing")
    assert manager.movements[0].description == "Salary"


