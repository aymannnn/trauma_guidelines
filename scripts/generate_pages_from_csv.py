import os
import csv

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
    <base href="/trauma_guidelines/">
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <img src="logos/trauma_logo.jpeg" alt="generic_logo" class="logo">
    <h1>{title}</h1>
    <button onclick="location.href='index.html'">Back to Home</button>
    {content}
</body>

</html>
"""

all_csv_outputs = [] # Store all csv outputs for later use

# I actually want to add all of the CSV outputs to "all trauma guidelines"

for filename, title in categories:
    if filename == "adult_trauma_surgery":
        content = """
        <div class="button-container">
            <button onclick="location.href='pages/head.html'">Head</button>
            <button onclick="location.href='pages/neck.html'">Neck</button>
            <button onclick="location.href='pages/chest.html'">Chest</button>
            <button onclick="location.href='pages/abdomen.html'">Abdomen</button>
            <button onclick="location.href='pages/pelvis.html'">Pelvis</button>
            <button onclick="location.href='pages/spine.html'">Spine</button>
            <button onclick="location.href='pages/extremities.html'">Extremities</button>
            <button onclick="location.href='pages/other_adult_trauma.html'">Other Adult Trauma</button>
        </div>
        """
    elif filename == "outside_resources":
        content = """
        <div class="button-container">
            <button onclick="location.href='https://www.east.org/education-resources/practice-management-guidelines/category/trauma'">EAST PMG</button>
            <button onclick="location.href='https://www.westerntrauma.org/algorithms.php'">WTA Algorithms</button>
            <button onclick="location.href='https://www.surgicalcriticalcare.net/guidelines.php'">ORMC Surgical Critical Care Guidelines</button>
            <button onclick="location.href='https://app.behindtheknife.org/home'">Behind the Knife</button>
            <button onclick="location.href='https://litfl.com/'">Life in the Fast Lane</button>
            <button onclick="location.href='https://emcrit.org/category/pulmcrit/'">PulmCrit/EMCrit</button>
            <button onclick="location.href='https://www.thebottomline.org.uk/'">The Bottom Line</button>
            <button onclick="location.href='https://rebelem.com/'">RebelEM</button>
            <button onclick="location.href='https://thetraumapro.com/'">The Trauma Pro</button>
            <button onclick="location.href='https://intensivecarenetwork.com/'">Intensive Care Network</button>
            <button onclick="location.href='https://criticalcarereviews.com/index.php'">Critical Care Reviews</button>
            <button onclick="location.href='https://www.wikijournalclub.org/wiki/Main_Page'">Wiki Journal Club</button>
            <button onclick="location.href='https://www.orthobullets.com'">Ortho Bullets</button>
        </div>
        """
    elif filename != "all_guidelines":
        csv_path = f"../docs/csvs/{filename}.csv"
        content = "<div>\n"
        if os.path.exists(csv_path):
            with open(csv_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    text, pdf_path = row
                    pdf_path = 'test_pdfs/' + pdf_path
                    all_csv_outputs.append((text, pdf_path))
                    content += f'    <div><a href="{pdf_path}">{text}</a></div>\n'
        content += "</div>"
    else:
        if filename != 'all_guidelines':
            print(f"Error: {filename} entered this path.")
        continue
    with open(f"../docs/pages/{filename}.html", "w") as file:
        file.write(category_template.format(title=title, content=content))

# now do all_guidelines

all_content = "<div>\n"
all_csv_outputs.sort(key=lambda x: x[0])
for text, url in all_csv_outputs:
    all_content += f'    <div><a href="{url}">{text}</a></div>\n'
    all_content += "</div>"

with open(f"../docs/pages/all_guidelines.html", "w") as file:
    file.write(category_template.format(title="All Guidelines", content=all_content))

with open("all_csv_search.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all_csv_outputs)

print("Updated all pages successfully.")