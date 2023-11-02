from typing import Any, Optional, List, Annotated
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="fast api LMS",
    description="lms para gestionar estudiantes y cursos",
    version="0.0.1",
    contact={
        "bane": "dnda for everyone"
    },
    license_info={
        "name":"Apache 2.0",
    }
)

users = []
class User(BaseModel):
    name: str = "NN"
    is_active: bool = False
    bio: None | str | int = None
    


@app.get("/users",response_model=list[User])
async def root():
    return users
@app.post("/users")
async def root(a:User) -> Any:
    users.append(a)
    return a
@app.get("/users/{id}")
async def root(
        id: Annotated[
            int,
            Path(
                description="Ingrese un Id valido",
                gt=2
            )],
        q: Annotated[
            str,
            Query(
                description="Ingresa el query",
                max_length=5
            )]
):
    return {"user": users[id], "query": q}