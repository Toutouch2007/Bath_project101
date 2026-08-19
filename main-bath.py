import time
def bath():
    Time = time.gmtime()
    Dates = ["20/8", "23/8","24/8","25/8","26/8","27/8","30/8","31/8","1/9","2/9","3/9","6/9","7/9","8/9","9/9","10/9","13/9","14/9","15/9","16/9","17/9"]
    Total = len(Dates)
    DayCollected = False
    for i in range(Total):
        if f"{Time.tm_mday}/{Time.tm_mon}" == Dates[i]:
            print(f"You Have {Total -  i -1} Baths Left")
            DayCollected = True
            break
    if not DayCollected:
        print(f"You Have {Total} Baths Left")
    input("Press Enter To Continue...")
    

def main():
    print('Welcome, what do you want to do? \n bath or bath')
    input()
    bath()
    
if __name__ == '__main__':
    main()