import hashlib
import hmac
import os
from dotenv import load_dotenv
from fastapi import Request, HTTPException, Header

load_dotenv()

HMAC_SECRET = os.environ['HMAC_SECRET'].encode('ascii')


async def hmac_auth(
  request: Request,
  x_gitea_signature: str = Header(),
):
  key = HMAC_SECRET
  msg = await request.body()
  payload_signature = hmac.new(key=key, digestmod=hashlib.sha256).update(msg=msg).hexdigest()

  if not hmac.compare_digest(payload_signature, x_gitea_signature):
    raise HTTPException(status_code=403, detail='Invalid signature')
