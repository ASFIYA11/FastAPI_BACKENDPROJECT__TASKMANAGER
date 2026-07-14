# Persistent Task Management Engine (RESTful API)

A modular RESTful backend API built using FastAPI and SQLAlchemy ORM, featuring persistent data tracking through an SQLite architecture.

---

## Project Objective

The primary aim of this project is to implement a robust data pipeline that enforces strict data integrity and separation of concerns. Instead of utilizing unstable in-memory tracking, this engine functions as a reliable, scalable intermediary between client interfaces and physical hardware storage.

### Key Engineering Focus Areas:
1. **Data Sanitization and Integrity:** Leveraging Pydantic schemas to validate type safety and block malicious or malformed request payloads before they reach downstream services.
2. **Data Persistence Layer:** Utilizing SQLAlchemy Object-Relational Mapping (ORM) to handle transactional commits, reads, and deletes securely without writing raw SQL.
3. **Modular Code Architecture:** Separating application routing logic, operational database engines, and structural database blueprints into independent modules to ensure high maintainability and ease of scaling.

---

## Database Architecture and Schema

The underlying storage engine uses an SQLite relational structure managed programmatically via SQLAlchemy.

### tasks Table Blueprint
Tracks application-wide task attributes, execution prioritization, and status management.

| Column Name    | SQL Data Type | Operational Constraints      | Description                                    |
|:---------------|:--------------|:-----------------------------|:-----------------------------------------------|
| `id`           | INTEGER       | Primary Key, Auto-Increment  | Unique system identifier for indexing records. |
| `title`        | VARCHAR       | NOT NULL                     | The specific name or summary of the entry.     |
| `description`  | VARCHAR       | NULL (Optional)              | Granular textual details about the execution.  |
| `is_completed` | BOOLEAN       | DEFAULT `False`              | Current implementation status flag.            |
| `priority`     | INTEGER       | DEFAULT `1`                  | Priority weights (e.g., 1–5 scale).           |

---

## Technology Stack and Ecosystem

- **Core Framework:** FastAPI (High-performance, asynchronous ASGI web framework)
- **Data Validation:** Pydantic (Type-safety layer)
- **Object-Relational Mapper:** SQLAlchemy ORM
- **Database Engine:** SQLite
- **ASGI Web Server:** Uvicorn

---

## API Endpoints Documentation

The service automatically provisions an interactive OpenAPI/Swagger ecosystem accessible locally at `/docs`.

### Task Operations Matrix

| Method   | Route            | Request Body     | Success (Status) | Error Modes Handled | Functionality Description |
|:---------|:-----------------|:-----------------|:-----------------|:--------------------|:--------------------------|
| **POST** | `/tasks/`        | `TaskCreate` schema | `200 OK`         | `422 Validation Error` | Validates client JSON, maps to ORM object, and commits it to disk. |
| **GET**  | `/tasks/`        | None             | `200 OK`         | None                | Queries database tables and returns all existing active entries. |
| **DELETE**| `/tasks/{id}`    | Path Parameter   | `200 OK`         | `404 Not Found`     | Targets database record by primary ID key and purges it from storage. |

---

## Local Environment Deployment Setup

Follow these steps to configure and boot the application locally:

1. **Clone the Repository:**
   ```bash
   git clone [# Persistent Task Management Engine (RESTful API)

A modular RESTful backend API built using FastAPI and SQLAlchemy ORM, featuring persistent data tracking through an SQLite architecture.

---

## Project Objective

The primary aim of this project is to implement a robust data pipeline that enforces strict data integrity and separation of concerns. Instead of utilizing unstable in-memory tracking, this engine functions as a reliable, scalable intermediary between client interfaces and physical hardware storage.

### Key Engineering Focus Areas:
1. **Data Sanitization and Integrity:** Leveraging Pydantic schemas to validate type safety and block malicious or malformed request payloads before they reach downstream services.
2. **Data Persistence Layer:** Utilizing SQLAlchemy Object-Relational Mapping (ORM) to handle transactional commits, reads, and deletes securely without writing raw SQL.
3. **Modular Code Architecture:** Separating application routing logic, operational database engines, and structural database blueprints into independent modules to ensure high maintainability and ease of scaling.

---

## Database Architecture and Schema

The underlying storage engine uses an SQLite relational structure managed programmatically via SQLAlchemy.

### tasks Table Blueprint
Tracks application-wide task attributes, execution prioritization, and status management.

| Column Name    | SQL Data Type | Operational Constraints      | Description                                    |
|:---------------|:--------------|:-----------------------------|:-----------------------------------------------|
| `id`           | INTEGER       | Primary Key, Auto-Increment  | Unique system identifier for indexing records. |
| `title`        | VARCHAR       | NOT NULL                     | The specific name or summary of the entry.     |
| `description`  | VARCHAR       | NULL (Optional)              | Granular textual details about the execution.  |
| `is_completed` | BOOLEAN       | DEFAULT `False`              | Current implementation status flag.            |
| `priority`     | INTEGER       | DEFAULT `1`                  | Priority weights (e.g., 1–5 scale).           |

---

## Technology Stack and Ecosystem

- **Core Framework:** FastAPI (High-performance, asynchronous ASGI web framework)
- **Data Validation:** Pydantic (Type-safety layer)
- **Object-Relational Mapper:** SQLAlchemy ORM
- **Database Engine:** SQLite
- **ASGI Web Server:** Uvicorn

---

## API Endpoints Documentation

The service automatically provisions an interactive OpenAPI/Swagger ecosystem accessible locally at `/docs`.

### Task Operations Matrix

| Method   | Route            | Request Body     | Success (Status) | Error Modes Handled | Functionality Description |
|:---------|:-----------------|:-----------------|:-----------------|:--------------------|:--------------------------|
| **POST** | `/tasks/`        | `TaskCreate` schema | `200 OK`         | `422 Validation Error` | Validates client JSON, maps to ORM object, and commits it to disk. |
| **GET**  | `/tasks/`        | None             | `200 OK`         | None                | Queries database tables and returns all existing active entries. |
| **DELETE**| `/tasks/{id}`    | Path Parameter   | `200 OK`         | `404 Not Found`     | Targets database record by primary ID key and purges it from storage. |

---
## Local Environment Deployment Setup

Follow these steps to configure and boot the application locally:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/ASFIYA11/FastAPI_BACKENDPROJECT__TASKMANAGER.git](https://github.com/ASFIYA11/FastAPI_BACKENDPROJECT__TASKMANAGER.git)
   cd FastAPI_BACKENDPROJECT__TASKMANAGER
   
