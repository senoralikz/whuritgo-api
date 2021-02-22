#!/bin/bash

curl "http://localhost:8000/expenses/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
