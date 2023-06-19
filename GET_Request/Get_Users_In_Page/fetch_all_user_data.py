import requests
import json
import jsonpath


def fetch_and_save_json(url, output_file):
    try:
        # Send GET request and retrieve JSON delete_response
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()

        # Parse JSON delete_response
        json_data = response.json()

        # Write JSON data to a file
        with open(output_file, "w") as file:
            json.dump(json_data, file)

        # Read JSON data from the file and return it
        with open(output_file, "r") as file:
            read_data = file.read()
            return read_data

    except requests.exceptions.RequestException as e:
        # Handle any network-related errors
        print("Error occurred during the HTTP request:", e)

    except IOError as e:
        # Handle file-related errors
        print("Error occurred while working with the file:", e)

    except json.JSONDecodeError as e:
        # Handle JSON parsing errors
        print("Error occurred while parsing JSON delete_response:", e)


# Example usage:
url = "https://reqres.in/api/users/2"
output_file = "single_user.json"

result = fetch_and_save_json(url, output_file)
if result is not None:
    print(result)
