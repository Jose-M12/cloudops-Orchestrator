from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_kubernetes_resources():
    return {"message": "Kubernetes resources"}
