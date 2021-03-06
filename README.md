# M-S2022
# Modeling and Simulation: Conservation of Momentum for COVID-19 simulation
This is the final project of the subject Modeling and Simulation of the [Escuela Nacional de Estudios Superiores UNAM campus Morelia](https://www.enesmorelia.unam.mx/).

## Contact

- Team leader: Jorge Oscar Vázquez Fuerte 
     · Mail: jorgeovf01@gmail.com 
     
- P.R.: Paola González Hernández
     · Mail: paaoogh@gmail.com

- Tech leader: Kevin Gómez 
     · Mail: kgomez0800@gmail.com
     


## Introduction

Conservation of Momentum is one of the main topics in the project, so first we have to explain what is conservation of momentum, is a general law of physics, an idea of this is, if you apply forces on a object it is going to keep moving forever if and only if no other force affect the object but if this object is affected for at least one forces this will transmit the first force to the second so momentum is neither created nor destroyed, but only changed through the action of forces as described by Newton's laws of motion.
One example of conservation of momentum is Newton's cradle device that demonstrates the conservation of momentum, it consists of four or more balls hanging together, and when one is lifted from its place functioning as a pendulum and then released, it will collide with the other balls, but not all of them will move, but will transfer their momentum to the ball on the opposite side to the one that moved.

the behavior of one particle can be describe by the next equation p = mv where p is a particle, m is the mass and v is the velocity and if exist more than one particle the equation is  

![image](https://user-images.githubusercontent.com/79944448/146283321-2b0f55a3-bd9d-41d0-a257-92d761413ddb.png) 

The momentum of conservation can be seen as a vector than have a magnitude and a direction. Momentum is conserved in all three physical directions at the same time. It is even more difficult when dealing with a gas because forces in one direction can affect the momentum in another direction because of the collisions of many molecules.





## Justification

The purpose of this project is to analyze previous data of covid spreading in Mexico and recreate an environment with an arbitrary population of healthy individuals and an initial point of infected people. All the individuals will interact between each other causing the contagion of the healthy individuals, at the same time some of the infected individuals will develop immunity meanwhile another infected community will die. As is expected, at some point, all the survivors will develop immunity.  As a result, we are looking for a model that describe the virus behavior over certain time intervals and, most importantly, these results will be helpful to plan strategies of virus scan and protection on hard to reach areas like rural communities which are far away from vaccinations plans and the latest technological innovations in some future work.

Local data will be retrieved, not only for complexity purposes, but also due to the fact that local data is important because not all socioeconomic, cultural and other conditions affect on the strategies that each health organization and government take into consideration. COVID-19 has had an effect diferent in many countries, states and cities; then, understading the behaviour of phenomena like a pandemic requieres from a lot of analysis. Modeling this behaviour, taking into account different external factors, could benefit future interdisciplinary work.

## Objectives

* Use initial parameters based on data provided by the [CONACYT and Centro Geo](https://datos.covid-19.conacyt.mx/) and we will take only the data of cases in the city of Morelia to keep the complexity feascible to manage. Data will take only within lapse of July 1st to October 31st as there is a clear trend shown in the CONACyT graphs about cumulative and confirmed cased.

* Create a conservation of momentum model to define and describe the interactions of each particle with space and with other particles, the interaction is an important part because when one particle be close of other can transmit momentum to other and activate certain states like exposed health state. 
 
* Implement a  SEIR model for describe the interaction abd state of the particles, when a particle should turning in an infected particle or a dead, this model will be have a function of time with probability of being infected and a infected particle have a similar function with a probability of turning a severed infected and a severed infected particle can turning a dead particle or a recovered particle.
 
* show with graphics how many particles were infected,  recovered, or dead.



## Methodology

The interaction between individuals is based on Particles methods and the conservation of momentum properties, hence every Particle (individual) has a position on the plane, velocity, state of health and the time that the particle has spent in the state of health. Also, the definition of an interaction threshold between particles is one of the most important parts of the simulations as it will activate some functions to change the health state of the Particle.

The states of health of the COVID-19 an its activations  an transitions are shaped with a SEIR model, specifically this type of model has 4 main states of health:
* Susceptible, these are the common people that haven't had any type of interaction with the virus.
* Exposed, individuals who had contact with an infected Particle.
* Infected, individuals who have the disease and are contagious agents.
* Recovered, these people became immune after being infected.

Noting that every state is in function of time, that's because the time of state is an important property of the Particles. Also, more complexity is meant to be added to the model, as we want to ensure a death function that will be activated after a new state of severe infected, so for this project there are going to be 6 states of health. To a better understanding of the modelation and the states of health we present the following chart:

![image](https://i.ibb.co/m0Vwpjm/seir-diagram.png)

Note that as explained before, the transitions between the states of health will be described as functions of time, for example, in real life the time between being infected and being recovered is approximately 10 to 14 days.  In some cases the state functions work with ratios, for example, the transition between infected and severed infected will depend on the time and a ratio that describes a probability of turn on a worse health states, something similar happens with the transition between the severe infected state and the Dead state where there will also be a ratio that describes the probability of death.

The information of every particle will be tracked and stored in a data file at every increment of time &delta; (t) with the purpose of graphing every frame of the simulation and joining the frames into a video of the complete simulation of the interaction between individuals and the progress of the COVID-19. Also, the data file is parsed to draw a graph with the fluctuation of the infected, recovered and dead individuals along the time.



### Software tools
* `Python3`


As the programming language is python, somo of the basic libraries for plotting and for vector operations are needed:
* matplotlib
* numpy
* pandas
* seaborn
## Results

In this project we work with 100 randomly scattered particles with the 5% of the population exposed to the virus as initial condition. Almost every change of state is a function of time, but we calculated two extra ratios for the change of state from infected to severe infected and on the change of state from severe infected and dead. These probabilities were obtained from the Secretaria de Salud COVID-19 data in December, 2021, also we only use the information of Morelia. All the process of getting the probabilities is in `data_cleaning.ipynb` and the probabilities are the following:
* The probability of being severe infected after being infected is 1.28%.
* The probability of being dead after being severe infected is 88.88%.

Note that every infected person gets recovered after a period of time has passed but a severely infected person gets recovered with the inverse of the probability of being dead.

Also we want to specify an important probability for a pandemic model, as a healthy person may not have serious symptoms if they get infected, also the probabilities for a healthy person dying from a virus are considerably lower than the probabilities of a person who has chronic diseases such as diabetes, cancer or asthma. From the Morelia data we also got results for this sector of the population.
* 66.78% of the infected population sample of Morelia tested positive for COVID-19 and didn’t have any other disease.
* The probability of a healthy person dying from the virus is only 3.14%.

The code we used to get this probabilities is also in `data_cleaning.ipynb`.

With all the necessary probabilities  setted, the model is ready for the simulation, the pandemic interactions are simulated for 5,000 iterations, after running the model, we can see the pandemic propagation with the `viewStates.py` where the number of susceptible, exposed, infected, severe infected and dead particles at every iteration.

![states](https://user-images.githubusercontent.com/80866685/152631738-8271c30e-d197-4395-b865-b092a2190fe3.png)

Analyzing the plot we can see a pandemic behavior similar to the COVID-19, with a stage where the number of infected particles raises considerably and the number of immune individuals also starts to grow also with the severe infected ratio we can see that just a few of the particles got severe infected and with a high dead ratio almost every severe infected died after a period of iterations. 

Due to the population size setted for the simulation, the pandemic propagation was at some point faster than a real life virus propagation, but with the COVID-19 we hope a similar final stage of the pandemic, where a high percentage of the population got infected and immune to the virus and the other part of the population did not get infected so the virus propagation stops, however, in the real scenario we know the virus mutes in order to still being contagious regardless the population immunity. Our simulation is not that far from the real scenario because the final stage of the simulation can also be seen like a virus control stage where the virus is still contagious but the most of the population got exposed to the virus so the number of infected, severe infected and dead individuals drops and gets almost constant at this final stage.

In conclusion, we achieved the objectives setted in the project and developed an interesting pandemic propagation model that can be also used for modeling other pandemic propagation besides the main modeling of the project based on the COVID-19 spread, regardless all the complexity of the human interactions with other human beings and all the features that a human has, we managed to develop this pandemic propagation model and as mentioned before the model has the specifications in order to get results similar to a common pandemic behavior.

We also created an animation of the pandemic propagation using the information of the particles at every iteration and plotting the particles and using the plots for the iterations as frames of the animation, to plot every frame we used the `view.py` script, before running the script we created the ‘animation’ folder. [Here is the Animation.](https://youtu.be/T1TGYhn6Cfw)


## Code running instructions
In order to run the code you need to clone this repository and change the scrpits permission to an executable mode, you might use this command:
```
chmod 750 *.py
```
To run the model simulation you must specify the percentage of the population that will be initialized as exposed also you need to specify an output file where the information of the pandemic states and person updates at every iteration will be written, for example, if you want the 10% of the population to be infected at the beggining of the simulation you will run the scrpit with the next command:
```
./people.py 0.1 > view2D.dat
```
for this project we are simulating the pandemic propagation with a starting point of 5% of the population exposed to the virus, so if you want to get similar results as the presented in this project you must run the following command:

```
./people.py 0.05 > view2D.dat
```
The simulation results can be viewed by running the `viewStats.py` script, you will see a graph showing the progress of each pandemic state by its frequency over time. Run the script by typing this in the terminal:

```
./viewStats.py
```
## References
Kuzdeuov, A., Karabay, A., Baimukashev, D., Ibragimov, B., et al. (2020). "Particle-Based COVID-19 Simulator with Contact Tracing and Testing". Preprint for Medical and Healthe Services. [https://www.medrxiv.org/content/10.1101/2020.12.07.20245043v1.full](https://www.medrxiv.org/content/10.1101/2020.12.07.20245043v1.full)


Nuraini, N; Khairudin, K; Apri, M. (2020) "Modeling Simulation of COVID-19 In Indonesia Based on Early Endemic Data". COVID-19 Literatura global sobre doença de coronavírus. [https://pesquisa.bvsalud.org/global-literature-on-novel-coronavirus-2019-ncov/resource/pt/covidwho-1260246](https://pesquisa.bvsalud.org/global-literature-on-novel-coronavirus-2019-ncov/resource/pt/covidwho-1260246)

Ortigoza, G; Lorandi, A; Neri, I. (2020) "Simulación Numérica y Modelación Matemática de la propagación del Covid 19 en el estado de Veracruz". Revista Mexicana Médica Forense, 5(3): 21-37 ISSN: 2448-8011. Retrieved from: https://www.medigraphic.com/pdfs/forense/mmf-2020/mmf203c.pdf


The Editors of Encyclopaedia Britannica (n.d.) "conservation of momentum physics". Retrived from https://www.britannica.com/science/conservation-of-momentum


### Disclaimer: 
This project is protected under the GNU Licence v3, please refer to the document in case of any doubt towards referencing and usage of this project.
