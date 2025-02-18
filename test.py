import requests

url = "http://127.0.0.1:8000/services/api/v1/services"


data ={
        "title": "api-new-request",
        "content": "api-con-req",
        "description": "api-desc-req",
        "catalog_file": "cccccccccccccccccccccc",
        "catalog_doc": "fffffffffffffffffff",
        "status": True,
        "creator": 1,
        "specials": [
            1,
            2,
            3
        ],
        "category": [
            2
        ]
    }
response = requests.post(url, data=data)
if response.status_code == 201:
    print ("OOOKKK")
