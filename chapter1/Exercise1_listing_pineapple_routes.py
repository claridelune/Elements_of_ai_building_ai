def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    route = [port1]
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

                    print(' '.join([portnames[i] for i in route]))

                    route.pop()
                route.pop()
            route.pop()
        route.pop()

main()
