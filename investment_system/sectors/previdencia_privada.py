from typing import Dict


class PrevidenciaPrivadaStrategy:
    """Simula alocação em planos de previdência privada."""

    def allocate(self, capital: float) -> Dict[str, float]:
        return {"plano_gerador_beneficio_livre": capital}
