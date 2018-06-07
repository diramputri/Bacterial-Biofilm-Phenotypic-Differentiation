r = te.loada('''
    model pathway()

  $X -> GTP; a - b*GTP - c*CodY*GTP + d*Complex;
  $X -> CodY; (e*f)/(g*CodY + f) - c*CodY*GTP + d*Complex - h*CodY;
  $X -> Complex; c*CodY*GTP - d*Complex - i*Complex;
  $X -> Pe; l + m*Pin - n*Pe; 
  $X -> Pin; (o*p)/(q*Complex + p) - m*Pin - r*Pin;
  $X -> Pa; m*Pin - s*R*Pa - t*Pa;
  $X -> R; (o*u)/(v*CodY + u) - w*R*SFP - s*R*Pa - x*R;
  $X -> Kb; (y*z)/(aa*CodY + z) - bb*Kb - cc*Kb*SFP - dd*Kb;
  $X -> SFP; ee*Kb*SFP - w*R*SFP - ff*SFP - gg*SFP*SAP - hh*SFP;
  $X -> SAP; gg*SAP*SFP - ii*SAP - jj*SAP;
   
#Model that does not converge
#   $X -> GTP; a - b*GTP - c*CodY*GTP + d*GTPCodY;
#   $X -> CodY; (e*f)/(g*CodY + f) - c*CodY*GTP + d*GTPCodY - h*CodY;
#   $X -> GTPCodY; c*CodY*GTP - d*GTPCodY - i*GTPCodY;
#   $X -> Pe; l + m*Pin - n*Pe - (qq*rr*Pe)/(qq*ss); 
#   $X -> Pin; (o*p)/(q*GTPCodY + p) - m*Pin - r*Pin;
#   $X -> Pa; m*Pin - s*R*Pa + j*R*Pa - t*Pa + (qq*rr*Pe)/(qq*ss);
#   $X -> R; (o*u)/(v*CodY + u) - w*R*SFP - s*R*Pa + oo*PhrRap + pp*PhrRap + kk*R*Pa - x*R;
#   $X -> PhrRap; w*R*SFP - mm*PhrRap - nn*PhrRap;
#   $X -> Kb; (y*z)/(aa*CodY + z) - bb*Kb - cc*Kb*SFP - dd*Kb;
#   $X -> SFP; ee*Kb*SFP - w*R*SFP - ff*SFP - gg*SFP*SAP - hh*SFP;
#   $X -> SAP; gg*SAP*SFP - ii*SAP - jj*SAP;

    # Initialize values

X=0;
Complex=0;
GTP=10;
CodY=10.0;
GTPCodY=0;
Pe=50.0;
Pin=0.02;
Pa=0.1;
R=0;
Kb=0;
SFP=1.0;
SAP=1.0;
PhrRap=0;
a=2;
b=0.02;
c=0.0001;
d=0.1;
e=0.4;
f=20;
g=20;
h=0.002;
i=0.002;
j= 1;
l= 5;
m= 1;
n= 0.02;
o= 20;
p= 20;
q= 20;
r= 0.02;
s= 0.083;
t= 0.02;
u= 2;
v= 2;
w= 0.0004;
x= 0.002;
y= 10;
z= 20;
aa= 20;
bb= 0.1;
cc= 0.000000017;
dd= 0.002;
ee= 0.01;
ff= 0.0004;
gg= 0.01;
hh= 0.002;
ii= 0.05;
jj= 0.00008;
kk= 1;
mm= 0.0004;
nn= 0.002;
oo= 0.002;
pp= 0.0004;
qq= 1;
rr= 1;
ss= 1;
 end
''')
   
res = r.simulate(0, 1000, 1000, ['Time', 'SAP']);
plt.ylim ((0,1))
plt.xlabel ('Time')
plt.ylabel ('Concentration')
plt.title ('My First Plot ($y = x^2$)')
r.plot(m);