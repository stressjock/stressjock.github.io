# README: Stressjock's Almost-Pro Continuous Beam Analysis tool

### ⚠️ LEGAL DISCLAIMER & CAVEATS

**FOR EDUCATIONAL AND INFORMATIONAL PURPOSES ONLY.** This software is provided "as is," without warranty of any kind, express or implied. The calculations performed by this tool are based on simplified Euler-Bernoulli beam theory and numerical methods that may not account for all real-world variables (e.g., shear deformation in deep beams, material non-linearity, or buckling).

* **Not for Professional Engineering Use:** This tool should not be used for the final design of structural components or life-safety systems.
* **Verification Required:** All results must be independently verified by a qualified licensed professional engineer (PE) using industry-standard software and established building codes.
* **Liability:** The developers and distributors of this code assume no liability for any errors, omissions, or damages resulting from the use or misuse of this program.

---

## Overview

**Continuous Beam Analysis Pro** is a lightweight, browser-based engineering utility designed to solve indeterminate beam problems. It utilizes the **Direct Stiffness Method** to calculate displacements, shear forces, bending moments, and maximum bending stresses across multiple spans with varying properties.

## Key Features

* **Multi-Node Configuration:** Define an arbitrary number of nodes and supports (Fixed, Pin, Roller, or Free).
* **Diverse Loading:** Supports point loads (), concentrated moments (), and linearly varying distributed loads ( to ) across spans.
* **Span-Specific Properties:** Customize Modulus of Elasticity (), Moment of Inertia (), Cross-sectional Area (), and Neutral Axis distance () for every segment.
* **Real-time Visualization:** An interactive canvas displays the beam's physical setup, including support types and load vectors.
* **Dynamic Graphing:** High-fidelity charts (via Chart.js) visualize:
* Vertical Displacement
* Shear Force Diagram (SFD)
* Bending Moment Diagram (BMD)
* Maximum Bending Stress


* **Data Management:** Export your beam configuration to a CSV file or load existing project files for further analysis.

## How to Use

### 1. Define Nodes

In the **Nodes & Constraints** table, enter the -coordinate for each boundary or load point.

* **Supports:** Select the boundary condition (e.g., "Fixed" for a cantilever start).
* **Loads:** Apply point loads (negative for downward) or moments directly to the node.

### 2. Configure Spans

Once nodes are added, the **Span Properties** table will populate automatically.

* Input the material and geometric properties for each segment.
* Apply distributed loads by setting  (start of span) and  (end of span).

### 3. Run Analysis

Click the **SOLVE** button. The program will:

1. Assemble the global stiffness matrix.
2. Solve for unknown displacements and rotations.
3. Calculate internal forces at 200 points along the beam.
4. Update all diagrams with peak values automatically labeled.

## Technical Specifications

* **Language:** HTML5, CSS3, JavaScript (ES6).
* **Dependencies:** [Chart.js](https://www.chartjs.org/) (loaded via CDN).
* **Solver:** Finite Element Method (FEM) using 1D beam elements with two degrees of freedom per node (translation and rotation).

## File Structure

* `BeamSolver_v1.html`: A single-file solution containing the UI structure, styling, and mathematical logic. No external local assets are required.