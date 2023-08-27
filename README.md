# End-to-End-Galaxy-Classification

![HomepageUI](./flowcharts/Pipeline.png)

## Table of Contents

- [Model Preparation](#model-preparation)
- [User Interface Development](#user-interface-development)
- [Model Deployment and Automation](#model-deployment-and-automation)
- [How to run?](#steps)
---

## Model Preparation

1. **Data Ingestion**
   - Description: Ingest raw data from various sources and prepare it for training.
   - Tasks: Data collection, data preprocessing, and transformation.

2. **Prepare Base Model**
   - Description: Create a basic machine learning model that will serve as the starting point for training.
   - Tasks: Model architecture selection, parameter initialization.

3. **Training**
   - Description: Train the base model using the prepared data.
   - Tasks: Model training, optimization, hyperparameter tuning.

4. **Evaluation**
   - Description: Evaluate the trained model's performance to assess its accuracy and other relevant metrics.
   - Tasks: Model validation, metric calculation.

5. **Prediction**
   - Description: Apply the trained model to make predictions on new data.
   - Tasks: Implement prediction functionality, integration with data pipelines.

## User Interface Development

1. **Create Flask App Structure**
   - Description: Set up the directory structure and files for the Flask web application.
   - Tasks: Folder creation, file setup.

2. **Develop Flask App**
   - Description: Write the Flask application code to handle user interactions and serve model predictions.
   - Tasks: Route definitions, views, template rendering.

3. **Configure Dependencies**
   - Description: Specify the required Python packages and libraries for the Flask app.
   - Tasks: Create a `requirements.txt` file.

4. **Deploy on a Local Server**
   - Description: Test the Flask app on a local development server to ensure functionality.
   - Tasks: Use the `flask run` command to start the app locally.

5. **User Interface Testing**
   - Description: Conduct thorough testing of the user interface to ensure a seamless user experience.
   - Tasks: UI testing, bug fixing.

## Model Deployment and Automation

1. **Dockerize the Flask App**
   - Description: Create a Dockerfile to containerize the Flask app for easy deployment.
   - Tasks: Define the Dockerfile, specify dependencies.

2. **Build Docker Image**
   - Description: Build a Docker image of the Flask app with the necessary dependencies.
   - Tasks: Use the Docker CLI to build the image.

3. **Push to Container Registry on AWS**
   - Description: Push the Docker image to an AWS container registry for storage and deployment.
   - Tasks: Set up an AWS container registry, push the image.

4. **Configure EC2 Instance**
   - Description: Set up an EC2 instance on AWS to host the deployed app.
   - Tasks: Instance creation, security group configuration, Docker installation.

5. **Automate Deployment with Github Actions**
   - Description: Create a GitHub Actions workflow to automate the deployment process.
   - Tasks: Define the workflow YAML, specify build and deployment steps.

---

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Apheironn//End-to-End-Galaxy-Classification
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.10 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
# Open up you local host and port
localhost:8080
```

First go to,
```bash
# You have to train your data first on:
localhost:8080/train
```

Finally,
```bash
# Go back to main address and enter values to estimate the price of the vehicle:
localhost:8080/
```

## License

This project is licensed under the [MIT License](LICENSE).
