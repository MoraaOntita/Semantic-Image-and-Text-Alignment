# Variables
PYTHON = python
SCRIPT = main.py

# Targets
.PHONY: all run env clean

all: run

run:
	$(PYTHON) $(SCRIPT)

env:
	@echo "Checking Python environment..."
	@$(PYTHON) --version
	@echo "Checking for required packages..."
	@pip check || (echo "Dependencies are not satisfied. Please install the required packages." && exit 1)

clean:
	@echo "Cleaning up temporary files..."
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -type d -exec rm -r {} +
