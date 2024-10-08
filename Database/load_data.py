import psycopg2
import csv

# Step 1: Connect to the Aiven-hosted PostgreSQL database
try:
    # Replace these details with your Aiven credentials
    connection = psycopg2.connect(
        user="avnadmin",              
        password="AVNS_blUS8t5v_YlvF0J_omz",          
        host="pg-353bb115-adeitanemmanuel086-380.h.aivencloud.com",              
        port="26014",                  
        database="defaultdb",     
        sslmode="require"                        
    )
    cursor = connection.cursor()
    print("Connected to Aiven PostgreSQL")

    # Step 2: Define function to load data from CSV into a table
    def load_csv_to_db(table_name, csv_file_path, columns):
        with open(csv_file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            
            try:
                for row in reader:
                    placeholders = ', '.join(['%s'] * len(columns))
                    insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
                    cursor.execute(insert_query, row)
            except Exception as row_error:
                print(f"Error occurred while inserting row: {row}. Error: {row_error}")
        
        print(f"Data loaded successfully into {table_name}")

    # Step 3: Load data into the students table
    students_columns = ['student_id', 'student_name', 'class', 'age', 'gender', 'ethnicity', 'disability_status', 
                        'family_size', 'favorite_subjects', 'access_to_constant_electricity', 'on_scholarship', 'sleep', 
                        'average_study_time', 'enjoy_reading', 'enjoy_dancing', 'enjoy_socialising', 
                        'anxiety_before_during_exams', 'distance_to_school', 'mode_of_transportation']
    load_csv_to_db("students", r"Data\students.csv", students_columns)

    # Load data into the parents table
    parents_columns = ['parent_id', 'student_id', 'parent_name', 'gender', 'email', 'familyIncomeRange', 
                       'numberOfChildren', 'occupation', 'houseOwnership', 'educationLevel', 'maritalStatus', 'location', 
                       'age', 'workHoursPerWeek', 'employmentStatus', 'transportationMode', 'internetAccess', 
                       'qualification', 'phone_number']
    load_csv_to_db("parents", r"Data\parents.csv", parents_columns)

    # Load data into the teachers table
    teachers_columns = ['teacher_id', 'teacher_name', 'teacher_email', 'salary_range', 'department', 
                        'qualification', 'employmentStatus', 'gender', 'yearsOfExperience', 'phone_number']
    load_csv_to_db("teachers", r"Data\teachers.csv", teachers_columns)

    # Load data into the attendance table
    attendance_columns = ['attendance_id', 'student_id', 'date', 'status']
    load_csv_to_db("attendance", r"Data\attendance.csv", attendance_columns)

    # Load data into the student_academic_data table
    student_academic_data_columns = ['academic_record_id', 'student_id', 'subject_id', 'attendance_percentage', 
                                     'assignment_score', 'exam_score', 'final_grade']
    load_csv_to_db("student_academic_data", r"Data\student_academic_data.csv", student_academic_data_columns)

    # Load data into the teacher_evaluation_data table
    teacher_evaluation_data_columns = ['student_id', 'subject_id', 'evaluation_date', 'comments', 'point']
    load_csv_to_db("teacher_evaluation_data", r"Data\teacher_evaluation_data.csv", teacher_evaluation_data_columns)

    # Load data into the subjects_offered table
    subjects_offered_columns = ['subject_id', 'subject']
    load_csv_to_db("subjects_offered", r"Data\subjects_offered.csv", subjects_offered_columns)

    # Load data into the class_to_teacher table
    class_to_teacher_columns = ['class', 'subject_id', 'teacher_id']
    load_csv_to_db("class_to_teacher", r"Data\class_to_teacher.csv", class_to_teacher_columns)

    # Load data into the aggregated_teacher_evaluation table
    aggregated_teacher_evaluation_columns = ['student_id', 'average_teacher_evaluation']
    load_csv_to_db("aggregated_teacher_evaluation", r"Data\aggregated_teacher_evaluation.csv", aggregated_teacher_evaluation_columns)

    # Load data into the aggregated_academic table
    aggregated_academic_columns = ['student_id', 'average_final_grade']
    load_csv_to_db("aggregated_academic", r"Data\aggregated_academic.csv", aggregated_academic_columns)

    # Load data into the attendance_summary table
    attendance_summary_columns = ['student_id', 'totalDaysPresent', 'attendancePercentage_overall']
    load_csv_to_db("attendance_summary", r"Data\attendance_summary.csv", attendance_summary_columns)

    # Step 4: Commit the transaction to make sure the data is saved
    connection.commit()
    print("Data upload complete and committed")

except Exception as error:
    print(f"Error occurred: {error}")

finally:
    # Step 5: Close the cursor and connection to release the resources
    if connection:
        cursor.close()
        connection.close()
        print("Aiven PostgreSQL connection is closed")
