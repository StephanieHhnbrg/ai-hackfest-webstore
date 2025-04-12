import functions_framework
from flask import Flask, request, jsonify, make_response
from google.cloud import firestore

@functions_framework.http
def track_webpage_purchase(request):
  if request.method == 'OPTIONS':
    return handle_cors()

  request_json = request.get_json(silent=True)
  request_args = request.args
  if get_time_from_req(request_json, request_args) == 0:
    return create_response() # if time is not present, purchased is not logged due to falsification of metrics otherwise

  update_webpage_metrics(request_json, request_args)
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
    purchases = data.get('purchases', 0) + 1
    time = data.get('time', 0) + get_time_from_req(request_json, request_args)
    doc_ref.update({
      'purchases': purchases,
      'time': time
    })


def update_webpage_metrics(request_json, request_args):
  db = firestore.Client(database='marketing-campaign')
  doc_ref = db.collection('webpage-metrics').document('store')
  doc = doc_ref.get()

  if doc.exists:
    data = doc.to_dict()
    purchases = data.get('purchases', 0) + 1
    time = data.get('time', 0) + get_time_from_req(request_json, request_args)
    doc_ref.update({
      'purchases': purchases,
      'time': time
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


def get_time_from_req(request_json, request_args):
  if request_json and 'duration' in request_json:
    return request_json['duration']
  elif request_args and 'duration' in request_args:
    return request_args['duration']
  else:
    return 0

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
