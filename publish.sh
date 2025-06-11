#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

source .venv/Scripts/activate

# echo "Running tests with pytest..."
# pytest

echo "Cleaning old builds..."
rm -rf dist build *.egg-info

echo "Building the packages..."
.venv/bin/python -m build

echo "Uploading to TestPyPI for verification..."
.venv/bin/python -m twine upload --repository testpypi dist/*

echo "If the upload to TestPyPI was successful, press ENTER to upload to the real PyPI or CTRL+C to cancel."
read -r

echo "Uploading to the real PyPI..."
.venv/bin/python -m twine upload dist/*

echo "Publication completed successfully!"
