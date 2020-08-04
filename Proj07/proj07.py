import csv
import pylab

def open_file(message):
    '''Prompts user for a file, repeats if error occurs.'''
    bool_loop = False
    while bool_loop == False:
       file_str = input(message)
       try: 
                fp = open(file_str,"r")
                return(fp)
                bool_loop = True
              
       except:
                print("File is not found! Try Again!")
    pass

def ip_converter(ip):
    '''takes lists'''
    if '.' in ip:
        ip =  ip.split(".")
        converted_ip = ""
        for element in ip:
            converted_ip += str(element).zfill(3)
        return(converted_ip)
    else:
        return(ip)
  

            
def read_ip_location(file):
    ip_location_list = []
    header = file.readline(3) 
    tuplelist = []
    for line in file:
        line = line.strip().split(",")
        n=0
        for element in line:
            if '.' in element:
                element = ip_converter(element)
                element = int(element)
            tuplelist.append(element)
            n+=1
            
            if n==3:
                tuplelist = tuple(tuplelist)
                ip_location_list.append(tuplelist)
                tuplelist = []
                n=0
                
    return(ip_location_list)
pass

def read_ip_attack(file):
  
    #   2017-09-27-attacks-small.txt
    ip_attack_list = []
    twelvedigit = []
    templine = []
    tuplelist = []
    
    for line in file:
        line = line.strip()
        
        twelvedigit = line
        templine = line
        twelvedigit = ip_converter(twelvedigit)
        twelvedigit = twelvedigit + "000"   
        twelvedigit = int(twelvedigit)
        
        templine = templine + ".xxx"
        tuplelist.append(twelvedigit)
        tuplelist.append(templine)
        tuplelist = tuple(tuplelist)
        ip_attack_list.append(tuplelist)
        tuplelist = []
 
    return(ip_attack_list)
pass


def read_country_name(file):
    country_list= [] 
    temp_list = []
    
    for line in file:
        line = line.strip().split(";")
        temp_list.append(line[1])
        temp_list.append(line[0])
        temp_list = tuple(temp_list)
        country_list.append(temp_list)
        temp_list = []
    return(country_list)   
    pass
    
def locate_address(ip_list, ip_attack):
    for ip in ip_list:
        ip_start = ip[0]
        ip_end = ip[1]
        c_code = ip[2]
        
        if ip_start <= ip_attack <= ip_end:        
            return(c_code)    
    pass

def get_country_name(country_list, code):
    for tup in country_list:
        if code == tup[0]:
            return(tup[1])
    pass

def country_count(count_dict,country_name):
       if country_name in count_dict:
            count_dict[country_name] +=1
       else:
          count_dict[country_name]= 1
       return count_dict
     
    

def bar_plot(count_list, countries):
    pylab.figure(figsize=(10,6))
    pylab.bar(list(range(len(count_list))), count_list, tick_label = countries)
    pylab.title("Countries with highest number of attacks")
    pylab.xlabel("Countries")
    pylab.ylabel("Number of attacks")
    
def main():
    ip_data = []
    attack_data = []
    count_dict = {}
    key_list = []
    count_list = []
    temp_list = [] 
    n=0
    

    
    file = open_file("Enter the filename for the IP Address location list: ")
    ip_data = read_ip_location(file)
  
    file = open_file("Enter the filename for the IP Address attacks: ")
    attack_data = read_ip_attack(file)
    
    file = open_file("Enter the filename for the country codes: ")
    country_data = read_country_name(file)
   
    for attack in attack_data:
        c_code = locate_address(ip_data,attack[0])
        country_name =  get_country_name(country_data,c_code)
        count_dict = country_count(count_dict,c_code)
        print("{:5s}{:18}{:17}{:<12s}".format("The IP Address: ", attack[1]," originated from", country_name))
    print()
    print("Top 10 Attack Countries")
    print("{}{:>7}".format("Country" ,"Count"))
    
 
    #print(count_dict[key])
    for key in sorted(count_dict, key=count_dict.get, reverse=True):
       # if n<10           
            key = key.strip("'")
            temp_list.append(key.strip("'"))
            temp_list.append(count_dict[key])
            temp_list = tuple(temp_list)
            count_list.append(temp_list)
            temp_list = []
           # n+=1
            
    
#    for key in count_dict:
#        keys=count_dict.keys()
#        value = count_dict.
    #count_list = count_list.strip("'")
    print (count_list)
#            
#            try:
#                print(count_list[n],count_list[n+1])
#                if count_list[n] == count_list[n+1]:
#                  print(key_list[n],key_list[n-1])
#                  key_list=(key_list[n:n-1]).sort()
#            except: pass
#            print("{}{:>12}".format(key_list[n-1],count_list[n-1]))
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
          
#    print(count_dict)   
#    count_dict = list(reversed(sorted(count_dict.keys())))  
#   
#    for pair in count_dict:
#        print(pair)
#        temp_list.append(key)
#        temp_list.append(value)
#        final_list.append(tuple(temp_list))
#        temp_list = []
#    print(final_list)
#        
#    answer = input("\nDo you want to plot? ")
#    if answer.lower() == 'yes':
#        bar_plot(count_dict[key],key)
#     #   2017-09-27-attacks-small.txt
# #   dbip-country.csv
 #    country_names.txt
if __name__ == "__main__":
    main()
    
