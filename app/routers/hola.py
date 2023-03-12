from fastapi import APIRouter
router = APIRouter (    
    prefix= "/root"
    #tags= ["Kmils"]
)
@router.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}
