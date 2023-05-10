import spacy

nlp = spacy.load('en_core_web_md')
# Some section from wikipedia: https://en.wikipedia.org/wiki/Red_Bull_Racing_RB18
doc = nlp("The Red Bull Racing RB18 is a Formula One car designed and constructed by Red Bull Racing which competed in the 2022 Formula One World Championship. The RB18 was driven by defending world champion Max Verstappen and Sergio Pérez. Verstappen secured his second consecutive Drivers' Championship driving the RB18 and Red Bull secured their fifth Constructors' Championship, their first since 2013. The RB18 is Adrian Newey's most successful F1 design to date and one of the most dominant Formula One cars ever built.")
query = nlp("Who was the defending champion in 2022")

print(doc.similarity(query))  # 0.786756001899998
