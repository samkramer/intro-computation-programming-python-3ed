# 5.7 Dictionaries
# Figure 5-9: Translating text (badly)

EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je',
    'eat':'mange', 'drink':'bois', 'John':'Jean',
    'friends':'amis', 'and':'et', 'of':'du', 'red':'rouge'}
FtoE = {'pain': 'bread', 'vin': 'wine', 'avec': 'with', 'Je': 'I',
    'mange': 'eat', 'bois': 'drink', 'Jean': 'John',
    'amis': 'friends', 'et': 'and', 'du': 'of', 'rouge': 'red'}
dicts = {'English to French':EtoF, 'French to English':FtoE}

def translate_word(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    return '"' + word + '"'

def translate(phrase, lang_dict):
    UC_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LC_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UC_letters + LC_letters
    punctuation = '.,;:?'
    
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        elif word != '':
            if c in punctuation:
                c = c + ' '
            translation = (translation +
                           translate_word(word, lang_dict) + c)
            word = ''
    return translation

if __name__ == "__main__":
    print(translate('I drink good red wine, and eat bread.',
                    dicts['English to French']))
    print(translate('Je bois du vin rouge.',
                    dicts['French to English']))
    