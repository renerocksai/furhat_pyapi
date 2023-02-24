# furhat_pyapi Skill

This is a minimal sample project to showcase:

- how to expose arbitrary python code as JSON APIs over HTTP, utilizing
  [flask](https://palletsprojects.com/p/flask/) and
  [flask-restful](https://flask-restful.readthedocs.io/en/latest/)
- how to consume said API from a Furhat Skill

It consists of the python project and a Furhat skill project. All the
python-related code is contained in the [python/](python/) subdirectory, while
the rest comprises the Furhat skill.

At runtime, the furhat skill must be able to find the API. At the moment, all
API URLs are hardcoded in the skill (see below for more info).

Also, please note that in this example **no authentication** method is used
yet; I will update to "basic HTTP authentication" as I see fit.

## Python server 

We use the flask module, and also flask_restful for a quick and easy HTTP API
python server.

The functionalities we want to expose, are "greet" which greets a name
(parameter) with a random greeting - and "shuffle" which randomly shuffles the
list of available greetings. That stuff is implemented in
[python/greets.py](python/greets.py).

[python/main.py](python/main.py) shows how to use our independent python
greeting code from within an API server that speaks JSON over HTTP.

Make sure you have the following python packages installed:

- flask
- flask-restful

Install them how you usually install modules for your projects.

To start the development server from the command line:

```shell
$ cd python 
$ python main.py
```
![](img/term.png)

Then point your browser to: 

- [http://localhost:5000/shuffle](http://localhost:5000/shuffle)
- [http://localhost:5000/greet/rene](http://localhost:5000/greet/rene)

... to get a feel for what the server sends back. You see the JSON responses
that the furhat skill will receive.

![](img/browser.png)

## Furhat skill 

After starting the skill, switch to the wizard view of Furhat's web interface.

_(Make sure that the python server is started. See the section above.)_

There, you'll find a button "python" that, when pressed, will fetch the next
random greeting from the python API server - and have Furhat speak it:

```kotlin
    onButton("python") {
        var response = khttp.get("http://localhost:5000/greet/rene");
        var greeting = response.jsonObject.get("greeting");
        print(greeting);
        furhat.say(greeting as String);
    }
```

Note that there's a bit more documentation and links in the Furhat SDK docs, in
the section detailing the Wolfram Alpha API access.

