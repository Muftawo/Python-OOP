
f_charged= [f"bat.{i}" for i in range(1,3)]
charging= {}


# class SwapStation:
#     def __init__(self,f_charged=None,charging=None):
#         self.f_charged=f_charged
#         self.charging=charging
        
#     def 

print("charged batteries are",f_charged )



print("charged batteries are",f_charged )

class MoreThanAllowed(Exception):
    pass

class LessThanAllowed(Exception):
    pass


class NoBatteriesAttached(Exception):
    pass



class Battery_user:
    def __init__(self, attched_batteries=None):
        attched_batteries = []
        self.attched_batteries = attched_batteries
        

    def get_batteries(self,num=2):
        if num > 2:
            raise MoreThanAllowed
        elif num <=0:
            raise LessThanAllowed
        self.attched_batteries.extend([f_charged.pop(0) for _ in range(0,num)])
        return self.attched_batteries

    def release_batteries(self):
        if len(self.attched_batteries) == 0:    
            raise NoBatteriesAttached
        for x in self.attched_batteries:
            charging[x]=0
        print(f"{self.attched_batteries} Released")
        self.attched_batteries= []
        return "released"
    

okada1 = Battery_user()
print(f"okada1 has",okada1.get_batteries(1))
okada2 = Battery_user()
print(f"okada2 has",okada2.get_batteries())
okada3 = Battery_user()
print(f"okada2 has",okada3.get_batteries())

print(f"batteries on charge {charging}")

print(f"==="*10)

okada1.release_batteries()
okada2.release_batteries()
# okada1.release_batteries()


print(f_charged)
print(f"batteries on charge {charging}")
