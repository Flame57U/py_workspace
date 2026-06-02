import requests
response = requests.get('http://www.github.com')
print(response.status_code)


"""
data = {'key1':'value1','key2':'value2'}
response = requests.post('http://www.github.com', data=data)
"""