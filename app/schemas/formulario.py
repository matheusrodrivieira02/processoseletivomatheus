from pydantic import BaseModel, EmailStr

class RespostasFormularioCreate(BaseModel):
    nome_completo: str
    email: EmailStr
    telefone: int
    cargo_desejado: str
    cargo_nivel: str
    pretensao_salarial: str
    anos_experiencia: str
    habilidades: str
    link_linkedin: str
    sobre_voce: str
    porque_trabalhar_aqui: str
    status: str