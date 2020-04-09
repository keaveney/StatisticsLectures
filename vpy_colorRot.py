from vpython import *

scene = canvas()

scene.background=vector(1.0,1.0,1.0)
scene.ambient=color.white

No = 1.0
ba = arrow(pos=vector((1.0-0.5/No)*q13[0],(1.0-0.5/No)*q18[0],0), axis=vector(q13[0]/No,q18[0]/No,0), shaftwidth=0.05, color=vector(0,0,1), emissive=True)
ra = arrow(pos=vector((1.0-0.5/No)*q23[0],(1.0-0.5/No)*q28[0],0), axis=vector(q23[0]/No,q28[0]/No,0), shaftwidth=0.05, color=vector(1,0,0), emissive=True)
ga = arrow(pos=vector((1.0-0.5/No)*q33[0],(1.0-0.5/No)*q38[0],0), axis=vector(q33[0]/No,q38[0]/No,0), shaftwidth=0.05, color=vector(0,1,0), emissive=True)

blue_quark = sphere(pos=vector(q13[0],q18[0],0), radius=0.05, color=vector(0,0,1), emissive=True)
red_quark = sphere(pos=vector(q23[0],q28[0],0), radius=0.05, color=vector(1,0,0), emissive=True)
green_quark = sphere(pos=vector(q33[0],q38[0],0), radius=0.05, color=vector(0,1,0), emissive=True)

bt = sphere(pos=vector((1.0+0.5/No)*q13[0],(1.0+0.5/No)*q18[0],0), radius=0.005, color=vector(0,0,1), emissive=True, make_trail=True)
rt = sphere(pos=vector((1.0+0.5/No)*q23[0],(1.0+0.5/No)*q28[0],0), radius=0.005, color=vector(1,0,0), emissive=True, make_trail=True)
gt = sphere(pos=vector((1.0+0.5/No)*q33[0],(1.0+0.5/No)*q38[0],0), radius=0.005, color=vector(0,1,0), emissive=True, make_trail=True)

scene.waitfor("click")

n = 0
for i in range(0,Nt):
    rate(30) #100 frames /sec in a real clock
    ba.axis = vector(q13[i]/No,q18[i]/No,0)
    ra.axis = vector(q23[i]/No,q28[i]/No,0)
    ga.axis = vector(q33[i]/No,q38[i]/No,0)
    
    ba.pos = vector(q13[0]-0.5*q13[i]/No,q18[0]-0.5*q18[i]/No,0)
    ra.pos = vector(q23[0]-0.5*q23[i]/No,q28[0]-0.5*q28[i]/No,0)
    ga.pos = vector(q33[0]-0.5*q33[i]/No,q38[0]-0.5*q38[i]/No,0)
    
    bt.pos = vector(q13[0]+0.5*q13[i]/No,q18[0]+0.5*q18[i]/No,0)
    rt.pos = vector(q23[0]+0.5*q23[i]/No,q28[0]+0.5*q28[i]/No,0)
    gt.pos = vector(q33[0]+0.5*q33[i]/No,q38[0]+0.5*q38[i]/No,0)
    
    #change of color to anti-color functions
    hb = (np.mod(13.0*np.pi/6.0 - np.arctan2(q18[i],q13[i]),2.0*np.pi)/(2.0*np.pi))  #hue
    sb = ((q13[i]**2 + q18[i]**2)/max(q13**2 + q18**2))**(1/7)    #saturation, (qurks get whiter near origin)
    blue_quark.color = color.hsv_to_rgb(vector(hb,sb,1.0))
    ba.color = color.hsv_to_rgb(vector(hb,sb,1.0))
    
    hr = (np.mod(13.0*np.pi/6.0 - np.arctan2(q28[i],q23[i]),2.0*np.pi)/(2.0*np.pi))  #hue
    sr = ((q23[i]**2 + q28[i]**2)/max(q23**2 + q28**2))**(1/7)
    red_quark.color = color.hsv_to_rgb(vector(hr,sr,1.0))
    ra.color = color.hsv_to_rgb(vector(hr,sr,1.0))
    
    hg = (np.mod(13.0*np.pi/6.0 - np.arctan2(q38[i],q33[i]),2.0*np.pi)/(2.0*np.pi))  #hue
    sg = ((q33[i]**2 + q38[i]**2)/max(q33**2 + q38**2))**(1/7)
    
    
    green_quark.color = color.hsv_to_rgb(vector(hg,sg,1.0))
    ga.color = color.hsv_to_rgb(vector(hg,sg,1.0))
    
    bt.color = color.hsv_to_rgb(vector(hb,sb,1.0))
    rt.color = color.hsv_to_rgb(vector(hr,sr,1.0))
    gt.color = color.hsv_to_rgb(vector(hg,sg,1.0))
    
    rt.trail_color = color.hsv_to_rgb(vector(hr,sr,1.0))
    bt.trail_color = color.hsv_to_rgb(vector(hb,sb,1.0))
    gt.trail_color = color.hsv_to_rgb(vector(hg,sg,1.0))

