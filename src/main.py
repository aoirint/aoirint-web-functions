from fastapi import FastAPI

from api import const
from api.routers import (
  site_aoirint_com,
)

app = FastAPI()
app.include_router(site_aoirint_com.router, prefix='/site.aoirint.com')
