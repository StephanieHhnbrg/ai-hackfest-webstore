import functions_framework
from flask import Flask, request, jsonify, make_response
from google.cloud import firestore

@functions_framework.http
def track_mail_campaign_click(request):
  if request.method == 'OPTIONS':
    return handle_cors()

  update_tracking_db(request)

  return create_response()


def update_tracking_db(request):
  request_json = request.get_json(silent=True)
  request_args = request.args
  user_id = get_field_from_req(request_json, request_args, 'userId')
  capaign_id = get_field_from_req(request_json, request_args, 'campaign')


  db = firestore.Client(database='marketing-campaign')
  db.collection('tracking').add({
    "user_id": user_id,
    "capaign_id": capaign_id,
    "event": "email_bttn_clicked",
    "timestamp": firestore.SERVER_TIMESTAMP
  })


def get_field_from_req(request_json, request_args, field):
  if request_json and field in request_json:
    return request_json[field]
  elif request_args and field in request_args:
    return request_args[field]
  else:
    return ""


def handle_cors():
  response = make_response()
  response.status_code = 204
  response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4200'
  response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
  response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
  return response


def create_response():
  response = make_response()
  response.status_code = 200
  response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4200'
  return response
