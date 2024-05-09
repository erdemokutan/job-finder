
# Job Finder

API of a Linkedin-like job search platform written in Python Django

# 🚀 Quick start

### Step 1: Clone The Repo

```bash
git clone https://github.com/erdemokutan/job-finder.git
```
### Step 2: Create a Virtual Environment
python -m virtualenv venv

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚠️ If you have **trouble installing the GDAL package** while installing dependencies **pip install -r requirements.txt** , you can install it with **Anaconda** without any problems

Download the Anaconda on your system (https://www.anaconda.com/download)



Then within your virtual env you can install with conda (https://anaconda.org/conda-forge/gdal)


### Step 4: Run Migrations

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
### Step 5: Run the App
```bash
python manage.py runserver
```


### Settings.py Environment Variables
You should configure the following settings specifically for your own project
```bash
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

VIRTUAL_ENV_BASE = os.environ.get('VIRTUAL_ENV')

#GDAL_LIBRARY_PATH = r'C:\\Users\\ERDEM OKUTAN\\Desktop\\job-portal\\myenv\\Lib\\site-packages\\osgeo\\gdal304.dll'
#GEOS_LIBRARY_PATH=r'C:\\Users\\ERDEM OKUTAN\\Desktop\\job-portal\\myenv\\Lib\\site-packages\\osgeo\\geos_c.dll'

#print(VIRTUAL_ENV_BASE)

GDAL_LIBRARY_PATH =VIRTUAL_ENV_BASE + '/Lib/site-packages/osgeo/gdal304.dll'
GEOS_LIBRARY_PATH=VIRTUAL_ENV_BASE + '/Lib/site-packages/osgeo/geos_c.dll'
```







## API Manual

### Register

```http
  POST /api/register/
```

| Parameter | Type     | 
| :-------- | :------- | 
| `first_name` | `string` 

| Parameter | Type     | 
| :-------- | :------- | 
| `last_name` | `string` 

| Parameter | Type     | 
| :-------- | :------- | 
| `email` | `string` | 

| Parameter | Type     | 
| :-------- | :------- | 
| `password` | `string` | 

#### Login

```http
  POST /api/token/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` |  |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `password` | `string` |   |

#### Get Current User

```http
  GET /api/me/
```

| Parameter |      | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      |  |  Bearer Token |

### Update User

```http
  PUT /api/me/update/
```

| Parameter | Type     | 
| :-------- | :------- | 
| `first_name` | `string` 

| Parameter | Type     | 
| :-------- | :------- | 
| `last_name` | `string` 

| Parameter | Type     | 
| :-------- | :------- | 
| `email` | `string` | 

| Parameter | Type     | 
| :-------- | :------- | 
| `password` | `string` | 


### Upload Resume

```http
  PUT /api/upload/resume/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `resume` | `file` |  Upload your resume on AWS S3 Bucket |


### Get All Jobs

```http
  GET /api/jobs/
```



### Get a Job

```http
  GET /api/jobs/1/
```


### Delete a Job

```http
  DEL /api/jobs/1/delete/
```

### Get Job Stats

```http
  GET /api/stats/devops/
```

### Get Current User Applied Jobs

```http
  GET /api/me/jobs/applied/
```

### Apply to Job

```http
  POST /api/jobs/2/apply/
```

### Check Applied Jobs

```http
  GET /api/jobs/3/check
```

### Get Current Users Shared Jobs

```http
  GET /api/me/jobs
```
### Get Candidates Applied


```http
  GET /api/job/3/candidates/
```





  
## Tech Stack



**Backend:** Django, Postgresql,JWT, AWS S3 Bucket

  
