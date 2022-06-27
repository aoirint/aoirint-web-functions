import hashlib
import hmac
import os
from dotenv import load_dotenv
from fastapi import Body, HTTPException, Header

load_dotenv()

HMAC_SECRET = os.environ['HMAC_SECRET']


async def hmac_auth(
  body: str = Body(),
  x_gitea_signature = Header(),
):
  key = HMAC_SECRET
  msg = body
  signature = hmac.digest(key=key, msg=msg, digest=hashlib.sha256)

  if signature != x_gitea_signature:
    raise HTTPException(status_code=403, detail='Invalid signature')
