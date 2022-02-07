#!/usr/bin/env python3

import math
import random
import numpy as np
import sys

class People():
    age=0
    gender=0
    status =0
    time_recovery=0
    position = []
    velocity = []
    updated = False
    def __init__(self,age,gender,status,time_recovery,p_x,p_y,r_x,r_y):
        self.age = age
        self.gender = gender
        self.status = status
        self.time_recovery = time_recovery
        self.position = [p_x,p_y]
        self.velocity = [r_x,r_y]
        self.updated = False

    def print_people(self):
        print(f"{self.age}\t{self.gender}\t{self.status}\t{self.time_recovery}\t[{self.position[0]},{self.position[1]}]\t[{self.velocity[0]},{self.velocity[1]}]")





class Population():
    particles = []
    def __init__(self,population):
        self.particles = population
    
    def print_particles(self):
        self.particles[0].print_people()
        for particle in self.particles:
            particle.print_people()

class Modelo():
    population = []
    steps = 0
    prints = 0
    radii = 0
    dt=0
    rt = 0
    A = 0
    B =0
    def __init__(self,population,A,B,steps,prints,radii,dt,rt,et,st):
        self.population = population
        self.steps = steps
        self.prints = prints
        self.radii = radii
        self.dt = dt
        self.rt = rt
        self.A = A
        self.B = B
        self.et = et
        self.st = st
    
    def exposedtoInfected(self,p):
        p.status=2
        p.time_recovery = 0.0
    
    def infectedtoSR(self,p):
        choice = np.random.choice([True,False],p=[0.03,0.97])
        if choice:
            p.status=4
            p.time_recovery=0.0
            p.velocity = [0.0,0.0]
        else:
            p.status=3
            p.time_recovery = 0.0
    
    def severetoDR(self,p):
        choice = np.random.choice([True,False],p=[0.88,0.12])
        if choice:
            p.status=-1
            p.time_recovery = 0.0
            p.velocity = [0.0,0.0]
        else:
            p.status=3
            p.velocity = [1.0,1.0]
            p.time_recovery
    
    def exposedtoInfected(self,p):
        p.status=2
        p.time_recovery = 0.0

    def intersection(self,k,m):
        a = k.position[0]
        b = k.position[1]
        c = m.position[0]
        d = m.position[1]

        if a<0:
            if (self.A+a)<self.radii:
                if c>0:
                    if (self.A-c) < self.radii:
                        c = -2*self.A+c
        
        if a>0:
            if (self.A-a)<self.radii:
                if c<0:
                    if (self.A+c) < self.radii:
                        a = -2*self.A+a
        
        if b<0:
            if (self.B+b)<self.radii:
                if d>0:
                    if (self.B-d) < self.radii:
                        d = -2*self.B+d
        
        if b>0:
            if (self.B-b)<self.radii:
                if d<0:
                    if (self.B+d) < self.radii:
                        b = -2*self.B+b

        distance = math.sqrt(math.pow(c-a,2)+math.pow(d-b,2))
        if distance <= self.radii and k.status not in [-1,4] and m.status not in [-1,4]:
            if k.status in [1,2,4] and m.status==0:
                m.status=1
                m.time_recovery=0.0
            elif k.status==0 and m.status in [1,2,4]:
                k.status=1
                k.time_recovery = 0.0
            return True
        else:
            return False
    
    def fix_borders(self,p):
        x_A = -self.A/2
        x_B = self.A/2
        y_A = self.B/2
        y_B = -self.B/2
        if p.position[0]< x_A:
            p.position[0] = x_B + (p.position[0]-x_A)
        elif x_B < p.position[0]:
            p.position[0] = x_A + (p.position[0]-x_B)
        
        if p.position[1]> y_A:
            p.position[1] = y_B + (p.position[1]-y_A)
        elif p.position[1]<y_B:
            p.position[1] = y_A + (p.position[1]-y_B)

    def updateTraj(self,k,m):
        v1x = k.velocity[0]
        v1y = k.velocity[1]
        v2x = m.velocity[0]
        v2y = m.velocity[1]
        x1 = k.position[0]
        y1 = k.position[1]
        x2 = m.position[0]
        y2 = m.position[1]

        if x1 <0.0:
            if (self.A+x1) < self.radii:
                if x2>0.0:
                    if (self.A-x2) < self.radii:
                        x2 = -2.0*self.A +x2
        
        if x1 >0.0:
            if (self.A-x1) < self.radii:
                if x2<0.0:
                    if (self.A+x2) < self.radii:
                        x1 = -2.0*self.A +x1
        
        if y1 <0.0:
            if (self.B+y1) < self.radii:
                if y2>0.0:
                    if (self.B-y2) < self.radii:
                        y2 = -2.0*self.B +y2
        
        if y1 >0.0:
            if (self.B-y1) < self.radii:
                if y2<0.0:
                    if (self.B+y2) < self.radii:
                        y1 = -2.0*self.B +y1
        norm = abs(math.pow(x1-x2,2)+math.pow(y1-y2,2))
        dot_prod = (v1x-v2x)*(x1-x2) + (v1y-v2y)*(y1-y2)
        k.velocity[0] = v1x -(dot_prod/norm)*(x1-x2)
        k.velocity[1] = v1y -(dot_prod/norm)*(y1-y2)

        norm = abs(math.pow(x2-x1,2)+math.pow(y2-y1,2))
        dot_prod = (v2x-v1x)*(x2-x1) + (v2y-v1y)*(y2-y1)
        m.velocity[0] = v2x -(dot_prod/norm)*(x2-x1)
        m.velocity[1] = v2y -(dot_prod/norm)*(y2-y1)
    
    def integrate(self,people):
        v = people.velocity[0]
        d = v*self.dt
        people.position[0] += d

        v = people.velocity[1]
        d = v*self.dt
        people.position[1] += d
        people.time_recovery+=1.0

    
    def interaction(self):
        for i in range(len(self.population.particles)):
            for j in range(i+1,len(self.population.particles)):
                if(self.intersection(self.population.particles[i],self.population.particles[j])==True):
                    self.updateTraj(self.population.particles[i],self.population.particles[j])
    
    def run(self):
        j=0

        stats = {i:0 for i in range(-1,5)}
        for i in self.population.particles:
            stats[i.status]+=1
        
        print(f"#0\t{stats[0]}\t{stats[1]}\t{stats[2]}\t{stats[3]}\t{stats[4]}\t{stats[-1]}")
        for k in self.population.particles:
            k.print_people()

        
        for i in range(self.steps):
            self.interaction()

            for k in self.population.particles:
                self.integrate(k)
                #k.print_people()
                if k.status ==1 and k.time_recovery>=self.et:
                    self.exposedtoInfected(k)
                if k.status==2 and k.time_recovery>=self.rt:
                    self.infectedtoSR(k)
                if k.status==4 and k.time_recovery >=self.st:
                    self.severetoDR(k)
            for k in self.population.particles:
                self.fix_borders(k)
            j+=1
            stats = {i:0 for i in range(-1,5)}
            for p in self.population.particles:
                stats[p.status]+=1
            
            print(f"#{i+1}\t{stats[0]}\t{stats[1]}\t{stats[2]}\t{stats[3]}\t{stats[4]}\t{stats[-1]}")
            # print(f"#\t{i+1}")
            for k in self.population.particles:
                k.print_people()




    

pop = []
steps=5000
prints=1
radii = 2
A = 100.0
B = 100.0
v_A = 1.0
v_B = 1.0
dt=0.1
rt = 1000.0
et = 300.0
st = 300.0
porc_exp = float(sys.argv[1])
for i in range(int(100*(1-porc_exp))):

    x = random.uniform(-A/2,A/2)
    y = random.uniform(-B/2,B/2)
    v_1 = random.uniform(-v_A/2,v_A/2)
    v_2 = random.uniform(-v_B/2,v_B/2)
    pop.append(People(18,0,0,0.0,x,y,v_1,v_2))

for i in range(int(100*porc_exp)):
    x = random.uniform(-A/2,A/2)
    y = random.uniform(-B/2,B/2)
    v_1 = random.uniform(-v_A/2,v_A/2)
    v_2 = random.uniform(-v_B/2,v_B/2)
    pop.append(People(18,0,1,0.0,x,y,v_1,v_2))


population = Population(pop)
print(f"#{10000}\t{100}\t{-A/2}\t{A/2}\t{-B/2}\t{B/2}\t{radii/2.0}")
mod = Modelo(population,A,B,steps,prints,radii,dt,rt,et,st)
mod.run()



