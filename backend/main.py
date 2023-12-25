from flask import Flask, request, jsonify
from db_builder import DbBuilder
from searcher import Searcher
from flask_cors import CORS


class MyFlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.setup_routes()
        self.searcher = Searcher('user', '123456', 'melingo-db', 'postgres')
        self.db_builder = DbBuilder('user', '123456', '5432', 'melingo-db', 'postgres')
        try:
            self.db_builder.update_db('files')
        except Exception as e:
            print(f"An exception occurred: {type(e).__name__}: {e}")

    def setup_routes(self):
        self.app.route('/search')(self.search)
        self.app.route('/')(self.homepage)

    def homepage(self):
        return "homepage"

    def search(self):
        word = request.args.get('word', '')
        json_dict = {
            "translation": self.searcher.get_translation(word),
            "examples": self.searcher.get_examples(word)
        }
        return jsonify(json_dict)

    def run(self):
        self.app.run(debug=True,host="0.0.0.0")


if __name__ == '__main__':
    my_app = MyFlaskApp()
    my_app.run()
