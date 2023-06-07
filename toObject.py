import json

def filter_json_by_keywords(json_file_path, keywords):
    with open(json_file_path, encoding='utf-8') as file:
        data = json.load(file)

    data_tweets = [tweet['full_text'] for tweet in data]
    filtered_data = [value for value in data_tweets if any(keyword in value.lower() for keyword in keywords)]

    return filtered_data

json_file_paths = [
    r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\GTP\json\corpus1.json',
    r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\GTP\json\corpus2.json',
    r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\GTP\json\corpus3.json',
    r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\GTP\json\corpus4.json',
    # Agrega aquí más paths de archivos JSON
]

keywords = ['cuarentena', 'covid', 'coronavirus', 'pandemia']

all_filtered_data = []

for json_file_path in json_file_paths:
    filtered_data = filter_json_by_keywords(json_file_path, keywords)
    all_filtered_data.extend(filtered_data)
    


print(len(all_filtered_data))

all_filtered_data2 = all_filtered_data[121:]
print(len(all_filtered_data2))