Molecular Dynamics Simulation Files

This folder documents the molecular dynamics (MD) simulation used to evaluate
the stability of the docked fluoroquinolone analog within the hERG channel.

Simulation Overview
-------------------

Simulation length: 200 ns
Software: GROMACS
Force field: CHARMM36
Water model: TIP3P

System Preparation
------------------

The docked complex of FLQ_Mod_2 with the hERG channel was embedded in a
solvated box with explicit water molecules and neutralized using Na+ and Cl-
counter ions.

Simulation Steps
----------------

1. Energy minimization
2. NVT equilibration
3. NPT equilibration
4. 200 ns production simulation

Key Analyses
------------

• RMSD analysis
• RMSF residue flexibility
• Binding stability assessment
• Interaction persistence with key residues

Key hERG residues monitored:

Tyr542  
Phe551  
Ala548  
Arg541

These residues are known contributors to drug-induced hERG blockade.

Purpose
-------

The MD simulation validates that the modified analog maintains stable
binding without strong aromatic stacking interactions that contribute to
cardiotoxicity.
