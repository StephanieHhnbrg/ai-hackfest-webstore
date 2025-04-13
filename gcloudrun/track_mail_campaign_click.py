import functions_framework
from flask import Flask, request, jsonify, make_response
from google.cloud import firestore

@functions_framework.http
def track_mail_campaign_click(request):
  if request.method == 'OPTIONS':
    return handle_cors(request)

  update_tracking_db(request)

  return create_response({}, request)


def update_tracking_db(request):
  request_json = request.get_json(silent=True)
  request_args = request.args
  user_id = get_utm_field_from_req(request_json, request_args, 'userId')
  campaign_id = get_utm_field_from_req(request_json, request_args, 'campaign')


  db = firestore.Client(database='marketing-campaign')
  db.collection('tracking').add({
    "user_id": user_id,
    "campaign_id": campaign_id,
    "event": "email_bttn_clicked",
    "timestamp": firestore.SERVER_TIMESTAMP
  })


def get_utm_field_from_req(request_json, request_args, field):
  if request_json and 'utm' in request_json:
    return request_json['utm'][field]
  elif request_args  and 'utm' in request_args:
    return request_args['utm'][field]
  else:
    return ""


ALLOWED_ORIGINS = [
  'http://localhost:4200',
  'https://stephaniehhnbrg.github.io'
]


def handle_cors(request):
  response = make_response()
  response.status_code = 204
  origin = request.headers.get('Origin')
  if origin in ALLOWED_ORIGINS:
    response.headers['Access-Control-Allow-Origin'] = origin
  response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
  response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
  return response


def create_response(data, request):
  response = make_response(jsonify(data))
  response.status_code = 200
  origin = request.headers.get('Origin')
  if origin in ALLOWED_ORIGINS:
    response.headers['Access-Control-Allow-Origin'] = origin
  return response
