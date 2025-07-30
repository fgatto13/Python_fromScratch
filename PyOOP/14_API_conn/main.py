# to make an API request, we need the requests module
import requests
import json

# let's create a global variable for the URL
base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    # we first want to complete the URL:
    url = f"{base_url}/pokemon/{name}"
    # then, to make an API request, we use the get method
    response = requests.get(url) # it'll return a response object
    # the response contains an HTTP status code (200, 400, 500)
    if response.status_code == 200:
        print("Success")
        # the content is passed as a JSON,
        # so it can be converted to a dictionary in Python
        data = response.json()
        # being a JSON, we could also insert it in a JSON file
        return data
    else:
        # we can print the status code to check the error
        print(f"Fail to retrieve data: {response.status_code}")
        return None

# we can store locally data using a JSON file
def save_data(data):
    file_name = "data.json"
    try:
        with open(file_name, "w") as file:
            json.dump(data, file)
    except FileNotFoundError:
        print(f"File {file_name} not found.")

def main():
    pokemon_name = input("Enter pokemon name: ")
    pokemon_info = get_pokemon_info(pokemon_name)
    # we first check if the dictionary exists
    if pokemon_info:
        print(f"Pokemon info: \n"
              f"Name: {pokemon_info["name"]}\n"
              f"ID: {pokemon_info["id"]}")
        save_data(pokemon_info)
    else:
        print("Pokemon not found")

if __name__ == "__main__":
    main()