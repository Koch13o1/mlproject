# End to End Machine Learning Project

## Student Math Score Prediction - Machine Learning Pipeline

This project is a modular machine learning pipeline designed to predict a student's math score based on various input features. The project follows a structured Software Development Life Cycle (SDLC) approach, ensuring modularity, scalability, and maintainability. The pipeline includes data ingestion, data transformation, model training, and prediction, with custom logging and exception handling for better debugging. The application is deployed on AWS Elastic Beanstalk using AWS Codepipeline. It has a Flask-based web interface.

## Project Structure

The project is structured as follows:

```
student_math_score_prediction/
├── artifacts/                     # Stores processed data, models, and transformation pipelines
│   ├── data/                      # Train and test datasets
│   ├── models/                    # Trained models saved as pickle files
│   └── transformers/              # Column transformers saved as pickle files
├── src/                           # Source code for the ML pipeline
│   ├── components/                # Modular components of the pipeline
│   │   ├── data_ingestion.py      # Handles data ingestion and splitting
│   │   ├── data_transformation.py # Handles data preprocessing and transformation
│   │   └── model_trainer.py       # Handles model training and evaluation
│   ├── pipeline/                  # Prediction pipeline for transforming and predicting data
│   │   ├── prediction_pipeline.py
│   ├── exception/                 # Custom exception handling
│   ├── logger/                    # Custom logging
│   └── utils.py                   # Utility functions (e.g., model evaluation)
├── application.py                 # Flask application for serving predictions
├── setup.py                       # Package setup file
├── requirements.txt               # Dependencies for the project
├── .ebextensions/                 # AWS Elastic Beanstalk configuration
│   └── python.config              # WSGI server configuration
└── README.md                      # Project documentation
```

## Key Features

### Modular Pipeline:
- **Data Ingestion:** Reads raw data, splits it into train and test sets, and stores them in the artifacts folder.
- **Data Transformation:** Handles missing values, scales numerical features, and encodes categorical features using ColumnTransformer. The transformation pipeline is saved as a pickle file.
- **Model Training:** Trains multiple regression models using GridSearchCV for hyperparameter tuning. The best model is selected based on the R² score and saved as a pickle file.
- **Prediction Pipeline:** Takes input data, applies the saved transformation pipeline, and predicts the math score using the trained model.

### Custom Logging and Exception Handling:
- Logs are generated at each step of the pipeline for better debugging and tracking.
- Custom exceptions are raised to handle errors gracefully.

### Flask Application:
- A REST API is built using Flask to serve predictions.
- The `/predictdata` endpoint accepts a POST request with input data and returns the predicted math score.

### AWS Elastic Beanstalk Deployment:
- The application is deployed on AWS Elastic Beanstalk using a WSGI server.
- A custom `python.config` file in the `.ebextensions` folder configures the deployment environment.

### Package Setup:
- The project can be shipped as a Python package using `setup.py`.
- Dependencies are listed in `requirements.txt`.

## Models and Hyperparameter Tuning

The following regression models are trained and evaluated:

```python
models = {
    "Random Forest": RandomForestRegressor(),
    "Decision Tree": DecisionTreeRegressor(),
    "Gradient Boosting": GradientBoostingRegressor(),
    "Linear Regression": LinearRegression(),
    "K-Neighbors Regressor": KNeighborsRegressor(),
    "XGB Regressor": XGBRegressor(),
    "CatBoosting Regressor": CatBoostRegressor(),
    "AdaBoost Regressor": AdaBoostRegressor()
}
```

Hyperparameter tuning is performed using `GridSearchCV` for each model. The best model is selected based on the R² score.

## How to Use

### Prerequisites
- Python 3.8+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Pipeline
#### Data Ingestion:
Run `data_ingestion.py` to split the raw data into train and test sets.

#### Data Transformation:
Run `data_transformation.py` to preprocess the data and save the transformation pipeline.

#### Model Training:
Run `model_trainer.py` to train and evaluate models. The best model is saved in the `artifacts/models` folder.

#### Prediction:
Use `prediction_pipeline.py` to make predictions on new data.

### Running the Flask Application
Start the Flask application:
```bash
python application.py
```

Send a POST request to the `/predictdata` endpoint with input data in JSON format.



#### Example response:
```json
{
    "predicted_math_score": 85.3
}
```

### Deploying to AWS Elastic Beanstalk
1. Install the AWS CLI and Elastic Beanstalk CLI.
2. Initialize the Elastic Beanstalk environment:
   ```bash
   eb init -p python-3.8 <application-name>
   ```
3. Deploy the application:
   ```bash
   eb deploy
   ```

## Project Goals
The goal of this project is to develop a modular ML project which can be deployed using AWS ElasticBeanstalk and AWS CodePipeline to predict a student's math score based on various input features such as:
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

The predicted math score is capped at 100 to ensure realistic results.

