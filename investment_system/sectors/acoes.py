from typing import Dict


class AcoesStrategy:
    """Simula alocação em ações de empresas consolidadas."""

    def allocate(self, capital: float) -> Dict[str, float]:
        return {"empresa_blue_chip": capital}
