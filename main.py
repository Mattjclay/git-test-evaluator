import requests
import json
import pprint

# This is the link to the user's test answers
# This will not work with private repositories, you will need to copy the blob link from the file
# on a public repository
user_test = 'https://github.com/Mattjclay/prototype-data/blob/44709a6149cb8a326c4b6d42652bc1430c9f54b2/test1'
# This is the baseline test, the correct answers
test_baseline = 'https://github.com/Mattjclay/prototype-data/blob/7a3ce4551085d51c36d351d7d337741a4362e2bd/test_baseline'

# Initialize empty dictionaries
user_test_dict = {}
test_baseline_dict = {}

# Send a GET request to the URL for the user's test answers
response = requests.get(user_test)

# Check if the request was successful
if response.status_code == 200:
    # Load the response text as a JSON object
    json_object = json.loads(response.text)

    # Convert the JSON object into a dictionary
    user_test_dict = dict(json_object)
else:
    print(response.status_code)

# Send a GET request to the URL for the baseline test answers
response_baseline = requests.get(test_baseline)

# Check if the request was successful
if response_baseline.status_code == 200:
    # Load the response text as a JSON object
    json_object = json.loads(response_baseline.text)

    # Convert the JSON object into a dictionary
    test_baseline_dict = dict(json_object)
else:
    print(response_baseline.status_code)

# Extract the rawLines from the dictionaries (the test answers)
rawLines = user_test_dict.get('payload').get('blob').get('rawLines')
rawLines_baseline = test_baseline_dict.get('payload').get('blob').get('rawLines')

# Converting from list to dictionary
user_test_dict = {item.split(') ')[0]: item.split(') ')[1] for item in rawLines}
test_baseline_dict = {item.split(') ')[0]: item.split(') ')[1] for item in rawLines_baseline}

# Initialize a counter for different values, figuring out how many questions were missed
missed_questions = 0

# Iterate over the keys in user_test_dict
for key in user_test_dict.keys():
    # Check if the key is in the test_baseline_dict
    if key in test_baseline_dict:
        # Compare the values of the key in both dictionaries
        if user_test_dict[key] != test_baseline_dict[key]:
            # If the values are different, increment the counter
            missed_questions += 1

# Print the number of missed questions
print("You missed " + str(missed_questions) + " questions")

# Calculate the total number of keys in test_baseline_dict
total_keys = len(test_baseline_dict)

# Calculate the percentage of different values
percentage_different_values = 100 - (missed_questions / total_keys) * 100

# Print the percentage
print("The percentage correct is " + str(percentage_different_values) + "%")
