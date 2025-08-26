from typing import Dict


class SmallCapsStrategy:
    """Simula alocação em empresas de pequena capitalização."""

    def allocate(self, capital: float) -> Dict[str, float]:
        return {"small_cap": capital}
