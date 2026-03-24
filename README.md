# Flask Project: pyweb

This project is a Flask-based web application. Below are the steps to set up and run the project.

## Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd pyweb
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     .\.venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask Application**
   ```bash
   python pyweb.py
   ```

6. **Access the Application**
   Open your browser and navigate to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Notes
- Ensure all static assets are correctly placed to avoid 404 errors.
- Update the `requirements.txt` file if additional dependencies are added.


set -e
python --version
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi

# if command -v flake8 >/dev/null 2>&1; then
#   flake8 .
# else
#   echo "flake8 not installed, skipping lint step"
# fi

# if [ -f pytest.ini ] || [ -d tests ] || [ -f setup.cfg ]; then
#   pytest -q
# else
#   echo "No pytest config or tests folder found; skipping tests"
fi