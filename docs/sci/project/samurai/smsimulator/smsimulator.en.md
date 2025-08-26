---
title: smsimultor
---

## 

read_me

readme.txt
16 Oct 2019 --- version 5.0 (compiled with Geant4.10.05.p01)
28 Dec 2017 --- version 4.0 (compiled with Geant4.9.6.p04)
18 Jul 2014 --- version 3.2 (compiled with Geant4.9.6.p02)

--------
ABSTRACT
--------
"smsimulator" is developed by R. Tanaka, Y. Kondo, and M. Yasuda for
simulating SAMURAI experiment. From version 5.0, Geant4.10.X is
compatible. Version 4.X or former is compatible to Geant4.9.X. From
version3.0, conversion from Geant4 steps to observables, like
TArtNEBULAPla is implemented. ANAROOT library is required. simtrace,
which simulate trajectory of charged particles in SAMURAI magnet, is
also included form this version. 

Currently smsimulator includes,
 - README: this file
 - setup.sh: setup script
 - smg4lib: main files to create libraries for SAMURAI simulation
 - crosssection: create cross section data set, and plot by gnuplot
 - get_pdgmass: simple program to show PDG mass of heavy ion
 - simtrace: simple example for checking trajectory in SAMURAI Magnet
 - simdayone: simulator example for heavy ion + neutron 
 - sim_samurai21: simulator example for 28O experiment including NeuLAND
 - sim_tm1510: TM1510, SAMURAI with DALI, NeuLAND, NEBULA
 - sim_dali: DALI
 - sim_s21dali: DALI with MINOS(as object) for SAMURAI21 experiment
 - sim_catana: CATANA

----------
HOW TO USE
----------
(1) Install Geant4
The smsimulator 5.x is compatible with Geant4.10.x. Smsimulator 4.x is
compatible with Geant4.9.x. (Version4.9.6.p02 or later is recommended
for neutron simulation.) If you use old version, you need
modifications in addition to (1.a). See details at
http://be.nucl.ap.titech.ac.jp/~ryuki/iroiro/geant4/  
(written in Japanese)

(1.a) Modify G4INCLCascade.cc for avoiding fatal abort as follows.
(not necessary for smsimulator 5.x)

---------------------------------------------------------------------------
  G4bool INCL::prepareReaction(const ParticleSpecies &projectileSpecies, const G4double kineticEnergy, const G4int A, const G4int Z) {
    if(A < 0 || A > 300 || Z < 1 || Z > 200) {
      ERROR("Unsupported target: A = " << A << " Z = " << Z << std::endl);
      ERROR("Target configuration rejected." << std::endl);
      return false;
    }

    //--> added to avoid abort
    if (projectileSpecies.theA==1 && A==1){
      return false;
    }
    //<--

    // Initialise the maximum universe radius
    initUniverseRadius(projectileSpecies, kineticEnergy, A, Z);
---------------------------------------------------------------------------

(1.b) Compile Geant4

(2) install ANAROOT
(2.a)
ANAROOT can be downloaded form the RIBFDAQ web page.
http://ribf.riken.jp/RIBFDAQ/

(3) Compile smsimulator
Modify smsimulator/setup.sh for your system.

$ . setup.sh
$ cd smg4lib
$ make
$ cd ../simtrace
$ make
... (same for simdayone, get_pdgmass, crosssection, ...)

(4) Run Geant4
Copy the working directory "smsimulator/work" to somewhere. (Working
at "smsimulator/work" is not recommended for future update of
smsimulator.) The field map of the SAMURAI magnet can be downloaded at
http://ribf.riken.jp/SAMURAI/. You can find some examples of Geant4
macros in work/xxxxx/g4mac/examples/. 

- vis.mac
  example of visualization

- example_Pencil.mac
  example for pencil beam

- example_Gaus.mac
  example for mono-energetic beam having position and angle spread of
  Gaussian distributions

- example_Tree.mac
  example for Tree input for phase space decay of three body system

(4.a) Detector geometry of NEBULA is given by two csv files in
smsimulator/simdayone/geometry/.
  - NEBULADetectors_xxx.csv : position of each detector
  - NEBULA_xxx.csv : geometry of whole NEBULA system

Examples of perl scripts are also included for creating the parameter 
files. Use as follows. 

$ ./CreatePara_NEBULAFull.pl > NEBULADetector_Full.csv

(4.b) Output root file
Output root file contains Tree of
  - Geant4 steps
  - Parameters
  - Observables converted from Geant4 steps.
Since storing Geant4 steps gives large file size, you can skip storing
Geant4 steps via 
  - /action/data/NEBULA/StoreSteps false in geant4 macro
  - NEBULASimDatainitializer::SetDataStore(false).

(5) Analyze Geant4 output
See examples of ROOT macros in smsimulator/xxxx/macros/examples/ for 
analyzing Geant4 output.

  - GenerateInputTree_PhaseSpaceDecay.cc
    example to make input tree file for simulation of three body phase
    space decay.

  - analysis_example.cc
    simple example for analyzing Geant4 output.

(5.a) Crosstalk analysis
If you want to use example of crosstalk analysis, do following things.

(5.a.1) Modify ANAROOT data class 
Add the following lines in TArtNEBULAPla.hh (ANAROOT class) for
TClonesArray::Sort.

---------------------------------------------------------------------------
  // overriding functions for sorting based on TAveSlw
public:
  Bool_t IsEqual(TObject *obj) const {return fTAveSlw == ((TArtNEBULAPla*)obj)->fTAveSlw;}
  Bool_t IsSortable() const {return kTRUE;}
  Int_t Compare(const TObject *obj) const{
    if (fTAveSlw < ((TArtNEBULAPla*)obj)->fTAveSlw) return -1;
    else if (fTAveSlw > ((TArtNEBULAPla*)obj)->fTAveSlw) return 1;
    else return 0;
  }
---------------------------------------------------------------------------

(5.a.2) Make library file for ROOT 
Make library file in smsimulator/work/smanalib/.
$ cd smsimulator/work/smanalib/
$ ./auto.sh
$ make
$ make install

Modify rootlogon.C to load the library and to add include
path. You can find an example to use TArtCrosstalk_XXX classes in
smsimulator/work/sim_samurai21/macros/examples/analysis_crosstalk_example.cc.

-----------
UPDATE INFO
-----------
- version 4.2
  - TargetThickness is added in TFragSimData

- version 3.2
  - NeuLAND is implemented
  - Example of crosstalk analysis is implemented

- version 3.0
  - simtrace is merged.
  - conversion from Geant4 step data to TArtNEBULAPla is
    implemented.
  - definition of data class is modified.
  - enable to fill air in the experimental room.
  - command names of Messenger are organized.
  - BeamTypeDemocraticDecay is removed because it can be done via
    BeamTypeTree.
  - DetectorConstruction for each element is prepared for future use. 

-----
HINTS
-----
- Simulating a lot of events
  To avoid abortion, put the follwoing line in your g4mac/xxx.mac.
  /control/suppressAbortion 1
  It is improved in Geant4.10.x.

- Update your code for smsimulator 5.x + Geant4.10.x.
  When you use units, add "#include "G4SystemOfUnits.hh"".

- Command via messenger
  you can see the list of implemented command by the following way in
  the interactive mode of Geant4.
  Idle> ls /action/
  Idle> ls /samurai/

- Event generator
  - Arbitrary distribution can be inputted to smsimulator via
    tree. get_pdgmass is useful to obtain mass value of heavy ion.

- Simulation for your experiment with NeuLAND
  - smsimulator3.2/sim_samurai21 is an example for 28O experiment
    using NEBULA+NeuLAND configuration. You can copy the directory to
    sim_samuraiXX, for example, and modify it for your experimental
    setup.

- Your crosstalk algorithm
  - You can develop your crosstalk algorithm. Base class
    TArtCrosstalkAnalysis is useful for the purpose. Copy
    TArtCrosstalkAnalysis_XXX.cc and .hh, and modify them. Don't 
    forget to add a line in smanalib/sources/smana_linkdef.hh to use
    it in ROOT.

- Your data class
  If you want to create your data class, create following classes.
  - TXXXSimData : data class for storing Geant4 steps
  - XXXSimDataInitializer : Initializer (inherit SimDataInitializer)
  - XXXSimDataConverter : Converter from Geant4 steps to observables
    (inherit SimDataConverter)
  - XXXSD : Sensitive Detector class (inherit G4VSensitiveDetector)

  Then you can control them via SimDataManager.

-----
TO DO
-----
- Several things are NOT included
  - resolution of heavy ion
  - energy loss difference in target (one of the important effect on
    Erel resolution)

- Documentation about the validity/evaluation of the simulator.

