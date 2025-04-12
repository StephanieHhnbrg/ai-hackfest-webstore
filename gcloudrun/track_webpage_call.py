import functions_framework
from flask import Flask, request, jsonify, make_response
from google.cloud import firestore

@functions_framework.http
def track_webpage_call(request):
  if request.method == 'OPTIONS':
    return handle_cors()

  update_tracking_db()
  return create_response()


def update_tracking_db():
  db = firestore.Client(database='marketing-campaign')
  db.collection('tracking').add({
    "event": "webpage_call",
    "timestamp": firestore.SERVER_TIMESTAMP
  })

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
