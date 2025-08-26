from typing import Dict


class OpcoesStrategy:
    """Simula alocação em operações com opções."""

    def allocate(self, capital: float) -> Dict[str, float]:
        return {"call_coberta": capital}
