# python-stuff

Expanding on the contents in here: http://flask.pocoo.org/


## Starting Flask
To start, execute `./run.sh playing_with_flask.sh`.  This will hog the terminal so Ctrl-C will kill the process.
This can be accessed in the browser at `http://localhost:5000`

## Routes/Endpoints
- `/`: default route, returns a page saying `Hello World!`
- `/text`: renders the questions as plain text on the page, with no input capability
- `fancy`: renders the questions using the `template/questions.html` to render quetsions with formatting and inputs.
