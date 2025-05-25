import json


def load_login_data(json_path="data/login_data.json"):
    with open(json_path, "r") as file:
        raw_data = json.load(file)
        cleaned_data = []
        for entry in raw_data:
            try:
                cleaned_data.append((entry["username"], entry["password"], entry["expected"]))
            except KeyError as e:
                print(f"Skipping entry due to missing key: {e} in {entry}")
        return cleaned_data

def load_login_data_invalid(json_path="data/login_data_invalid.json"):
    with open(json_path, "r") as file:
        raw_data = json.load(file)
        cleaned_data = []
        for entry in raw_data:
            try:
                cleaned_data.append((entry["username"], entry["password"], entry["expected"]))
            except KeyError as e:
                print(f"Skipping entry due to missing key: {e} in {entry}")
        return cleaned_data