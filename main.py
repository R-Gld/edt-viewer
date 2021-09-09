import requests
from ics import Calendar


def main():
    url = "https://sedna.univ-fcomte.fr/jsp/custom/ufc/cal.jsp?data=6a71cce2832312288f83bef9a258de069a574610c6c4a3fe5" \
          "9c1187cf28b1313692613b21192e5f0e0b7c5a5601c933db9e64e383fb75a376c817b9ec1a742a7e0699745d798fcad67d7f8ffdc1" \
          "73ecb29ecbbae75627a1e7d25d946b10dc628,1"
    c = Calendar(requests.get(url).text)

    for i in list(c.timeline.today()):
        start = str(i.begin)
        end = str(i.end)
        print(f"Cours: '{i.name}'\n\t-> Début {getHourAndMinute(start)}\n\t-> Fin {getHourAndMinute(end)}"
              f"\n\t-> Salle: {i.location[2:]}\n\t-> Durée: {str(i.duration)[:-3]}")


def getHourAndMinute(time):
    hours = int(time[11:-12]) + 2
    minute = time[14:-9]
    return "{}:{}".format(hours, minute)


if __name__ == '__main__':

    launch = True
    while launch:
        cmd = str(input("\t> "))
        if cmd == "quit":
            launch = False
            quit()
        elif cmd == "help":
            print("--==={ Help }===--")
            print("quit - Exit the program.")
            print("today - Give the edt for today.")
            print("week - Give the edt for the week. INDEV")
            print("semester - Give the edt for the semester. INDEV")
            print("--==={ Help }===--")
        elif cmd == "today":
            main()
        elif cmd == "week" or cmd == "semester":
            print("This function is in dev.")

    print("Goodbye. :)")
