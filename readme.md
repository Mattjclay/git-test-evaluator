# Test Evaluator

### Script Usage

Downloads 2 test files from the github and compares them.
Files must be in a public repository.
Works best with the permanent link to the github file.


### Installation

To set up a Python environment in Windows, macOS, and Linux, you can use the `virtualenv` package. Here are the steps for each operating system:

**Windows:**

1. Install Python: Download the latest version of Python from the official website and install it. Make sure to check the box that says "Add Python to PATH" during the installation.
2. Verify Python Installation: Open a new Command Prompt window and type `python --version`. You should see the Python version you installed.
3. Install virtualenv: Virtualenv is a tool to create isolated Python environments. You can install it using pip, the Python package installer. Type `pip install virtualenv` in the Command Prompt.
4. Create a new virtual environment: Navigate to your project directory and type `virtualenv env`. This will create a new virtual environment in a folder named "env" in your project directory.
5. Activate the virtual environment: Type `.\env\Scripts\activate` in the Command Prompt. Your prompt should change to indicate that you are now working within a Python virtual environment.

```bash
# Navigate to your project directory
cd your_project_directory

# Install virtualenv
pip install virtualenv

# Create a new virtual environment
virtualenv env

# Activate the virtual environment
.\env\Scripts\activate
```

**macOS and Linux:**

1. Install Python: Python comes pre-installed on most Linux distributions and macOS. You can verify the installation by typing `python3 --version` in the terminal. If Python is not installed, you can install it using the package manager of your Linux distribution or download it from the official website for macOS.
2. Install virtualenv: You can install virtualenv using pip, the Python package installer. Type `pip3 install virtualenv` in the terminal.
3. Create a new virtual environment: Navigate to your project directory and type `virtualenv env`. This will create a new virtual environment in a folder named "env" in your project directory.
4. Activate the virtual environment: Type `source env/bin/activate` in the terminal. Your prompt should change to indicate that you are now working within a Python virtual environment.

```bash
# Navigate to your project directory
cd your_project_directory

# Install virtualenv
pip3 install virtualenv

# Create a new virtual environment
virtualenv env

# Activate the virtual environment
source env/bin/activate
```

In all cases, you can install any Python packages you need using pip, and they will be installed in the virtual environment, isolated from your global Python installation.

## Install the Required Packages
To install the requirements from a `requirements.txt` file using pip, you can use the `pip install -r` command followed by the path to your `requirements.txt` file. Here's how you can do it:

```bash
pip install -r requirements.txt
```

This command will install all the packages listed in the `requirements.txt` file in your current Python environment.

## Run the Script
To run the script, you can use the `python` command followed by the name of the script file. Here's how you can do it:

```bash
python main.py
```

## TODO 
- [x] Create a script that downloads 2 files from the github and compares them.
- [ ] Add the option to specify the file path, either by local file or by github link. using the -f flag or --file flag. or -u flag or --url flag.
- [ ] Add the option to specify the baseline with -b and the answers with -a
- [ ] General error handling, it will currently break easily
- 