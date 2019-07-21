# Flask Backend

### Requirements

- Python version 3.x
- pip
- [Postman](https://www.getpostman.com/) or [Advanced Rest Client](https://install.advancedrestclient.com/install)

Installation instructions for [Mac](https://github.com/hack4impact-uiuc/wiki/wiki/Mac-Setup) and [Windows](https://github.com/hack4impact-uiuc/wiki/wiki/Windows-Subsystem-for-Linux-Setup#setting-up-python).

Another great resource for anything on Python, including installation is [The Hitchhiker's guide to python](https://docs.python-guide.org/).

Check if you have the correct versions by running the following commands in your terminal (if you don't have Python2 installed, you may need to replace `python3` with `python` and `pip3` with `pip`):

```
python3 -V
```

```
pip3 -V
```

### Setup

First, setup your virtual environment and install the Python dependencies required to run this app. We're using virtualenv, which is a virtual Python environment isolated from other Python projects, incapable of interfering with or being affected by other Python programs on the same machine. You are thus capable of running different versions of the same package or even different Python versions. In the backend directory, run the following commands:

```
pip3 install --user virtualenv
virtualenv -p python3 venv
```

You must be in this virtual environment to install dependencies and start this server. Once you do this, you will see `(venv)` preceding your prompts. To do this:

```
source venv/bin/activate
```

Then to install dependencies, run:

```
pip install -r requirements.txt
```

Then, to start the server run:

```
python app.py
```

Note: This will remain a running process in your terminal, so you will need to open a new tab or window to execute other commands.

To stop the server, press `Control-C`.

To exit your virtual environment, run:

```
deactivate
```
