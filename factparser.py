x = {"m":{"ft":3.28},"ft":{"in":12},"hr":{"min":60},"min":{"sec":60}}
def parse(fact):
    #2m = ? in
     t=fact.split("=")
     b = t[0]
     c= t[1].split("?")[1]
     d= ""
     e= 0
     for i in b:
          try:
               r= int(i)
          except:
               d+=str(i).strip()
          else:
               e+=r            
     try:
       l=x.get(d)  
       z=next(iter(l))
       print(z)
       if str(z).strip()!=str(c).strip():
          e*=l.get(z)
          u=x.get(z)
          w=next(iter(u))
          print(w,c)
          if str(c).strip() == str(w).strip():
            e*=u.get(w)
          print(e,c)
       elif str(z).strip()==str(c).strip():
          e*=l.get(z)
          print(e,c)
     except:
       reversed_dict =  { v:{k:1/we}
                    for k, innerdict in x.items()
                    for v,we in innerdict.items()
                    } 

       print(reversed_dict)

       try:
           ber=reversed_dict.get(d)
           reb=ber.get(next(iter(ber)))
           reb*= r
           # we realize that the repeated units are keys in both reversed in normal dict
           count = len(x) 
           for i in range(count +1):
              q=next(iter(x))
              dependency_list = []
              if reversed_dict.get(q)!= None:
                 print(q) 
                 print(reversed_dict.get(q))
                 print(x.get(q))
                 dependency_list.append(q)     
              x.pop(q)
           for i in dependency_list:
                  print(i)    
           if str(c).strip()== str(next(iter(ber))).strip():
               print(reb,c)
           elif str(c).strip in dependency_list:
               pass
           else:
               print("no dependency exists")
               exit
       except Exception as e:
           print(f"i dunno bro,script not working i guess \n {e}")
       else:
           print("works")
          
     else: 
         print ("hello"); 

parse("2in = ? m")