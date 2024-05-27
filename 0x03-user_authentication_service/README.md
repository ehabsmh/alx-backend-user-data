<p align="center">
  <img src="https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png" />
</p>

# This project is to implement a User Authentication system
**You should use `auth_venv` virtual environment as compiler to run python scripts:**
`source auth_venv/bin/activate`

## Tasks
[0. User model]()
In this task you will create a SQLAlchemy model named `User` for a database table named `users` (by using the [mapping declaration](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping) of SQLAlchemy).

The model will have the following attributes:

- `id`, the integer primary key
- `email`, a non-nullable string
- `hashed_password`, a non-nullable string
- `session_id`, a nullable string
- `reset_token`, a nullable string
