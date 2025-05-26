# Database Tool Server

A Flask-based database tool server that provides database table management, query interfaces, and log monitoring functionality. The project was initially developed with SQLite but is designed to support future migration to Oracle database.

## Features

- Complete REST API for DEPT (Department), EMP (Employee), BONUS, and SALGRADE (Salary Grade) tables
- Real-time log file monitoring with WebSocket updates
- Configurable monitoring parameters (log file path, update interval, etc.)
- Clean and beautiful log monitoring interface
- Supports SQLite database with Oracle compatibility

## Tech Stack

- **Backend**: Flask, SQLAlchemy, Flask-SocketIO
- **Database**: SQLite (can be migrated to Oracle)
- **Communication**: RESTful API, WebSocket, Server-Sent Events
- **Tools**: Flask-Migrate, Blueprint, Eventlet

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/db-tool-server.git
cd db-tool-server
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Initialize database
```bash
flask db upgrade
```

## Configuration

Main configuration is in `config/config.py`. You can customize settings through environment variables or by directly modifying the configuration file:

```python
# Database configuration
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(BASE_DIR, 'db_tool.db')

# Log monitoring configuration
LOG_MONITOR_FILE = os.environ.get('LOG_MONITOR_FILE') or '/var/log/system.log'  # Default log file to monitor
LOG_MONITOR_MAX_LINES = int(os.environ.get('LOG_MONITOR_MAX_LINES') or 1000)    # Maximum lines to display
LOG_MONITOR_UPDATE_INTERVAL = int(os.environ.get('LOG_MONITOR_UPDATE_INTERVAL') or 5)  # Update interval (seconds)
```

## Running

Start the server:
```bash
python run.py
```

Server runs by default at `http://localhost:5001`

## API Endpoints

### Department Management (DEPT)

- `GET /api/dept/` - Get all departments
- `GET /api/dept/<deptno>` - Get specific department information
- `POST /api/dept/` - Create new department
- `PUT /api/dept/<deptno>` - Update department information
- `DELETE /api/dept/<deptno>` - Delete department

### Employee Management (EMP)

- `GET /api/emp/` - Get all employees
- `GET /api/emp/<empno>` - Get specific employee information
- `GET /api/emp/dept/<deptno>` - Get all employees in a department
- `GET /api/emp/job/<job>` - Get all employees in a specific position
- `POST /api/emp/` - Create new employee
- `PUT /api/emp/<empno>` - Update employee information
- `DELETE /api/emp/<empno>` - Delete employee

### Bonus Management (BONUS)

- `GET /api/bonus/` - Get all bonus records
- `GET /api/bonus/ename/<ename>` - Get bonus records for specific employee
- `GET /api/bonus/job/<job>` - Get bonus records for specific position
- `POST /api/bonus/` - Create bonus record
- `PUT /api/bonus/<id>` - Update bonus record
- `DELETE /api/bonus/<id>` - Delete bonus record

### Salary Grade Management (SALGRADE)

- `GET /api/salgrade/` - Get all salary grades
- `GET /api/salgrade/<grade>` - Get salary range for specific grade
- `GET /api/salgrade/sal/<sal>` - Get grade for specific salary
- `POST /api/salgrade/` - Create salary grade
- `PUT /api/salgrade/<grade>` - Update salary grade
- `DELETE /api/salgrade/<grade>` - Delete salary grade

### Log Monitoring

- `GET /api/log/` - Get log content
- `GET /api/log/stream` - Stream log updates (Server-Sent Events)
- `GET /api/log/info` - Get log file information
- `GET /logs` - Log monitoring web interface

## Log Monitoring Feature

The project includes a real-time log monitoring system that can monitor server log files and display them through a web interface in real-time.

Key features:
- Real-time monitoring of specified log files
- WebSocket support for real-time log updates
- Configurable monitoring parameters (display lines, update interval, etc.)
- Beautiful monitoring interface with log download and scroll control features

## Migration to Oracle (TODO...)

The project was initially developed with SQLite but is designed to be compatible with Oracle database. Migration steps:

1. Modify the database connection string in the configuration file:
```python
SQLALCHEMY_DATABASE_URI = 'oracle://username:password@hostname:port/sid'
```

2. Install Oracle database driver:
```bash
pip install cx_Oracle
```

3. Run database migrations:
```bash
flask db migrate
flask db upgrade
```

## Project Structure

```
db-tool-server/
├── app/                      # Main application directory
│   ├── api/                  # API interfaces
│   ├── models/               # Data models
│   ├── templates/            # Template files
│   ├── utils/                # Utility functions
│   ├── __init__.py           # Application initialization
│   ├── routes.py             # Page routes
│   └── socket_events.py      # WebSocket event handlers
├── config/                   # Configuration files
│   ├── config.py             # Main configuration
│   └── db/                   # Database scripts
├── migrations/               # Database migration files
├── venv/                     # Virtual environment
├── .gitignore                # Git ignore file
├── README.md                 # Project documentation
├── requirements.txt          # Dependency list
└── run.py                    # Run script
```

## License

[MIT License](LICENSE) 