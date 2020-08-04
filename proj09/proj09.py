#==============================================================================
#Project 9
# Prompts for file. Returns file point.
# Pulls relevant data from file using loops.
# Sends tweets to several functions to find the hashtags
# Calls several functions to organize data by counting the hashtags in a given month
# or by counting hashtags by a given user
# Sends the hashtag counts to another function to check for similarities 
# between user tweets
# Displays data in table format
# Data is sent to function to be graphed and displayed. 
#==============================================================================





import string, calendar, pylab

MONTH_NAMES = [calendar.month_name[month] for month in range(1,13)]

def open_file():
    '''tries to open a file, prompts user again if file is not found'''
    bool_loop = False
    while bool_loop == False:
       file_str = input('Input a filename:')
       
       try: 
                fp = open(file_str,"r")
                #fp = open('smalldata.csv')
                return(fp)
                bool_loop = True
              
       except:
                print(" Error in input filename. Please try again.")
    pass

def validate_hashtag(s):
    '''makes sure the hashtag found is in correct format'''
    for c in s:
        if c in string.punctuation and c != '#':
            #print('post',s)
            return False
        
    if len(s) == 2 and s[1].isdigit():
            #print('post',s)
            return False
    else:
            return True
   
    pass
#
def get_hashtags(s):
    '''finds the hashtag in the tweet and sends it to be validated'''
    hashtags_list = []
    s = s.split(" ")
    for word in s:
        if word != '':
            if word[0]== '#':
                #print('pre',word)
                if validate_hashtag(word) == True:
                    hashtags_list.append(word)
    
    return hashtags_list 
    pass

def read_data(fp):
    '''reads the data from the file and organizes it into a list'''
    data_list = []
    
    for line in fp:
        line = line.split(',')
        username = line[0]
        month = int(line[1])
        tweet = line[2]
        hashtags_list = get_hashtags(tweet)
        data = []
        data.append(username)
        data.append(month)
        data.append(hashtags_list)
       
        data_list.append(data)        
    return(data_list)
    pass


def get_histogram_tag_count_for_users(data,usernames):
    '''counts the hashtags used by a given user'''
    dict_count = {}
    

    for listt in data: 
        if listt[0] in usernames:
            tag = listt[2]
            for i,c in enumerate(tag):
                if c in dict_count:
                    dict_count[c] += 1
                else:
                    dict_count[c] = 1        
                
    #print(dict_count)
    return(dict_count)
    

    
    pass

def get_tags_by_month_for_users(data,usernames):
    '''counts the hashtag used by the user in a given month'''
    empty_set = set()
    key = 0
    month_list = []
    m=0
    temp_list = [] 
    
    for m in range(1,13):
        key = m 
        for listt in data:
            if key == int(listt[1]):
                if listt[0] in usernames:
                    for tag in listt[2]:
                        empty_set.add(tag)
          
        temp_list.append(m)
        temp_list.append(empty_set)
        temp_list = tuple(temp_list)
        
        month_list.append(temp_list)
        
        empty_set = set()
        temp_list = [] 

    return(month_list)
           
    pass

def get_user_names(L):
    '''creates a list of usernames given a set of data'''
    user_name_list = []
    for tup in L:
        if tup[0] not in user_name_list:
            user_name_list.append(tup[0])
    user_name_list = sorted(user_name_list)
    return(user_name_list)

def three_most_common_hashtags_combined(L,usernames):
     '''returns the 3 most common hashtags out of all users'''
     dict_count = {}
     data = L
     most_common_list = []
     num = 0
     tag = ''
     create_tup = []
     
     for listt in data: 
        if listt[0] in usernames:
            tag = listt[2]
            for i,c in enumerate(tag):
                if c in dict_count:
                    dict_count[c] += 1
                else:
                    dict_count[c] = 1
                    

     dict_count = sorted(dict_count.items(), key=lambda x: x[1],reverse = True)
     n = 0 
     for tup in dict_count:
             for k in tup:
                 if n == 2:
                     create_tup.append(num)
                     create_tup.append(tag)
                     create_tup = tuple(create_tup)
                     most_common_list.append(create_tup)
                     create_tup = []
                     n=0
                 if n == 0 :
                         tag = k
                 if n == 1 :
                         num = k 
                    
                 n+=1
                 
     most_common_list = most_common_list[0:3]
     
     return (most_common_list)
  
     pass

def three_most_common_hashtags_individuals(data_lst,usernames):
     '''finds the 3 most common hashtags for all individual users then returns the highest 3'''
     most_common_list = []
     num = 0
     tag = ''
     create_tup = []
     count = 0
     
     n = 0 
     for name in usernames:   
         num = get_histogram_tag_count_for_users(data_lst,name)
         num = sorted(num.items(), key=lambda x: x[1],reverse = True)
         for tup in num:
             for element in tup:
                 if n ==2:
                     create_tup.append(count)
                     create_tup.append(tag)
                     create_tup.append(name)
                     create_tup = tuple(create_tup)
                     most_common_list.append(create_tup)
                     create_tup=[]
                     n = 0 
                 if n % 2 == 0:
                     tag = element
                 if n % 2 != 0:
                     count = element
                 n+=1
     
     most_common_list = sorted(most_common_list, reverse = True)
     most_common_list = most_common_list[0:3]
     
     return(most_common_list)
 
     pass
            
def similarity(data_lst,user1,user2):
    '''counts the similar hashtags used between users for each month'''
    data = data_lst
    tup_list = []
    sim_list = []
    
    
    
    user1_month = get_tags_by_month_for_users(data,[user1])
    user2_month = get_tags_by_month_for_users(data,[user2])   

    for n in range(0,len(user1_month)):
        intersection = user1_month[n][1].intersection(user2_month[n][1])
       # print('intersection:',intersection)
        tup_list.append(n+1)
        tup_list.append(intersection)
        tup_list = tuple(tup_list)
        sim_list.append(tup_list)
        tup_list = []
        
  
    #print(sim_list)
       # xxx

#twitterdata.csv
#
#xxx
#
#xxx, yyy
#
#WKARnewsroom,             michiganstateu
#
#no
   
    

    return(sim_list)

    
    pass
        
def plot_similarity(x_list,y_list,name1,name2):
    '''Plot y vs. x with name1 and name2 in the title.'''
    
    pylab.plot(x_list,y_list)
    pylab.xticks(x_list,MONTH_NAMES,rotation=45,ha='right')
    pylab.ylabel('Hashtag Similarity')
    pylab.title('Twitter Similarity Between '+name1+' and '+name2)
    pylab.tight_layout()
    pylab.show()
    # the next line is simply to illustrate how to save the plot
    # leave it commented out in the version you submit
    #pylab.savefig("plot.png")


def main():
    data_list = []
    usernames = []
    usernames_str = '' 
    y_list = []
    
    fp = open_file()
    data_list = read_data(fp)
    usernames = get_user_names(data_list)
    tag_count_dict = get_histogram_tag_count_for_users(data_list,usernames)
    tag_month =  get_tags_by_month_for_users(data_list,usernames)
    most_common_combined = three_most_common_hashtags_combined(data_list,usernames)
    most_common_individual = three_most_common_hashtags_individuals(data_list,usernames)
    similarity_list = similarity(data_list,usernames[0],usernames[1])
    
  
   
          

    print("Top Three Hashtags Combined")
    print("{:>6s} {:<20s}".format("Count","Hashtag"))
    for element in most_common_combined:
      print("{:>6} {:<20}".format(element[0],element[1]))
    print()
    
    print("Top Three Hashtags by Individual")
    print("{:>6s} {:<20s} {:<20s}".format("Count","Hashtag","User"))
    for element in most_common_individual:
      print("{:>6} {:<20} {:<20s}".format(element[0],element[1],element[2]))

    print()
        
    usernames_str = ', '.join(usernames)
    print("Usernames: ", usernames_str)
 


    while True:  # prompt for and validate user names
        user_str = input("Input two user names from the list, comma separated: ")
        
        user_str = user_str.replace(" ",'')       
     #   print(user_str)
        try:
            user_str = user_str.split(',')    
            username1 = user_str[0]
            username2 = user_str[1]
        except:
            pass
            
        if username1 in usernames_str and username2 in usernames_str:
                       
            break
        else:
             print("Error in user names.  Please try again")
   
    
    similarity_list = similarity(data_list,username1,username2)
    print()
    print("Similarities for "+username1+" and "+username2)
    print("{:12}{:2}".format("Month","Count"))
   
    for tup in similarity_list:
            count = 0 
            n = tup[0]
               
            for tag in tup[1]:
                count +=1
            y_list.append(count)
            print("{:10}{:3}".format(MONTH_NAMES[n-1],count))
 
    print()
    
    # Prompt for a plot
    choice = input("Do you want to plot (yes/no)?: ")
    if choice.lower() == 'yes':
        
        x_list = [1,2,3,4,5,6,7,8,9,10,11,12]
        plot_similarity(x_list,y_list,username1,username2)

if __name__ == '__main__':
    main()