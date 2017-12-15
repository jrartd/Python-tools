# Data minig Facebook
#token EAAJZCEULgfrgBAHwxmI8Y0WbZBZAewQ4knuZAFnKS851jZASGuk4FNnSF8NTL57lkRjyqtrrvR5ZA6ZAMjxWtqLcIEdf74JZBbA8n5oa4XBAcgTOomFFfz1XzyxBZCZCZASnKPZAf6bTZBcVLWgiMSHLIZBJ82yUmVZAWKc2vRrrPyxICzm9hZAo7kZBQYwcapUL2jIImZC1mQQxyuCnojaQZDZD

"""setear token
set FACEBOOK_TEMP_TOKEN="your token"
"""
import os
import json
import facebook

FACEBOOK_TEMP_TOKEN = "EAAJZCEULgfrgBANMU9Umwh0yJWIfOxHe1YZAfW9aH98ZCIzUeDsR2Hi82EYdPR84z2Tj71GzOv1opafM3ClWcQ7hy1IZAUgSI2aeUFDfqjAzDQYqR58ktKFfU1h6fY30ofDruFzcFhe2G5loljs5zIyF9jcsUlziTqMsAUuzerQuRjoZAe4ohrFZCBeE8n6yzVMyqNZBNWWKAZDZD"

if __name__ == '__main__':
	token = os.environ.get("FACEBOOK_TEMP_TOKEN")

	graph = facebook.GraphAPI()
	profile = graph.get_object("me", fields="name,location")

	print (json.dumps(profile,indent=4))