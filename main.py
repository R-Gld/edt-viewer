import requests
from ics import Calendar


def main():
    url = "https://sedna.univ-fcomte.fr/jsp/custom/ufc/cal.jsp?data=950afc9111df47b15220b59c9ebb60bc9a574610c6c4a3fe59c1187cf28b1313692613b21192e5f0e0b7c5a5601c933db9e64e383fb75a376c817b9ec1a742a7e0699745d798fcad67d7f8ffdc173ecb29ecbbae75627a1e7d25d946b10dc628,1"
    c = Calendar(requests.get(url).text)

    for i in list(c.timeline.today()):
        start = str(i.begin)
        end = str(i.end)
        t = "Cours: '{}'\n\t-> Début {}\n\t-> Fin {}\n\t-> Salle: {}".format(i.name, getHourAndMinute(start),
                                                                             getHourAndMinute(end), i.location[2:])
        print(t)


def getHourAndMinute(time):
    hours = int(time[11:-12]) + 2
    minute = time[14:-9]
    return "{}:{}".format(hours, minute)


if __name__ == '__main__':
    main()
