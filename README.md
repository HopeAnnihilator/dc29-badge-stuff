
# dc29-badge-stuff

This is my dumb project to make the Defcon 29 Badge blink colors.

### Getting Started
1. Setup a python virtual environment
```python3 -m venv .venv```
2. Source you virtual environment
Windows ```.venv/scripts/activate```
Bash ```source .venv/bin/activate```
3. Install requirements
```pip3 install -r requirements.txt``` 
or 
```python3 -m pip install -r requirements.txt```
4. run serial write script and read script
	* serial port must be read while writing or it will pause till read
