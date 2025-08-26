from typing import Dict


class CriptoStrategy:
    """Simula alocação em criptomoedas."""

    def allocate(self, capital: float) -> Dict[str, float]:
        return {"bitcoin": capital * 0.5, "ethereum": capital * 0.5}
