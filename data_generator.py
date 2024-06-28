import random

# Define product categories
categories = ["Electronics", "Clothing", "Beauty", "Home", "Toys"]

# Function to generate random review text
def generate_review(i):
  if i==1:
    words = ["Great product!", "Love it!", "Would recommend", "Easy to use"]
  else:
    words = ["Bad product!", "Waste of Money", "Disappointed",  "Not Easy to use"," Would not recommend"]

  return ", ".join(random.sample(words, 2))

# Generate data
data = []
for _ in range(10):
  # Choose first entity type
  entity_type = "Product" if random.random() < 0.8 else "Customer"
  
  if entity_type == "Product":
    # Choose relationship for product
    relationship = random.choice(["belongs_to_category", "has_review"])
    entity_type = f"Product_{random.randint(1, 100)}"
    if relationship == "belongs_to_category":
      # Second entity is category name
      second_entity = random.choice(categories)
    else:
      # Second entity is customer ID and review text
      customer_id = f"CUST_{random.randint(1, 10000)}"
      review = generate_review(random.randint(0,1))

      second_entity = (customer_id, review)
      
  else:
    # Choose relationship for customer
    relationship = random.choice(["purchased", "viewed"])
    
    # Second entity is product ID
    second_entity = f"Product_{random.randint(1, 100)}"
  
  data.append((entity_type, relationship, second_entity))

  
import pandas
df = pandas.DataFrame(data=data, columns=["entity_type", "relationship", "second_entity"])
df.to_csv("ecommerce_data.csv", sep=',',index=False)

# Print a sample of the data
# print(data[:10])