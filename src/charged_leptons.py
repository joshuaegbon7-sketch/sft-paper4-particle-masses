"""Reproduce the leading-order charged-lepton masses."""

from constants import M_SURF_MEV
from utils import write_csv

# Determinants from the closure-deficit and generation-chain construction.
LEPTON_DETERMINANTS = {
    "electron": 1 / 54,
    "muon": 4,
    "tau": 64,
}

def lepton_rows():
    rows = []
    for name, det in LEPTON_DETERMINANTS.items():
        mass_mev = M_SURF_MEV * det
        rows.append({
            "particle": name,
            "determinant": det,
            "mass_MeV": mass_mev,
            "mass_GeV": mass_mev / 1000,
        })
    return rows

def main():
    rows = lepton_rows()
    for r in rows:
        print(f"{r['particle']}: det={r['determinant']:.12g}, mass={r['mass_MeV']:.6g} MeV")
    path = write_csv("charged_leptons.csv", rows, ["particle", "determinant", "mass_MeV", "mass_GeV"])
    print(f"Wrote {path}")

if __name__ == "__main__":
    main()
