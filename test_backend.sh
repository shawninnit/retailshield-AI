#!/bin/bash

echo "🧪 Testing RetailShield AI Backend..."

# Test health endpoint
echo "1. Testing health endpoint..."
curl -s http://localhost:5000 | python -m json.tool

echo -e "\n2. Testing API health..."
curl -s http://localhost:5000/api/health | python -m json.tool

echo -e "\n3. Testing login endpoint..."
curl -s -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}' | python -m json.tool

echo -e "\n4. Testing status endpoint..."
curl -s http://localhost:5000/api/status | python -m json.tool

echo -e "\n✅ Backend tests completed!"
