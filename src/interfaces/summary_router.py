import zlib
from base64 import b64encode
from pydantic import BaseModel
from src.app.summaries import CreateTextSummaryUseCase
from src.interfaces.middlewares.verify_requester_access_to_resource import VerifyRequesterAccessToResource


def set_summary_router(app):
    class CreateTextSummaryBody(BaseModel):
        text: str

    a = """A inteligência artificial está influenciando vários setores, inclusive a medicina, ao passo que a in­dústria farmacêutica, outrora imbatível e altamente rentável, está perdendo espaço em razão da exigência por parte de médicos e pacientes. É o surgimento da “Medicina do Amanhã”, tema que dá nome ao livro de Pedro Schestatsky, médico neurologista, professor, pesquisador e empreendedor de novas tecnologias em medicina. No livro, ele põe em xeque o tradicionalismo da área médica para defender um novo caminho: a Medicina Personalizada, baseada em Big Data e na Inteligência Artificial acessível.

    Em entrevista à Medicina S/A, ele conta que, num futuro próximo, os dados individuais serão utilizados para guiar o paciente em suas decisões de saúde – o que, até então, era feito apenas por meio de pesqui­sas e evidências extraídas de grandes populações."""
    a = zlib.compress(a.encode())
    print(str(b64encode(a), 'utf-8')) 

    app.add_middleware(VerifyRequesterAccessToResource)

    @app.post('/summaries')
    def create_text_summary(body: CreateTextSummaryBody):
        usecase = CreateTextSummaryUseCase(body.text)
        data = usecase.execute()
        return data