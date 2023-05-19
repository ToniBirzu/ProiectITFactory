# API Proiect Final IT Factory #

This API allows you to see users and interact with them.

The API is available at 'https://reqres.in/'

## Endpoints ##

### List of users on page 1 ###

GET '/users?page=1'

Returns a list of users and data that are on page 1

Optional querry parameters:
- limit: a number between 1 and 6


### Get a single user ###

GET `/users/?id=2`

Retrieve detailed information about a user.


### Create a user ###

POST `/users`

Allows you to create a new user.

The request body needs to be in JSON format and include the following properties:

 - `name` - 
 - `job` - 

Example
```
POST /users/

{
  "name": "florin",
  "job": "leader"
}
```

The response body will contain the order Id and createdAt


### Update an user ###

PATCH `/users/2`

Update an existing user. 

The request body needs to be in JSON format and allows you to update the following properties:

 - `name` - 
 - `job` - 

 Example
```
{
  "name": "neo",
  "job": "the chosen one"
}
```


## API Register Successful ##

POST `/register`

The request body needs to be in JSON format and include the following properties:

 - `email` - String
 - `password` - String

 Example

 ```
 {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
 ```

The response body will contain the Id and access token.

**Possible errors**

Status code 400 - "error": "Missing password". Enter a password.

Status code 400 - "error": "Missing email or username". Enter email.

Status code 400 - "error": "Note: Only defined users succeed registration". Enter the corect email
