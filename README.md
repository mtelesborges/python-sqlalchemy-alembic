<p align="center">
  <img src="assets/sqla_logo.png" alt="SQLAlchemy Logo"/>
</p>
<h1 align="center">SQLAlchemy & Alembic</h1>

> This project contain a basic implementation using SQLAlchemy and Alembic

This project uses poetry for environment managing and some libraries for code formatting

## Installing SQLAlchemy and Alembic 

```shell
poetry add SQLAlchemy

poetry add alembic
```

## Configuring alembic
- Initilizing alembic
```shell
alembic init alembic
```

- Configuring alembic database url
```python
# update the file project/alembic/env.py adding the following code before the functions
config.set_main_option('sqlalchemy.url', os.environ.get('DATABASE_URL'))
```

## Migrations
```shell
# creating migration
alembic revision --autogenerate -m "Initial migration"

# executing migrations
alembic upgrade head
```