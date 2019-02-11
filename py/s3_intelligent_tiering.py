"""
MIT License
Copyright (c) 2019 Blue Cloud Red Dot
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
import boto3
import botocore

PARSER = argparse.ArgumentParser()
PARSER.add_argument("bucket", help="Please enter the name of the S3 bucket", type=str)
PARSER.add_argument("key", help="Please enter the key (prefix) of the object(s)", type=str)
PARSER.add_argument("--recursive", help="Please use if all objects with the prefix should be included", action="store_true")
ARGS = PARSER.parse_args()

CLIENT = boto3.client('s3')
S3 = boto3.resource('s3')

COPY_SOURCE = {
    'Bucket': ARGS.bucket,
    'Key': ARGS.key
}

if ARGS.recursive:
    try:
        RESPONSE = CLIENT.list_objects_v2(Bucket=ARGS.bucket, Prefix=ARGS.key)
        for obj in RESPONSE[Contents][Key]:
            print(obj)
            S3.meta.client.copy(COPY_SOURCE, ARGS.bucket, prefix.get('Prefix'), ExtraArgs={'StorageClass':'INTELLIGENT_TIERING'})
    except botocore.exceptions.ClientError:
        print("404 - Sorry, the object you tried cannot be found.")
else:
    S3.meta.client.copy(COPY_SOURCE, ARGS.bucket, ARGS.key, ExtraArgs={'StorageClass':'INTELLIGENT_TIERING'})
