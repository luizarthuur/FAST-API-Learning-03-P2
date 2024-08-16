from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/usuarios')
async def getusuarios():
    return {'info': 'Todos os usuarios'}
