import functions_framework
from flask import Flask, request, jsonify, make_response
from google.cloud import firestore

@functions_framework.http
def track_mail_campaign_click(request):
  if request.method == 'OPTIONS':
    return handle_cors()

  request_json = request.get_json(silent=True)
  request_args = request.args
  if is_marketing_campaign(request_json, request_args):
    update_campaign_metrics(request_json, request_args)

  return create_response()


def update_campaign_metrics(request_json, request_args):
  name = get_field_from_req(request_json, request_args, 'campaign')
  variant = get_field_from_req(request_json, request_args, 'content')
  id = f"{name}_{variant}"

  db = firestore.Client(database='marketing-campaign')
  doc_ref = db.collection('marketing-campaign').document(id)
  doc = doc_ref.get()
  if doc.exists:
    data = doc.to_dict()
    clicks = data.get('clicks', 0) + 1
    doc_ref.update({
      'clicks': clicks,
    })


def is_marketing_campaign(request_json, request_args):
  return (request_json and 'campaign' in request_json) or (request_args and 'campaign' in request_args)


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
