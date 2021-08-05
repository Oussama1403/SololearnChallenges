in_day = input()
month={"January":"1","February":"2","March":"3","April":"4","May":"5","June":"6","July":"7","August":"8","September":"9","October":"10","November":"11","December":"12"}
#separate month, date and year
in_day = in_day.replace("/", " ")
in_day = in_day.replace(",","")
word_list = in_day.split()

if word_list[0].isalpha():
    mm = month[word_list[0]]
else:
    mm = word_list[0]
dd = word_list[1]
yyyy = word_list[2]
out = "{d}/{m}/{y}".format(d=dd ,m =mm ,y=yyyy)
print(out)
