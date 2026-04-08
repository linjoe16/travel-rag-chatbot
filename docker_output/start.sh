#!/bin/bash

echo "Installing dependencies..."
pip install azure-search-documents azure-core

echo "Starting PromptFlow..."
pf flow serve --host 0.0.0.0 --port $PORT