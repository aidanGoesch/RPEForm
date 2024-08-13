import pandas as pd

# Write this later
class ResponseData:
    def __init__(self, participant_id) -> None:
        self.id  = participant_id
        self.responses = []

    def add_response(self, submission : dict) -> None:
        self.responses.append([value for value in list(submission.values())[:-1]])


class Loader:
    def __init__(self) -> None:
        pass


class Writer:
    def __init__(self, file_path : str) -> None:
        self.file = file_path

    def write(self, data : ResponseData) -> None:
        df = pd.DataFrame(data.responses)

        df.to_csv(self.file)