#==============================================================================
# This program takes water usage data from the united states in 2010 and 
# outputs the population of the county, total water used in the county, and
# average water used per person, when given a state. The user then has a choice
# to have the usage displayed in a pie chart if desired. 
#==============================================================================

import pylab
STATES = {'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY'}
USERS = ["Public", "Domestic", "Industrial", "Irrigation","Livestock"]
def open_file():
    '''Prompts user for a file, repeats if error occurs.'''
    file_str = input("Input a file name: ")
    while
        try: 
          
            fp = open(file_str,"r")
            return fp
        except:
            print("Unable to open file. Please try again.")
            return open_file()
    pass
    
def read_file(fp):
    '''traverses the file and returns a list of the relevant information'''
    data_list = []
    header = fp.readline()
    for line in fp:
        line_list =  line.strip().split(',')
        try:
            state = line_list[0] 
            county = line_list[2]
            population = float(line_list[6]) * 1000
            fresh_water = float(line_list[114])
            salt_water = float(line_list[115])
            public = float(line_list[18])
            domestic = float(line_list[26])
            industrial = float(line_list[35])
            irrigation = float(line_list[45])
            livestock = float(line_list[59])
        except:
            pass
             
        tup = (state, county, population, fresh_water, salt_water, 
               public, domestic, industrial, irrigation, livestock)
        data_list.append(tup)
    return data_list
    
def compute_usage(state_list):
    '''calculates total water used in the county and average use per person'''
    tot_water =0
    per_person_water =0
    templist = []
    county_list=[] 
    
    for tup in state_list:
        tot_water =  tup[3]+tup[4]
        per_person_water = tup[3] / tup[2] 
        templist.append(tup[1])
        templist.append(tup[2])
        templist.append(tot_water)
        templist.append(per_person_water)
        templist = tuple(templist)
        county_list.append(templist)
        templist=[]
    return(county_list)
    pass
        
    
def extract_data(data_list, state):
    '''pulls out all the data to a specific state, or entire data set'''
    ''' returns an empty string if state code was no found in data'''
    extract_datalist = []
    for tup in data_list:    
        if state == tup[0]:
            extract_datalist.append(tup)
        elif state== 'ALL':
            extract_datalist.append(tup)
        elif state =='QUIT':
            return(extract_datalist)
    return(extract_datalist)
          

def display_data(state_list, state):
    '''prints out title and column names, formats data contained in state_list''' 
    county_list = compute_usage(state_list)   
    title = "{:^88s}".format ("Water Usage in " + state + " for 2010")
    header = "{:22s} {:>22s} {:>22s} {:>22s}".format("County", \
    "Population", "Total (Mgal/day)", "Per Person (Mgal/person)")
    print()
    print(title)
    print(header)
    for county in county_list:
        name = county[0]
        str(name)
        name = name.rstrip('0')
        population = county[1]
        tot_water_county = county[2]
        tot_water_p_person = county[3]
        d_format = "{:22s} {:>22,.00f} {:>22.02f} {:>22.04f}".format(name,population,tot_water_county,tot_water_p_person)
        print(d_format)
    print()
    return(title)       
        
def plot_water_usage(some_list, plt_title):
    '''
        Creates a list "y" containing the water usage in Mgal/d of all counties.
        Y should have a length of 5. The list "y" is used to create a pie chart
        displaying the water distribution of the five groups.

        This function is provided by the project.
    '''
    # accumulate public, domestic, industrial, irrigation, and livestock data
    y =[ 0,0,0,0,0 ]

    for item in some_list:

        y[0] += item[5]
        y[1] += item[6]
        y[2] += item[7]
        y[3] += item[8]
        y[4] += item[9]

    total = sum(y)
    y = [round(x/total * 100,2) for x in y] # computes the percentages.

    color_list = ['b','g','r','c','m']
    pylab.title(plt_title)
    pylab.pie(y,labels=USERS,colors=color_list)
    pylab.show()
    #pylab.savefig("plot.png")  # uncomment to save plot to a file
    
def main():
   print("Water Usage Data from the US and its States and Territories.\n")
   state_list=[]
   fp = open_file()
   print()
   data_list = read_file(fp)
   state_input = ""
   while state_input!= 'QUIT':
       state_input = input("Enter state code or 'all' or 'quit':")   
       print()
       state_input = state_input.upper()
       if state_input == "QUIT":
           break
       state_list = extract_data(data_list, state_input)
       if state_list ==[]:
               print("Error in state code.  Please try again.\n")
       else:
           title = display_data(state_list,state_input)           
           bool_input = input("Do you want to plot?\n")
           print()
           bool_input = bool_input.upper()
           if bool_input == "YES":
               print()
               plot_water_usage(state_list,title)
           else:
               pass
   pass

if __name__ == "__main__":
    main()