#!/bin/bash

echo "Activating virtual environment..."
source venv/bin/activate

echo "Running test suite..."
pytest test_app.py

TEST_RESULT=$?

if [ $TEST_RESULT -eq 0 ]; then
    echo "Success: All tests passed!"
    exit 0
else
    echo "Error: One or more tests failed."
    exit 1
fi