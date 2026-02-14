# 46. AWS SAM CURL


```bashcurl -H "x-api-key: <API_KEY>" https://vmjjx0ik5b.execute-api.eu-central-1.amazonaws.com/dev/car
[]
```
```bash
curl -H "x-api-key: <API_KEY>" https://vmjjx0ik5b.execute-api.eu-central-1.amazonaws.com/dev/car -X POST -d @data.json
OK
```
```bash
curl -H "x-api-key: <API_KEY>" https://vmjjx0ik5b.execute-api.eu-central-1.amazonaws.com/dev/car
[{"Cars_brand": "BMW", "Cars_model": "X5", "Cars_id": "CAR#c0a9daea-06bb-11f1-a427-417a3675e050", "Cars_year": "2023"}]
```