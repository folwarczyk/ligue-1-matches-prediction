# French Football League Match Outcome Prediction

This project is focused on predicting the outcomes of French Football League matches using various machine learning techniques. The data for this project was sourced from [fbref.com](https://fbref.com) using Python's `read_html` function, which allowed us to create a comprehensive dataset of French League match results.

## Data Collection and Processing

The data was collected from [fbref.com](https://fbref.com), where I used the `read_html` function to scrape match results data. This data was then cleaned and processed appropriately to prepare it for predictive modeling. The preprocessing steps involved handling missing data, converting categorical data into a numerical format, and feature engineering.

## Predictive Modeling

I employed several machine learning models for this task, including a Random Forest classifier, an XGBoost classifier, and a Neural Network built with Keras. Extensive work went into tuning these models and selecting the most relevant features to improve their performance.

## Results

Despite rigorous model tuning and feature selection, the highest accuracy achieved was between 58-60%. This underscores the inherent unpredictability of football matches. While the models performed reasonably well, it's essential to keep in mind that the nature of football is highly volatile, and outcomes can change in an instant, making it a challenging area for predictive modeling.

## Key Learnings

This project underscored the importance of every step in the machine learning workflow, from understanding the problem and collecting data to data cleaning, exploratory analysis, modeling, and result interpretation. It served as a hands-on experience with the complexities and challenges of predicting real-world outcomes, particularly in an unpredictable domain like football.

## Technologies Used

* [Pandas](https://pandas.pydata.org/)
* [Numpy](https://numpy.org/)
* [Scikit-Learn](https://scikit-learn.org/stable/)
* [Keras](https://keras.io/)
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)


## Running the Project
To run the project, you'll need Python along with several packages including Pandas, Numpy, Sklearn, and others. The main code for the project can be found in the Jupyter Notebook file in the jupyter-notebook directory: ligue_1_matches_prediction.ipynb, data preparation code can be found in the file ligue1_web_scraping.

Clone the repository, install the necessary packages, and then you can run the notebook file in a Jupyter Notebook environment. Please make sure you have the required dataset available in your local directory for the notebook to access (you can use the data file located in the data folder, or web scrap your own file and customize it to your needs).


## Contributing

Contributions, issues, and feature requests are welcome. Please provide feedback to help me improve.
