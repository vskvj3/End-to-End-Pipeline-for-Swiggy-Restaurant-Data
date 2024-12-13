'''
This script extracts each item from the menu of each restaurants, category is not added to the output data
'''
import json
import csv

small_data = "../Abohar.json"
big_data = r"C:\Users\285497\Documents\Swiggy Dataset\data.json"

# Load JSON data
file_path = big_data
with open(file_path, "r") as f:
    data = json.load(f)

# Prepare CSV output
output_rows = []
city_name = list(data.keys())[0]
restaurants = data[city_name]["restaurants"]

for restaurant_id, details in restaurants.items():
    restaurant_name = details["name"]
    menu = details.get("menu", {})
    
    for category, items in menu.items():
        for dish_name, dish_details in items.items():
            output_rows.append({
                "Restaurant ID": restaurant_id,
                "Restaurant Name": restaurant_name,
                "Dish Name": dish_name,
                "Dish Price": dish_details["price"],
                "Veg/Non-Veg": dish_details["veg_or_non_veg"]
            })

# Write to CSV
csv_file = "each_item_of_menu.csv"
with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=output_rows[0].keys())
    writer.writeheader()
    writer.writerows(output_rows)

print(f"Menu data extracted to {csv_file}")
