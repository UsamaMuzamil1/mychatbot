import re
import long_responses as long

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True


    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1


    # calculate the percent of recognized words in a user message
    percentage = float(message_certainty) / float(len(recognized_words))

    # Check that the required words are in a string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
         return int(percentage*100)
    else:
        return 0



def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Response --------------------------------------------------------
    response('Welcome to TPL Insurance. Please select your option to proceed.', ['hi', 'hello', 'hi'], single_response=True)
    response('Please select the item you wish to insure. 1:auto insurance, 2:travel insurance, 3:home insurance', ['buy', 'insurance'], required_words=['buy'])
    response('Option1: Visit our website to purchase the policy. Option2: Download our app to purchase the policy Option3: Talk to our representative.', ['auto', 'insurance', 'travel', 'insurance', 'home', 'insurance'], single_response=True)
    response('https://tplinsurance.com', ['option1'], single_response=True)
    response('https://tplinsurance.com/mobile-app', ['option2'], single_response=True)
    response('021 111 000 301', ['option3'], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)

    return best_match



def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

 # Testing the response system

while True:
    print('Bot: ' + get_response(input('You: ')))
