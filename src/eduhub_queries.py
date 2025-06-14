#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient
from datetime import datetime
import random
import string


# In[2]:


# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Drop existing database to reset
client.drop_database("EduHub_Db_Project")

# Re-create the database
db = client["EduHub_Db_Project"]
print("EduHub_Db_Project reset and ready.")


# In[3]:


# Generate real-looking random names
first_names = ["Grace", "David", "Ifeanyi", "Chinaza", "Adebayo", "Fatima", "Emeka", "Zainab", "Samuel", "Ngozi"]
last_names = ["Okoro", "Afolayan", "Ugochukwu", "Nwosu", "Adewale", "Mohammed", "Eze", "Aliyu", "Adegoke", "Ezeh"]
roles = ["student", "instructor"]

# Generate users
users = []
for i in range(30):
    first = random.choice(first_names)
    last = random.choice(last_names)
    role = random.choice(roles)
    user = {
        "userId": f"user_{100+i}",
        "email": f"{first.lower()}.{last.lower()}@example.com",
        "firstName": first,
        "lastName": last,
        "role": role,
        "dateJoined": datetime.utcnow(),
        "isActive": True,
        "profile": {
            "bio": f"I am a {role} at EduHub.",
            "avatar": "",
            "skills": random.sample(["Python", "Excel", "Java", "MongoDB", "HTML", "CSS", "JavaScript"], k=3)
        }
    }
    users.append(user)

# Insert users
result = db.users.insert_many(users)
print(f"Inserted {len(result.inserted_ids)} users into 'users' collection."


# In[4]:


# Generate users
users = []
for i in range(30):
    first = random.choice(first_names)
    last = random.choice(last_names)
    role = random.choice(roles)
    user = {
        "userId": f"user_{100+i}",
        "email": f"{first.lower()}.{last.lower()}@example.com",
        "firstName": first,
        "lastName": last,
        "role": role,
        "dateJoined": datetime.utcnow(),
        "isActive": True,
        "profile": {
            "bio": f"I am a {role} at EduHub.",
            "avatar": "",
            "skills": random.sample(["Python", "Excel", "Java", "MongoDB", "HTML", "CSS", "JavaScript"], k=3)
        }
    }
    users.append(user)

# Insert users
result = db.users.insert_many(users)
print(f"Inserted {len(result.inserted_ids)} users into 'users' collection.")


# In[5]:


# Generate real-looking random names
first_names = ["Grace", "David", "Ifeanyi", "Chinaza", "Adebayo", "Fatima", "Emeka", "Zainab", "Samuel", "Ngozi"]
last_names = ["Okoro", "Afolayan", "Ugochukwu", "Nwosu", "Adewale", "Mohammed", "Eze", "Aliyu", "Adegoke", "Ezeh"]
roles = ["student", "instructor"]


# In[6]:


# Generate users
users = []
for i in range(30):
    first = random.choice(first_names)
    last = random.choice(last_names)
    role = random.choice(roles)
    user = {
        "userId": f"user_{100+i}",
        "email": f"{first.lower()}.{last.lower()}@example.com",
        "firstName": first,
        "lastName": last,
        "role": role,
        "dateJoined": datetime.utcnow(),
        "isActive": True,
        "profile": {
            "bio": f"I am a {role} at EduHub.",
            "avatar": "",
            "skills": random.sample(["Python", "Excel", "Java", "MongoDB", "HTML", "CSS", "JavaScript"], k=3)
        }
    }
    users.append(user)

# Insert users
result = db.users.insert_many(users)
print(f"Inserted {len(result.inserted_ids)} users into 'users' collection.")


# In[7]:


# Courses

# Get instructors from the users collection
instructors = [doc["userId"] for doc in db.users.find({"role": "instructor"}, {"userId": 1, "_id": 0})]

# Sample course categories and levels
categories = ["Programming", "Design", "Business", "Data Science", "Marketing"]
levels = ["beginner", "intermediate", "advanced"]


# In[8]:


# Generate 12 courses
courses = []
for i in range(12):
    instructor_id = random.choice(instructors)
    category = random.choice(categories)
    level = random.choice(levels)
    course = {
        "courseId": f"course_{200+i}",
        "title": f"Course {i+1} in {category}",
        "description": f"A comprehensive {level} course in {category}.",
        "instructorId": instructor_id,
        "category": category,
        "level": level,
        "duration": random.randint(5, 40),
        "price": round(random.uniform(20, 100), 2),
        "tags": random.sample(["python", "ui/ux", "strategy", "analytics", "ads", "machine learning"], k=3),
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
        "isPublished": random.choice([True, False])
    }
    courses.append(course)

# Insert courses
result = db.courses.insert_many(courses)
print(f"Inserted {len(result.inserted_ids)} courses into 'courses' collection.")


# In[9]:


# Enrollments

# Get all students
students = [doc["userId"] for doc in db.users.find({"role": "student"}, {"userId": 1, "_id": 0})]
course_ids = [doc["courseId"] for doc in db.courses.find({}, {"courseId": 1, "_id": 0})]

# Generate 20 enrollments
enrollments = []
for i in range(20):
    enrollment = {
        "enrollmentId": f"enroll_{300+i}",
        "studentId": random.choice(students),
        "courseId": random.choice(course_ids),
        "enrolledAt": datetime.utcnow(),
        "progress": round(random.uniform(0, 100), 2),
        "completed": random.choice([True, False])
    }
    enrollments.append(enrollment)

# Insert enrollments
result = db.enrollments.insert_many(enrollments)
print(f"Inserted {len(result.inserted_ids)} enrollments into 'enrollments' collection.")


# In[10]:


# Lessons

# Generate 30 lessons
lessons = []
for i in range(30):
    course_id = random.choice(course_ids)
    lesson = {
        "lessonId": f"lesson_{400+i}",
        "courseId": course_id,
        "title": f"Lesson {i+1} for {course_id}",
        "content": f"Detailed content for lesson {i+1}...",
        "duration": random.randint(10, 60),  # in minutes
        "createdAt": datetime.utcnow()
    }
    lessons.append(lesson)

# Insert lessons
result = db.lessons.insert_many(lessons)
print(f"Inserted {len(result.inserted_ids)} lessons into 'lessons' collection.")


# In[13]:


# Assignments

# Generate 13 assignments
assignments = []
for i in range(13):
    course_id = random.choice(course_ids)
    assignment = {
        "assignmentId": f"assign_{500+i}",
        "courseId": course_id,
        "title": f"Assignment {i+1} for {course_id}",
        "description": f"Complete the exercises for Assignment {i+1}.",
        "dueDate": datetime.utcnow() + timedelta(days=random.randint(3, 14)),
        "createdAt": datetime.utcnow()
    }
    assignments.append(assignment)

# Insert assignments
result = db.assignments.insert_many(assignments)
print(f"Inserted {len(result.inserted_ids)} assignments into 'assignments' collection.")


# In[12]:


from datetime import datetime, timedelta


# In[14]:


# Assignment Submissions

# Get assignment and student IDs
assignment_ids = [doc["assignmentId"] for doc in db.assignments.find({}, {"assignmentId": 1, "_id": 0})]

# Generate 15 assignment submissions
submissions = []
for i in range(15):
    submission = {
        "submissionId": f"sub_{600+i}",
        "assignmentId": random.choice(assignment_ids),
        "studentId": random.choice(students),
        "submittedAt": datetime.utcnow(),
        "content": f"This is submission content #{i+1}.",
        "grade": random.randint(60, 100),
        "feedback": f"Feedback for submission #{i+1}."
    }
    submissions.append(submission)

# Insert submissions
result = db.submissions.insert_many(submissions)
print(f"Inserted {len(result.inserted_ids)} submissions into 'submissions' collection.")


# In[15]:


#Task 3.1 – Create Operations

# Add a new student user
new_student = {
    "userId": "user_999",
    "email": "new.student@example.com",
    "firstName": "New",
    "lastName": "Student",
    "role": "student",
    "dateJoined": datetime.utcnow(),
    "isActive": True,
    "profile": {
        "bio": "I am excited to learn.",
        "avatar": "",
        "skills": ["Python", "MongoDB"]
    }
}
db.users.insert_one(new_student)


# In[16]:


# Create a new course
instructor = db.users.find_one({"role": "instructor"})
new_course = {
    "courseId": "course_999",
    "title": "Advanced MongoDB",
    "description": "Master advanced MongoDB techniques",
    "instructorId": instructor["userId"],
    "category": "Data Science",
    "level": "advanced",
    "duration": 30,
    "price": 120.00,
    "tags": ["mongo", "database"],
    "createdAt": datetime.utcnow(),
    "updatedAt": datetime.utcnow(),
    "isPublished": True
}
db.courses.insert_one(new_course)


# In[17]:


# Enroll a student in a course
new_enrollment = {
    "enrollmentId": "enroll_999",
    "studentId": new_student["userId"],
    "courseId": new_course["courseId"],
    "enrolledAt": datetime.utcnow(),
    "progress": 0.0,
    "completed": False
}
db.enrollments.insert_one(new_enrollment)


# In[18]:


# Add a new lesson to the new course
new_lesson = {
    "lessonId": "lesson_999",
    "courseId": new_course["courseId"],
    "title": "Lesson 1: Indexes",
    "content": "Introduction to Indexes in MongoDB",
    "duration": 45,
    "createdAt": datetime.utcnow()
}
db.lessons.insert_one(new_lesson)


# In[19]:


#Task 3.2 – Read Operations

# Find all active students
active_students = list(db.users.find({"role": "student", "isActive": True}))
for student in active_students:
    print(student["firstName"], student["lastName"], "–", student["email"])


# In[20]:


# Retrieve course details with instructor information
pipeline = [
    {"$match": {"courseId": "course_999"}},
    {"$lookup": {
        "from": "users",
        "localField": "instructorId",
        "foreignField": "userId",
        "as": "instructorInfo"
    }}
]
course_details = list(db.courses.aggregate(pipeline))
print(course_details)


# In[21]:


# Get all courses in a specific category
data_science_courses = list(db.courses.find({"category": "Data Science"}))
for course in data_science_courses:
    print(course["title"])


# In[22]:


# Find students enrolled in a particular course
enrolled_students = db.enrollments.find({"courseId": "course_999"})
for enrollment in enrolled_students:
    print(enrollment["studentId"])


# In[23]:


# Search courses by title (case-insensitive, partial match)
search_keyword = "mongo"
mongo_courses = db.courses.find({"title": {"$regex": search_keyword, "$options": "i"}})
for course in mongo_courses:
    print(course["title"])


# In[24]:


#Task 3.3 – Update Operations

# Update a user's profile information
db.users.update_one(
    {"userId": "user_999"},
    {"$set": {"profile.bio": "Updated student profile", "profile.skills": ["Python", "Data Analysis"]}}
)


# In[25]:


# Mark a course as published
db.courses.update_one(
    {"courseId": "course_999"},
    {"$set": {"isPublished": True, "updatedAt": datetime.utcnow()}}
)


# In[26]:


# Update assignment grades for a submission
db.submissions.update_one(
    {},  # Update the first available document
    {"$set": {"grade": 88.5, "feedback": "Well done!"}}
)


# In[27]:


# Add tags to an existing course
db.courses.update_one(
    {"courseId": "course_999"},
    {"$addToSet": {"tags": {"$each": ["NoSQL", "performance"]}}}
)


# In[29]:


#Task 3.4 – Delete Operations

# Soft delete a user by marking them inactive
db.users.update_one(
    {"userId": "user_999"},
    {"$set": {"isActive": False}}
)


# In[30]:


# Delete an enrollment
db.enrollments.delete_one(
    {"enrollmentId": "enroll_999"}
)


# In[31]:


# Delete a lesson from a course
db.lessons.delete_one(
    {"lessonId": "lesson_999"}
)


# In[32]:


#Part 4: Advanced Queries and Aggregation

#Part 4.1 – Complex Queries

# Find courses with price between $50 and $200
price_range_courses = db.courses.find({"price": {"$gte": 50, "$lte": 200}})
for course in price_range_courses:
    print(course["title"], course["price"])


# In[33]:


# Get users who joined in the last 6 months
six_months_ago = datetime.utcnow() - timedelta(days=180)
recent_users = db.users.find({"dateJoined": {"$gte": six_months_ago}})
for user in recent_users:
    print(user["firstName"], user["lastName"], user["dateJoined"])


# In[34]:


# Get users who joined in the last 6 months
six_months_ago = datetime.utcnow() - timedelta(days=180)
recent_users = db.users.find({"dateJoined": {"$gte": six_months_ago}})
for user in recent_users:
    print(user["firstName"], user["lastName"], user["dateJoined"])


# In[35]:


# Retrieve assignments with due dates in the next week
next_week = datetime.utcnow() + timedelta(days=7)
upcoming_assignments = db.assignments.find({"dueDate": {"$lte": next_week}})
for assignment in upcoming_assignments:
    print(assignment["title"], assignment["dueDate"])


# In[36]:


#Part 4.2 – Aggregation Pipeline

#4.2.1 - Course Enrollment Statistics

# Count total enrollments per course
enrollment_stats = db.enrollments.aggregate([
    {"$group": {"_id": "$courseId", "totalEnrollments": {"$sum": 1}}},
    {"$sort": {"totalEnrollments": -1}}
])
for stat in enrollment_stats:
    print("Course:", stat["_id"], "→ Total Enrollments:", stat["totalEnrollments"])


# In[37]:


# Calculate average course rating (if 'rating' field exists in course)
avg_rating_stats = db.courses.aggregate([
    {"$match": {"rating": {"$exists": True}}},
    {"$group": {"_id": "$category", "avgRating": {"$avg": "$rating"}}}
])
for stat in avg_rating_stats:
    print("Category:", stat["_id"], "→ Avg Rating:", round(stat["avgRating"], 2))


# In[38]:


# Group courses by category
category_group = db.courses.aggregate([
    {"$group": {"_id": "$category", "courseCount": {"$sum": 1}}},
    {"$sort": {"courseCount": -1}}
])
for group in category_group:
    print("Category:", group["_id"], "→ Number of Courses:", group["courseCount"])


# In[39]:


#4.2.2 Student Performance Analysis

# Average grade per student
avg_grade_per_student = db.submissions.aggregate([
    {"$group": {
        "_id": "$studentId",
        "avgGrade": {"$avg": "$grade"}
    }}
])
for result in avg_grade_per_student:
    print("Student:", result["_id"], "→ Average Grade:", round(result["avgGrade"], 2))


# In[40]:


# Completion rate by course
completion_rate = db.enrollments.aggregate([
    {"$group": {
        "_id": "$courseId",
        "total": {"$sum": 1},
        "completed": {"$sum": {"$cond": ["$completed", 1, 0]}}
    }},
    {"$project": {
        "completionRate": {"$multiply": [{"$divide": ["$completed", "$total"]}, 100]}
    }}
])
for result in completion_rate:
    print("Course:", result["_id"], "→ Completion Rate:", round(result["completionRate"], 2), "%")


# In[41]:


# Top-performing students (highest average grades)
top_students = db.submissions.aggregate([
    {"$group": {"_id": "$studentId", "avgGrade": {"$avg": "$grade"}}},
    {"$sort": {"avgGrade": -1}},
    {"$limit": 5}
])
for student in top_students:
    print("Student:", student["_id"], "→ Avg Grade:", round(student["avgGrade"], 2))


# In[42]:


#4.2.3 Instructor Analytics

# Total students taught by each instructor
instructor_students = db.enrollments.aggregate([
    {"$lookup": {
        "from": "courses",
        "localField": "courseId",
        "foreignField": "courseId",
        "as": "course"
    }},
    {"$unwind": "$course"},
    {"$group": {
        "_id": "$course.instructorId",
        "totalStudents": {"$sum": 1}
    }},
    {"$sort": {"totalStudents": -1}}
])
for instructor in instructor_students:
    print("Instructor:", instructor["_id"], "→ Total Students:", instructor["totalStudents"])


# In[43]:


# Average course rating per instructor (if rating exists)
avg_rating_per_instructor = db.courses.aggregate([
    {"$match": {"rating": {"$exists": True}}},
    {"$group": {
        "_id": "$instructorId",
        "avgInstructorRating": {"$avg": "$rating"}
    }},
    {"$sort": {"avgInstructorRating": -1}}
])
for result in avg_rating_per_instructor:
    print("Instructor:", result["_id"], "→ Avg Rating:", round(result["avgInstructorRating"], 2))


# In[44]:


# Revenue generated per instructor
instructor_revenue = db.courses.aggregate([
    {"$lookup": {
        "from": "enrollments",
        "localField": "courseId",
        "foreignField": "courseId",
        "as": "enrollments"
    }},
    {"$project": {
        "instructorId": 1,
        "price": 1,
        "enrollmentCount": {"$size": "$enrollments"},
        "revenue": {"$multiply": ["$price", {"$size": "$enrollments"}]}
    }},
    {"$group": {
        "_id": "$instructorId",
        "totalRevenue": {"$sum": "$revenue"}
    }},
    {"$sort": {"totalRevenue": -1}}
])
for result in instructor_revenue:
    print("Instructor:", result["_id"], "→ Revenue:", result["totalRevenue"])


# In[45]:


#4.2.4 Advanced Analytics

# Monthly enrollment trends
monthly_trends = db.enrollments.aggregate([
    {"$addFields": {
        "month": {"$dateToString": {"format": "%Y-%m", "date": "$enrolledAt"}}
    }},
    {"$group": {
        "_id": "$month",
        "count": {"$sum": 1}
    }},
    {"$sort": {"_id": 1}}
])
for trend in monthly_trends:
    print("Month:", trend["_id"], "→ Enrollments:", trend["count"])


# In[46]:


# Most popular course categories
popular_categories = db.courses.aggregate([
    {"$lookup": {
        "from": "enrollments",
        "localField": "courseId",
        "foreignField": "courseId",
        "as": "enrollments"
    }},
    {"$group": {
        "_id": "$category",
        "totalEnrollments": {"$sum": {"$size": "$enrollments"}}
    }},
    {"$sort": {"totalEnrollments": -1}}
])
for cat in popular_categories:
    print("Category:", cat["_id"], "→ Enrollments:", cat["totalEnrollments"])


# In[47]:


# Student engagement metrics (average submissions per enrolled student)
engagement_metrics = db.enrollments.aggregate([
    {"$lookup": {
        "from": "submissions",
        "localField": "studentId",
        "foreignField": "studentId",
        "as": "submissions"
    }},
    {"$group": {
        "_id": "$studentId",
        "submissionCount": {"$sum": {"$size": "$submissions"}}
    }},
    {"$group": {
        "_id": None,
        "avgSubmissions": {"$avg": "$submissionCount"}
    }}
])
for result in engagement_metrics:
    print("Average Submissions per Student:", round(result["avgSubmissions"], 2))


# In[48]:


#Part 5 – Indexing and Performance

# Create indexes
# Index on email for faster lookup
db.users.create_index("email")

# Index on course title and category for searching
db.courses.create_index([("title", 1), ("category", 1)])

# Index on dueDate in assignments
db.assignments.create_index("dueDate")

# Index on studentId and courseId in enrollments
db.enrollments.create_index([("studentId", 1), ("courseId", 1)])

# Confirm created indexes
print(list(db.users.index_information().keys()))
print(list(db.courses.index_information().keys()))
print(list(db.assignments.index_information().keys()))
print(list(db.enrollments.index_information().keys()))


# In[51]:


#5.2 Query Optimization and Performance Timing

# Measure query time before optimization
start_time = time.time()
list(db.users.find({"email": "grace.okoro@example.com"}))
end_time = time.time()
print("Email Lookup Time:", round(end_time - start_time, 6), "seconds")


# In[50]:


from pymongo import MongoClient
from datetime import datetime, timedelta
import time


# In[52]:


# Measure indexed course search
start_time = time.time()
list(db.courses.find({"title": {"$regex": "python", "$options": "i"}}))
end_time = time.time()
print("Course Search Time:", round(end_time - start_time, 6), "seconds")


# In[53]:


# Measure dueDate query with index
start_time = time.time()
list(db.assignments.find({"dueDate": {"$exists": True}}))
end_time = time.time()
print("Due Date Query Time:", round(end_time - start_time, 6), "seconds")


# In[54]:


#Part 6: Data Validation and Error Handling

#Schema Validation
# Create users collection with schema validation
user_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["userId", "email", "firstName", "lastName", "role", "dateJoined", "isActive"],
        "properties": {
            "userId": {"bsonType": "string"},
            "email": {
                "bsonType": "string",
                "pattern": "^.+@.+\\..+$",
                "description": "Must be a valid email"
            },
            "firstName": {"bsonType": "string"},
            "lastName": {"bsonType": "string"},
            "role": {
                "enum": ["student", "instructor"],
                "description": "Role must be either student or instructor"
            },
            "dateJoined": {"bsonType": "date"},
            "isActive": {"bsonType": "bool"},
            "profile": {
                "bsonType": "object",
                "properties": {
                    "bio": {"bsonType": "string"},
                    "avatar": {"bsonType": "string"},
                    "skills": {"bsonType": "array", "items": {"bsonType": "string"}}
                }
            }
        }
    }
}

# Drop and recreate collection with validation
if "users" in db.list_collection_names():
    db.users.drop()

db.create_collection("users", validator=user_schema)
print("Users collection created with schema validation.")


# In[55]:


#6.2 Error Handling

# Example 1: Handle duplicate user insertion
try:
    db.users.insert_one({
        "userId": "U001",
        "email": "grace.okoro@example.com",  # Assuming already inserted
        "firstName": "Grace",
        "lastName": "Okoro",
        "role": "student",
        "dateJoined": datetime.utcnow(),
        "isActive": True
    })
except Exception as e:
    print("Duplicate insertion error:", e)


# In[56]:


# Example 2: Handle missing required fields
try:
    db.users.insert_one({
        "userId": "U999"
    })
except Exception as e:
    print("Validation failed due to missing fields:", e)


# In[57]:


# Example 3: Handle invalid data types
try:
    db.courses.insert_one({
        "courseId": "C999",
        "title": "Test Course",
        "instructorId": "I001",
        "price": "Free"  # Invalid: should be a number
    })
except Exception as e:
    print("Invalid data type error:", e)


# In[58]:


course_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["courseId", "title", "instructorId", "price"],
        "properties": {
            "courseId": {"bsonType": "string"},
            "title": {"bsonType": "string"},
            "instructorId": {"bsonType": "string"},
            "price": {"bsonType": "double"}  # or "number"
        }
    }
}

if "courses" in db.list_collection_names():
    db.courses.drop()

db.create_collection("courses", validator=course_schema)


# In[59]:


# Example 3: Handle invalid data types
try:
    db.courses.insert_one({
        "courseId": "C999",
        "title": "Test Course",
        "instructorId": "I001",
        "price": "Free"  # Invalid: should be a number
    })
except Exception as e:
    print("Invalid data type error:", e)


# In[ ]:




