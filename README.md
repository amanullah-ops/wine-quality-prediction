# White Wine Quality Prediction

A beginner machine learning project that predicts white wine quality scores from physicochemical measurements using regression models.

## Dataset

The project uses the UCI White Wine Quality dataset (`data/winequality-white.csv`). It contains 4,898 wine samples, 11 input features and one target column (`quality`). The CSV is semicolon-separated.

## Project workflow

1. Exploratory data analysis
2. Feature and target separation
3. Train/test split
4. Baseline model
5. Train and compare Linear Regression, Decision Tree, Random Forest and Extra Trees
6. Five-fold cross-validation
7. Final model evaluation
8. Residual and feature-importance analysis

## Best model

The selected model is `ExtraTreesRegressor` with 300 estimators, `max_features="sqrt"`, and `random_state=42`. In the recorded experiment, it achieved:

| Metric | Test result |
|---|---:|
| MAE | 0.3598 |
| RMSE | 0.5603 |
| R² | 0.5947 |

These results are estimates, not a completely untouched final assessment: test-set results were consulted during experimentation and model selection. See the notebook's limitations section.

## Run the project

1. Clone or download this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Open `notebooks/01_wine_quality_prediction.ipynb` in Jupyter or PyCharm and run the cells from top to bottom.

The notebook reads the dataset using the relative path `../data/winequality-white.csv`, so keep the folder structure intact.

## Repository structure

```text
├── data/
│   └── winequality-white.csv
├── notebooks/
│   └── 01_wine_quality_prediction.ipynb
├── .gitignore
├── README.md
└── requirements.txt
```

## Scope

This is a beginner-level regression project. It intentionally does not include an API, deployment, production pipeline, or model-serving code.
