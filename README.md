# Duplicate-File-Detector

## Overview

The Duplicate File Detector is a machine learning model built with the tkinter library that can identify duplicate image files from a given set of images. The model uses a combination of image processing techniques and feature extraction to find similarities between images and determine which ones are duplicates.

## Dataset

The dataset used to train and test the Duplicate Image Detector consists of multiple image files in different formats (e.g., JPEG, PNG). The dataset should contain both original images and their duplicates for the model to learn the patterns and similarities between them.

## Requirements

- Python (>= 3.6)
- tkinter (Python GUI library)
- NumPy
- Hashlib

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/MadhavJain0119/File-Duplicate-Detector.git
cd File-Duplicate-Detector
``` 

2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

- Ensure you have installed all the dependencies.
- Add the image files to the data/ directory that you want to check for duplicates.
- Run the main.py script for the model to identify duplicate images and display the results.

## Model Evaluation

The model's performance can be evaluated by using a labeled dataset containing known duplicate and non-duplicate image pairs. The evaluation metrics, such as accuracy, precision, recall, and F1 score, have been used to assess the model's ability to correctly identify duplicate images.
