from typing import Dict


class VentureCapitalStrategy:
    """Simula alocação em participações de startups."""

    def allocate(self, capital: float) -> Dict[str, float]:
        return {"startup_series_a": capital}
