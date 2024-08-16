from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/cursos')
async def getcursos():
    return {'info': 'Todos os cursos'}
