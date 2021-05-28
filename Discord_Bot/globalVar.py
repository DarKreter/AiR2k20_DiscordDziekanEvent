quizStages = 5
quizAnswers = 4

wybieraczRoliMessageID = 758457353959505941 #Do zmiany (nie trzeba chyba)
wybieraczRoliChannelID = 758436604955328532 #Do zmiany
wybieraczRoliEmojiName = "📧"               #Do zmiany

instrukcjaMessageID = 847561432194351144
instrukcjaChannelID = 847561311918620692
instrukcjaEmojiAccept = ":PepoG:758293943912759336" 
instrukcjaEmojiResign = ":PepoExit:823811310005125130" 
instrukcjaEmojiAName = "PepoG" 
instrukcjaEmojiRName = "PepoExit" 

pytanieMessageID = [847562146954739742, 847562443340120124, 847563640499470347, 847564003844423762, 847563709114351646]
pytanieChannelID = [847561949348757544, 847562314165125180, 847562590795857933, 847562631275085834, 847563247534997564]
 
# gratulacjeMessageID = 804056526611677234 
# gratulacjeChannelID = 803992529401413662 
# gratulacjeEmojiName = "🍺"


# loseChannelID           = 804052256873906267 
# loseMessageContent      = "Kocham piwo!" 


# wybieraczRoliRoleToAddName = "DZIEKAN IMPOSTOR?"



# Rola do zaczęcia eventu
wybieraczRoliRole = "List wstęp"
# Rola do wstępu
tresc1 = "Zacznij mail"
# Rola do rezygnacji
resign = "2/10"

# Reakcje pod pytaniami
reactionsEmojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣']

przelicznikOdpowiedzi = [ [1, 2, -1, -4], [2, 0, 1, -1], [0, -69, -1, 2], [2, 1, -2, -1], [-1, 2, 1, -2] ]
przelicznikOdpowiedziCichockiego = [ [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0]]

zlozonyMail = [ ["Dzień dobry\n\n", "Szanowny panie profesorze\n\n", "Witam\n\n", ""],
["Piszę w sprawie potencjalnie błędnej punktacji mojej pracy.\n", "Chciałbym zgłosić reklamację mojego wyniku z wczorajszej kartkówki.\n", "Chciałbym zapytać o kryteria oceniania kolokwium.\n", "Moim zdaniem źle Pan ocenił kartkówkę.\n"],
["Ponieważ przeliczyłem przed chwilą ten sam przykład i jestem pewny, że rozwiązałem go prawidłowo.\n", "Podczas kolokwium kontaktowałem się z studentem z wydziału matematyki i nie ma szans, że wynik jest błędny.\n", "Sprawdziłem ten przykład w kalkulatorze wolframAlpha i uzyskany wynik był identyczny do tego który otrzymałem.\n", "Spróbowałem przeliczyć ten sam przykład kilka razy i otrzymałem ten sam wynik.\n"],
["Chciałbym prosić o ponownie przejrzenie mojej pracy przez Pana Profesora.\n\n", "Czy moglibyśmy umówić się na konsultacje, ponieważ nie jestem w stanie znaleźć błędów w moim rozumowaniu.\n\n", "Uważam, że ocena 2/10 jest nieadekwatna do pracy którą Panu przesłałem.\n\n", "Czy mógłby Pan sprawdzić moją prace ponownie?\n\n"],
["Pozdrawiam\n", "Z wyrazami szacunku\n", "Z poważaniem\n", "Miłego wieczoru\n"] 
]

finishRoleListWithWeight = [    
                    (10, 7, "Ważniak🤓"),             #
                    (7,-4, "🍺Student Debil🍺"),       #
                    (-4,-11, "Zjeb🤡"),
                    ( -20,   -80,"⛔skreślony z listy⛔"), # 3 pytanie 2 odpowiedz

                    (69, 69, "2/10"),                # wychodzi na początku
                    (-696, -1000, "Marcin Cichocki👑"),   # 13 22 31 43 51
]

# Zbanowane role, które nie biorą udziału w quizie
bannedRoles = [x[2] for x in finishRoleListWithWeight]