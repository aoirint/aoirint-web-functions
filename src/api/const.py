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
  signature_bytes = hmac.digest(key=key, msg=msg, digest=hashlib.sha256)

  given_signature_bytes = x_gitea_signature.encode('ascii')

  if not hmac.compare_digest(signature_bytes, given_signature_bytes):
    raise HTTPException(status_code=403, detail='Invalid signature')
