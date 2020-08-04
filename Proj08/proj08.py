import pylab as py

def open_file():
    '''Prompts user for a file, repeats if error occurs.'''
    bool_loop = False
    while bool_loop == False:
      # file_str = input('Enter a file name ')
       
       try: 
                #fp = open(file_str,"r")
                fp = open('storm_track1.txt')
                return(fp)
                bool_loop = True
              
       except:
                print("File is not found! Try Again!")
    pass

def update_dictionary(dictionary, year, hurricane_name, data):
    '''adds new years to the dictionary, adds new hurricanes under correct years, and adds data to correct hurricanes'''

    name_dict = {}
    name_dict[hurricane_name]=data
   
    if year not in dictionary.keys():
        dictionary[year] = name_dict
    else:
       if hurricane_name not in dictionary[year]:
           dictionary[year][hurricane_name]= data
       
       else:
           dictionary[year][hurricane_name] += data
           
    pass
    
def create_dictionary(fp):
    '''pulls relevant information from the file and organizes it into tuples to send to update dictionary'''
    dictionary = {}
    tuple_list = [] 
    
    for line in fp:
        line = line.strip(" ")
        line = line.split()
        year = line[0]
        hurricane_name = line[1]
       
        lat = float(line[3])
        lon = float(line[4])
        date = line[5]
        try:       
            wind = float(line[6])
        except:
            wind = 0
        try:
            pressure = float(line[7])
        except:
            pressure = 0
            
        tuple_list.append(lat) 
        tuple_list.append(lon)
        tuple_list.append(date)
        tuple_list.append(wind)
        tuple_list.append(pressure)
                
        tuple_list = tuple(tuple_list)     
        update_dictionary(dictionary,year,hurricane_name,tuple_list)
        tuple_list = []
    return dictionary
    pass

def display_table(dictionary, year):
    '''Remember to put a docstring here'''
    
    
    print("{:^70s}".format("Peak Wind Speed for the Hurricanes in " + year))
    print("{:15s}{:>15s}{:>20s}{:>15s}".format("Name","Coordinates","Wind Speed (knots)","Date"))
    for i,k in enumerate(name):
         print("{:15s}{:>15s}{:>20s}{:>15s}".format(k,coordinate[i],speed[i],year))
  

def get_years(dictionary):
    '''Remember to put a docstring here'''
    min_year = 5000
    max_year = 0 
    tup = []
    for k in dictionary.keys():
       if int(k) < int(min_year):
           min_year = k
       if int(k) > int(max_year):
           max_year = k
           
    tup.append(min_year)
    tup.append(max_year)
    tup = tuple(tup)
  
    return(tup)

def prepare_plot(dictionary, year):
    '''Remember to put a docstring here'''
    year = str(year)
 
    names = []
    temp_speed = 0 
    max_speed = []
    temp_coords = []
    coordinates = []
    return_tuple = []
    
    for key,value in sorted(dictionary[year].items()):
       names.append(key)
       for x in range(3,len(value),5):
            if temp_speed <= value[x]:
                temp_coords.clear()
                temp_speed = value[x]
                temp_coords.append(value[x-3])
                temp_coords.append(value[x-2])
           
       max_speed.append(temp_speed)
       temp_coords = tuple(temp_coords)
       coordinates.append(temp_coords)
       temp_coords = []
       temp_speed = 0 
            
    return_tuple.append(names)
    return_tuple.append(coordinates)
    
    return_tuple.append(max_speed)
    return_tuple = tuple(return_tuple)
    return return_tuple  
    
    # create everything that is required for plotting
    #return names, coordinates, max_speed
    
def plot_map(year, size, names, coordinates):
    '''Remember to put a docstring here'''
    
    # The the RGB list of the background image
    img = py.imread("world-map.jpg")

    # Set the max values for the latitude and longitude of the map
    max_longitude, max_latitude = 180, 90
    
    # Set the background image on the plot
    py.imshow(img,extent=[-max_longitude,max_longitude,\
                          -max_latitude,max_latitude])
    
    # Set the corners of the map to cover the Atlantic Region
    xshift = (50,190) 
    yshift = (90,30)
    
    # Show the atlantic ocean region
    py.xlim((-max_longitude+xshift[0],max_longitude-xshift[1]))
    py.ylim((-max_latitude+yshift[0],max_latitude-yshift[1]))
	
    # Generate the colormap and select the colors for each hurricane
    cmap = py.get_cmap('gnuplot')
    colors = [cmap(i/size) for i in range(size)]
    
    
    # plot each hurricane's trajectory
    for i,key in enumerate(names):
        print(coordinates[i])
        lat = [ lat for lat,lon in coordinates[i] ]
        lon = [ lon for lat,lon in coordinates[i] ]
        py.plot(lon,lat,color=colors[i],label=key)
    

     # Set the legend at the bottom of the plot
    py.legend(bbox_to_anchor=(0.,-0.5,1.,0.102),loc=0, ncol=3,mode='expand',\
              borderaxespad=0., fontsize=10)
    
    # Set the labels and titles of the plot
    py.xlabel("Longitude (degrees)")
    py.ylabel("Latitude (degrees)")
    py.title("Hurricane Trayectories for {}".format(year))
    py.show() # show the full map


def plot_wind_chart(year,size,names,max_speed):
    '''Remember to put a docstring here'''
    
    # Set the value of the category
    cat_limit = [ [v for i in range(size)] for v in [64,83,96,113,137] ]
    
    
    # Colors for the category plots
    COLORS = ["g","b","y","m","r"]
    
    # Plot the Wind Speed of Hurricane
    for i in range(5):
        py.plot(range(size),cat_limit[i],COLORS[i],label="category-{:d}".format(i+1))
        
    # Set the legend for the categories
    py.legend(bbox_to_anchor=(1.05, 1.),loc=2,\
              borderaxespad=0., fontsize=10)
    
    py.xticks(range(size),names,rotation='vertical') # Set the x-axis to be the names
    py.ylim(0,180) # Set the limit of the wind speed
    
    # Set the axis labels and title
    py.ylabel("Wind Speed (knots)")
    py.xlabel("Hurricane Name")
    py.title("Max Hurricane Wind Speed for {}".format(year))
    py.plot(range(size),max_speed) # plot the wind speed plot
    py.show() # Show the plot
    

def main():
    '''Remember to put a docstring here'''
    dictionary = create_dictionary(open_file())

    min_year = get_years(dictionary)[0]
    max_year = get_years(dictionary)[1]


    print("Hurricane Record Software")
    print("Records from {:4s} to {:4s}".format(min_year, max_year))
    
    year = input("Enter the year to show hurricane data or 'quit': ")
    names, coordinates, max_speed = prepare_plot(dictionary, year)
   
    display_table(dictionary,names,coordinates,max_speed,year)
    
    decision = input("\nDo you want to plot? ")
    size = len(dictionary[year].keys())
   # print(size)
    if decision.lower() != 'quit':
        plot_map(year, size, names, coordinates)
        plot_wind_chart(year, size, names, max_speed)
    else:
        pass
    
    print("Error with the year key! Try another year")
    pass
    
if __name__ == "__main__":
    main()