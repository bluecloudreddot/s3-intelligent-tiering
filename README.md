# S3 Intelligent Tiering

## Instructions
1. Install [Python](https://www.python.org/downloads/)
2. Install and configure the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
3. Install [boto3](https://pypi.org/project/boto3/) and [botocore](https://pypi.org/project/botocore/)
4. Download the [S3 Intelligent Tiering Python script](https://github.com/bluecloudreddot/s3-intelligent-tiering/blob/master/py/s3_intelligent_tiering.py)
5. In Windows:
    * Open a Command Prompt by clicking Start, typing 'cmd' and pressing 'Enter'
    * Navigate to the folder containing the downloaded file by typing 'cd (filepath)' and pressing 'Enter'
    * Run the Python file by typing 'python s3_intelligent_tiering.py' followed by the arguments below. 
6. In Mac OS X:
    * Open a Terminal window by pressing Command + Space, typing 'Terminal' and pressing 'Enter'
    * Navigate to the folder containing the downloaded file by typing 'cd (filepath)' and pressing 'Enter'
    * Run the Python file by typing 'python s3_intelligent_tiering.py' followed by the arguments below. 
7. Arguments:
    * "bucket" - enter the name of the S3 bucket
    * "-k"/"--key" - enter the key of the object
    * "-p"/"--prefix" - enter the prefix of the objects
    * "-s"/"--suffix" - enter the suffix of the objects
    * "-r"/"--recursive" - use if all objects with the prefix/suffix should be included

## Example commands
### To move a specific object to S3 Intelligent Tiering
```` python s3_intelligent_tiering.py "bucket_name" -k "folder_name/object.obj"````

### To move all objects within a specific folder to S3 Intelligent Tiering
```` python s3_intelligent_tiering.py "bucket_name" -p "folder_name" -r````

### To move all objects with a specific suffix to S3 Intelligent Tiering
```` python s3_intelligent_tiering.py "bucket_name" -s ".csv" -r````

### To move all objects within a specific bucket to S3 Intelligent Tiering
```` python s3_intelligent_tiering.py "bucket_name" -r````
