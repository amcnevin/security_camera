#!/usr/bin/python

import uuid
import os
import requests


# generate a uuid and capture an image from the raspistill cmd
# upload to slack via files.upload method and remove file upon success
def slack_capture():
	imgId = uuid.uuid4()

	filename = str(imgId)+'.jpg'

	command = 'raspistill -o "{0}"'.format(filename)

	os.popen(command)


	methodUrl = "https://slack.com/api/files.upload"

	token = "<SLACK_TOKEN>"

	payload = {
		"filename":filename,
		"token": token,
		"channels":['notifications'],
	}

	fileContents = {
		'file' : (filename, open(filename, 'rb'), 'jpg')
	}


	r = requests.post(methodUrl, params=payload, files=fileContents)


	if r.status_code == 200:
		print "Captured"
		os.remove(filename)
	else:
		print "Captured, but not uploaded"

