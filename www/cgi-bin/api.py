#!/usr/bin/python
from __future__ import print_function

import cgi
import subprocess
import json
import os
import sys
form = cgi.FieldStorage()

FILESHARE_DIR = '/tmp/simple-fileshare/files/'

def get_buckets():
	return os.listdir(FILESHARE_DIR)

def get_folders(bucket):
	return os.listdir(FILESHARE_DIR + bucket)

def get_field(name, allowed_values=False):
	value = form.getvalue(name)
	if value is None or value is "":
		print("the field '{name}' must be defined.".format(**locals()))
		sys.exit(1)
	elif allowed_values != False and value not in allowed_values:
		print("ERROR: value '{value}' for field '{name}' is not in '{allowed_values}'".format(**locals()))
		sys.exit(1)
	else:
		return value

def send_json(obj):
	print("Content-type:application/json\r\n\r\n")
	print(json.dumps(obj))
	sys.exit(0)

if form.has_key('folder-action'):
	action = get_field('folder-action', ['remove', 'add'])
	folder = get_field('folder')
	bucket = get_field('bucket', allowed_values=get_buckets())
	path = os.path.join(os.path.join(FILESHARE_DIR, bucket, folder))
	os.rmdir(path) if action == 'remove' else os.mkdir(path)
	send_json(path)

if form.has_key('list-buckets'):
	send_json(get_buckets())

if form.has_key('list-folders'):
	bucket = get_field('bucket', allowed_values=get_buckets())
	bucket_path = os.path.normpath(bucket)

	if '.' in bucket_path:
		print("Not cool man!")
		sys.exit(1)

	send_json(get_folders(bucket_path))

print("Content-type:text/html\r\n\r\n")

link = get_field('link')
bucket = get_field('bucket', get_buckets())
folder = get_field('folder', get_folders(bucket))

filename = link.split("/").pop()

with open(os.path.join(FILESHARE_DIR, bucket, folder, filename), 'w') as f:
    subprocess.call(["curl", "-L", "-v", link], stdout=f)
    print("Request was successful. <br>")
    print("Link to the file: <br>")
    print("<a href='/{bucket}/{folder}/{filename}'>download /{bucket}/{folder}/{filename}</a>".format(**locals()))
    print("<br><br>")
    print("<a href='/{bucket}/{folder}'>go to /{bucket}/{folder}/</a>".format(**locals()))
    print("<br><br>")
    print("<a href='/'>go to /</a>".format(**locals()))

