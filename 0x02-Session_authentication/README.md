<p align="center">
  <img src="https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png" />
</p>

# In this project, I'm learning about the authentication process and how to implement Session Authentication on a simple API.

# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)


## Tasks

### [0. Et moi et moi et moi!](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x02-Session_authentication/api/v1/app.py) & (https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x02-Session_authentication/api/v1/views/users.py)
Copy all your work of the 0x06. Basic authentication project in this new folder.

In this version, you implemented a Basic authentication for giving you access to all User endpoints:

- `GET /api/v1/users`
- `POST /api/v1/users`
- `GET /api/v1/users/<user_id>`
- `PUT /api/v1/users/<user_id>`
- `DELETE /api/v1/users/<user_id>`
Now, you will add a new endpoint: `GET /users/me` to retrieve the authenticated `User` object.

- Copy folders `models` and `api` from the previous project `0x06. Basic authentication`
- Please make sure all mandatory tasks of this previous project are done at 100% because this project (and the rest of this track) will be based on it.
- Update `@app.before_request` in `api/v1/app.py`:
  - Assign the result of `auth.current_user(request)` to `request.current_user`
- Update method for the route `GET /api/v1/users/<user_id>` in `api/v1/views/users.py`:
  - If `<user_id>` is equal to me and request.current_user is `None`: `abort(404)`
  - If `<user_id>` is equal to me and request.current_user is not `None`: return the authenticated `User` in a JSON response (like a normal case of `GET /api/v1/users/<user_id>` where `<user_id>` is a valid `User` ID)
  - Otherwise, keep the same behavior

---

