# FLQ_Mod2_hERG_AI_Docking_MD
Computational dataset for AI-guided redesign of fluoroquinolone scaffold with reduced predicted hERG interaction and preserved antibacterial binding.
# AI-Guided Redesign of Fluoroquinolone Scaffold with Reduced Predicted hERG Liability

This repository contains computational datasets and scripts supporting the study:

"AI-assisted structural redesign of fluoroquinolone scaffolds to reduce predicted hERG channel interaction while preserving antibacterial binding."

## Contents

The repository includes:

• Ligand structures used in docking simulations  
• Prepared hERG receptor structure (PDB ID: 5VA1)  
• Docking input grids and representative binding poses  
• Molecular dynamics input files and representative trajectory frames  
• RMSD and RMSF analysis datasets  
• MM/PBSA binding free energy calculations  
• Convergence analysis scripts used to generate Supplementary Figure S8  

## Methods Summary

Docking simulations were performed using Glide and GNINA against the hERG channel structure (PDB ID: 5VA1). Molecular dynamics simulations were conducted for 200 ns to assess ligand stability within the channel cavity. Binding free energies were estimated using MM/PBSA analysis over the final 100 ns of trajectory sampling.

## Reproducibility

All data are provided to support reproducibility of the computational workflow and enable independent verification of docking, molecular dynamics, and binding free energy analyses.

## Corresponding Author

Computational Drug Design Laboratory

## Data Availability

All computational datasets, docking inputs, molecular dynamics trajectories,
and MM/PBSA analysis files are available in this repository.

This dataset enables reproducibility of the AI-guided redesign of
fluoroquinolone scaffolds targeting reduced hERG interaction.
