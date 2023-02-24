from flask import (
    Flask,
    jsonify,
    make_response,
    # request,
)

from flask_restful import (
    Api,
    Resource,
)

from greets import greet

app = Flask(__name__)
api = Api(app)


class GreetApi(Resource):
    def get(self, name):
        # we return a dict, converted to JSON
        return make_response(jsonify({
            'result': greet(name),
            'status': 'OK',
            }))


class ShuffleApi(Resource):
    def get(self):
        # we return a dict, converted to JSON
        return make_response(jsonify({
            'status': 'OK',
            }))


api.add_resource(GreetApi, "/greet/<string:name>", endpoint="Greet")
api.add_resource(ShuffleApi, "/shuffle", endpoint="Shuffle")


# we don't need Resources, we can also just call on slugs
@app.route("/")
def get():
    # return make_response(app.send_static_file("index.html"))
    return make_response(jsonify({
        'status': 'Not implemented',
        }))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
