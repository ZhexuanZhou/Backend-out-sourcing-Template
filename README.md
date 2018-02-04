# Backend-out-sourcing-Template
flask outsourcing template

## Enviroment settings

1. export FLASK_APP = Template.py
2. flask db init (for database initial)
3. flask db migrate
4. flask db upgrade

## Common issuses

1. Duplicate entry ... fro key ...
- unique key is same to exist one.
2. db import error when use blueprint
- Before import blueprint packages, db should be initialed.
