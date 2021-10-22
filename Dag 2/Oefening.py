##set_a = {1,4,2,8,5,9}
##set_b = {5,6,2,7,3}
##
##in_set_a = 4 in set_a
##print(in_set_a)
##in_set_b = 4 in set_b
##print(in_set_b)
##
### Combineer 'in' met 'not'
##niet_in_set_a = 7 not in set_a
##print(niet_in_set_a)
##niet_in_set_b = 7 not in set_b
##print(niet_in_set_b)
##
##for cijfer in set_a:
##    print(cijfer)
##
##
##b = {'appel', 3, 4.32, (2, 3)}
##
##for x in b:
##    print(x)
##
##a = {1,2}
##a.add(3)
##
##print(a)

##aantal_knikkers = int(input("Aantal knikkers: "))
##
##if aantal_knikkers == 5:
##    print(f"Het aantal knikkers is gelijk aan {aantal_knikkers}" + ", toch?")

##a = input("Geef een waarde (geen 0) ")
##
##try:
##    a = int(a)
##    b = 100 / a
##    print(b)
##except:
##    print("Ik zei nog zo: geen 0")
##finally:
##    print("Bedankt voor het meedoen")

##a = None
##
##while type(a) != type(0):
##
##    a = input("Geef een waarde (geen 0) ")
##
##    try:
##
##        a = int(a)
##
##        b = 100/a
##
##        print(b)
##
##    except ValueError:
##
##        print("en ook niet Smurf")
##
##    except ZeroDivisionError:
##
##        print("Ik zei nog zo: geen 0")
##
##    finally:
##
##        print("Bedankt voor het meedoen")

##while True:
##  dier = input("Voer een dier in, of geef  om af te sluiten: ")
##  if len(dier) == 0:
##    print("Ok, tot ziens")
##    break
##  print("Uw invoer is", len(dier), "lang")

a = input("Geef een waarde (geen 0) ")

try:
  a = int(a)
  b = 100 / a
  print(b)
except:
  print("Ik zei nog zo: geen 0")
finally:
  print("Bedankt voor het meedoen")
