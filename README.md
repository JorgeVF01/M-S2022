# M-S2022
# Modeling and Sumulation: N-body modeling
This is the final project of the subject Modeling and Simulation of the [Escuela Nacional de Estudios Superiores UNAM campus Morelia](https://www.enesmorelia.unam.mx/).

## Contact

- Team leader: Jorge Oscar Vázquez Fuerte 
     · Mail: jorgeovf01@gmail.com 
     
- P.R.: Paola González Hernández
     · Mail: paaoogh@gmail.com

- Tech leader: Kevin Gómez 
     · Mail: kgomez0800@gmail.com
     
##

The aim of this project is to model and simulate the SARS-COV19 growth and behavior as a N-body system applying physics laws to the model.

## Introduction

N-body simulations have been a powerful tool to describe natural phenomena, however, most of the N-body problems are unsolvable but can be approximated with numerical methods. Its origin is related with the measuring of time based on sky observations centuries ago, as a matter of fact, astronomers were fitting models to describe the Solar System with all the data collected about the sky.

Isaac Newton solved a sort of 2-Body problem with the formulation of classical gravity interactions, nevertheless he could not solve a 3-Body problem presuming that the problem exceeds human knowledge as it must consider complex force and motion interactions. Leonhard Euler described and solved a restricted 3-Body problem as a mathematical problem.


![alt text](https://serving.photos.photobox.com/93652483ac5ecb2cf4da2d31f6a9d47adf85c21bb10546d0543fed263f0d2d1b8f77f2d6.jpg)

*Python Implementation of a simple N-Body simulation. Mocz, P. (2020)*





## Justification

The purpose of this project is to analyze previous data of covid spreading in Mexico and recreate an environment with an arbitrary population of healthy individuals and an initial point of infected people, all the bodies will interact between each other causing the contagion of the healthy individuals, at the same time some of the infected individuals will develop immunity meanwhile another infected community will die. As is expected, at some point all the survivors will develop immunity.  Finally, we are looking for an  accurate model that can describe the virus behavior over certain time intervals and most importantly these results will be helpful to plan strategies of virus scan and protection on hard to reach areas like rural communities which are far away from vaccinations plans and the latest technological innovations.

## Objectives and methodology

* Use initial parameters based on data provided by the [CONACYT and Centro Geo](https://datos.covid-19.conacyt.mx/). Data will take only within lapse of July 1st to October 31st as there is a clear trend shown in the CONACyT graphs about cumulative and confirmed cased.

* Implement an N-Body system with `Python3` in order to describe the COVID-19 Spreading and Behavior as a pandemic based on the CIER model based on the Kuzdeuov, A. et al publication "Particle-Based COVID-19 Simulator with Contact Tracing and Testing" (2020) with the following steps:
     * Definition of initial conditions based on the CONACyT data retrieved from the specified dates.
     * Implementation of the Monte-Carlo Method witht the eXtreme programming paradigm. 
     * Production of a graphical mp4 format tool to preview the interaction of people representation.

* Implement a Death function triggering a statement of no interaction between the death body and the population.
     * Create a method to calculate the death probability of an infected particle based on the contagion time of the particle and features like age.
     * Calculate a contagion rate in order to simulate an real-life environment where not every interaction with an infected particle and a susceptible produces the healthy particle infected.



## References

Nuraini, N; Khairudin, K; Apri, M. (2020) "Modeling Simulation of COVID-19 In Indonesia Based on Early Endemic Data". COVID-19 Literatura global sobre doença de coronavírus. [https://pesquisa.bvsalud.org/global-literature-on-novel-coronavirus-2019-ncov/resource/pt/covidwho-1260246](https://pesquisa.bvsalud.org/global-literature-on-novel-coronavirus-2019-ncov/resource/pt/covidwho-1260246)

Ortigoza, G; Lorandi, A; Neri, I. (2020) "Simulación Numérica y Modelación Matemática de la propagación del Covid 19 en el estado de Veracruz". Revista Mexicana Médica Forense, 5(3): 21-37 ISSN: 2448-8011. Retrieved from: https://www.medigraphic.com/pdfs/forense/mmf-2020/mmf203c.pdf

Aguilar, R. (n.d.). The N-body problem - astrosen.unam.mx. Instituto de Astronomía. Retrieved October 26, 2021, from https://www.astrosen.unam.mx/~aguilar/MySite/Outreach_files/Nbody1_eng.pdf.

Mocz, P. (2020) "Create Your Own N-body Simulation (With Python)" Retrived October26, 2021, from: https://medium.com/swlh/create-your-own-n-body-simulation-with-python-f417234885e9

### Disclaimer: 
This project is protected under the GNU Licence v3, please refer to the document in case of any doubt towards referencing and usage of this project.
