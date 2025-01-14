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

# Template for the category pages
category_template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Guidelines</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <h1>{title}</h1>
    <ul>
        <!-- Add PDFs for {title} here -->
    </ul>
    <button onclick="location.href='index.html'">Back to Home</button>
</body>

</html>
"""

# Create the docs directory if it doesn't exist
os.makedirs("docs", exist_ok=True)

# Generate the HTML files for each category
for filename, title in categories:
    with open(f"docs/{filename}.html", "w") as file:
        file.write(category_template.format(title=title))

print("Category pages generated successfully.")