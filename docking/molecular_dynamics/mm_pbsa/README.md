MM/PBSA Binding Free Energy Analysis

This folder contains files related to the molecular mechanics / Poisson–
Boltzmann surface area (MM/PBSA) binding free energy analysis performed
on the FLQ_Mod_2 – hERG complex.

Method Overview
---------------

Binding free energies were estimated from molecular dynamics trajectories
using the MM/PBSA approach.

Trajectory frames were extracted from the final 100 ns of the
200 ns molecular dynamics simulation.

The analysis was performed to estimate the stability and energetic
favorability of the ligand–channel interaction.

Energy Components
-----------------

The following energy terms were evaluated:

• van der Waals energy
• Electrostatic energy
• Polar solvation energy
• Non-polar solvation energy

The total binding free energy (ΔGbind) was calculated as:

ΔGbind = ΔEvdW + ΔEele + ΔGpolar + ΔGnonpolar

Convergence Analysis
--------------------

Running averages of ΔGbind were monitored across trajectory frames
to confirm energetic convergence.

The convergence plot is provided in the supplementary materials
of the manuscript.
