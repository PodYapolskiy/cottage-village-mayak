@REM TODO: Check for python existance
@REM Set environment
python -m venv env
env\scripts\activate
echo "Virtual environment is ready"

@REM TODO: Check for pip existance
@REM Install dependecies
pip install -r requirements.txt
echo "All dependecies are installed"
