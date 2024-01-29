# langchain_math

## Python Mathematical Tools 

### Overview
This repository contains two Python scripts designed for mathematical calculations and operations. The scripts utilize the OpenAI GPT-4 model and various other libraries to perform advanced mathematical tasks and provide a user-friendly interface for complex calculations.

### Files in Repository
math_app.py
circle.py

# 1. math_app.py
Description
math_app.py is designed to perform a variety of mathematical operations. It integrates the OpenAI GPT-4 model for advanced computational capabilities. This script is particularly focused on solving complex mathematical problems, possibly including geometry, algebra, and calculus.

### Features
Integration with OpenAI GPT-4 for advanced calculations.
Support for complex mathematical operations.
Environment variable management for API keys and configurations.

### Usage
To use math_app.py, ensure that you have the OpenAI API key set in your environment. The script requires external libraries such as langchain, math, os, and sys. Run the script in a Python environment where these dependencies are satisfied.

# 2. circle.py
Description
circle.py is a specialized tool for calculations related to circles. It can compute circumferences and other related metrics, providing an easy-to-use interface for common circular calculations.

### Features
Circumference calculation using the radius of a circle.
Integration with OpenAI GPT-4 for complex reasoning and calculations.
Conversational memory feature for enhanced user interaction.

### Usage
Before running circle.py, ensure that the necessary environment variables are set, including the OpenAI API key. The script uses libraries like langchain, math, and typing. Ensure these are installed and accessible in your Python environment.

### Installation and Requirements
Both scripts require Python 3.x and several external libraries, including openai, langchain, and dotenv. Make sure to install these dependencies using pip:


pip install openai langchain python-dotenv
Additionally, you need to have an OpenAI API key and set it as an environment variable:

export OPENAI_API_KEY='your_api_key_here' 
