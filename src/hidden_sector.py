"""Reproduce the hidden neutral closure excitation m_X ≈ 5.24 GeV."""

from constants import M_SURF_MEV, HIDDEN_X_DETERMINANT
from utils import write_csv

def hidden_rows():
    mass_mev = M_SURF_MEV * HIDDEN_X_DETERMINANT
    return [{
        "state": "X",
        "determinant": HIDDEN_X_DETERMINANT,
        "mass_MeV": mass_mev,
        "mass_GeV": mass_mev / 1000,
    }]

def main():
    rows = hidden_rows()
    r = rows[0]
    print(f"X: det={r['determinant']}, mass={r['mass_MeV']:.6g} MeV = {r['mass_GeV']:.6g} GeV")
    path = write_csv("hidden_sector.csv", rows, ["state", "determinant", "mass_MeV", "mass_GeV"])
    print(f"Wrote {path}")

if __name__ == "__main__":
    main()
