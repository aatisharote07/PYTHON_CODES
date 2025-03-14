
distances={
    "voyager 1":163,
    "voyager 2":136,
    "pioneer 10":80,
    "New horizon":58,
    "pioneer 11":44
}

def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")
    
def convert(au):
    return au *149597870700
    
main()    