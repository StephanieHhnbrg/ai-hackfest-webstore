import functions_framework
from flask import Flask, request, jsonify, make_response
from google.cloud import firestore

@functions_framework.http
def track_webpage_purchase(request):
  if request.method == 'OPTIONS':
    return handle_cors()

  update_tracking_db(request)

  return create_response()


def update_tracking_db(request):
  request_json = request.get_json(silent=True)
  request_args = request.args
  user_id = get_field_from_req(request_json, request_args, 'userId')
  campaign_id = get_field_from_req(request_json, request_args, 'campaign')
  time = get_time_from_req(request_json, request_args)


  db = firestore.Client(database='marketing-campaign')
  db.collection('tracking').add({
    "user_id": user_id,
    "campaign_id": campaign_id,
    "time": time,
    "event": "purchases_completed",
    "timestamp": firestore.SERVER_TIMESTAMP
  })


def get_field_from_req(request_json, request_args, field):
  if request_json and field in request_json:
    return request_json[field]
  elif request_args and field in request_args:
    return request_args[field]
  else:
    return ""


def get_time_from_req(request_json, request_args):
  if request_json and 'duration' in request_json:
    return request_json['duration']
  elif request_args and 'duration' in request_args:
    return request_args['duration']
  else:
    return 0


ALLOWED_ORIGINS = [
  'http://localhost:4200',
  'https://stephaniehhnbrg.github.io'
]


def handle_cors():
  response = make_response()
  response.status_code = 204
  for origin in ALLOWED_ORIGINS:
    response.headers['Access-Control-Allow-Origin'] = origin
  response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
  response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
  return response


def create_response(data):
  response = make_response(jsonify(data))
  response.status_code = 200
  for origin in ALLOWED_ORIGINS:
    response.headers['Access-Control-Allow-Origin'] = origin
  return response

