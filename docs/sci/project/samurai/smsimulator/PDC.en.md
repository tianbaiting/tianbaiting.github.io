# PDC Drift Chamber Simulation Plan

## References and Tutorials

### 1. Drift Chamber Principles
- [Drift Chamber Tutorial (Chinese)](https://yznkxjs.xml-journal.net/cn/article/pdf/preview/10.7538/yzk.1981.15.01.0116.pdf)
- [Drift Chamber Tutorial (ICFA 2005)](https://indico.cern.ch/event/426015/contributions/1047606/attachments/906077/1278746/DriftChamber_ICFA2005.pdf)
- [Drift Chamber Principles (IOP)](https://iopscience.iop.org/article/10.1088/1742-6596/18/1/010/pdf)

### 2. Geant4 Simulation
- [Geant4 Simulation Tutorial (Munich 2018)](https://indico.cern.ch/event/709670/contributions/3027829/attachments/1670306/2679293/Munich.pdf)

### 3. PDC Detector Technical Documents
- [PDC Detailed Parameters and Design](https://www.nishina.riken.jp/ribf/SAMURAI/image/Detector-PDC.pdf)
- [PDC CAD Drawings (screenshots)](https://indico2.riken.jp/event/2752/contributions/11231/attachments/7528/8801/04_EMIS2012_KobayashiT.pdf)

## PDC Specifications

### 1. Design and Purpose

The PDC (Proton Drift Chamber) is used to measure the momentum of protons at projectile-rapidity and is placed downstream of the SAMURAI magnet. To reduce the number of detector planes, the PDC uses a cathode readout method to obtain position information. The anode plane employs a Walenta-type drift chamber with an 8 mm drift length designed to reduce the number of anode wires. To detect multi-particle events, the cathode wires are arranged in three different directions: 0, +45, and -45 degrees.

> **Note**: The PDC uses cathode readout. When electrons from ionization drift towards the anode wires and cause an avalanche, induced charges are generated on nearby cathode strips. Reading these induced charges determines the particle's position.

### 2. Key Parameters

- **Effective Area**: 1700mm × 800mm
- **Anode Wires**: Gold-plated Tungsten/Rhenium alloy, 30μm diameter, 16mm spacing, 8mm drift length
- **Cathode Wires**: Gold-plated Aluminum alloy, 80μm diameter, 3mm spacing
- **Anode-Cathode Gap**: 8mm
- **Cathode Strip Width**: 12mm (every 4 cathode wires are grouped into one strip)
- **Power Supply**: Positive HV on anode wires, slight negative HV on potential wires
- **Configuration**: Cathode(U)-Anode(V)-Cathode(X)-Anode(U)-Cathode(V)
- **Operating Gas**: Ar+25% i-C4H10 or Ar+50% C2H6

![PDC Structure Diagram](assets/PDC.zh/image.png)
*PDC Structure Diagram*

![PDC Wire Chamber Structure](assets/PDC.zh/image-1.png)
*PDC Wire Chamber Structure. The X, U, and V layers use wires (or strips) in different orientations to determine the 2D position of a particle. For example, the X-layer wires are typically perpendicular to the X-axis to precisely measure the X-coordinate.*

### 3. Readout Scheme and Development

- **Initial Scheme (Tested)**: To reduce readout channels, a charge-division readout method was tested. Cathode strips were connected in series with resistors, and every 8 strips were read out by one charge-sensitive preamplifier. A prototype detector (600mm × 480mm) achieved a position resolution of 1mm (rms) for X-rays but could not handle two-proton events correctly.
- **New Scheme (In Development)**: To address the multi-particle issue and improve resolution, a new readout circuit is being developed. Each cathode signal is directly connected to a preamplifier, shaper, and sample-and-hold circuit, then digitized on a Front-End Board (FEB). This new method is expected to improve position resolution by a factor of about 5 and requires approximately 810 readout channels.

---

## Simulation Plan Overview

A custom PDC detector needs to be built. Geant4 can accurately simulate the ionization process of particles with gas molecules. Our alternative approach is as follows:

1.  Simulate particles passing through the drift chamber gas using Geant4.
2.  In Geant4's user action class (SteppingAction), record the position of all ionization events (energy deposition).
3.  Construct a Sensitive Detector near each wire, using the shortest drift distance as time and the total deposited energy as amplitude.
4.  This method simplifies "firing" to "ionization occurred nearby," ignoring complex processes like electron drift time, diffusion, and avalanche gain.

## Method Limitations

- **Ignores Electron Drift**: In reality, ionized electrons drift along electric field lines, not just towards the nearest wire. In high-field regions, electrons create an avalanche, which is the actual "firing" process. This method cannot simulate this.
- **Cannot Simulate Signal Shape and Time**: Without considering drift time, you cannot obtain precise signal timing information and waveform.
- **Cannot Simulate Gain**: Geant4 does not simulate the avalanche process itself, so you cannot get the signal gain for each "firing" event.

---

## 1. Physics Model Summary

- Build the PDC drift chamber geometry and gas material in Geant4.
- When particles (e.g., protons) pass through the gas, they cause ionization, and the energy deposition is recorded.
- In SteppingAction, determine if an ionization event is near an anode wire, using the nearest distance as the drift time and the energy deposition as the signal amplitude.
- This approach ignores electron drift, avalanche gain, and signal waveform, simulating only the spatial distribution and energy response.

## 2. Geometry and Material Construction

- **Define Gas Mixture**: e.g., 75% Ar + 25% i-C4H10 at 1 atm.
- **Build Drift Chamber Box**: Use G4Box or G4Trap to represent the gas volume.
- **Build Wire Array**: Use G4Cylinder or G4Tubs to represent the anode wires, arranged according to their actual positions.

## 3. Sensitive Detector Setup

- Set the gas volume as a Sensitive Detector (SD) to record the energy deposition and position at each step.

## 4. SteppingAction Implementation

- In UserSteppingAction, check if each step occurs within the gas volume.
- Calculate the distance from the step to the nearest wire, treating it as the drift distance.
- Record energy deposition, position, nearest wire ID, etc.

## 5. Data Output

- For each event, output all "firing" signals (using TTree/TClonesArray), including energy, position, nearest wire ID, drift distance, etc.