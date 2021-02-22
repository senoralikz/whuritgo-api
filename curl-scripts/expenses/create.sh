#!/bin/bash

curl "http://localhost:8000/expenses/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "expense": {
      "item": "'"${ITEM}"'",
      "quantity": "'"${QUANTITY}"'",
      "date": "'"${DATE}"'",
      "cost": "'"${COST}"'"
    }
  }'

echo
