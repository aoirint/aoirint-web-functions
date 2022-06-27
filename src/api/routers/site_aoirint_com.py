from typing import Any, Dict
from fastapi import APIRouter, Depends
from ..const import hmac_auth

router = APIRouter()

@router.get('/sync', dependencies=[Depends(hmac_auth)])
async def sync(body: Dict[str, Any]):
  print(body)
