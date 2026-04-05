from sqlalchemy import Column, DateTime, Integer, String, func, text
from app.db.database import Base

class RespostasFormulario(Base):
    __tablename__ = "respostas_formulario"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=text("TIMEZONE('America/Sao_Paulo', NOW())"))
    nome_completo = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(Integer, nullable=False)
    cargo_desejado = Column(String, nullable=False)
    cargo_nivel = Column(String, nullable=False)
    pretensao_salarial = Column(String, nullable=False)
    anos_experiencia = Column(String, nullable=False)
    habilidades = Column(String, nullable=False)
    link_linkedin = Column(String, nullable=True)
    sobre_voce = Column(String, nullable=False)
    porque_trabalhar_aqui = Column(String, nullable=False)
    status = Column(String, nullable=False)
