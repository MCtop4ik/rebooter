import requests
import json


def get_tales_info():
    tales_info = {}
    for i in range(1, 46):
        try:
            resp = requests.get(f"http://localhost:3000/v1/tale?id={i}").json()
            tales_info[str(i)] = resp
        except Exception as e:
            tales_info[str(i)] = None
    return tales_info


def get_all_tales():
    labels = ['tiny', 'small', 'medium', 'big']
    values = [300, 600, 900, 1200]
    all_tales = {}
    for i in range(4):
        try:
            resp = requests.get(f"http://localhost:3000/v1/get_tales?timestamp=morning&width={values[i]}").json()
            all_tales['all_tales_' + labels[i]] = resp
        except Exception as e:
            all_tales['all_tales_' + labels[i]] = None
    return all_tales


def get_grammar():
    try:
        resp = requests.get(f"http://localhost:3000/v1/glossary").json()
        return resp
    except Exception as e:
        return None


# Construct the full JSON structure
full_data = {
    "tales": get_tales_info(),
    "all_tales": get_all_tales(),
    "grammar": get_grammar()
}

# Convert the data structure to a JSON string
full_json = json.dumps(full_data, indent=4)

# Print the JSON string
print(full_json)
