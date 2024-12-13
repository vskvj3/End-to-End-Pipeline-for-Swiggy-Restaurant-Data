import json
import csv
 
# Load the JSON file
with open(r"C:\Users\285497\Documents\Swiggy Dataset\data.json", 'r') as file:  # Replace with your JSON file path
    data = json.load(file)
 
# Create a list to store the flattened records
records = []
 
# Iterate over the JSON structure to extract relevant fields
for city, city_data in data.items():
    if 'restaurants' in city_data:
        for restaurant_id, restaurant_data in city_data['restaurants'].items():
            if 'menu' in restaurant_data:
                for category, items in restaurant_data['menu'].items():
                    for item_name, item_data in items.items():
                        record = {
                            'Category': category,
                            'Price': item_data.get('price', ''),
                            'id': f"{restaurant_id}_{item_name.replace(' ', '_')}",
                            'Veg_or_Non_Veg': item_data.get('veg_or_non_veg', ''),
                            'Item_Name': item_name,
                            'Restaurant_ID': restaurant_id
                        }
                        records.append(record)
 
# Define the output CSV file path
output_csv = "data.csv"  # Replace with your desired CSV file path
 
# Save the records to a CSV file
with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    # Define the fieldnames (CSV column headers)
    fieldnames = ['Category', 'Price', 'id', 'Veg_or_Non_Veg', 'Item_Name', 'Restaurant_ID']
   
    # Create a writer object
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   
    # Write the header row
    writer.writeheader()
   
    # Write the data rows
    writer.writerows(records)
 
print(f"CSV file saved successfully at: {output_csv}")