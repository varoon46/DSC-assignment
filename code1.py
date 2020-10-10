Thriller=["Dark","mindhunter","parasite","inception","insidious","kahaani","prison break","money heist","war","Jack Ryan"]
Comedy=["Friends","3 idiots","golmaal","Brooklyn 99","How i met your mother","rick and morty","The big bang theory","The office","Space Force"]
film=input()
film=film.lower()
Thriller=map(str.lower,Thriller)
Comedy=map(str.lower,Comedy)
if film in Thriller:
  print("It's a Thriller")
elif film in Comedy:
  print("It's a Comedy")
else:
  print("It's neither Comedy nor Thriller")
