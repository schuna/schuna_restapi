from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, status

from common.oauth2 import get_current_user
from container import Container
from schemas.inbody import InBodyDisplay, InBodyBase
from schemas.user import UserBase
from services.inbody import InBodyService

router = APIRouter(
    prefix="/inbody",
    tags=["inbody"]
)


@router.post('/', response_model=InBodyDisplay)
@inject
def create_inbody(request: InBodyBase,
                  inbody_service: InBodyService = Depends(Provide[Container.inbody_service]),
                  current_user: UserBase = Depends(get_current_user)):
    response = inbody_service.create_inbody(request)
    if response.success:
        return response.data
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{response.message}")


@router.get("/{user_id}", response_model=List[InBodyDisplay])
@inject
def get_posts(user_id: int,
              inbody_service: InBodyService = Depends(Provide[Container.inbody_service]),
              current_user: UserBase = Depends(get_current_user)):
    return inbody_service.get_inbodies(user_id)
