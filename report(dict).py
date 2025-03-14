def main():
    spacecraft={"name":"James web space telescope"}
    spacecraft.update({"distance":0.01,"orbit":"sun"})
    print(create_report(spacecraft))
def create_report(spacecraft):
    return f'''
    ========== REPORT ================
    Name:{spacecraft.get("name")}
    Distance:{spacecraft.get("distance","Unknown")} AU
    orbit:{spacecraft.get("orbit", "unknown")}
    ==================================
    '''
main()
