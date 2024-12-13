import json

# Load JSON data from the file
with open(r"C:\Users\285497\Documents\Swiggy Dataset\data.json", "r") as file:
    data = json.load(file)

# Function to get data for specific cities and save it to one file
def save_multiple_cities_data(json_data, city_names, output_file):
    # Dictionary to store city data
    all_cities_data = {}

    # Loop over each city and add its data if available
    for city_name in city_names:
        city_data = json_data.get(city_name)
        if city_data:
            all_cities_data[city_name] = city_data
        else:
            print(f"No data available for {city_name}")

    # Save all cities data into one file
    with open(output_file, "w") as out_file:
        json.dump(all_cities_data, out_file, indent=4)
    print(f"Data for selected cities saved to {output_file}")

# Example: Save data for multiple cities into one file
city_names = ["Agartala", "Adoni", "Abohar"]
output_file = "multiple_cities_data.json"
save_multiple_cities_data(data, city_names, output_file)
