import psycopg2
import pandas as pd
import os

#Define paths to CSV files
csv_folder_path = r"Database\Data"

# Define the CSV files
csv_files = {
    "students": os.path.join(csv_folder_path, "students.csv"),
    "parents": os.path.join(csv_folder_path, "parents.csv"),
    "teachers": os.path.join(csv_folder_path, "teachers.csv"),
    "attendance": os.path.join(csv_folder_path, "attendance.csv"),
    "student_academic_data": os.path.join(csv_folder_path, "student_academic_data.csv"),
    "teacher_evaluation_data": os.path.join(csv_folder_path, "teacher_evaluation_data.csv"),
    "subjects_offered": os.path.join(csv_folder_path, "subjects_offered.csv"),
    "class_to_teacher": os.path.join(csv_folder_path, "class_to_teacher.csv"),
    "aggregated_teacher_evaluation": os.path.join(csv_folder_path, "aggregated_teacher_evaluation.csv"),
    "attendance_summary": os.path.join(csv_folder_path, "attendance_summary.csv")
}

#Connect to the PostgreSQL database
def connect_to_db():
    try:
        connection = psycopg2.connect(
            user="avnadmin",
            password="AVNS_blUS8t5v_YlvF0J_omz",
            host="pg-353bb115-adeitanemmanuel086-380.h.aivencloud.com",
            port="26014",
            database="defaultdb",
            sslmode="require"
        )
        return connection
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        return None

#Extract data from CSV files into Pandas DataFrames
def extract_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Data extracted from {file_path}")
        return data
    except Exception as error:
        print(f"Error extracting data from {file_path}: {error}")
        return None

#Transform data (Example transformation: cleaning up missing values)
def transform_data(df):
    try:
        # Remove any rows with missing values (as an example)
        cleaned_df = df.dropna()
        print("Data transformed: cleaned up missing values")
        return cleaned_df
    except Exception as error:
        print(f"Error during data transformation: {error}")
        return df

#Load data into PostgreSQL database
def load_data_to_db(connection, table_name, data_frame):
    try:
        cursor = connection.cursor()

        # Generate column names and placeholders for SQL insert
        columns = data_frame.columns.tolist()
        placeholders = ', '.join(['%s'] * len(columns))
        insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"

        # Convert DataFrame rows into list of tuples
        rows = data_frame.values.tolist()

        # Insert each row into the table
        for row in rows:
            cursor.execute(insert_query, row)
        
        connection.commit()
        print(f"Data loaded into {table_name}")
    except Exception as error:
        print(f"Error loading data into {table_name}: {error}")

#Run the ETL process
def run_etl_pipeline():
    connection = connect_to_db()
    if connection is None:
        return
    
    try:
        # Iterate over each CSV file and its corresponding database table
        for table_name, csv_file in csv_files.items():
            # Extract
            df = extract_data(csv_file)

            if df is not None:
                # Transform
                transformed_df = transform_data(df)

                # Load
                load_data_to_db(connection, table_name, transformed_df)
        
        print("ETL process completed successfully.")
    
    except Exception as pipeline_error:
        print(f"Error occurred in the ETL pipeline: {pipeline_error}")
    
    finally:
        if connection:
            connection.close()
            print("Database connection closed.")

#Execute the ETL pipeline
if __name__ == "__main__":
    run_etl_pipeline()
