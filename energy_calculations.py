from __future__ import annotations

import math
from dataclasses import dataclass
from decimal import Decimal, getcontext
from pathlib import Path

# ===================== CONFIGURAÇÃO =====================
getcontext().prec = 60

TON_TNT_TO_J = Decimal("4.184e9")
C_LIGHT = Decimal("3.0e8")
KAPPA_NUM_TO_J = Decimal("1.0")


@dataclass
class Veto:
    """Vetor Vetográfico - base da linguagem Vetografia (pilar 1)"""

    kind: str  # Tipo semântico (NUM, ENE, SUM, BIND...)
    unit: str
    value: Decimal

    @property
    def mantissa(self) -> float:
        if self.value == 0:
            return 0.0
        s = f"{self.value:.15e}"
        return float(s.split("e")[0])

    @property
    def exponent(self) -> int:
        if self.value == 0:
            return 0
        s = f"{self.value:.15e}"
        return int(s.split("e")[1])

    def __str__(self) -> str:
        return f"⟨{self.kind} | {self.unit} | {self.mantissa:.12f} × 10^{self.exponent}⟩"


# ===================== OPERAÇÕES VETOGRÁFICAS =====================
def factorial_energy(n: int) -> Veto:
    """Energia informacional baseada em fatorial (NUM)"""

    raw = Decimal(math.factorial(n)) * KAPPA_NUM_TO_J
    return Veto(kind="NUM", unit="J", value=raw)


def energy_mc2(mass_kg: float) -> Veto:
    """E = mc² (ENE)"""

    m = Decimal(mass_kg)
    return Veto(kind="ENE", unit="J", value=m * C_LIGHT**2)


def energy_tnt(tons: float) -> Veto:
    """Energia TNT"""

    t = Decimal(tons)
    return Veto(kind="TNT", unit="J", value=t * TON_TNT_TO_J)


def dominance(*vetos: Veto) -> Veto:
    """Dominância (Δ) - pilar 2: seleciona a camada mais forte"""

    return max(vetos, key=lambda v: v.exponent)


def vetographic_sum(*vetos: Veto) -> Veto:
    """Soma Vetográfica (⊕) - Bundling"""

    if not vetos:
        raise ValueError("Nenhum vetor informado")
    units = {v.unit for v in vetos}
    if len(units) > 1:
        raise ValueError(f"Unidades incompatíveis: {units}")
    total = sum((v.value for v in vetos), Decimal(0))
    return Veto(kind="SUM", unit=vetos[0].unit, value=total)


def binding(v1: Veto, v2: Veto, name: str = "BIND") -> Veto:
    """Binding (⊗) - pilar 2: cria novo conceito composto"""

    new_value = v1.value * v2.value
    return Veto(kind=name, unit=v1.unit, value=new_value)


# ===================== RELATÓRIO =====================
def build_report(a: Veto, b: Veto, c: Veto, dom: Veto, total: Veto, bind_exemplo: Veto) -> str:
    total_tnt = float(total.value / TON_TNT_TO_J)
    return f"""# 🧬 Vetografia v3.1 - Teste Oficial

**Entradas:**
- n = 30
- Massa = 500 kg
- TNT = 1.000.000 t
- κ = {KAPPA_NUM_TO_J}

**Vetores gerados:**
- A → {a}
- B → {b}
- C → {c}

**Operações Vetográficas:**
- Dominância (Δ) → {dom}
- Soma (⊕)       → {total}
- Binding exemplo → {bind_exemplo}

**Resultado em TNT:**
{total_tnt:.6e} toneladas

✅ Versão corrigida e pronta para o GitHub!
"""


def save_report(content: str, filename: str = "vetografia_v3.1_resultado.md") -> Path:
    path = Path(filename)
    path.write_text(content, encoding="utf-8")
    return path


# ===================== EXECUÇÃO =====================
def main() -> None:
    a = factorial_energy(30)
    b = energy_mc2(500)
    c = energy_tnt(1_000_000)

    dom = dominance(a, b, c)
    total = vetographic_sum(a, b, c)
    bind_ex = binding(a, b)

    report = build_report(a, b, c, dom, total, bind_ex)
    report_path = save_report(report)
    print(f"Relatório salvo em: {report_path}")
    print("\nDominância:", dom)


if __name__ == "__main__":
    main()
