import requests

output = requests.get(input("Enter Url to display its content")).text
for data in output:
    print(data,end='')