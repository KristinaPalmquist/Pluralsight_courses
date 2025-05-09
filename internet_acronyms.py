acronyms = {
    'LOL': 'laugh out loud',
    'IDK': "i don't know",
    'TBH': 'to be honest',
}

acronyms['SMH'] = 'shaking my head'
acronyms['BFN'] = 'bye for now'
acronyms['IMHO'] = 'in my humble opinion'
acronyms['BTW'] = 'by the way'
acronyms['IIRC'] = 'if i recall correctly'
acronyms['IDK'] = "I don't know"

# del acronyms['IMHO']


for key in acronyms:
    print(key, '-', acronyms[key])
# print(acronyms.get('LOL')) # to avoid crashing the program if no match
# definition = acronyms.get('IDK')
# if definition:
#     print(definition)
# else:
#     print("Key doesn't exist")
    
# sentence = 'IDK', ' what happened ', 'TBH'
# new_sentence = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')
# new_sentence = ''
# for word in sentence:
#     definition = acronyms.get(word)
#     if definition:
#         new_sentence += definition
#         continue
#     new_sentence += word
            
# print(new_sentence)

# word = 'BFN'

# if word in acronyms:
#     print('Word is in the list')
# else:
#     print('The sword is not in the list ' +  word)
    
# for acr in acronyms:
#     print(acr)
    



