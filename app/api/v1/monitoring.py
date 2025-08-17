from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_monitoring_data():
    return {"message": "Monitoring data"}
