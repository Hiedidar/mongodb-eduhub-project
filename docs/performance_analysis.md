# Performance Analysis

This document summarizes the query performance evaluation and optimization efforts for the EduHub MongoDB project.

## 1. Query Performance Evaluation with `explain()`

We used MongoDB's `explain()` method to analyze the execution plan for multiple queries:

### Example: User Email Lookup

```python
explain_result = db.users.find({"email": "grace.okoro@example.com"}).explain()
```

- Execution Time: 12ms
- Winning Plan: COLLSCAN (Collection Scan)

## 2. Query Optimization through Indexing

We created indexes to improve performance for frequently used queries:

- `users.email` → to speed up email lookups
- `courses.title`, `courses.category` → for faster course searches
- `assignments.dueDate` → for time-sensitive assignments
- `enrollments.studentId`, `enrollments.courseId` → to improve join performance

## 3. Timing Query Execution Before & After Indexing

We measured query durations using Python's `time` module:

```python
start_time = time.time()
result = list(db.users.find({"email": "grace.okoro@example.com"}))
end_time = time.time()
print("Execution time:", end_time - start_time, "seconds")
```

### Example Result:

- **Before indexing:** \~0.0102s
- **After indexing:** \~0.0008s

## 4. Summary of Improvements

| Query                      | Time Before | Time After | Improvement |
| -------------------------- | ----------- | ---------- | ----------- |
| Email Lookup               | 0.0102s     | 0.0008s    | 12.8x       |
| Course Title Search        | 0.0153s     | 0.0011s    | 13.9x       |
| Upcoming Assignments Query | 0.0097s     | 0.0007s    | 13.9x       |

## 5. Tools Used

- MongoDB Compass
- PyMongo (with `.explain()` method)
- Python `time` module for benchmarking

## 6. Conclusion

Proper indexing significantly improved query efficiency across user, course, and assignment-related queries. Performance bottlenecks were identified and addressed, ensuring optimal access patterns for the EduHub platform.

