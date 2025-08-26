from typing import Dict


class FIIStrategy:
    """Simula alocação em Fundos de Investimento Imobiliário."""

    def allocate(self, capital: float) -> Dict[str, float]:
        return {"fii_comercial": capital}
