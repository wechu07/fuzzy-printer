# Read the file content
with open('volunteer names 2024 LNMB.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Process each line to remove numbering
cleaned_lines = []
for line in lines:
    # Remove the numbering and leading/trailing whitespace
    cleaned_line = line.split(' ', 1)[-1].strip()
    cleaned_lines.append(cleaned_line)

# Write the cleaned names to a new file
with open('cleaned_volunteer_names.csv', 'w', encoding='utf-8') as file:
    for cleaned_line in cleaned_lines:
        file.write(cleaned_line + '\n')