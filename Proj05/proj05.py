#==============================================================================
# This Program opens a file containing data for the advertisements of a product
# and analyzes the most effective advertisement in terms of the best rate of 
# return, and the advertisement that lead to the most sales.
# #==============================================================================
def open_file():
    filename = input("Input a file name: ")
    datafile = open(filename,"r")
    return datafile
    pass
    
def revenue(num_sales, sale_price):
    num_sales =int(num_sales)
    sale_price = float(sale_price)
    revenue = num_sales * sale_price
    return revenue
    pass

def cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost):
    goods_sold = (num_ads * ad_price) + (num_sales * production_cost)
    return goods_sold
    pass

def calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost):
    good_sold = cost_of_goods_sold(num_ads,ad_price,num_sales,production_cost)
    rev = revenue(num_sales,sale_price)
    ROI = (rev-good_sold )/ good_sold
    return ROI
    pass

def main():
    try:
        filecount= open_file() 
        datalist=[]
        product_name =[]
        ad_name=[]
        ad_count = []
        price_per_copy = []
        sales = []
        sale_price = []
        prod_cost = []
        temp_product =""
        TempROI =0
        BestROI =0
        ROI_index =0
        BestSales =0
        line_count =0
        Sale_index =0
        first =0     
        
        for line in filecount:       
            line_count += 1
            product_name.append(line[0:27])
            ad_name.append(line[27:55])
            
            ad_count.append(int(line[55: 64].strip(" ")))
            price_per_copy.append(float(line[64:72]))
            sales.append(int(line[72:78]))
            sale_price.append(float(line[78:86]))
            prod_cost.append(float(line[86:94]))
            datalist.append(line)      
            
        temp_product = product_name[0]
        for n in range(0,line_count):       
            TempROI = calculate_ROI(ad_count[n],price_per_copy[n],sales[n],sale_price[n],prod_cost[n])
            
            if BestROI < TempROI:
                ROI_index =n
                BestROI = TempROI
            if BestSales < sales[n]:
                Sale_index=n
                BestSales=sales[n]
            try :
              if temp_product != product_name[n+1]: 
                if first ==0:
                    print()
                    print("RobCo AdStats M4000")
                    print("-------------------")
                    print() 
                    first = 1
            
                print(product_name[ROI_index])
                print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
                print("  {:27s}{:>10}".format(ad_name[Sale_index],sales[Sale_index]))
                  
                print("  {:27s}{:>11s}".format("Best ROI","percent"))
                print("  {:27s}{:>9}{}".format(ad_name[ROI_index],round(BestROI,2),'%'))
                print()
                ROI_index =0
                Sale_index=0
                TempROI   =0
                BestROI   =0
                BestSales =0
                
                temp_product = product_name[n+1]  
                pass
            except IndexError:
                if first==0:
                    print()
                    print("RobCo AdStats M4000")
                    print("-------------------")
                    print() 
                    first =1
             
                print(product_name[ROI_index])
                print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
                print("  {:27s}{:>10}".format(ad_name[Sale_index],sales[Sale_index]))
                  
                print("  {:27s}{:>11s}".format("Best ROI","percent"))
                print("  {:27s}{:>9}{}".format(ad_name[ROI_index],round(BestROI,2),'%'))
                ROI_index =0
                Sale_index=0
                TempROI   =0
                BestROI   =0
                BestSales =0
        pass
    except FileNotFoundError:
          print("Unable to open file. Please try again.")
          main()

if __name__ == "__main__":
    main()