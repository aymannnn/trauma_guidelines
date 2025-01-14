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
    <title>{title}</title>
    <link rel="stylesheet" href="../styles.css">
</head>

<body>
    <img src="../logos/trauma_logo.jpeg" alt="generic_logo" class="logo">
    <h1>{title}</h1>
    <button onclick="location.href='../index.html'">Back to Home</button>
    {content}
</body>

</html>
"""

# Create the docs/pages directory if it doesn't exist
os.makedirs("docs/pages", exist_ok=True)

# Generate the HTML files for each category
for filename, title in categories:
    if filename == "adult_trauma_surgery":
        content = """
        <div class="button-container">
            <button onclick="location.href='head.html'">Head</button>
            <button onclick="location.href='neck.html'">Neck</button>
            <button onclick="location.href='chest.html'">Chest</button>
            <button onclick="location.href='abdomen.html'">Abdomen</button>
            <button onclick="location.href='pelvis.html'">Pelvis</button>
            <button onclick="location.href='spine.html'">Spine</button>
            <button onclick="location.href='extremities.html'">Extremities</button>
            <button onclick="location.href='other_adult_trauma.html'">Other Adult Trauma</button>
        </div>
        """
    else:
        content = """
        <ul>
            <!-- Add PDFs for {title} here -->
        </ul>
        """
    with open(f"docs/pages/{filename}.html", "w") as file:
        file.write(category_template.format(title=title, content=content))

print("Category pages generated successfully.")