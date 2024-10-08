#pip install psycopg2-binary
import psycopg2

# Connect to the Aiven-hosted PostgreSQL database
try:
    # Replace these details with your Aiven credentials
    connection = psycopg2.connect(
        user="*****",              # Aiven provided username
        password="*******",  # Aiven provided password
        host="*******",  # Aiven hostname 
        port="********",                 # Aiven port 
        database="*********",          # Aiven database name
        sslmode="**********"              # SSL mode required by Aiven
    )
    cursor = connection.cursor()
    print("Connected to Aiven PostgreSQL")

    # Table creation SQL queries
    
    # Students table
    create_students_table = '''
    CREATE TABLE IF NOT EXISTS students (
        student_id VARCHAR(20) PRIMARY KEY,
        student_name VARCHAR(50) NOT NULL, 
        class VARCHAR(20) NOT NULL,
        age INT NOT NULL, 
        gender VARCHAR(20) NOT NULL,
        ethnicity VARCHAR(25) NOT NULL,
        disability_status BOOLEAN NOT NULL,
        family_size VARCHAR(25) NOT NULL,
        favorite_subjects VARCHAR(50) NOT NULL,
        access_to_constant_electricity BOOLEAN NOT NULL,
        on_scholarship BOOLEAN NOT NULL,
        sleep VARCHAR(20) NOT NULL,  
        average_study_time VARCHAR(20) NOT NULL,
        enjoy_reading BOOLEAN NOT NULL,
        enjoy_dancing BOOLEAN NOT NULL, 
        enjoy_socialising BOOLEAN NOT NULL,
        anxiety_before_during_exams BOOLEAN NOT NULL,
        distance_to_school VARCHAR(25) NOT NULL,
        mode_of_transportation VARCHAR(25) NOT NULL
    );
    '''
    
    # Parents table
    create_parents_table = '''
    CREATE TABLE IF NOT EXISTS parents (
        parent_id VARCHAR(20) PRIMARY KEY,
        student_id VARCHAR(20) NOT NULL,
        parent_name VARCHAR(50) NOT NULL,
        gender VARCHAR(20) NOT NULL,
        email VARCHAR(100) NOT NULL,
        familyIncomeRange VARCHAR(50) NOT NULL,
        numberOfChildren VARCHAR(25) NOT NULL,
        occupation VARCHAR(50) NOT NULL,
        houseOwnership VARCHAR(20) NOT NULL,
        educationLevel VARCHAR(50) NOT NULL,
        maritalStatus VARCHAR(20) NOT NULL,
        location VARCHAR(25) NOT NULL,
        age VARCHAR(20) NOT NULL,
        workHoursPerWeek INT NOT NULL,
        employmentStatus VARCHAR(20) NOT NULL,
        transportationMode VARCHAR(20) NOT NULL,
        internetAccess BOOLEAN NOT NULL,
        qualification VARCHAR(50) NOT NULL,
        phone_number VARCHAR(15) NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
    '''
    
    # Teachers table
    create_teachers_table = '''
    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id VARCHAR(50) PRIMARY KEY,
        teacher_name VARCHAR(50) NOT NULL,
        teacher_email VARCHAR(100) NOT NULL,
        salary_range VARCHAR(50) NOT NULL,
        department VARCHAR(50) NOT NULL,
        qualification VARCHAR(50) NOT NULL,
        employmentStatus VARCHAR(20) NOT NULL,
        gender VARCHAR(20) NOT NULL,
        yearsOfExperience INT NOT NULL,
        phone_number VARCHAR(25) NOT NULL
    );
    '''
    
    # Attendance table
    create_attendance_table = '''
    CREATE TABLE IF NOT EXISTS attendance (
        attendance_id INT PRIMARY KEY,
        student_id VARCHAR(15) NOT NULL,
        date DATE NOT NULL,
        status BOOLEAN NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
    '''
    
    # Student Academic Data table
    create_student_academic_data_table = '''
    CREATE TABLE IF NOT EXISTS student_academic_data (
        academic_record_id INT PRIMARY KEY,
        student_id VARCHAR(20) NOT NULL,
        subject_id VARCHAR(20) NOT NULL,
        attendance_percentage DECIMAL(5,2) NOT NULL,
        assignment_score DECIMAL(5,2) NOT NULL,
        exam_score DECIMAL(5,2) NOT NULL,
        final_grade DECIMAL(5,2) NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
    '''
    
    # Teacher Evaluation Data table
    create_teacher_evaluation_data_table = '''
    CREATE TABLE IF NOT EXISTS teacher_evaluation_data (
        evaluation_id SERIAL PRIMARY KEY,
        student_id VARCHAR(20) NOT NULL,
        subject_id VARCHAR(20) NOT NULL,
        evaluation_date DATE NOT NULL,
        comments TEXT NOT NULL,
        point INT NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
    '''
    
    # Subjects Offered table
    create_subjects_offered_table = '''
    CREATE TABLE IF NOT EXISTS subjects_offered (
        subject_id VARCHAR(20) PRIMARY KEY,
        subject VARCHAR(100) NOT NULL
    );
    '''
    
    # Class to Teacher table
    create_class_to_teacher_table = '''
    CREATE TABLE IF NOT EXISTS class_to_teacher (
        class VARCHAR(20) NOT NULL,
        subject_id VARCHAR(20) NOT NULL,
        teacher_id VARCHAR(20) NOT NULL,
        PRIMARY KEY (class, subject_id, teacher_id),
        FOREIGN KEY (subject_id) REFERENCES subjects_offered(subject_id),
        FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
    );
    '''
    
    # Aggregated Teacher Evaluation table
    create_aggregated_teacher_evaluation_table = '''
    CREATE TABLE IF NOT EXISTS aggregated_teacher_evaluation (
        student_id VARCHAR(20) PRIMARY KEY,
        average_teacher_evaluation FLOAT NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
    '''
    
    # Aggregated Academic table
    create_aggregated_academic_table = '''
    CREATE TABLE IF NOT EXISTS aggregated_academic (
        student_id VARCHAR(20) PRIMARY KEY,
        average_final_grade FLOAT NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
    '''
    
    # Attendance Summary table
    create_attendance_summary_table = '''
    CREATE TABLE IF NOT EXISTS attendance_summary (
        student_id VARCHAR(20) PRIMARY KEY,
        totalDaysPresent INT NOT NULL,
        attendancePercentage_overall FLOAT NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
    '''
    
    # Execute all the table creation queries
    cursor.execute(create_students_table)
    cursor.execute(create_parents_table)
    cursor.execute(create_teachers_table)
    cursor.execute(create_attendance_table)
    cursor.execute(create_student_academic_data_table)
    cursor.execute(create_teacher_evaluation_data_table)
    cursor.execute(create_subjects_offered_table)
    cursor.execute(create_class_to_teacher_table)
    cursor.execute(create_aggregated_teacher_evaluation_table)
    cursor.execute(create_aggregated_academic_table)
    cursor.execute(create_attendance_summary_table)

    # Commit the changes
    connection.commit()
    print("All tables created successfully in Aiven PostgreSQL")

except Exception as error:
    print(f"Error occurred: {error}")

finally:
    # Close the cursor and connection
    if connection:
        cursor.close()
        connection.close()
        print("Aiven PostgreSQL connection is closed")
