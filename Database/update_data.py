import psycopg2
import csv

# Step 1: Connect to the Aiven-hosted PostgreSQL database
try:
    connection = psycopg2.connect(
        user="********",              
        password="**********",          
        host="*******************",              
        port="**********",                  
        database="*********",     
        sslmode="*******"                        
    )
    cursor = connection.cursor()
    print("Connected to Aiven PostgreSQL")

    # Step 2: Define function to update records from CSV
    def update_data_from_csv(table_name, csv_file_path, key_columns, update_columns):
        with open(csv_file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row

            # For each row in the CSV, generate an UPDATE statement
            for row in reader:
                key_values = row[:len(key_columns)]    # Primary key values
                update_values = row[len(key_columns):] # Values to update

                # Create update key condition (e.g., WHERE student_id = %s)
                key_conditions = ' AND '.join([f"{key} = %s" for key in key_columns])
                update_set = ', '.join([f"{col} = %s" for col in update_columns])

                # Final SQL query
                update_query = f"UPDATE {table_name} SET {update_set} WHERE {key_conditions}"

                try:
                    cursor.execute(update_query, update_values + key_values)
                    print(f"Updated row: {key_values}")
                except Exception as row_error:
                    print(f"Error occurred while updating row {key_values}: {row_error}")

    # Step 3: Update students table
    students_key_columns = ['student_id']
    students_update_columns = ['student_name', 'class', 'age', 'gender', 'ethnicity', 'disability_status', 
                               'family_size', 'favorite_subjects', 'access_to_constant_electricity', 'on_scholarship', 
                               'sleep', 'average_study_time', 'enjoy_reading', 'enjoy_dancing', 'enjoy_socialising', 
                               'anxiety_before_during_exams', 'distance_to_school', 'mode_of_transportation']
    update_data_from_csv("students", r"Data\students_update.csv", students_key_columns, students_update_columns)

    # Step 4: Update parents table
    parents_key_columns = ['parent_id']
    parents_update_columns = ['parent_name', 'student_id', 'gender', 'email', 'familyIncomeRange', 'numberOfChildren', 
                              'occupation', 'houseOwnership', 'educationLevel', 'maritalStatus', 'location', 'age', 
                              'workHoursPerWeek', 'employmentStatus', 'transportationMode', 'internetAccess', 'qualification', 
                              'phone_number']
    update_data_from_csv("parents", r"Data\parents_update.csv", parents_key_columns, parents_update_columns)

    # Step 5: Update teachers table
    teachers_key_columns = ['teacher_id']
    teachers_update_columns = ['teacher_name', 'teacher_email', 'salary_range', 'department', 'qualification', 
                               'employmentStatus', 'gender', 'yearsOfExperience', 'phone_number']
    update_data_from_csv("teachers", r"Data\teachers_update.csv", teachers_key_columns, teachers_update_columns)

    # Step 6: Update attendance table
    attendance_key_columns = ['attendance_id']
    attendance_update_columns = ['student_id', 'date', 'status']
    update_data_from_csv("attendance", r"Data\attendance_update.csv", attendance_key_columns, attendance_update_columns)

    # Step 7: Update academic records table
    student_academic_data_key_columns = ['academic_record_id']
    student_academic_data_update_columns = ['student_id', 'subject_id', 'attendance_percentage', 
                                            'assignment_score', 'exam_score', 'final_grade']
    update_data_from_csv("student_academic_data", r"Data\student_academic_data_update.csv", 
                         student_academic_data_key_columns, student_academic_data_update_columns)

    # Step 8: Commit the updates to ensure they are saved in the database
    connection.commit()
    print("Data update complete and committed")

except Exception as error:
    print(f"Error occurred: {error}")

finally:
    # Step 9: Close the cursor and connection to release the resources
    if connection:
        cursor.close()
        connection.close()
        print("Aiven PostgreSQL connection is closed")
