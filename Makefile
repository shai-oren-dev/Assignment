# target build

build:
    echo "building the container packages and modules..."
    sudo apt update
    sudo apt install python3.7
    sudo apt-get install python-pip
    pip install colorama

run:
    # testing the UnitTests
    echo "testing the UnitTests..."
    python3 UnitTests/UnitTests.py
