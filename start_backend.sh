#!/bin/bash

echo "🚀 Starting RetailShield AI Backend..."
echo "📦 Installing dependencies..."

# Install dependencies
pip install -r requirements.txt

echo "🔧 Setting up directories..."
# Create necessary directories
mkdir -p logs
mkdir -p data

echo "🌐 Starting Flask server..."
# Start the Flask application
python app.py
