from pyspark.sql.utils import AnalysisException
from pyspark.sql.functions import expr
import sys
def read_file(input_dataset):
    """Reads input dataset from Azure Blob Storage or Delta Table."""
    try:
        if input_dataset.endswith(".csv"):  # File is in cloud
            container = "containerproject"
            mount_name = "storageaccountproject13"
            file_path = f"wasbs://{container}@{mount_name}.blob.core.windows.net/{input_dataset}"
            
            df_input_data = spark.read.format("csv").option("header", "true").option("InferSchema", "true").load(file_path)
        else:  # Assume it's a Delta table (e.g., bank_fraud)
            df_input_data = spark.read.format("delta").table(input_dataset)
        
        print(f"Successfully read input data: {input_dataset} with {df_input_data.count()} records")
        return df_input_data
    except AnalysisException as e:
        print(f"Error reading {input_dataset}: {e}")
        raise e

def read_metadata():
    """Fetches metadata from metadata_table"""
    try:
        query = "SELECT * FROM metadata_table ORDER BY workflow_id"
        metadata_df = spark.sql(query)
        print("Metadata fetched successfully")
        return metadata_df
    except Exception as e:
        print(f"Error fetching metadata: {e}")
        return None
    


def mount_storage():
    """Mounts the Azure Blob Storage to Databricks."""
    try:
        dbutils.fs.unmount("/mnt/storageaccountproject13")
    except Exception as e:
        print("Unmounting failed or not mounted. Proceeding with mount.")
    
    container = "containerproject"
    mount_name = "storageaccountproject13"
    sas_token = "sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2025-03-04T04:01:20Z&st=2025-02-02T20:01:20Z&spr=https&sig=8VsqqMcAZRu1HYbS76rVOufbtaul7ZW%2FdAZvBxL0ymc%3D"
    storage_account_name = "storageaccountproject13"

    dbutils.fs.mount(
        source=f"wasbs://{container}@{storage_account_name}.blob.core.windows.net/",
        mount_point=f"/mnt/{mount_name}",
        extra_configs={f"fs.azure.sas.{container}.{storage_account_name}.blob.core.windows.net": sas_token}
    )
    print("Mount successful!")

def read_and_store_data():
    """Reads bank fraud dataset and stores it as Delta table."""
    source_path = "/dbfs/mnt/storageaccountproject13/bank_fraud.csv"
    destination_path = "/mnt/storageaccountproject13/delta/bank_fraud"
    
    df = spark.read.csv(source_path, header=True, inferSchema=True)
    df.write \
        .format("delta") \
        .mode("overwrite") \
        .option("header", "true") \
        .save(destination_path)
    print("Data successfully written to Delta table.")

def store_csv(df):
    """Writes the given DataFrame to a CSV file."""
    output_path = "/dbfs/mnt/storageaccountproject13/bank_fraud.csv"
    df.write.option("header", "true").mode("overwrite").csv(output_path)
    print("Data successfully written to CSV.")

def ten_main():
    """Main function to process datasets based on metadata rules."""
    print("***** Preprocessing Started *****")

    # Enable schema evolution for Delta tables
    spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")

    metadata_df = read_metadata()
    if metadata_df is None or metadata_df.count() == 0:
        print("No metadata found. Exiting.")
        sys.exit(0)

    for row in metadata_df.collect():
        try:
            workflow_id = row["workflow_id"]
            rule_id = row["rule_id"]
            rule_condition = row["filter_condition"]
            output_dataset = row["output_dataset"]
            input_dataset = row["input_dataset"]
            income_category = row["income_category"]

            print(f"Processing workflow_id: {workflow_id}, Rule_id: {rule_id}")

            input_data_df = read_file(input_dataset)
            if input_data_df is None:
                print(f"Skipping workflow_id {workflow_id} due to read error.")
                sys.exit(0)

            input_data_df.createOrReplaceTempView("input_data_table")

            # Check if the rule is a transformation (contains CASE)
            if "CASE" in rule_condition:
                output_data_df = input_data_df.withColumn(income_category,expr(rule_condition))
            else:
                query = f"SELECT * FROM input_data_table WHERE {rule_condition}"
                output_data_df = spark.sql(query)

            # Write the output data to Delta table
            output_data_df.write.format("delta").mode("overwrite").option("mergeSchema", "true").saveAsTable(output_dataset)
            spark.catalog.clearCache()
            spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "false")

            print(f"Successfully written output dataset: {output_dataset}, number of records inserted: {output_data_df.count()}")
        
        except Exception as e:
            print(f"Error processing workflow_id {workflow_id}: {e}")
    
    # Call the additional functions at the end of ten_main()
    mount_storage()
    read_and_store_data()
    store_csv(output_data_df)
    print("All tasks completed.")
ten_main()





