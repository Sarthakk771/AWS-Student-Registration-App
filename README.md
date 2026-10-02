# Task 3 – Student Registration Application on AWS

## 1. Project Overview

This project deploys a student registration application using Amazon EC2 and Amazon RDS MySQL.

The application is hosted on an Ubuntu EC2 instance using Flask. Student registration data is stored in an Amazon RDS MySQL database. Secure connectivity is configured between the EC2 application server and the RDS database using AWS Security Groups.

The project demonstrates:
- Creating an Amazon RDS MySQL database
- Creating and configuring an EC2 application server
- Establishing secure EC2-to-RDS connectivity
- Creating a student database table
- Building a Flask student registration application
- Inserting student records into RDS MySQL
- Retrieving and displaying stored student records
- Testing successful data insertion and retrieval

## 2. AWS Services Used

Only the required AWS services are used for the cloud implementation:

- Amazon EC2
- Amazon RDS for MySQL
- AWS VPC networking and security components associated with EC2 and RDS

### EC2 Configuration
- Instance name: `Task3-Student-App-Server`
- Instance type: `t3.micro`
- Operating system: Ubuntu Server LTS
- Application framework: Flask
- Public IPv4 used for testing: `44.222.199.95`

### RDS Configuration
- DB identifier: `task3-student-db`
- Database engine: MySQL
- Instance class: `db.t3.micro`
- Database name: `studentdb`
- Master username: `admin`
- Port: `3306`
- Public access: Disabled

## 3. Architecture

```text
Student
   |
   v
Web Browser
   |
   | HTTP
   v
Amazon EC2
Ubuntu + Flask Application
   |
   | TCP 3306
   | Secure Security Group Access
   v
Amazon RDS
MySQL
   |
   v
studentdb
   |
   v
students table
```

### Application Flow
1. The student opens the application using the EC2 public IP.
2. Flask displays the student registration form.
3. The student enters name, email, course, and phone.
4. The application sends the submitted data to MySQL.
5. Amazon RDS stores the student record in the `students` table.
6. The application retrieves stored records from RDS.
7. The registered student records are displayed in the browser.

See `architecture/architecture-diagram.png` for the architecture diagram.

## 4. Network and Security Configuration

### EC2 Security Group

Security group: `Task3-EC2-SG`

Inbound rules:

| Type | Port | Source |
|---|---:|---|
| HTTP | 80 | `0.0.0.0/0` |
| SSH | 22 | User's IP address |
| SSH | 22 | EC2 Instance Connect prefix list |

### RDS Security Group

Security group: `Task3-RDS-SG`

Inbound rule:

| Type | Port | Source |
|---|---:|---|
| MySQL/Aurora | 3306 | `Task3-EC2-SG` |

RDS public access is disabled. MySQL port 3306 is allowed only from the EC2 application's security group.

## 5. Database Configuration

Database: `studentdb`

Table: `students`

| Column | Type | Description |
|---|---|---|
| id | INT | Auto-increment primary key |
| name | VARCHAR(100) | Student name |
| email | VARCHAR(100) | Student email |
| course | VARCHAR(100) | Student course |
| phone | VARCHAR(15) | Student phone |

The `id` column uses `AUTO_INCREMENT`, so each new record receives a unique ID.

## 6. Application Files

### `app.py`
The Flask application displays the registration page, receives form data, inserts student records into MySQL, retrieves student records, and displays them.

### `templates/index.html`
Provides the student registration form.

### `templates/students.html`
Displays student records retrieved from RDS.

### `requirements.txt`
```text
Flask
mysql-connector-python
```

## 7. Application Deployment

The application was deployed on the Ubuntu EC2 instance using Python 3, Flask, and MySQL Connector/Python.

A Python virtual environment was used for the application.

The Flask application runs on:

```text
0.0.0.0:80
```

RDS connection settings were provided through environment variables rather than placing the database password directly inside the application source code.

## 8. Database Connectivity Testing

The EC2 instance successfully connected to the RDS MySQL database using:

```text
Host: task3-student-db.c6pw8mi44xxl.us-east-1.rds.amazonaws.com
Port: 3306
Database: studentdb
User: admin
```

The MySQL client was used from the EC2 instance to verify connectivity.

The `students` table was successfully created.

## 9. Testing and Results

| Test | Result | Evidence |
|---|---|---|
| RDS database creation | PASS | `01-rds-database-created` |
| EC2 instance | PASS | `02-ec2-instance-created` |
| EC2 security group | PASS | `03-ec2-security-group` |
| RDS security group | PASS | `04-rds-security-group` |
| Database table creation | PASS | `05-database-table-created` |
| Table structure | PASS | `06-student-table-structure` |
| Registration application | PASS | `07-student-registration-form` |
| Student record insertion | PASS | `08-student-record-inserted` |
| RDS data verification | PASS | `09-rds-data-verification` |
| Data retrieval | PASS | `10-final-data-retrieval-test` |

Application URL used for testing:

`http://44.222.199.95`

RDS data was also verified directly using:

```sql
SELECT * FROM students;
```

## 10. Project Structure

```text
AWS-Student-Registration-App/
│
├── architecture/
│   └── architecture-diagram.png
│
├── screenshots/
│   ├── 01-rds-database-created
│   ├── 02-ec2-instance-created
│   ├── 03-ec2-security-group
│   ├── 04-rds-security-group
│   ├── 05-database-table-created
│   ├── 06-student-table-structure
│   ├── 07-student-registration-form
│   ├── 08-student-record-inserted
│   ├── 09-rds-data-verification
│   └── 10-final-data-retrieval-test
│
├── app.py
├── requirements.txt
└── README.md
```

## 11. Architecture Diagram

The architecture diagram is stored at:

```text
architecture/architecture-diagram.png
```

It represents:

```text
Student
   ↓
Web Browser
   ↓
EC2 Flask Application
   ↓
Secure MySQL Connection
   ↓
Amazon RDS MySQL
   ↓
Student Records
```

## 12. Security Considerations

- RDS public access was disabled.
- RDS MySQL port 3306 was not opened to the public internet.
- Only the EC2 security group was allowed to connect to RDS on port 3306.
- SSH access to EC2 was restricted.
- The database password was not hard-coded in `app.py`.
- Environment variables were used for database connection credentials.

## 13. Conclusion

The student registration application was successfully deployed using Amazon EC2 and Amazon RDS MySQL.

The EC2 instance hosts the Flask application, while RDS provides the MySQL database. Secure security-group-based connectivity was configured between the application server and database.

The project successfully demonstrates:
- EC2 application deployment
- RDS MySQL database deployment
- Secure EC2-to-RDS connectivity
- Student record insertion
- Student record storage
- Student record retrieval
- Browser-based display of registered students

The required application functionality and testing were completed successfully.
