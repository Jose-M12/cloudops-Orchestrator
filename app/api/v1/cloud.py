from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_cloud_resources():
    return {"message": "Cloud resources"}
