from scripts.data_manager import ResponseData, Writer
from multiprocessing import Process
import multiprocessing
import numpy as np
from flask import Flask, render_template, request, jsonify

multiprocessing.set_start_method("fork")

PARTICIPANT_ID = 1

class ServerManager:
    def __init__(self):
        self.app = Flask(__name__)
        self.server = None
        self.participant_data = ResponseData("test_id")
        self.setup_routes()

        self.writer = Writer(f"./data/participant_{PARTICIPANT_ID}")

    def setup_routes(self):
        @self.app.route("/")
        def home():
            return render_template("./index.html")

        @self.app.route('/submit_responses', methods=['POST'])
        def submit_responses():
            data = request.json

            if data.get("submitting"):  # Use get to safely access the key
                print("Form submitted - writing data")
                self.writer.write(self.participant_data)

                if self.server is not None:
                    print(type(self.server))
                    # IDK why this isn't working
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
