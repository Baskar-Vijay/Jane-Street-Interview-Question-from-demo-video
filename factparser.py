x = {"m":{"ft":3.28},"ft":{"in":12},"hr":{"min":60},"min":{"sec":60}}
reversed_dict =  { v:{k:1/we}
                    for k, innerdict in x.items()
                    for v,we in innerdict.items()
                    } 
def parse(fact):
     # I Realized that the repeated units are keys in both reversed and orginal dict
     dependency_list=[]
     te=x.copy()
     for i in range(len(x)):
      q=str(next(iter(te)))
      if reversed_dict.get(q)!=None:
        dependency_list.append(q)
      elif reversed_dict.get(q)==None:
        pass
      else: 
        continue
      te.pop(q)
    #2m = ? in
     try:
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
        #print(z)
        if str(z).strip()!=str(c).strip():
            e*=l.get(z)
            u=x.get(z)
            w=next(iter(u))
            #print(w,c)
            if str(c).strip() == str(w).strip():
              e*=u.get(w)
            print(e,c)
        elif str(z).strip()==str(c).strip():
            e*=l.get(z)
            print(e,c)
      except:
        

        #print(reversed_dict)

        try:
            ber=reversed_dict.get(d)
            reb=ber.get(next(iter(ber)))
            reb*= r
            if str(c).strip()!=next(iter(ber)):
                if next(iter(ber)) in dependency_list:
                  if next(iter(reversed_dict.get(next(iter(ber)))))==str(c).strip():
                      much = reversed_dict.get(next(iter(ber)))
                      reb*=much.get(next(iter(much)))
                      print(reb,str(c).strip())
                  elif next(iter(reversed_dict.get(next(iter(ber)))))!=str(c).strip():
                      print("i don't think there even is reference for this")
            elif str(c).strip()==next(iter(ber)):
                print(reb,str(c).strip())
            else:
                pass     
        except Exception as e:
            print("I have no clue what edge case u tested throw this error,but here is explanation of why your code may have failed:",f"{e}","\n 2")
        else:
            pass
            
      else: 
          pass
     except Exception as e:
            print("I have no clue what edge case u tested throw this error,but here is explanation of why your code may have failed:",f"{e}","\n 1")
     else:
        pass
parse("2in = ? m")
parse("2m = ? ft")
parse("2 min = ? sec")
parse("2 m = ? in")
parse(" 3in = ? min")
parse(" 2min = ? in")
#note min to inch fails silent 

