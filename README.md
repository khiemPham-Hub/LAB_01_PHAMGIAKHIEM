# Study Assistant — starter

A starter repository for the CSC10014 Smart Virtual Assistant project.

## Setup

**Prerequisites:**



* Git
* Python 3.10
* Windows CMD or a compatible terminal



**Installation steps:**



1. Clone the repository: git clone https://github.com/Pgkhiem31/Lab01\_Pgkhiem31.git
2. Navigate to the project directory:  cd Lab01\_Pgkhiem31
3. Create a virtual environment:  python -m venv .venv
4. Activate the virtual environment on Windows CMD:  .venv\\Scripts\\activate.bat
5. Install the required dependencies:  python -m pip install -r requirements.txt
6. Install the project in editable mode: python -m pip install -e .

## Run

Run the assistant with a sample question:



python -m assistant "Where is the IT helpdesk?"

## Test

Run the test suite:



python -m pytest -q

## Project structure

Lab01\_Pgkhiem31/ 

├── src/ 

│   └── assistant/ 

├── tests/ 

├── scripts/ 

│   └── check\_env.py 

├── data/ 

├── requirements.txt 

├── pyproject.toml 

├── README.md 

└── .gitignore



**src/assistant/**: application source code.

**tests/**: automated tests.

**scripts/check\_env.py**: environment validation script.

**data/**: project data files.

**requirements.txt**: Python dependencies.

**pyproject.toml**: Python project configuration.

**.gitignore**: files and directories excluded from Git.

