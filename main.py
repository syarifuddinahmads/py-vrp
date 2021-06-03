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
    rute = []

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

        counter = 0
        temp_node = []
        while counter < len(temp_distance):
            max_distance = temp_distance[counter]
            for index, k in enumerate(self.distance):
                if max_distance in k:
                    node_one = (index+1)
                    node_two = (k.index(max_distance)+1)
                    if len(temp_node) == 0:
                        temp_node.extend([node_one, node_two])
                    else:

                        if node_one not in temp_node:
                            temp_node.append(node_one)

                        if node_two not in temp_node:
                            temp_node.append(node_two)

                        if node_one and node_two not in temp_node:
                            temp_node.extend([node_one, node_two])

            counter += 1

        return temp_node

    def create_rute(self, index):
        node = self.create_node()
        max_capacity = 225
        order_capacity = 0
        temp_node = []

        for i in node[index:len(node)]:
            order_capacity += self.customer[i-1][1]
            if order_capacity >= max_capacity:
                self.rute.append(temp_node)
                self.create_rute(node.index(i))
                break
            else:
                temp_node.append(i)

            if node.index(i) == (len(node)-1):
                self.rute.append(temp_node)
                break

        return self.rute
    
    def nearest_insert(self):
        return True

    def nearest_neighbor(self):
        return True


data = DataModel()
distance = Distance(data.customer_data_model(),
                    data.create_distance_data_model())
rute = Rute(data.customer_data_model(), distance.execute_distance())
print("Rute = ", rute.create_rute(0))
