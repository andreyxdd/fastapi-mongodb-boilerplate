# Template starter project based on FastAPI and MongoDB

## Structure

- api: for implementing endpoints
- core: general settings of the project, i.e. initiating environmental variables
- db: for establishing a connection to MongoDB and implementing methods for CRUD operations
- utils: general utility folder, e.g. useful methods to handle date-time objects and sending emails (via smtplib)
- ```main.py```: script to initiate the server, open/close connection to db

## Launching
First, initiate the virtual environment in the root folder. Then install all the necessary packages with:
```
pip install -r requirements.txt
```
Then start the FastAPI app with:
```
uvicorn main:app --reload
```

## Linting and pre-commit hooks

This template project also utilizes the pre-commit hooks (see ```.pre-commit-config.yaml``` for details). The ```pylint``` is selected as a default linter. To avoid certain warnings, create (or generate) ```.pylintrc``` in the root folder. Make sure the below settings are added to this file:
```
[MASTER]
init-hook='import sys; sys.path.append("global/path/to/root/directory")'
[BASIC]
good-names=i, df, e, ist, db
```
Besides running ```pylint```, the pre-commit hooks upgrade packages with ```pyupgrade``` and check code for formating with ```black```.

It is recommended to initiate the linter tool in the code editor. For example, in VSCode, press ```ctrl+shift+p```, search for ```Select linter``` and choose ```pylint```.

## Other notes
In the code, certain ```pylint``` warnings are disabled:
- ```E1136``` relates to the issues with ```Optional``` and ```Union``` types from ```typings```
- ```E0401``` is a ```pylint``` error for some imported modules
