from fastapi import FastAPI

from app.api import auth as auth_router
from app.api import users as users_router
from app.api import projects as projects_router 

app = FastAPI(
    title="Infrastructure Drift Detective",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


# include routers
app.include_router(auth_router.router)
app.include_router(users_router.router)
app.include_router(projects_router.router)  
