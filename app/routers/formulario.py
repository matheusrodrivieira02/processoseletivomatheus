from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from sqlalchemy import func

from app.services.get_db import get_db
from app.models.formulario import RespostasFormulario
from app.schemas.formulario import RespostasFormularioCreate


router = APIRouter(prefix="/respostas_formulario", tags=["Respostas Formulário"])

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/registrar", summary="Registra respostas no sistema")
def register_respostas(respostas_formulario: RespostasFormularioCreate, db: Session = Depends(get_db)):
    db_respostas_formulario = RespostasFormulario(       
        nome_completo=respostas_formulario.nome_completo,
        email=respostas_formulario.email,
        telefone=respostas_formulario.telefone,
        cargo_desejado=respostas_formulario.cargo_desejado,
        cargo_nivel=respostas_formulario.cargo_nivel,
        pretensao_salarial=respostas_formulario.pretensao_salarial,
        anos_experiencia=respostas_formulario.anos_experiencia,
        habilidades=respostas_formulario.habilidades,
        link_linkedin=respostas_formulario.link_linkedin,
        sobre_voce=respostas_formulario.sobre_voce,
        porque_trabalhar_aqui=respostas_formulario.porque_trabalhar_aqui,
        status=respostas_formulario.status,
    )

    db.add(db_respostas_formulario)
    db.commit()
    db.refresh(db_respostas_formulario)

    return {
        "id": db_respostas_formulario.id,
        "nome_completo": db_respostas_formulario.nome_completo,
        "email": db_respostas_formulario.email,
        "telefone": db_respostas_formulario.telefone,
        "cargo_desejado": db_respostas_formulario.cargo_desejado,
        "cargo_nivel": db_respostas_formulario.cargo_nivel,
        "pretensao_salarial": db_respostas_formulario.pretensao_salarial,
        "anos_experiencia": db_respostas_formulario.anos_experiencia,
        "habilidades": db_respostas_formulario.habilidades,
        "link_linkedin": db_respostas_formulario.link_linkedin,
        "sobre_voce": db_respostas_formulario.sobre_voce,
        "porque_trabalhar_aqui": db_respostas_formulario.porque_trabalhar_aqui,
        "status": db_respostas_formulario.status,
    }

@router.get("/todos", summary="Busca todos as respostas das candidaturas do processo seletivo")
def all_respostas(db: db_dependency):
    result = db.query(RespostasFormulario).all()

    if not result:
        raise HTTPException(status_code=404, detail="Candidaturas não encontradas")
    return result

@router.get("/count", summary="Busca a quantidade de respostas para o processo seletivo")
def count_respostas(db: Session = Depends(get_db)):
    total = db.query(func.count(RespostasFormulario.id)).scalar()
    return {"total": total}

@router.get("/count/aprovados", summary="Busca a quantidade de candidatos aprovados")
def count_aprovados(db: Session = Depends(get_db)):
    total = db.query(func.count(RespostasFormulario.id))\
        .filter(RespostasFormulario.status == "aprovado")\
        .scalar()

    return {"total_aprovados": total}

@router.get("/count/revisar", summary="Busca a quantidade de candidatos a revisar")
def count_revisar(db: Session = Depends(get_db)):
    total = db.query(func.count(RespostasFormulario.id))\
        .filter(RespostasFormulario.status == "revisar")\
        .scalar()

    return {"total_revisar": total}

@router.get("/chart/cargo_desejado", summary="Busca o cargo desejado e a quantidade de candidatos que selecionaram a opção")
def chart_cargo_desejado(db: Session = Depends(get_db)):
    results = db.query(
        RespostasFormulario.cargo_desejado, 
        func.count(RespostasFormulario.id).label("quantidade")  
    ).group_by(RespostasFormulario.cargo_desejado).all()

    return [
        {"cargo_desejado": cargo_desejado, "quantidade": quantidade}
        for cargo_desejado, quantidade in results
    ]

@router.get("/chart/anos_experiencia", summary="Busca os anos de experiência e a quantidade de candidatos que selecionaram a opção")
def chart_cargo_desejado(db: Session = Depends(get_db)):
    results = db.query(
        RespostasFormulario.anos_experiencia, 
        func.count(RespostasFormulario.id).label("quantidade")  
    ).group_by(RespostasFormulario.anos_experiencia).all()

    return [
        {"anos_experiencia": anos_experiencia, "quantidade": quantidade}
        for anos_experiencia, quantidade in results
    ]

@router.get("/chart/pessoas_nivel", summary="Busca o nível e a quantidade de candidatos que selecionaram a opção")
def chart_pessoas_nivel(db: Session = Depends(get_db)):
    results = db.query(
        RespostasFormulario.cargo_nivel, 
        func.count(RespostasFormulario.id).label("quantidade")  
    ).group_by(RespostasFormulario.cargo_nivel).all()

    return [
        {"nivel": cargo_nivel, "quantidade": quantidade}
        for cargo_nivel, quantidade in results
    ]