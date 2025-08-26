from typing import Dict


class RendaFixaStrategy:
    """Simula alocação em títulos de renda fixa."""

    def allocate(self, capital: float) -> Dict[str, float]:
        return {"tesouro_direto": capital}
