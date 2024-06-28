import csv
import random

# Define entities and relationships
entities = ["Product", "Customer", "Category", "Order", "Review"]
relationships = ["bought", "reviewed", "belongs to", "includes", "mentioned in"]

# Set number of records
num_records = 25000

# Open CSV file for writing
with open("simulated_data.csv", 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(["First Entity", "Relationship", "Second Entity"])

  # Generate random data
  for _ in range(num_records):
    first_entity = random.choice(entities)
    relationship = random.choice(relationships)
    second_entity = random.choice(entities)
    
    # Avoid creating nonsensical relationships (e.g., Order reviewing Product)
    if (first_entity == "Order" and relationship == "reviewed") or \
       (first_entity == "Review" and (relationship == "bought" or relationship == "includes")):
      continue

    writer.writerow([first_entity, relationship, second_entity])

print(f"Successfully generated simulated_data.csv with {num_records} records!")
