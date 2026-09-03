def analyze (ticks, barrier=2):
last=[int(str(p)[-1) for p in ticks]
over=sum(for d in last id d > barrier)
return over 
