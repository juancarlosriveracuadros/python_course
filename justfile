# Default recipe shows available commands
default:
    @just --list

## Create and prepare Environment

# Creat virtual environment
creat_venv:
    python3 -m venv .venv

# Init virtual environment
init_venv:
    source .venv/bin/activate

# Install the requirement dependencies
install_dep:
    pip install -r requirements.txt

## pytest library

# test my_func.py with pytest
test_my_func:
    pytest pytest-fcc/tests/test_my_func.py

# test shapes.py as circle with pytest
test_circle:
    pytest pytest-fcc/tests/test_circle.py

# test dinamic with pytest 
test_din param:
    pytest pytest-fcc/tests/{{param}}

# test dinamic with pytest allows you to see standard output (like print statements) 
test_s param:
    pytest --capture=no pytest-fcc/tests/{{param}}