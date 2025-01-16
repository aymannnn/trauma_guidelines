Scripts: 

Do NOT re-run generate_pages.py as it will wipe clear all of the pages and reset with nothing.

Reasonably there are two options:

1. Update each HTML for pages individually with the appropriate guidelines
2. Come up with some CSV system where files can easily be added

Option (2) is probably simple, steps should be:

1. New script to ONLY generate the filenames, the HTML structure AND the CSV blank names
2. New script to dynamically write all scripts by looking up the CSV and filling in the HTML

Will do this once we have some test guideline data.