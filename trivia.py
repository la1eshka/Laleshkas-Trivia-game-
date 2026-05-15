
if __name__ == '__main__':
    print('welcome to laleshka\'s trivia game')

    score = 0

    response = input('What is the largest bird on earth? ')
    if response.lower() == 'ostrich':
        score += 1
        print('correct!')
    else:
        print('incorrect ...')
    
    response = input('What is the capital of the United States?')
    if response.lower() == 'washington dc':
        score += 1 
        print('correct')
    else : 
        print('incorrect')

    response = input('On which continent would you find the largest desert?')
    if response.lower() == "antartica":
        score += 1
        print('correct')
    else : 
        print('incorrect')
    
    response = input('How many bones does a shark have?')
    if response.lower() == "0":
        score += 1 
        print('correct')
    else : 
        print('incorrect')
    
    response = input('Which is the only human body part that is fully grown from the moment you are born?')
    if response.lower() == "eyes":
        score += 1 
        print('correct')
    else : 
        print('incorrect')
    
    response = input('What is the hottest planet in our solar system?')
    if response.lower() == "venus":
        score += 1 
        print('correct')
    else : 
        print('incorrect')
    
    response = input('Which musical instrument has 88 keys?')
    if response.lower() == "piano":
        score += 1 
        print('correct')
    else : 
        print('incorrect')
    
    response = input('Which ocean is the largest?')
    if response.lower() == "pacific ocean":
        score += 1 
        print('correct')
    else : 
        print('incorrect')
    
    response = input('How many bones are in an adult human body?')
    if response.lower() == "206":
        score += 1 
        print('correct')
    else : 
        print('incorrect')

    response = input('In which year did World War II end?')
    if response.lower() == "1945":
        score += 1 
        print('correct')
    else : 
        print('incorrect')

    print(f'congratulations you scored {score}!')
    
    