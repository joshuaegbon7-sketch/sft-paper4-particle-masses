"""Reproduce the leading-order quark closure determinants and masses."""

from constants import M_SURF_MEV
from utils import write_csv

QUARK_DETERMINANTS = {
    "u": 1 / 12,
    "d": 1 / 6,
    "s": 4,
    "c": 48,
    "b": 144,
    "t": 3 ** 8,
}

def quark_rows():
    rows = []
    for name, det in QUARK_DETERMINANTS.items():
        mass_mev = M_SURF_MEV * det
        rows.append({
            "particle": name,
            "determinant": det,
            "mass_MeV": mass_mev,
            "mass_GeV": mass_mev / 1000,
        })
    return rows

def main():
    rows = quark_rows()
    for r in rows:
        print(f"{r['particle']}: det={r['determinant']:.12g}, mass={r['mass_MeV']:.6g} MeV = {r['mass_GeV']:.6g} GeV")
    path = write_csv("quarks.csv", rows, ["particle", "determinant", "mass_MeV", "mass_GeV"])
    print(f"Wrote {path}")

if __name__ == "__main__":
    main()
