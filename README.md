**Improving  Academic Outcome For Oginigba Comprehensive Secondary School**

**Table of Contents**
- [Project Overview]
- [Technologies Used]
- [Project Structure]
- [Setup Instructions]
- [Usage]
- [Database Access]
- [ETL Pipeline]
- [Cron Job Configuration]
- [Documentation]
- [Contributing]

**Project Overview**
This project aims to analyze student performance data from Oginigba Comprehensive Secondary School. The data collected includes student demographics, attendance, academic history, and teacher evaluations. The project involves loading this data into a PostgreSQL database hosted on Aiven and creating a pipeline to update the database nightly.

**Technologies Used**
- Python
- PostgreSQL
- Aiven Cloud
- pandas (for data manipulation)
- psycopg2 (PostgreSQL adapter for Python)
- CSV (for data storage)

**Project Structure**
```bash
├── Database/
|   ├──Data/                                #Data source csv
|   |    ├──students.csv
|   |    ├──teachers.csv
|   |    ├──parents.csv
|   |    ├──attendance.csv
|   |    ├──subjects_offered.csv
|   |    ├──student_academic_data.csv
|   |    ├──teacher_evaluation_data.csv
|   |    ├──class_to_teacher.csv
|   |    ├──aggregated_academic.csv
|   |    ├──attendance_summary.csv
|   |    ├──aggregated_teacher_evaluation.csv
|   |
|   ├── create_tables.py                    # Script to create tables in the database
|   ├── load_data.py                        # Script to load data from CSV into the database
|   ├── update_data.py                      # Script to update data in the database
├── docs/
│   ├── project_documentation.md      # Documentation explaining the project, schema, and process
│   ├── access_instructions.md         # How to access the database (Python, PGAdmin, Power BI)
├── pipeline/
│   ├── etl_script.py                  # ETL script for processing and loading data
│   ├── cron_job.txt                   # Cron job configuration for scheduling
├── venv/                               # Virtual environment folder
├── requirements.txt                    # Python dependencies
├── README.md                           # Project documentation
```

Setup Instructions
1. **Clone the repository**:
```bash
git clone <repository_url>
cd <repository_name>
```
2. **Create a virtual environment**:
```bash
python -m venv venv
```
3. **Activate the virtual environment**:
- **Windows Command Prompt**:
```bash
.\venv\Scripts\activate
```
- **Windows PowerShell**:
```bash
.\venv\Scripts\Activate.ps1
```
- **Git Bash or WSL**:
```bash
source venv/Scripts/activate
```
4. **Install dependencies**:
```bash
pip install -r requirements.txt
```
Usage
- **Create Tables**:
  Run the `create_tables.py` script to set up the database schema:
  ```bash
  python create_tables.py
  ```

- **Load Data**:
  Use the `load_data.py` script to load data from CSV files into the database:
  ```bash
  python load_data.py
  ```

- **Update Data**:
  Execute the `update_data.py` script to refresh data in the database:
  ```bash
  python update_data.py
  ```
Database Access
You can access the Aiven-hosted PostgreSQL database using different tools:
- **Python**: Use `psycopg2` to connect to the database and execute queries.
- **PGAdmin**: Connect using the provided Aiven credentials and access the database via the GUI.
- **Power BI**: Connect to the database for visualization and reporting.
ETL Pipeline
The ETL process is handled by the `etl_script.py`, which is designed to extract data from the source, transform it as needed, and load it into the PostgreSQL database.
Cron Job Configuration
A cron job is configured to run the ETL script every midnight. The configuration file is located at `cron_job.txt`. Add the following line to your crontab:
```
0 0 * * * /path/to/python /path/to/etl_script.py
```
Documentation
- **Project Documentation**: Check the `docs/project_documentation.md` for detailed information about the project structure, schema, and data flow.
- **Access Instructions**: Refer to `docs/access_instructions.md` for guidance on accessing the database with different tools.
Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Make your changes and commit: `git commit -m 'Add a new feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a Pull Request.

