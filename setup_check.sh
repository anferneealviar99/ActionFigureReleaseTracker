#!/bin/bash

echo "--- Development Environment Setup Check ---"

echo "Python: $(python --version 2>/dev/null || echo "Python not found")"
echo "Node.js: $(node --version 2>/dev/null || echo "Not installed")"
echo "npm: $(npm --version 2>/dev/null || echo "Not installed")"
echo "Git: $(git --version 2>/dev/null || echo "Not installed")"
echo "Docker: $(docker --version 2>/dev/null || echo "Not installed")"
echo "Terraform: $(terraform --version 2>/dev/null | head -n 1 || echo "Not installed")"

