from flask import Flask
app = Flask(__name__)


# import ...


@app.route('/') # Fill this in!
def index():
  return '<h1>Welcome! Go to puppy_latin/name to see you name in Puppy Latin </>'
@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!
    pupname = ''

    if name[-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
         pupname = name + 'y'

    return "<h1>Hi {}! Your puppylatin name is {} </h1>".format(name,pupname)

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    pass

if __name__ == '__main__':
    app.run()

