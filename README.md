# Guess the Disney Character API

## Config

To get the API up and running, you'll need to configure a Secret Key in a `config.py` file.

```py
# config.py
TESTING = True
DEBUG = True
FLASK_ENV = 'development'
SECRET_KEY = {SECRET_KEY}
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = "True"
```

## Dockerfile

To build the Docker image, use the following commands to make it easier to run locally.

```powershell
docker build -t docker/flask-app .
```

```powershell
docker run -it -p 8000:8000 -d docker/flask-app
```

The API should be running on `http://localhost:8000`.

## API

The base URL is `http://localhost:8000/api`.

### `/start`

Starts a game and stores session data. Returns a message confirmation of the game starting.

### `/question`

Returns a randomly generated question, and provides a correct answer from one of the options.

Returns an object containing the options for a question and an ID from the options which is the correct answer.

```json
{
  "correct_id": 793,
  "options": [
    {
      "appearance": "Kronk's New Groove",
      "id": 4736,
      "img": "https://static.wikia.nocookie.net/disney/images/a/a3/Ms._Birdwell_full_body_shot.png",
      "name": "Ms. Birdwell"
    },
    {
      "appearance": "Christopher Robin (film)",
      "id": 2663,
      "img": "https://static.wikia.nocookie.net/disney/images/2/29/Christopher-Robin.jpg",
      "name": "Giles Winslow Jr."
    },
    {
      "appearance": "Recess: School's Out",
      "id": 793,
      "img": "https://static.wikia.nocookie.net/disney/images/5/5d/Char_30580.jpg",
      "name": "Ashley B."
    },
    {
      "appearance": "The Cheetah Girls",
      "id": 6161,
      "img": "https://static.wikia.nocookie.net/disney/images/8/83/Channel_MainInfobox.jpg",
      "name": "Chanel Simmons"
    }
  ]
}
```

### `/score/<int:user_guess_id>`

Takes the ID of the character that the user has guessed and validates this against the session's correct answer for the given question.

Returns the next question number.

Example output:

```JSON
{"question_no": 2}
```

### `/finish`

Returns the total score for a player.

```JSON
{"score": 7}
```
