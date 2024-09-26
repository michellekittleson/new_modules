# Task 1: Your Mood Today

import mood_responses

mood = input("How are you feeling today? (happy/sad/excited) ").lower()
print(mood_responses.mood_response(mood))