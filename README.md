# Template starter project based on FastAPI and MongoDB

## Structure

- api: for implementing endpoints
- core: general settings of the project, i.e. initiating environmental variables
- db: for establishing a connection to MongoDB and implementing methods for CRUD operations
- utils: general utility folder, e.g. useful methods to handle date-time objects and sending emails (via smtplib)
- ```main.py```: script to initiate the server, open/close connection to db

## Launching
To launch the project, first install all the requirements (preferably after creating a virtual environment):
```
pip install -r requirements.txt
```

Then start the FastAPI app with:
```
uvicorn main:app --reload
```

## Other notes
This template project also utilizes the pre-commit hooks. For details see ```.pre-commit-config.yaml```
