from scripts.data_manager import ResponseData
from multiprocessing import Process
import multiprocessing
import numpy as np
from flask import Flask, render_template, request, jsonify

multiprocessing.set_start_method("fork")

class ServerManager:
    def __init__(self):
        self.app = Flask(__name__)
        self.server = None
        self.participant_data = ResponseData("test_id")
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/")
        def home():
            return render_template("./index.html")

        @self.app.route('/submit_responses', methods=['POST'])
        def submit_responses():
            data = request.json

            if data.get("submitting"):  # Use get to safely access the key
                print("Form submitted")
                if self.server is not None:
                    print(type(self.server))
                    self.server.terminate()
                    self.server.join()

            self.participant_data.add_response(data)
            print(np.matrix(self.participant_data.responses))

            return jsonify({"status": "success"})

    def run_app(self):
        self.app.run()

    def start_server(self):
        self.server = Process(target=self.run_app)
        self.server.start()

if __name__ == '__main__':
    manager = ServerManager()
    manager.start_server()

# app = Flask(__name__)
# server = None

# participant_data = ResponseData("test_id")

# @app.route("/")
# def home():
#     return render_template("./index.html")

# @app.route('/submit_responses', methods=['POST'])
# def submit_responses():
#     global server
#     data = request.json

#     if data["submitting"]:
#         print("Form submitted")
#         server.terminate()
#         server.join()

#     participant_data.add_response(data)
#     print(np.matrix(participant_data.responses))

#     return jsonify({"status": "success"})

# def run_app():
#     app.run()

# if __name__ == '__main__':
#     server = Process(target=run_app)
#     server.start()