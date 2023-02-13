from fastapi import APIRouter

router = APIRouter(
    prefix="/system",
    tags=["system"],
)

@router.get("/health", tags=["system"], summary="Get health status",
    description="Get health status of the system")
def get_health():
    return {"health": "OK"}

