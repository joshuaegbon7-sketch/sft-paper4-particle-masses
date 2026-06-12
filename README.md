# Spacefield Transformation IV: Particle Masses from Primitive Closure Invariants

This repository accompanies:

**Joshua Egbon, _Spacefield Transformation IV: Spectral Closure Determinants and the Geometric Origin of Particle Masses_**.

It provides reproducible Python calculations for the numerical spectra reported in the paper. The scripts reproduce the leading-order charged-lepton, quark, neutrino, and hidden neutral-sector mass estimates from the primitive closure invariants

\[
\chi_M=2,\qquad \chi_A=3,\qquad \chi_B=4,
\]

and the primitive closure kernel

\[
\mathcal K=\operatorname{diag}(2,3,4).
\]

No particle-specific mass parameters are introduced in the leading-order mass calculations.

## Repository contents

```text
paper/
  SFT_Paper_IV_source.tex

src/
  constants.py
  primitive_kernel.py
  charged_leptons.py
  quarks.py
  neutrinos.py
  hidden_sector.py
  run_all.py

output/
  generated CSV tables after running the scripts
```

## How to reproduce the tables

Run:

```bash
python src/run_all.py
```

This generates:

```text
output/primitive_kernel.csv
output/charged_leptons.csv
output/quarks.csv
output/neutrinos.csv
output/hidden_sector.csv
```

## Main reproduced values

### Primitive kernel

\[
\mathcal K=\operatorname{diag}(2,3,4)
\]

### Charged leptons

\[
m_e = 0.505~{\rm MeV},\qquad
m_\mu = 109.16~{\rm MeV},\qquad
m_\tau = 1.747~{\rm GeV}.
\]

### Quarks

\[
m_u = 2.27~{\rm MeV},\quad
m_d = 4.55~{\rm MeV},\quad
m_s = 109.16~{\rm MeV},
\]

\[
m_c = 1.31~{\rm GeV},\quad
m_b = 3.93~{\rm GeV},\quad
m_t = 179~{\rm GeV}.
\]

### Active neutrinos

\[
m_{\nu_1}=0,\qquad
m_{\nu_2}=9.0~{\rm meV},\qquad
m_{\nu_3}=54.0~{\rm meV}.
\]

### Hidden neutral sector

\[
m_X \simeq 5.24~{\rm GeV}.
\]

## Notes

The scripts are intended to reproduce the numerical mass-spectrum calculations reported in the paper. They do not replace the mathematical derivations in the manuscript; rather, they provide an executable implementation of the leading-order closure-determinant calculations.

## License

MIT License.
