# EduHub – Bonus Features

This document includes the implementation and sample output for the **Bonus Challenges** described in the project brief.

---

## Bonus 1: Text Search Functionality for Course Content

### Implementation:

```python
# Create a text index on course title and description
db.courses.create_index([("title", "text"), ("description", "text")])

# Perform a text search
search_query = {"$text": {"$search": "Python"}}
results = list(
    db.courses.find(search_query, {"score": {"$meta": "textScore"}})
    .sort([("score", {"$meta": "textScore"})])
)

for course in results:
    print(course["title"], "→", course.get("description", ""))
```

### Sample Output:

```
Intro to Python → Learn Python basics for beginners
Advanced Python Projects → Build real-world apps in Python
```

---

## Bonus 2: Recommendation System Using Aggregation

### Implementation:

```python
# Replace with a valid student ID
student_id = "student_1010"

# Get courses the student is already enrolled in
enrolled_ids = [e["courseId"] for e in db.enrollments.find({"studentId": student_id})]

# Extract tags from enrolled courses
tags_cursor = db.courses.find({"courseId": {"$in": enrolled_ids}}, {"tags": 1})
interested_tags = list({tag for doc in tags_cursor for tag in doc.get("tags", [])})

# Recommend new courses not already enrolled in
pipeline = [
    {"$match": {"courseId": {"$nin": enrolled_ids}, "tags": {"$in": interested_tags}}},
    {"$addFields": {
        "matchingTags": {"$setIntersection": ["$tags", interested_tags]},
        "matchCount": {"$size": {"$setIntersection": ["$tags", interested_tags]}}
    }},
    {"$sort": {"matchCount": -1}},
    {"$project": {"title": 1, "tags": 1, "matchCount": 1}}
]

recommended = list(db.courses.aggregate(pipeline))
for r in recommended:
    print(r["title"], "→ Tags matched:", r["matchCount"])
```

### Sample Output:

```
Data Science with Python → Tags matched: 2
Web APIs with Flask → Tags matched: 1
```

---

## Bonus 3: Archiving Strategy for Old Enrollments

### Implementation:

```python
from datetime import datetime, timedelta

# Define threshold (e.g., enrollments older than 1 year)
threshold = datetime.now() - timedelta(days=365)

# Move old enrollments to archived collection
old_enrollments = db.enrollments.find({"enrollmentDate": {"$lt": threshold}})
archived_docs = list(old_enrollments)

if archived_docs:
    db.enrollments_archive.insert_many(archived_docs)
    db.enrollments.delete_many({"enrollmentDate": {"$lt": threshold}})
```

### Notes:

- Use a scheduled script or cron job for automation.
- Archived data is stored in `enrollments_archive`.

---

## Bonus 4: Geospatial Queries for Location-Based Course Recommendations

### Schema Adjustment (add to users collection):

```python
# Add sample location to users
{
    "userId": "student_1001",
    "location": {
        "type": "Point",
        "coordinates": [3.3792, 6.5244]  # Longitude, Latitude (e.g., Lagos)
    }
}
```

### Index Creation:

```python
db.users.create_index([("location", "2dsphere")])
```

### Query Nearby Users (e.g., within 20km):

```python
nearby_users = db.users.find({
    "location": {
        "$near": {
            "$geometry": {
                "type": "Point",
                "coordinates": [3.3792, 6.5244]
            },
            "$maxDistance": 20000
        }
    }
})
```

### Use Case:

- Suggest locally trending courses to users in the same region.

