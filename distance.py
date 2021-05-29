class Distance():   

    customer = []
    distance = []
    
    def __init__(self,Customer,Distance):
        self.customer = Customer
        self.distance = Distance

    def count_distance_customer_dinamic(self,counter):
        data_distance = self.distance
        leng_matrix = len(data_distance)
        counter_loop = counter+1
        _data = []
        while counter_loop < leng_matrix:
            x = data_distance[counter_loop][0]
            y = data_distance[0][counter]
            xy = data_distance[counter_loop][counter]
            total_xy = x+y-xy
            print('Total = ',round(total_xy,2))
            _data.append(round(total_xy,2))
            
            counter_loop+=1
        return _data
    
    def execute_distance(self):
        starting_point = 1
        data_distance_matrix = []
        while starting_point < len(self.distance)-1:
            data_distance_matrix.append(self.count_distance_customer_dinamic(starting_point))
            starting_point+=1
        return data_distance_matrix

    