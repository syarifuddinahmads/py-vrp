# ini class untuk menampung data customer, depot , membentuk model jarak
class DataModel():

    def customer_data_model(self):
        customer = [
            ('Richa', 55),
            ('Calvin', 50),
            ('Yono', 50),
            ('Tutik', 55),
            ('Febri', 70),
            ('Zahwa', 45),
            ('Cipto', 60),
            ('Eko', 60),
            ('Khamimah', 40),
            ('Mamik', 35),
        ]
        return customer

    def create_distance_data_model(self):
        distance_matrix = [
            [0, 8.3, 10.2, 6.5, 6.6, 7.1, 7.7, 5.8, 6.0, 5.7, 8.1],
            [8.3, 0, 6.8, 7.2, 5.9, 8.8, 9.0, 4.4, 7.9, 9.1, 5.5],
            [10.2, 6.8, 0, 7.8, 6.1, 3.2, 8.0, 5.1, 10.0, 7.3, 4.5],
            [6.5, 7.2, 7.8, 0, 5.6, 4.7, 6.7, 7.0, 6.9, 6.8, 9.9],
            [6.6, 5.9, 6.1, 5.6, 0, 8.9, 6.2, 0.3, 8.2, 3.8, 5.3],
            [7.1, 8.8, 3.2, 4.7, 8.9, 0, 7.5, 4.8, 3.9, 4.1, 6.4],
            [7.7, 9.0, 8.0, 6.7, 6.2, 7.5, 0, 5.4, 6.5, 9.5, 7.4],
            [5.8, 4.4, 5.1, 7.0, 10.3, 4.8, 5.4, 0, 6.3, 4.6, 8.5],
            [6.0, 7.9, 10.0, 6.9, 8.2, 3.9, 6.5, 6.3, 0, 8.4, 11.0],
            [5.7, 9.1, 7.3, 6.8, 3.8, 4.1, 9.5, 4.6, 8.4, 0, 7.6],
            [8.1, 5.5, 4.5, 9.9, 5.3, 6.4, 7.4, 8.5, 11.0, 7.6, 0],
        ]
        return distance_matrix


# ini class untuk menghitung jarak dari depot ke customer
class Distance():

    customer = []
    distance = []
    depot = 0

    def __init__(self, Customer, Distance):
        self.customer = Customer
        self.distance = Distance

    def count_distance_customer_dinamic(self, counter):
        data_distance = self.distance
        leng_matrix = len(data_distance)
        counter_loop = counter+1
        _data = []
        while counter_loop < leng_matrix:
            x = data_distance[counter_loop][0]
            y = data_distance[0][counter]
            xy = data_distance[counter_loop][counter]
            total_xy = x+y-xy
            _data.append(round(total_xy, 2))

            counter_loop += 1
        return _data

    def execute_distance(self):
        starting_point = 1
        data_distance_matrix = []
        while starting_point < len(self.distance)-1:
            data_distance_matrix.append(
                self.count_distance_customer_dinamic(starting_point))
            starting_point += 1

        for i in data_distance_matrix:
            for j in range(len(self.customer)-len(i)):
                i.insert(j, 0)

        return data_distance_matrix

# ini class untuk membangun rute terbaik berdasarkan jarak dan kapasitas


class Rute:

    customer = []
    distance = []

    def __init__(self, Customer, Distance):
        self.customer = Customer
        self.distance = Distance

    def create_node(self):

        temp_distance = []
        for i in self.distance:
            for j in i:
                if j != 0:
                    temp_distance.append(j)
        temp_distance.sort(reverse=True)
        # print('Temp Distance = ', temp_distance)

        
        counter = 0
        temp_node = []
        while counter < len(temp_distance):
            max_distance = temp_distance[counter]
            for index, k in enumerate(self.distance):
                if max_distance in k:
                    # print('Row = ', (index+1), ' Column = ',
                    #       (k.index(max_distance)+1))
                    node_one = (index+1)
                    node_two = (k.index(max_distance)+1)
                    if len(temp_node) == 0:
                        temp_node.extend([node_one, node_two])
                    else:
                        # if node_one in temp_node:
                        #     print('Node = ', node_one,
                        #           ' Sudah ada di ', temp_node)
                        # else:
                        #     temp_node.append(node_one)

                        if node_one not in temp_node:
                            temp_node.append(node_one)

                        # if node_two in temp_node:
                        #     print('Node = ', node_two,' Sudah ada di ', temp_node)
                        # else:
                        #     temp_node.append(node_two)

                        if node_two not in temp_node:
                            temp_node.append(node_two)

                        # if node_one and node_two in temp_node:
                        #     print('Kedua node sudah ada di ', temp_node)
                        # else:
                        #     # print('Kedua node belum ada di ', temp_node)
                        #     temp_node.extend([node_one, node_two])
                        if node_one and node_two not in temp_node:
                            temp_node.extend([node_one, node_two])

            counter += 1

        return temp_node

    def create_rute(self, index):
        node = self.create_node()
        # rute = []
        max_capacity = 225
        order_capacity = 0
        temp_node = []

        # while counter < len(node):
        #     # order_capacity += self.customer[node[counter]-1][1]
        #     # print('Order Capacity = ',order_capacity)
        #     # temp_rute.append(node[counter])
        #     # print('Temp Rute = ',temp_rute)
        #     # counter+=1
        #     temp_node = []
        #     for i in node:
        #         order_capacity += self.customer[i-1][1]
        #         if order_capacity <= max_capacity:
        #             temp_node.append(i)
        #         else:
        #             rute.append(temp_node)
        #             counter += 1

        # print('Index start loop',index)
        # temp_node = []
        # for i in node[index:len(node)]:
        #     order_capacity += self.customer[i-1][1]
        #     print('Order capacity = ',order_capacity)
        #     if order_capacity > max_capacity:
        #         rute.append(temp_node)
        #         self.create_rute(node.index(i))
        #     else:
        #         temp_node.append(i)

        # for i in node[0:4]:
        #     order_capacity += self.customer[i-1][1]
        #     print('Order capacity = ',order_capacity)
        #     print('I = ',i)

        # counter = index
        # temp_node = []
        # while counter < len(node):
        #     order_capacity += self.customer[counter][1]
        #     print('Customer = ',self.customer[counter][0],'Order Customer = ',self.customer[counter][1])
        #     print('Order capacity = ',order_capacity)
        #     if order_capacity > max_capacity:
        #         rute.append(temp_node)
        #         temp_node = []
        #         self.create_rute(counter+1)
        #         counter+=1
        #     else:
        #         temp_node.append(node[counter])
        #     counter+=1

        # temp_node = []
        # for i in range(index,len(node)):
        #     order_capacity += self.customer[i-1][1]
        #     print('Order capacity = ',order_capacity)
        #     if order_capacity > max_capacity:
        #         rute.append(temp_node)
        #         self.create_rute(node.index(i))
        #     else:
        #         temp_node.append(i)
        
        # for i in node[0:4]:
        #     print('Node ',i,' Index ',node.index(i))

        # print('=================')
        
        # for i in node[4:8]:
        #     print('Node ',i,' Index ',node.index(i))

        # print('=================')
        
        # for i in node[8:len(node)]:
        #     print('Node ',i,' Index ',node.index(i))
        
        # print('=================')
        
        # for i in node[0:len(node)]:
        #     print('Node ',i,' Index ',node.index(i))
        # order_capacity = 0
        # for i in node[index:len(node)]:
        #     print('Node ',i,' Index ',node.index(i))
        #     order_capacity += self.customer[node.index(i)][1]
        #     print('Order capacity = ',order_capacity)
        #     if order_capacity <= max_capacity:
        #         temp_node.append(i)
        #     else:
        #         rute.append(temp_node)
        #         self.create_rute(node.index(i),indexrute+1)
 
        
                
        return temp_node



    
    


data = DataModel()
distance = Distance(data.customer_data_model(),
                    data.create_distance_data_model())
rute = Rute(data.customer_data_model(), distance.execute_distance())
print("Rute = ", rute.create_rute(0))
