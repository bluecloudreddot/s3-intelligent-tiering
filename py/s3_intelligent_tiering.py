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
PARSER.add_argument("-k" "--key", help="Please enter the key of the object", type=str)
PARSER.add_argument("-p" "--prefix", help="Please enter the prefix of the objects", type=str)
PARSER.add_argument("-s" "--suffix", help="Please enter the suffix of the objects", type=str)
PARSER.add_argument("-r" "--recursive", help="Please use if all objects with the prefix should be included", action="store_true")
ARGS = PARSER.parse_args()

CLIENT = boto3.client('s3')
S3 = boto3.resource('s3')

if ARGS.recursive:
    while True:
        RESPONSE = CLIENT.list_objects_v2(Bucket=ARGS.bucket, Prefix=ARGS.key)
        try:
            CONTENTS = RESPONSE['Contents']
        except KeyError:
            print("Key error.")
        for CONTENT in CONTENTS:
            KEY = CONTENT['Key']
            if KEY.startswith(ARGS.prefix) and KEY.endswith(ARGS.suffix):
                COPY_SOURCE = {
                    'Bucket': ARGS.bucket,
                    'Key': ARGS.prefix + ARGS.key + ARGS.suffix
                }
                print(CONTENT['Key'])
        # S3.meta.client.copy(COPY_SOURCE, ARGS.bucket, prefix.get('Prefix'), ExtraArgs={'StorageClass':'INTELLIGENT_TIERING'})
        try:
            ARGS['ContinuationToken'] = RESPONSE['NextContinuationToken']
        except KeyError:
            break
else:
    try:
        COPY_SOURCE = {
            'Bucket': ARGS.bucket,
            'Key': ARGS.key
        }
        S3.meta.client.copy(COPY_SOURCE, ARGS.bucket, ARGS.key, ExtraArgs={'StorageClass':'INTELLIGENT_TIERING'})
    except botocore.exceptions.ClientError:
        print("404 - Sorry, the object you tried cannot be found.")
