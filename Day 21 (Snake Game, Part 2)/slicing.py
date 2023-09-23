piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[2:5])
#think of the commas as points of slicing

piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[:5])
#slices all keys up to position 5, removing all the ones after

piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[2:5:2])
#this removes everything at up to position 2, keeps position 2, anything between 2 and 5, 
# keeps 5, then removes the next 2 positions

piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[-1])
#this saves the last item in the list, and removes everything else. 

piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[1:])
#removes the 1st item, keeps the rest. 
