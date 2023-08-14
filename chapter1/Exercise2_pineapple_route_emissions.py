def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    # Nautical miles converted to km
    D = [
            [0, 8943, 8019, 3652, 10545],
            [8943, 0, 2619, 6317, 2078],
            [8019, 2619, 0, 5836, 4939],
            [3652, 6317, 5836, 0, 7825],
            [10545, 2078, 4939, 7825, 0]
        ]

    # Assume 20g per km per metric ton (of pineapples)
    co2 = 0.020

    # Initial route
    route = [0]
    
    for port2 in range(1, 5):
        route.append(port2)
        for port3 in range(1, 5):
            if port3 in route:
                continue
            route.append(port3)
            for port4 in range(1, 5):
                if port4 in route:
                    continue
                route.append(port4)
                for port5 in range(1, 5):
                    if port5 in route:
                        continue
                    route.append(port5)

                    # Calculate distance and emissions for the route
                    distance = D[route[0]][route[1]] + D[route[1]][route[2]] + D[route[2]][route[3]] + D[route[3]][route[4]]
                    emissions = distance * co2
                    print(' '.join([portnames[i] for i in route]) + " %.1f kg" % emissions)

                    route.pop()  # Remove port5
                route.pop()  # Remove port4
            route.pop()  # Remove port3
        route.pop()  # Remove port2

main()
