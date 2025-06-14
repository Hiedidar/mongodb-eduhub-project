# EduHub MongoDB Project

## Project Overview
EduHub is an online e-learning platform database designed using MongoDB and PyMongo. This project showcases proficiency in NoSQL schema design, CRUD operations, data validation, indexing, aggregation, and performance optimization.

## Project Setup Instructions

1. **Requirements:**
   - MongoDB v8.0+
   - Python 3.8+
   - Libraries: `pymongo`, `datetime`, `random`, `time`, `pandas`
   - MongoDB Compass (optional)
   - Jupyter Notebook (for interactive execution)

2. **Steps:**
   - Install requirements via `pip install pymongo pandas`
   - Run MongoDB locally on `localhost:27017`
   - Clone the repository and run the notebook: `notebooks/eduhub_mongodb_project.ipynb`

---

## Database Schema Documentation

### Users Collection
- `userId`: string (unique)
- `email`: string (unique, validated)
- `firstName`, `lastName`: string
- `role`: string (enum: `student`, `instructor`)
- `dateJoined`: datetime
- `isActive`: boolean
- `profile`: { bio, avatar, skills[] }

### Courses Collection
- `courseId`: string (unique)
- `title`, `description`: string
- `instructorId`: string (reference)
- `category`: string
- `level`: string (enum)
- `duration`: number (hours)
- `price`: number
- `createdAt`, `updatedAt`: datetime

### Enrollments
- `enrollmentId`: string (unique)
- `userId`: string
- `courseId`: string
- `enrolledAt`: datetime
- `status`: string (enum: `active`, `completed`)

### Lessons, Assignments, Submissions
- Lessons contain `lessonId`, `courseId`, `title`, `content`, `order`
- Assignments have `assignmentId`, `courseId`, `title`, `dueDate`, `maxScore`
- Submissions include `submissionId`, `assignmentId`, `studentId`, `submittedAt`, `grade`, `feedback`

---

## Query Explanations

### CRUD Operations:
- Insertions, updates, and deletions for all collections
- Soft delete pattern for users
- Student enrollment and assignment submission

### Read Queries:
- Search by category, title (with regex)
- Join course and instructor data
- Retrieve active users, enrolled students

### Aggregations:
- Enrollments per course
- Average course rating (if available)
- Student performance (average grades, completion)
- Instructor analytics (students taught, revenue)
- Trends by month and category

---

## Performance Analysis Results

### Indexes Created For:
- `users.email` (unique)
- `courses.title`, `courses.category`
- `assignments.dueDate`
- `enrollments.userId`, `enrollments.courseId`

### Timing Stats (Sample):
- Email Lookup: ~0.0003s
- Course Search by Title (with regex): ~0.0006s
- Due Date Lookup: ~0.0004s

### Optimization:
- Used `explain()` to analyze query plans
- Applied indexes to reduce scan times

---

## Challenges Faced and Solutions

### 1. **Schema Enforcement**
- Issue: MongoDB is schema-less by default
- Solution: Applied `$jsonSchema` validation rules at collection creation

### 2. **Data Duplication**
- Issue: Duplicates in users or enrollments
- Solution: Used `unique` indexes and try/except blocks

### 3. **Performance Bottlenecks**
- Issue: Full collection scans on large documents
- Solution: Added strategic indexes and rewrote queries for efficiency

### 4. **Data Generation Consistency**
- Used controlled random generators for reproducible inserts (names, categories, lessons)

---

For more details, refer to:
- `src/eduhub_queries.py` for full code
- `data/sample_data.json` for all sample inserts
- `docs/test_results.md` for query outputs

---

**License**: MIT