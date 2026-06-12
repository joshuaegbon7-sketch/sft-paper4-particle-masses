"""Run all SFT Paper IV reproducibility calculations."""

import primitive_kernel
import charged_leptons
import quarks
import neutrinos
import hidden_sector

def main():
    print("\n=== Primitive Kernel ===")
    primitive_kernel.main()

    print("\n=== Charged Leptons ===")
    charged_leptons.main()

    print("\n=== Quarks ===")
    quarks.main()

    print("\n=== Neutrinos ===")
    neutrinos.main()

    print("\n=== Hidden Neutral Sector ===")
    hidden_sector.main()

if __name__ == "__main__":
    main()
