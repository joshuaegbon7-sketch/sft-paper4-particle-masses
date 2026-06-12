"""Reproduce active-neutrino masses from Lambda_eff = {0,4,24}."""

from constants import E_VAC_MEV
from utils import write_csv

NEUTRINO_LAMBDAS = {
    "nu_1": 0,
    "nu_2": 4,
    "nu_3": 24,
}

def neutrino_rows():
    rows = []
    for name, lam in NEUTRINO_LAMBDAS.items():
        mass_mev = E_VAC_MEV * lam
        rows.append({
            "particle": name,
            "Lambda_eff": lam,
            "mass_meV": mass_mev,
            "mass_eV": mass_mev / 1000,
        })
    return rows

def main():
    rows = neutrino_rows()
    for r in rows:
        print(f"{r['particle']}: Lambda={r['Lambda_eff']}, mass={r['mass_meV']:.6g} meV")
    mass_sum_eV = sum(r["mass_eV"] for r in rows)
    print(f"Sum m_nu = {mass_sum_eV:.6g} eV")
    path = write_csv("neutrinos.csv", rows, ["particle", "Lambda_eff", "mass_meV", "mass_eV"])
    print(f"Wrote {path}")

if __name__ == "__main__":
    main()
