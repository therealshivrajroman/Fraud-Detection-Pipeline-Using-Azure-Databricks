
**Fraud-Detection-Pipeline-Using-Azure-Databricks**

The objective of this project is to build a fraud detection pipeline to identify fraudulent banking transactions. The project aims to improve fraud detection accuracy, streamline processes, and provide actionable insights to help banks reduce fraudulent activities.

## Architecture

The fraud detection pipeline consists of the following components:
- **Azure Blob Storage**: Stores raw transaction data (e.g., Base.csv) and processed data.
- **Azure Databricks**: Used for data processing, rule application, and machine learning model training.
- **Metadata Table**: A Delta table (`metadata_table`) that stores business rules for data processing.
- **Machine Learning Models**: Logistic Regression and KNN models for fraud detection.
- **Automation Scripts**: Python scripts for data ingestion, processing, and model deployment.
- **Power BI Dashboards**: Provides fraud detection insights.
- **Streamlit UI**: A web-based interface for fraud detection and dashboard visualization.

### Fraud Detection Pipeline Diagram
Below is a textual representation of the fraud detection pipeline:

1. **Data Ingestion**
   - Raw data is ingested from **Azure Blob Storage**.
   - Data is preprocessed and transformed using **Azure Databricks** and **Spark SQL**.
   
2. **Processing & Storage**
   - Data is processed using **Delta Lake** for structured storage.
   - Metadata is stored in the **Metadata Table** for rule-based transformations.

3. **Fraud Prediction**
   - Machine learning models (**Logistic Regression & KNN**) are trained using the preprocessed data.
   - Trained models are saved for deployment.

4. **Deployment & Insights**
   - Fraud predictions are generated based on incoming data.
   - Reports and insights are visualized using **Power BI**.
   - A **Streamlit UI** is used for interactive fraud detection analysis.

## Directory Structure
```
📂 Fraud-Detection-Pipeline
 ├── 📂 scripts
 │   ├── practice.py  # Automation script
 │   ├── rules.ipynb  # Processing file in Databricks
 │   ├── ml_mod2.ipynb  # Model training file
 ├── 📂 data
 │   ├── base.csv  # Raw dataset
 ├── 📂 models
 │   ├── logistic_regression_model.pkl  # Saved model
 ├── 📂 dashboards
 │   ├── PowerBI_Reports.pbix  # Power BI dashboard file
 ├── 📂 ui
 │   ├── streamlit_app.py  # Streamlit UI script
```

## Data Ingestion and Preprocessing

### 1. Data Source
- **Kaggle Dataset**: The dataset used for this project is sourced from Kaggle and contains **1 million rows and 32 columns**, representing various features indicative of potential fraud.

### 2. Storage
- **Azure Blob Storage**: The raw transaction data is securely stored in Azure Blob Storage, ensuring high availability and durability.

### 3. Access and Processing
- **Azure Databricks**: The data is accessed and processed using Azure Databricks, an Apache Spark-based analytics platform optimized for Azure, allowing for fast, easy, and collaborative big data analytics and AI development.

### Steps Involved in Data Ingestion and Preprocessing:

#### Connecting to Azure Blob Storage
Establish a connection between Azure Databricks and Azure Blob Storage using Azure Storage account keys or a SAS token.

```python
storage_account_name = "your_storage_account"
container_name = "your_container"
storage_account_key = "your_storage_account_key"

dbutils.fs.mount(
    source = f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net/",
    mount_point = "/mnt/blob_storage",
    extra_configs = {f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net": storage_account_key}
)
```

#### Loading Data
Read the data from Azure Blob Storage into a Spark DataFrame for further processing.

```python
file_path = "/mnt/blob_storage/your_dataset.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)
```

#### Data Preprocessing with SQL in Databricks
Use SQL queries within Databricks to preprocess the data. Selecting,Validating andTransforming data

#### Storing Preprocessed Data
Store the preprocessed data in Azure Blob Storage or another suitable location for model training.

## Model Building, Evaluation, and Visualization

### Model Building
A supervised machine learning model is built using Python and  library like Scikit-learn to classify transactions as fraudulent or legitimate. The model is trained on historical transaction data.

### Model Evaluation
Evaluate the model's performance using metrics like **Precision, Recall, F1-score, and ROC-AUC**.

### Visualization
- **Power BI dashboards**: Used to visualize fraud detection insights, enabling analysts to monitor suspicious activities and take prompt action.
- Reports help decision-makers gain insights into trends, fraud risk, and other key metrics.

### UI Development
- A **Streamlit-based UI** is created for fraud detection, integrating dashboards for visualization and analysis.

## Challenges
- **Automation Gap**: Need for a more automated end-to-end fraud detection pipeline.


## Requirements
- Python 3.x
- Jupyter Notebook
- Azure Databricks
- Azure Blob Storage
- Power BI (for visualization)
- Streamlit (for UI)

## Contact
For any questions or clarifications, please reach out to shivrajroman@gmail.com


