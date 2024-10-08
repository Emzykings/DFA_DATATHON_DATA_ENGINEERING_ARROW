# Project Documentation

## Overview

This project is focused on creating a database system for Oginigba Comprehensive Secondary School. The database stores student information, parent details, teacher data, attendance records, academic data, and other relevant school data to improve exam performance and educational analytics and student performance with ML model.

### Key Objectives:
- Store and manage school data efficiently.
- Provide access to data for visualization and analysis using tools like Power BI.
- Enable multiple users to interact with the database (Python, PGAdmin, Power BI).
- Automate daily ETL pipeline to update the data in real-time.

## Database Schema

### 1. **students**
   - `student_id` (Primary Key)
   - `student_name`
   - `class`
   - `age`
   - `gender`
   - `ethnicity`
   - `disability_status`
   - `family_size`
   - `favorite_subjects`
   - `access_to_constant_electricity`
   - `on_scholarship`
   - `sleep`
   - `average_study_time`
   - `enjoy_reading`
   - `enjoy_dancing`
   - `enjoy_socialising`
   - `anxiety_before_during_exams`
   - `distance_to_school`
   - `mode_of_transportation`

### 2. **parents**
   - `parent_id` (Primary Key)
   - `student_id` (Foreign Key)
   - `parent_name`
   - `gender`
   - `email`
   - `familyIncomeRange`
   - `numberOfChildren`
   - `occupation`
   - `houseOwnership`
   - `educationLevel`
   - `maritalStatus`
   - `location`
   - `age`
   - `workHoursPerWeek`
   - `employmentStatus`
   - `transportationMode`
   - `internetAccess`
   - `qualification`
   - `phone_number`

### 3. **teachers**
   - `teacher_id` (Primary Key)
   - `teacher_name`
   - `teacher_email`
   - `salary_range`
   - `department`
   - `qualification`
   - `employmentStatus`
   - `gender`
   - `yearsOfExperience`
   - `phone_number`

### 4. **attendance**
   - `attendance_id` (Primary Key)
   - `student_id` (Foreign Key)
   - `date`
   - `status`

### 5. **student_academic_data**
   - `academic_record_id` (Primary Key)
   - `student_id` (Foreign Key)
   - `subject_id`
   - `attendance_percentage`
   - `assignment_score`
   - `exam_score`
   - `final_grade`

### 6. **teacher_evaluation_data**
   - `evaluation_id` (Primary Key)
   - `student_id` (Foreign Key)
   - `subject_id`
   - `evaluation_date`
   - `comments`
   - `point`

### 7. **subjects_offered**
   - `subject_id` (Primary Key)
   - `subject`

### 8. **class_to_teacher**
   - `class`
   - `subject_id` (Foreign Key)
   - `teacher_id` (Foreign Key)

### 9. **aggregated_teacher_evaluation**
   - `student_id` (Primary Key)
   - `average_teacher_evaluation`

### 10. **aggregated_academic**
   - `student_id` (Primary Key)
   - `average_final_grade`

### 11. **attendance_summary**
   - `student_id` (Primary Key)
   - `totalDaysPresent`
   - `attendancePercentage_overall`

## ETL Process

- **ETL Script**: The ETL pipeline (`etl_script.py`) is designed to extract, transform, and load data from CSV files into the PostgreSQL database. It runs daily at 2 AM, ensuring that data is updated regularly.
- **Cron Job**: The script is scheduled using cron to automate the daily updates.

### Steps:
1. Extract data from CSV files.
2. Transform the data to match the schema.
3. Load the data into the database.

---

## Technologies Used
- **PostgreSQL** (hosted on Aiven)
- **Python** (for ETL and data access)
- **PGAdmin** (for database administration)
- **Power BI** (for visualization)
- **Cron** (for automating the ETL process)

---
