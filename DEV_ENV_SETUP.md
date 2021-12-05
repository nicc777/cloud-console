# Setting up a Development Environment

This project is a Python 3 project and as such you need a fairly new version of Python 3

# Create a Python Virtual Environment

After cloning this repository, change into the project directory and create a virtual environment:

```shell
git clone https://github.com/nicc777/cloud-console.git

cd cloud-console

python3 -m venv venv

source venv/bin/activate

python3 -m pip install --upgrade build twine coverage pylint rope
```

Remember to set this virtual environment in VSCode or your favorite IDE as well.

# Unit Testing

To run unit tests at this stage, simply run:

```shell
python3 -m unittest tests/*.py
```

# Build and Manual UI Testing

Build with the following command:

```shell
python3 -m build
```

The following command will install the new build in a virtual environment in `~/tmp/venv` (*nix only):

```shell
./test_launcher.sh
```

In a separate terminal window, you can now test with the following commands:

```shell
cd ~/tmp

source venv/bin/activate

venv/bin/cloudconsole
```


