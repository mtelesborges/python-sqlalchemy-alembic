<h1 align="center">
  <img src="assets/sqla_logo.png" alt="SQLAlchemy Logo"/>
</h1>

> This project contain a basic implementation using SQLAlchemy and Alembic

*This project uses poetry for environment managing and some libraries for code formatting*

## Installing SQLAlchemy and Alembic 

```shell
poetry add SQLAlchemy

poetry add alembic
```

## Configuring alembic
- Initilizing alembic
```shell
# inside the project folder, run the following code
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

## Tests
```shell
# inside the poetry environment, run the following code
task test
```