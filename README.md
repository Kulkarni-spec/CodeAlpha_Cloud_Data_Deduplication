\# Cloud Data Deduplication System



\## Overview

This project is a cloud-based system that detects and prevents duplicate data storage using hashing techniques.



\## Features

\- Identifies redundant data using SHA-256 hashing

\- Validates new data against existing records

\- Prevents duplicate entries

\- Stores unique data in AWS S3

\- Stores metadata in DynamoDB



\## Technologies Used

\- Python

\- AWS S3

\- AWS DynamoDB

\- Boto3



\## How It Works

1\. User inputs data

2\. System generates hash

3\. Hash is checked in DynamoDB

4\. If duplicate → rejected

5\. If unique → stored in S3 and DynamoDB



\## Setup Instructions

1\. Install dependencies:

