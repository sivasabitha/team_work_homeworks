'''
Ask first friend the movies they like. Save it in a list
Ask another friend the same question. If the movie is in the first friend's list, 
Print "You both like "name of the movie"
Continue until they is atleast 3 movies they both like
'''
movies_list=[]
#initialise variables
movies = input("What movies you like ?" )
#convert movies into a List
movies_list.append(movies)
commonMoviewCount = 0
common_movie_list=[]
while (True) :
    #ask the second friend for one movie at a time
    movie = input (f"What movies you like (ask to friend)? ")
    #Check if this movie is in the movie list
    if movie in movies_list:
        #if present, 
        commonMoviewCount+=1
    #check if we reached the max
    if(commonMoviewCount >= 3):
        common_movie_list.append(movie)
        break
    else:
        print ("Try again")
    
# list all the common movies
print (f"common movies are : {common_movie_list}") 

'''
output:

What movies you like ?ps
What movies you like (ask to friend)? ps
Try again
What movies you like (ask to friend)? ps
Try again
What movies you like (ask to friend)? ps
common movies are : ['ps']
'''