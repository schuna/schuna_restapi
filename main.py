from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import endpoints.authentication as auth_endpoints
import endpoints.comment as comment_endpoints
import endpoints.inbody as inbody_endpoints
import endpoints.post as post_endpoints
import endpoints.user as user_endpoints
from container import Container

load_dotenv()
container = Container()
db = container.db()
db.create_database()

app = FastAPI()
app.container = container
app.include_router(inbody_endpoints.router)
app.include_router(comment_endpoints.router)
app.include_router(auth_endpoints.router)
app.include_router(user_endpoints.router)
app.include_router(post_endpoints.router)

origins = [
    'http://localhost:3000',
    'http://localhost:3001'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

