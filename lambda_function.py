import json
import os
import time
import uuid

import boto3

bedrock = boto3.client("bedrock-runtime")
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

MODEL_ID = os.environ["MODEL_ID"]
BUCKET = os.environ.get("UPLOAD_BUCKET")
TABLE_NAME = os.environ.get("TABLE_NAME")

MAX_CHARS = 20000

PROMPT = """You are a study assistant. Read the notes below and reply with ONLY valid JSON
in this exact shape, with no extra text and no markdown fences:

{
  "summary": "A clear summary in 4-6 sentences.",
  "quiz": [
    {
      "question": "...",
      "options": ["A", "B", "C", "D"],
      "answer": "the correct option, copied exactly"
    }
  ]
}

Write 5 multiple-choice questions.

NOTES:
"""


def _response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(body),
    }


def _get_text(payload):
    if payload.get("text"):
        return payload["text"]
    key = payload.get("s3_key")
    if key and BUCKET:
        obj = s3.get_object(Bucket=BUCKET, Key=key)
        return obj["Body"].read().decode("utf-8", errors="ignore")
    return None


def _parse_model_output(raw):
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        if cleaned.lower().startswith("json"):
            cleaned = cleaned[4:]
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {"summary": raw, "quiz": []}


def lambda_handler(event, context):
    try:
        payload = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return _response(400, {"error": "Request body must be valid JSON."})

    text = _get_text(payload)
    if not text or not text.strip():
        return _response(400, {"error": "Send 'text' or an 's3_key'."})

    text = text[:MAX_CHARS]
    language = str(payload.get("language") or "English")[:30]

    try:
        resp = bedrock.converse(
            modelId=MODEL_ID,
            messages=[{"role": "user", "content": [{"text": f"Write all text values in {language}.\n\n" + PROMPT + text}]}],
            inferenceConfig={"maxTokens": 1500, "temperature": 0.3},
        )
        raw = resp["output"]["message"]["content"][0]["text"]
    except Exception as exc:
        print("Bedrock error:", exc)
        return _response(502, {"error": "The AI model call failed."})

    result = _parse_model_output(raw)
    session_id = str(uuid.uuid4())
    result["id"] = session_id

    if TABLE_NAME:
        try:
            dynamodb.Table(TABLE_NAME).put_item(
                Item={
                    "id": session_id,
                    "created_at": int(time.time()),
                    "result": json.dumps(result),
                }
            )
        except Exception as exc:
            print("DynamoDB error:", exc)

    return _response(200, result)
