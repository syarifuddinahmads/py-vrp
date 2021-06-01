# class Distance():   

#     customer = []
#     distance = []
    
#     def __init__(self,Customer,Distance):
#         self.customer = Customer
#         self.distance = Distance

#     def count_distance_customer_dinamic(self,counter):
#         data_distance = self.distance
#         leng_matrix = len(data_distance)
#         counter_loop = counter+1
#         _data = []
#         while counter_loop < leng_matrix:
#             x = data_distance[counter_loop][0]
#             y = data_distance[0][counter]
#             xy = data_distance[counter_loop][counter]
#             total_xy = x+y-xy
#             print('Total = ',round(total_xy,2))
#             _data.append(round(total_xy,2))
            
#             counter_loop+=1
#         return _data
    
#     def execute_distance(self):
#         starting_point = 1
#         data_distance_matrix = []
#         while starting_point < len(self.distance)-1:
#             data_distance_matrix.append(self.count_distance_customer_dinamic(starting_point))
#             starting_point+=1
#         return data_distance_matrix

    
from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

lat1 = radians(-7.290546436757052)
lon1 = radians(112.77906311590614)
lat2 = radians(-7.284927374085095)
lon2 = radians(112.76159657045771)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance)
print("Should be:", round(distance), "km")