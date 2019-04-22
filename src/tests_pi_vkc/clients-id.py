import requests
headers = {"Authorization":"Basic bG9naW5hcmVhOnBhc3NhcmVh", "Accept":"text/plain, application/json, text/json" }
response = requests.get('http://st.nspk.aeroidea.ru:83/api/v2/clients?10', headers=headers)

print(response.text)