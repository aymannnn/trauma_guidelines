import os

# Define the categories and their corresponding titles
categories = [
    ("all_guidelines", "All Guidelines"),
    ("adult_trauma_surgery", "Adult Trauma Surgery"),
    ("head", "Head"),
    ("neck", "Neck"),
    ("chest", "Chest"),
    ("abdomen", "Abdomen"),
    ("pelvis", "Pelvis"),
    ("spine", "Spine"),
    ("extremities", "Extremities"),
    ("other_adult_trauma", "Other Adult Trauma"),
    ("pediatric_trauma_surgery", "Pediatric Trauma Surgery"),
    ("orthopedic_surgery", "Orthopedic Surgery"),
    ("neurosurgery", "Neurosurgery"),
    ("emergency_medicine", "Emergency Medicine"),
    ("ent", "ENT"),
    ("vascular_surgery", "Vascular Surgery"),
    ("administrative", "Administrative"),
    ("outside_resources", "Outside Resources")
]

# Create the docs/pages directory if it doesn't exist
os.makedirs("docs/pages", exist_ok=True)
os.makedirs("docs/csvs", exist_ok=True)

# Generate the HTML files for each category
for filename, title in categories:
    with open(f"docs/pages/{filename}.html", "w") as file:
        file.write('')

# Generate the CSV files for each category
for filename, title in categories:
    with open(f"docs/csvs/{filename}.csv", "w") as file:
        file.write("")

print("Category pages and CSVs generated successfully.")