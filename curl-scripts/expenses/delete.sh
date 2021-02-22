#!/bin/bash

curl "http://localhost:8000/expenses/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
