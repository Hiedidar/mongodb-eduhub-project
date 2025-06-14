# EduHub – Test Results

This document captures the **results of key queries and aggregation operations** from the EduHub MongoDB project using the PyMongo interface.

---

## CRUD Operations

### Insert New User

```json
{
  "acknowledged": true,
  "insertedId": ObjectId("...new id...")
}
```

### Enroll a Student

```json
{
  "acknowledged": true,
  "insertedId": ObjectId("...new id...")
}
```

### Assignment Submission

```json
{
  "acknowledged": true,
  "insertedId": ObjectId("...new id...")
}
```

---

## Read Queries

### Active Students Query

```json
[
  { "userId": "user_1023", "role": "student", "isActive": true },
  { "userId": "user_1035", "role": "student", "isActive": true }
]
```

### Course Search (title contains "Python")

```json
[
  { "title": "Intro to Python", "level": "beginner" },
  { "title": "Advanced Python Projects", "level": "advanced" }
]
```

### Courses by Category "Design"

```json
[
  { "courseId": "course_2002", "category": "Design" },
  { "courseId": "course_2005", "category": "Design" }
]
```

---

## Aggregations

### Enrollments Per Course

```json
[
  { "_id": "course_2001", "total_enrollments": 4 },
  { "_id": "course_2002", "total_enrollments": 6 }
]
```

### Completion Rate by Course

```json
[
  { "_id": "course_2001", "completionRate": 0.75 },
  { "_id": "course_2002", "completionRate": 0.6 }
]
```

### Top Performing Students

```json
[
  { "_id": "student_1004", "averageGrade": 92 },
  { "_id": "student_1010", "averageGrade": 89 }
]
```

---

## Performance Insights

### Email Lookup (with Index)

```json
{
  "executionTimeMillis": 0,
  "totalDocsExamined": 1,
  "usedIndex": true
}
```

### Due Date Assignment Query (with Index)

```json
{
  "executionTimeMillis": 1,
  "totalDocsExamined": 2,
  "usedIndex": true
}
```

---

## Error Handling Demonstration

### Example: Missing Required Fields

```json
{
  "error": "Document failed validation",
  "missingFields": ["email", "lastName", "dateJoined"]
}
```

### Example: Duplicate Email

```json
{
  "error": "E11000 duplicate key error collection: EduHub_Db_Project.users index: email_1 dup key"
}
```

## Bonus Features

Note: Full implementations and outputs for all bonus challenges are now available in 'docs/bonus_features.md'

---

These outputs validate that the operations performed through PyMongo work as expected and errors are handled appropriately.

