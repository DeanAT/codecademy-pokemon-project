# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()



def censor_algo(text):
  learn = "learning algorithms"
  text = text.replace(learn, "*" * len(learn))
  return text

def censor_list(text):
  proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", " her", "herself"]
  for i in proprietary_terms:
    text = text.replace(i.title(), "*" * len(i))
    text = text.replace(i, "*" * len(i))
  return text 

def negative_words(text):
    negative_words = ["concerned", "behind", "danger ", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "concerning", "horrible", "horribly", "questionable"]
    num = 0
    neg_count = []
    proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
    for p in proprietary_terms:
      text = text.replace(p, "*" * len(p))
      text = text.replace(p.title(), "*" * len(p))
    for i in negative_words:
      neg_count.append(0)
    neg_dict = {key:value for key,value in zip(negative_words, neg_count)}
   # print(neg_dict)
    for x in neg_dict.keys():
      num = text.count(x)
      neg_dict[x] = num
      num = 0
    for z,v in neg_dict.items():
      if v >= 2:
        text = text.replace(z, " ***CENSORED*** ")
    return text

def full_censor(text):
  negative_words = ["concerned", "behind", "danger ", "dangerous ", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
  proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her ", "herself"]
  count = 1
  fore_c = 0
  aft_c = 0
  for i in negative_words:
    text = text.replace(i, "*" * len(i))
    text = text.replace(i.title().strip(), "*" * len(i))
    text = text.replace(i.upper(),  "*" * len(i))
  for i in proprietary_terms:
    text = text.replace(i, "*" * len(i))
    text = text.replace(i.title(), "*" * len(i))
    text = text.replace(i.upper(), "*" * len(i))
  text1 = text.split() 
  text2 = text.split()
  while count < len(text2) - 2:
       bool1 = "*" in text2[count]
       fore_c = count + 1
       aft_c = count - 1
       count +=1
       if  bool1 == True:
        text1[aft_c] = "*" * len(i)
        text1[fore_c] = "*" * len(i)
       elif bool1 == False:
         continue
       
  text = " ".join(text1)
  return text



   



ca = censor_algo(email_one)
print(ca, "\n")
cl = censor_list(email_two)
print(cl, "\n")
nw = negative_words(email_three)
print(nw, "\n")
full = full_censor(email_four)
print(full, "\n")


