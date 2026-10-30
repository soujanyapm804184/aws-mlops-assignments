# Assignment 1: Flask App to List S3 Files

## Objective

Build and deploy a Flask web application that lists filenames from folders in an Amazon S3 bucket using Python and Boto3.

## Architecture

- **S3 bucket:** `tiger-mle-pg`
- **S3 region:** `ap-south-1`
- **S3 prefix:** `home/soujanya.puranmatt/`
- **EC2 instance type:** `t3.micro`
- **Application port:** `8085`
- **Application server:** Gunicorn

## S3 Folder Structure

```text
s3://tiger-mle-pg/home/soujanya.puranmatt/
├── A/
├── B/
└── C/
```

Each folder contains test files. The Flask app lists the files in the selected folder using Boto3.

## Prerequisites

- Python 3
- AWS CLI
- AWS credentials or an approved AWS CLI profile for local testing
- An S3 bucket with test files
- An EC2 instance with an IAM role allowing the required S3 listing operation

## Local Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

   `pip install -r requirements.txt`

3. Configure AWS credentials using an approved profile.
4. Start the app:

   `python app.py`

5. Open `http://127.0.0.1:8085/files?folder=A`.

## API Endpoints

| Endpoint | Description |
|---|---|
| `/` | Application status |
| `/files?folder=A` | List files in folder A |
| `/files?folder=B` | List files in folder B |
| `/files?folder=C` | List files in folder C |

Invalid folder names return HTTP 400.

## EC2 Deployment

1. Launch a `t3.micro` instance in `ap-south-1`.
2. Attach an IAM instance role with least-privilege S3 permissions.
3. Configure inbound access for TCP port 8085.
4. Install Python and the project dependencies.
5. Start Gunicorn:

   `gunicorn --bind 0.0.0.0:8085 app:app`

6. Open `http://13.127.8.196:8085/files?folder=A`.

## AWS Resource Tags

| Key | Value |
|---|---|
| `owner` | `soujanya.puranma@tigeranalytics.com` |
| `project` | `aws-training` |

## Screenshots

### 1. Connecting to EC2 using SSH

![Connecting to EC2 using SSH](./screenshots/EC2_console.png)

### 2. Local run

![Local run](./screenshots/local_run.png)

### 3. S3 Bucket Structure

![S3 Folders](./screenshots/S3_bucket_structure_1.png)

### 4. S3 File Listings

![Folder A Listing](./screenshots/S3_bucket_structure_2.png)

### 5. App output from EC2

![App output 1](./screenshots/result%201.png)

![App output 2](./screenshots/result%202.png)

![App output 3](./screenshots/result%203.png)





