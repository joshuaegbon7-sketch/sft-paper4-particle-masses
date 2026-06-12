"""Reproduce the primitive closure kernel K = diag(2,3,4)."""

from constants import CHI_M, CHI_A, CHI_B
from utils import write_csv

def primitive_kernel():
    return [
        [CHI_M, 0, 0],
        [0, CHI_A, 0],
        [0, 0, CHI_B],
    ]

def rows():
    K = primitive_kernel()
    return [
        {"row": i + 1, "col1": r[0], "col2": r[1], "col3": r[2]}
        for i, r in enumerate(K)
    ]

def main():
    K = primitive_kernel()
    print("Primitive closure kernel K = diag(2,3,4):")
    for r in K:
        print(r)
    print("Spectrum:", [CHI_M, CHI_A, CHI_B])
    path = write_csv("primitive_kernel.csv", rows(), ["row", "col1", "col2", "col3"])
    print(f"Wrote {path}")

if __name__ == "__main__":
    main()
