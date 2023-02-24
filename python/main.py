from flask import (
    Flask,
    jsonify,
    make_response,
    request,
)
from flask_restful import Api, Resource, reqparse, fields, marshal, inputs

app = Flask(__name__)
api = Api(app)



class DemoApi(Resource):

    def __init__(self):
        self.count = len(greets)

    def get(self, greetid):
        if greetid in greets:
            return make_response(jsonify(greets[greetid]))

    def post(self):
        body = request.json
        first_name = body.get("first_name", None)
        last_name = body.get("last_name", None)

        if first_name is not None and last_name is not None:
            self.count += 1
            greets[self.count] = {
                'id': self.count,
                'first_name': first_name,
                'last_name': last_name,
                }
            return make_response(jsonify({'status': 'OK', 'id': self.count}))

    def put(self, greetid):
        if greetid in greets:
            body = request.json
            first_name = body.get("first_name", None)
            last_name = body.get("last_name", None)

            if first_name is not None and last_name is not None:
                greets[greetid]['first_name'] = first_name
                greets[greetid]['last_name'] = last_name
                return make_response(jsonify({'status': 'OK', 'id': greetid}))

    def delete(self, greetid):
        if greetid in greets:
            del greets[greetid]
            return make_response(jsonify({'status': 'OK', 'id': greetid}))


api.add_resource(DemoApi, "/greets/<int:greetid>", endpoint="Demo")
api.add_resource(DemoApi, "/greets", endpoint="Demox")


@app.route("/")
def get():
    return make_response(app.send_static_file("index.html"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
