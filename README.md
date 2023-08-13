# Resume Categorization with Classification

This repository contains code and resources for performing resume categorization using classification techniques. The goal is to automatically classify resumes into different categories based on their content.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)

## Introduction

The task of resume categorization is important for various applications, such as job portals, recruitment agencies, and HR departments. This project explores the use of machine learning algorithms for automatically categorizing resumes into 24 different predefined categories, such as "Teacher," "Designer," "Engineering," etc.

## Installation

To use the code in this repository, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Nehlr1/Resume-Categorization-with-Classification.git

2. Run the resume_classification.ipynb file to create the model or use the models from the artifacts folder.

3. Run the script.py
    
   ```bash
   python script.py filepath/

> **Note**
> Here filepath/ indicates the folder where the resumes ,in pdf format, are located to be reorganised into its respective folder 


## Usage
To use the code in this repository, follow these steps:

1. Download the dataset from https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset

2. Preprocess the resume data. This step involves cleaning the text data, removing stopwords, tokenization, etc.

3. Train the classification model. I have chosen from various classification algorithms, such as Logistic Regression, Random Forest, and Gradient Boosting. Experimented with different algorithms and hyperparameters to find the best model for the dataset.

4. Evaluate the model. Used suitable evaluation metric, such as accuracy, precision, recall, or F1-score, to assess the performance of the trained model.

5. Use the trained model (Logistic Regression Model) for resume categorization. Once the model is trained and evaluated, I have use it to predict the category of new resumes.

## File Structure
The file structure of this repository is as follows:

1. resume_classification.ipynb: Jupyter Notebook containing the code for resume categorization. It provides a step-by-step guide and explanations of the code.

2. script.py: Python script version of the code for resume categorization.

3. artifacts/: Directory containing any necessary artifacts or saved models.

4. categorized_resumes.csv: The CSV have two columns named filename and category

## Contributing
Contributions to this project are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Let's make this project better together!