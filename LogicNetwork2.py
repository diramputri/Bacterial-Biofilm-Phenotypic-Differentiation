
"""
Created on Wed Jun 28 13:22:15 2017

@author: Andira

"""
import tellurium as te
import roadrunner as r

r = te.loada('''
    model pathway()

$X -> C; N - a*C
  $X -> P; Q + (k1^n)/(k1^n+C^n) - c*P
  $X -> R; (k2^n)/(k2^n+P^n) * (k3^n)/(k3^n+C^n) - f*R
  $X -> S; (k4^n)/(k4^n+R^n) * (k5^n)/(k5^n+C^n) - i*S

C=0.1
P=0.1
R=0.1
S=0.1
a=0.7
k1=1.67
c=6
k2=5
k3=3.3
f=4
k4=1
k5=0.58
i=2.78
n=2
N=1
Q=10
 end
''')

   
res = r.simulate(0, 1.5, 100, ['TIME','C','P','R','S'])
r.plot()

print r.getSteadyStateValues() 
print r.getFullEigenValues()

p = ps(r)

p.endTime = 1.5
p.numberOfPoints = 200
p.polyNumber = 10
p.startValue = 0
p.endValue = 5
#parameter to test
p.value = 'a' 
#variable you want to see affected by changing parameter
p.selection = ['S']
p.plotGraduatedArray()

print r.getScaledElasticityMatrix()
print r.getCC ('P', 'c')