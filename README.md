#  CodeAlpha - Cloud Data Deduplication System

##  Internship Task

This project is developed as part of the **CodeAlpha Cloud Computing Internship (Task 1: Data Redundancy Removal System)**.

---

##  Project Overview

This system is designed to detect and eliminate redundant data in a cloud environment using hashing techniques. It ensures that only unique data is stored, improving storage efficiency and preventing duplication.

---

##  Objectives

* Identify redundant data in cloud storage
* Validate incoming data against existing records
* Prevent duplicate data insertion
* Store only unique and verified data
* Improve database efficiency and accuracy

---

##  Features

*  SHA-256 hashing for duplicate detection
*  Real-time validation of new data
*  Automatic rejection of duplicate entries
*  Storage of unique data in AWS S3
*  Metadata storage using DynamoDB

---

##  Tech Stack

* Python
* AWS S3
* AWS DynamoDB
* Boto3

---

##  How It Works

1. User submits data
2. System generates SHA-256 hash
3. Hash is checked in DynamoDB
4. If duplicate → request rejected
5. If unique → data stored in S3 and metadata stored in DynamoDB

---

##  Testing

The system was tested for:

* Duplicate data inputs
* Unique data inputs
* Storage validation
* Hash comparison accuracy

---

##  Cloud Integration

* AWS S3 → stores actual data
* AWS DynamoDB → stores hashes for fast lookup

---

##  Conclusion

This system ensures efficient cloud storage by eliminating redundant data and maintaining a clean, optimized dataset. It demonstrates practical implementation of cloud-based deduplication techniques.

---

##  Author

Chaitanya Kulkarni
CodeAlpha Intern
