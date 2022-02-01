#from people  import People
import random
import time

def p_infected(comorbilities,vaccine,alfa=0.01,beta=0.01):
        #Tomar vacuna con 0.7 de evitar contagio y .85 de evitar hospitalizacion
        C=len(comorbilities)
        probs_com = C*alfa
        ruido = random.random()
        if ruido<0.5:
            beta = 0
        if C== 0: probs_com = 1

        if vaccine:
            normalize = abs((probs_com - vaccine + beta) - min([probs_com,vaccine]))/abs((probs_com - vaccine + beta) - max([probs_com,vaccine]))
        else:
            normalize = probs_com + beta
        
        if normalize > 0.7:
            return True
        else:
            return False

def p_recovered(comorbilities,vaccine,alfa=0.01,beta=0.01):
    #Tomar vacuna con 0.7 de evitar contagio y .85 de evitar hospitalizacion
    C=len(comorbilities)
    probs_com = C*alfa
    ruido = random.random()
    if ruido<0.5:
        beta = 0

    if C== 0: probs_com = 1
    if vaccine:
        p = probs_com*0.9 - beta
    else:
        p= probs_com - beta

    if p>0.5:
        return True
    else:
        return False

def p_severe_death(comorbilities,vaccine,alfa=0.01,beta=0.01):
    #Tomar vacuna con 0.9 de evitar muerte
    #Be
    C=len(comorbilities)
    probs_com = C*alfa
    ruido = random.random()
    if ruido<0.5:
        beta = 0
    if C== 0: probs_com = 1
    if vaccine:
        p = probs_com/0.9 - beta
    else:
        p = probs_com - beta
    if p>0.5:
        #Muere o severa la persona
        return True
    else:
        return False

def determinate_state(current, time, persona, interaccion=False):
    #Current 0, 1, 2, 3, 4, 5 -> 5 es recuperado
    if current == 1 and interaccion:
        infected = p_infected(persona.comorbilities, persona.vaccinated)
        time.sleep(0.5)
        if infected:
            persona.status = 2
    time.sleep(0.7)
    if current == 2:
        severo = p_severe_death(persona.comorbilities, persona.vaccinated)
        time.sleep(3)
        if severo:
            persona.status = 3
        else:
            persona.status = 5
    elif current == 3:
        m_ = p_severe_death(persona.comorbilities, persona.vaccinated) #Fallece?
        if m:
            persona.status = 4
        else:
            persona.status = 5
    return