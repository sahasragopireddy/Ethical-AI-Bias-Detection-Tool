# Ethical-AI-Bias-Detection-Tool
Identify and mitigate bias in AI using Streamlit

## Table of Contents
 - [Overview](#overview)
 - [Installation](#installation)
 - [Usage](#usage)

## Overview
This project is a Streamlit-based web app that helps users detect and visualize bias in AI models or datasets. Users can upload datasets, select sensitive attributes (like race or gender), and target labels (like income or other quantitiative features), and the tool will analyze disparities across groups and provide insights.

## Installation
### Clone the repository -
```
git clone git@github.com:sahasragopireddy/Ethical-AI-Bias-Detection-Tool.git
Ethical-AI-Bias-Detection-Tool
```
### Create and activate a virtual environment - 
```
python -m venv venv
source venv/bin/activate   # Mac/Linux  
venv\Scripts\activate      # Windows
```
### Install dependencies - 
```
pip install -r requirements.txt
```

## Usage
### Run the Streamlit app - 
```
streamlit run app.py
```
Open the browser window that appears, upload your dataset, and start exploring bias!
