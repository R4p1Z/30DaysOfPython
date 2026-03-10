print("This is falsely comparison as python and dragon doesn't have the same length.",len('python') != len('dragon'))

print('On is found in both python and dragon:', 'on' in 'python', 'and', 'on' in 'dragon')

print('The word jargon is in the sentence "I hope this course is not full of jargon." is', 'jargon' in 'I hope this course is not full of jargon.')

print('There is no "on" in both the word dragon and python?', 'on' not in "dragon", 'and', 'on' not in "python")

word_length = len('python')
int_float = int(word_length)
float_str = str(int_float)
print(type(float_str))