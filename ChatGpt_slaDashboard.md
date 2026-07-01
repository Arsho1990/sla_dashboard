# SLA & License Management Portal — Complete Migration & Setup Guide

## 1. Project Overview

Project Name: SLA & License Management Portal

Technology Stack:

* Backend: Python Flask
* Frontend: HTML, Bootstrap, JavaScript
* Database: Oracle Database
* Charts: Chart.js
* Authentication: Flask Session
* File Uploads: Oracle BLOB Storage

---

# 2. System Requirements

| Component       | Required Version          |
| --------------- | ------------------------- |
| Python          | 3.8+ (Recommended 3.11.9) |
| Oracle Database | 12c+                      |
| VS Code         | Latest                    |
| Git             | Latest                    |
| Browser         | Chrome / Edge             |
| Windows         | Windows 10/11             |

---

# 3. Install Required Software

## Install Python

Download from:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

During installation:

* Check “Add Python to PATH”

Verify installation:

```bash
py --version
```

IMPORTANT:
Use:

```bash
py
```

instead of:

```bash
python
```

---

## Install VS Code

Download from:
[https://code.visualstudio.com/](https://code.visualstudio.com/)

---

# 4. VS Code Extensions

Install these extensions:

* Python
* Pylance
* GitHub Copilot
* Oracle Developer Tools
* HTML CSS Support
* Bootstrap IntelliSense

---

# 5. Project Folder Setup

Copy project folder:

```bash
Sla_dashboard
```

Example Path:

```bash
D:\Projects\Sla_dashboard
```

---

# 6. Create Python Virtual Environment

Inside project folder:

```bash
py -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

---

# 7. Install Python Dependencies

Install required libraries:

```bash
pip install Flask pandas oracledb
```

Main Libraries:

| Library  | Purpose                |
| -------- | ---------------------- |
| Flask    | Backend Framework      |
| pandas   | Data Processing        |
| oracledb | Oracle DB Connectivity |

---

# 8. Recommended Additional Libraries

Install these additional libraries:

```bash
pip install python-dotenv openpyxl sqlalchemy
```

Purpose:

* python-dotenv → Environment Variables
* openpyxl → Excel Handling
* sqlalchemy → Future Database Optimization

---

# 9. Frontend Dependencies

No npm installation required.

Used CDN Libraries:

| Library   | Version |
| --------- | ------- |
| Bootstrap | 5.3.0   |
| jQuery    | 3.6.0   |
| Chart.js  | 4.4     |

---

# 10. Oracle Database Requirements

Database Information:

```bash
172.16.0.84:1521/orcl.avanza.pk
```

Required:

* Database Username
* Database Password
* Network/VPN Access

---

# 11. Oracle Instant Client Setup

Download:
[https://www.oracle.com/database/technologies/instant-client.html](https://www.oracle.com/database/technologies/instant-client.html)

After installation:

Add Oracle Instant Client path into:

```bash
Environment Variables → PATH
```

---

# 12. Environment Variables Setup (IMPORTANT)

Create file:

```bash
.env
```

Add:

```env
DB_USER=your_user
DB_PASSWORD=your_password
DB_DSN=172.16.0.84:1521/orcl.avanza.pk
SECRET_KEY=your_secret_key
```

---

# 13. Run the Project

Inside project folder:

```bash
py app.py
```

OR

```bash
flask run
```

Application URL:

```bash
http://localhost:5000
```

---

# 14. Database Auto Initialization

Tables auto-create on first run:

```bash
py app.py
```

---

# 15. Important Features in the Project

* SLA Dashboard
* License Management
* RDV License Tracking
* Nimbus License Tracking
* Charts & Analytics
* User Authentication
* Role-Based Access
* File Uploads
* Audit Logging
* Dark Mode
* Multi-Year SLA Tracking

---

# 16. API Endpoints Added

| API                     |
| ----------------------- |
| /api/sla-usage-data     |
| /api/license-usage-data |

Used For:

* SLA Graphs
* License Usage Charts
* Currency Analytics
* Trends

---

# 17. Recommended Folder Structure

```bash
Sla_dashboard/
│
├── app.py
├── templates/
├── static/
├── uploads/
├── venv/
├── .env
├── requirements.txt
├── README.md
```

---

# 18. Create requirements.txt

Generate requirements file:

```bash
pip freeze > requirements.txt
```

Install dependencies on new system:

```bash
pip install -r requirements.txt
```

---

# 19. Common Issues & Fixes

## Flask Not Starting

Use:

```bash
py app.py
```

NOT:

```bash
python app.py
```

---

## Oracle Connection Error

Check:

* VPN Access
* DB Credentials
* Oracle Instant Client
* Firewall Access

---

## Charts Not Loading

Check:

* Browser Console (F12)
* API Endpoints
* Chart.js CDN

---

# 20. Recommended Improvements Before Migration

* Use .env file
* Remove backup files
* Add Git repository
* Use SQLAlchemy
* Add Logging
* Add Input Validation

---

# 21. Git Setup

Initialize Git:

```bash
git init
```

Create:

```bash
.gitignore
```

Add:

```gitignore
venv/
__pycache__/
.env
*.bkp
```

---

# 22. Final Migration Checklist

Copy these files/folders:

* app.py
* templates/
* static/
* uploads/
* README.md
* requirements.txt
* .env

---

# 23. Final Setup Commands on New System

```bash
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
py app.py
```

---

# 24. Recommended Professional Project Structure

```bash
/AI-Prompts
/Architecture
/Presentation
/Backend
/AML-Rules
/Fraud-Rules
/Documentation
```

---

# 25. Important Notes

* Always activate virtual environment before running the project.
* Keep database credentials secure.
* Use .env for sensitive configuration.
* Take database backup before migration.
* Verify Oracle network access before deployment.
* Maintain Git repository for version control.

---

# 26. Recommended Future Enhancements

* Docker Containerization
* CI/CD Pipeline
* Centralized Logging
* Multi-Environment Support
* API Authentication
* Redis Caching
* JWT Authentication
* Automated Deployment

---

# 27. Project Startup Flow

1. Install Python
2. Install Oracle Instant Client
3. Copy Project Files
4. Create Virtual Environment
5. Install Requirements
6. Configure .env
7. Verify DB Access
8. Run Flask Application
9. Open Browser
10. Access:

```bash
http://localhost:5000
```






I have created the complete professional migration and setup guide file for your project, including:

* All prerequisites
* Dependencies
* Python libraries
* Oracle setup
* VS Code setup
* Virtual environment
* requirements.txt
* Common issues & fixes
* Migration checklist
* Git setup
* Future enhancements
* Complete setup commands

You can now easily copy, edit, and share it for your new system setup.
