import requests
import csv

# Define the API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Send the GET request to fetch the data
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response

    # Specify the CSV file name
    csv_file = 'posts.csv'

    # Open the CSV file to write data
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        header = data[0].keys()  # Use the keys from the first dictionary as headers
        writer.writerow(header)
        
        # Write each row of data
        for post in data:
            writer.writerow(post.values())

    print(f"Data has been written to {csv_file}")
else:
    print("Failed to retrieve data:", response.status_code)
