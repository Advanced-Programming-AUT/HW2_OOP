#این کد با دستور ENDبه پایان می رسد
class Legistick :
    def __init__(self,id,type,fixed_cost,cost_km,fuel_km):
        self.id = id
        self.type = type
        self.fixed_cost = fixed_cost
        self.cost_km = cost_km
        self.fuel_km = fuel_km
class Trip :
    def __init__(self,id,km = 0)->None:
        self.id = id
        self.km = km
    def total_km(self,a,b):
        if self.id == a :
            self.km += b



         #super.__init__(self,id,type,fixed_cost,cost_km,fuel_km)



request = input()
finalr = ""
legs = []
id = 1
pricefuel = {}
lis_trip = {}
while request != 'END':
    desireresult = ""

    if 'ADD_VEHICLE' in request:
        p= request.split()

        Legistick(id,p[1],p[2],p[3],p[4])
        legs.append(Legistick(id,p[1],p[2],p[3],p[4]))
        finalr += f"Vehicle {p[1]} added with fixed cost: {p[2]},variable cost per km :{p[3]},fuel consumption per km: {p[4]}"
        id += 1
    if 'ADD_TRIP' in request:
        p = request.split()
        vehicle_id = int(p[1])
        for i in legs :
            if i.id == vehicle_id :
                finalr += f"Trip registered : {i.type} from {p[2]} to {p[3]} carrying {p[4]} kg"


        if (p[2] == 'A' and p[3] == 'B') or (p[2] == 'B' and p[3] == 'A') :
            km = 100
        elif(p[2] == 'A' and p[3] == 'C') or (p[2] == 'C' and p[3] == 'A') :
            km = 200
        elif (p[2] == 'A' and p[3] == 'D') or (p[2] == 'D' and p[3] == 'A') :
            km = 150
        elif (p[2] == 'A' and p[3] == 'E') or (p[2] == 'E' and p[3] == 'A') :
            km = 300
        elif (p[2] == 'B' and p[3] == 'C') or (p[2] == 'C' and p[3] == 'B') :
            km = 250
        elif (p[2] == 'B' and p[3] == 'D') or (p[2] == 'D' and p[3] == 'B') :
            km = 180
        elif (p[2] == 'B' and p[3] == 'E') or (p[2] == 'E' and p[3] == 'B') :
            km = 400
        elif (p[2] == 'C' and p[3] == 'D') or (p[2] == 'D' and p[3] == 'C') :
            km = 120
        elif (p[2] == 'C' and p[3] == 'E') or (p[2] == 'E' and p[3] == 'C') :
            km = 350
        elif (p[2] == 'D' and p[3] == 'E') or (p[2] == 'E' and p[3] == 'D') :
            km = 280
        elif p[2] == p[3] :
            km = 0
        #m = Trip(p[1],km)
        #m.total_km(p[i],km)
        #lis_trip.append(Trip(p[1],km))
        if vehicle_id in lis_trip:

                lis_trip[vehicle_id] += km
        else:

            lis_trip[vehicle_id] = km


    if 'SET_FUEL_PRICE' in request:
        p = request.split()
        pricefuel[p[1]] = p[2]
        finalr += f"Fuel price for {p[1]} set to {p[2]} per liter"

    if request == 'END_MONTH':
        finalr += 'End of month report\n'
        totalfixed = 0
        total_costkm = 0
        for i in range (len(legs)) :
            totalfixed += int(legs[i].fixed_cost)
        finalr += f"Total fixed maintenace cost {totalfixed}\n"


        for i in range(len(legs)) :
            if legs[i].id in lis_trip :
                    total_costkm += int(lis_trip[legs[i].id])*int(legs[i].cost_km)
        finalr += f"Total variable maintenace cost: {total_costkm}\n"

        kmprice = 0
        for i in range(len(legs)):
            if legs[i].type == 'PLANE' :

                kmprice += int(lis_trip[i+1])*int(legs[i].fuel_km)*int(pricefuel['JET_FUEL'])
            if legs[i].type == 'TRUCK' :

                kmprice += int(lis_trip[i+1])*int(legs[i].fuel_km)*int(pricefuel['DIESEL'])
            if legs[i].type == 'CAR' or legs[i].type == 'PICKUPTRUCK' :

                kmprice += int(lis_trip[i+1])*int(legs[i].fuel_km)*int(pricefuel['GASOLINE'])
        finalr += f"Total fuel cost {kmprice}\n"
        tcost = kmprice +  total_costkm + totalfixed
        finalr += f"Total operational cost {tcost}\n"
        finalr += f"Detailed costs:\n"

        for i in range(len(legs)) :
            if legs[i].type == 'PLANE' :

                x = int(lis_trip[i+1])*int(legs[i].fuel_km)*int(pricefuel['JET_FUEL'])
            if legs[i].type == 'TRUCK' :

                x= int(lis_trip[i+1])*int(legs[i].fuel_km)*int(pricefuel['DIESEL'])
            if legs[i].type == 'CAR' or legs[i].type == 'PICKUPTRUCK' :

                x= int(lis_trip[i+1])*int(legs[i].fuel_km)*int(pricefuel['GASOLINE'])
            finalr += f" {legs[i].type} (ID: {legs[i].id}):\n  Fixed maintenace: {legs[i].fixed_cost}\n  Variable maintenace: {int(legs[i].cost_km)*int(lis_trip[i+1])}\n  Fuel cost: {x}\n"







    request = input()
    finalr += "\n"

print(finalr)
