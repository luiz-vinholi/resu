import zlib
import base64
from typing import Any
from pydantic import BaseModel
from src.interfaces import app
from src.infra.repositories import AIRepository


class CreateTextSummaryBody(BaseModel):
    text: str

a = """A inteligência artificial está influenciando vários setores, inclusive a medicina, ao passo que a in­dústria farmacêutica, outrora imbatível e altamente rentável, está perdendo espaço em razão da exigência por parte de médicos e pacientes. É o surgimento da “Medicina do Amanhã”, tema que dá nome ao livro de Pedro Schestatsky, médico neurologista, professor, pesquisador e empreendedor de novas tecnologias em medicina. No livro, ele põe em xeque o tradicionalismo da área médica para defender um novo caminho: a Medicina Personalizada, baseada em Big Data e na Inteligência Artificial acessível.

Em entrevista à Medicina S/A, ele conta que, num futuro próximo, os dados individuais serão utilizados para guiar o paciente em suas decisões de saúde – o que, até então, era feito apenas por meio de pesqui­sas e evidências extraídas de grandes populações."""
a = zlib.compress(a.encode())
print(str(base64.b64encode(a), 'utf-8')) 

@app.post('/summaries')
def create_text_summary(body: CreateTextSummaryBody):
    text = base64.b64decode(body.text)
    text = zlib.decompress(text).decode()
    print(text)
    ai = AIRepository()
    return ai.get_text_summary(text)