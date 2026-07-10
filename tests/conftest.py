"""Configuração compartilhada dos testes.

Sobe o app em memória via TestClient e desliga o rate limit para o suite poder
varrer muitos endpoints sem esbarrar no limite de 120/min. O comportamento 429
é dependente de janela de tempo (instável em CI) e já foi validado manualmente,
por isso não é exercitado aqui.
"""
import pytest
from fastapi.testclient import TestClient

import app as app_module


@pytest.fixture(scope="session")
def client():
    # Desliga o rate limit durante os testes (evita 429 ao varrer os endpoints).
    app_module.limiter.enabled = False
    # Forma context-manager: garante que os eventos de lifespan (startup/shutdown)
    # disparem — importante quando a inicialização migrar para lifespan (S2).
    with TestClient(app_module.app) as c:
        yield c
