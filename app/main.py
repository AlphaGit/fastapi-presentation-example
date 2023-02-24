from fastapi import FastAPI, Depends

from .post_routes import router as post_router
from .system_routes import router as system_router
from .users import router as users_router, oauth2_scheme

app = FastAPI(
    title="Blog API",
    description="API for a blog.",
    version="0.1.0",
    contact={
        "name": "JD",
        "url": "https://blog.alphasmanifesto.com",
        "email": "jraimondi@makingsense.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
    openapi_tags=[
        {
            "name": "system",
            "description": "System health and status",
        },
        {
            "name": "post",
            "description": "Operations related to posts",
        },
        {
            "name": "users",
            "description": "Operations related to users",
        },
    ]
)

app.include_router(system_router, dependencies=[Depends(oauth2_scheme)])
app.include_router(post_router, dependencies=[Depends(oauth2_scheme)])
app.include_router(users_router, dependencies=[])
