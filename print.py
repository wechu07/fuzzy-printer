import cv2

'''
I will write better comments for each function
'''

list_of_names = []

def cleanup_data():
    with open("names-data.txt") as file:
        for line in file:
            list_of_names.append(line.strip())

def generate_certificates():
    for name in list_of_names:
        template = cv2.('template.jpeg')
        cv2.putText(template, name, (125, 291), cv2.FONT, 1.5. (0, 0, 0), 4, cv2.LINE_AA)
        cv2,inwrite(f'generated-certificates-data/{name}.jpeg', template)

# now we run them
cleanup_data()
generate_certificates()