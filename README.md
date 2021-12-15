# M-S2022
# Modeling and Sumulation: COVID-19 simulation Momentum Conservation
This is the final project of the subject Modeling and Simulation of the [Escuela Nacional de Estudios Superiores UNAM campus Morelia](https://www.enesmorelia.unam.mx/).

## Contact

- Team leader: Jorge Oscar Vázquez Fuerte 
     · Mail: jorgeovf01@gmail.com 
     
- P.R.: Paola González Hernández
     · Mail: paaoogh@gmail.com

- Tech leader: Kevin Gómez 
     · Mail: kgomez0800@gmail.com
     
##

The aim of this project is to model and simulate the SARS-COV19 growth and behavior *Aquí va algo*

## Introduction
Conservation of Momentum is the principal them we'll talk, so first we have to explain what is conservation of momentum, is a general law of physics, a general idea of this is, if you apply forces on a object it is going to keep moving forever if and only if no other force afect the object but if this object is afected for at least one forces this will transmit the first force to the second so momentum is neither created nor destroyed, but only changed through the action of forces as described by Newton's laws of motion.

One example of conservation of momentum is Newton's cruble is device that demonstrates the conservation of momentum, it consists of four or more balls hanging together, and when one is lifted from its place functioning as a pendulum and then released, it will collide with the other balls, but not all of them will move, but will transfer their momentum to the ball on the opposite side to the one that moved.

the behavior of one particle can be describe by the next equation


<img src="https://latex.codecogs.com/svg.latex?\Large&space;p=mv" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />
where p is a particle, m is the mass adn v is the velocity






## Justification

The purpose of this project is to analyze previous data of covid spreading in Mexico and recreate an environment with an arbitrary population of healthy individuals and an initial point of infected people. All the bodies will interact between each other causing the contagion of the healthy individuals, at the same time some of the infected individuals will develop immunity meanwhile another infected community will die. As is expected, at some point, all the survivors will develop immunity.  As a result, we are looking for a model that describe the virus behavior over certain time intervals and, most importantly, these results will be helpful to plan strategies of virus scan and protection on hard to reach areas like rural communities which are far away from vaccinations plans and the latest technological innovations in some future work.

Local data will be retrieved, not only for complexity purposes, but also due to the fact that local data is important because not all socioeconomic, cultural and other conditions affect on the strategies that each health organization and government take into consideration. COVID-19 has had an effect diferent in many countries, states and cities; then, understading the behaviour of phenomena like a pandemic requieres from a lot of analysis. Modeling this behaviour, taking into account different external factors, could benefit future interdisciplinary work.

## Objectives

* Use initial parameters based on data provided by the [CONACYT and Centro Geo](https://datos.covid-19.conacyt.mx/) and we will take only the data of cases in the city of Morelia to keep the complexity feascible to manage. Data will take only within lapse of July 1st to October 31st as there is a clear trend shown in the CONACyT graphs about cumulative and confirmed cased.

* Implement an N-Body system with `Python3` in order to describe the COVID-19 Spreading and Behavior as a pandemic based on the SIR model based on the Kuzdeuov, A. et al publication "Particle-Based COVID-19 Simulator with Contact Tracing and Testing" (2020) with the following steps:
     * Definition of initial conditions based on the CONACyT data retrieved from the specified dates.
     * Implementation of the Monte-Carlo Method witht the eXtreme programming paradigm. 
     * Production of a graphical mp4 format tool to preview the interaction of people representation.

* Implement a Death function triggering a statement of no interaction between the death body and the population.
     * Create a method to calculate the death probability of an infected particle based on the contagion time of the particle and features like age.
     * Calculate a contagion rate in order to simulate an real-life environment where not every interaction with an infected particle and a susceptible produces the healthy particle infected.

## Methodology

*Aquí va mucho*

## References
Kuzdeuov, A., Karabay, A., Baimukashev, D., Ibragimov, B., et al. (2020). "Particle-Based COVID-19 Simulator with Contact Tracing and Testing". Preprint for Medical and Healthe Services. [https://www.medrxiv.org/content/10.1101/2020.12.07.20245043v1.full](https://www.medrxiv.org/content/10.1101/2020.12.07.20245043v1.full)


Nuraini, N; Khairudin, K; Apri, M. (2020) "Modeling Simulation of COVID-19 In Indonesia Based on Early Endemic Data". COVID-19 Literatura global sobre doença de coronavírus. [https://pesquisa.bvsalud.org/global-literature-on-novel-coronavirus-2019-ncov/resource/pt/covidwho-1260246](https://pesquisa.bvsalud.org/global-literature-on-novel-coronavirus-2019-ncov/resource/pt/covidwho-1260246)

Ortigoza, G; Lorandi, A; Neri, I. (2020) "Simulación Numérica y Modelación Matemática de la propagación del Covid 19 en el estado de Veracruz". Revista Mexicana Médica Forense, 5(3): 21-37 ISSN: 2448-8011. Retrieved from: https://www.medigraphic.com/pdfs/forense/mmf-2020/mmf203c.pdf



### Disclaimer: 
This project is protected under the GNU Licence v3, please refer to the document in case of any doubt towards referencing and usage of this project.
