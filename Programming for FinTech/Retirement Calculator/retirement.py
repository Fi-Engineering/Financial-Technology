
import sys
from sys import argv
import pandas as pd
import numpy as np

def proceed():
        x = input('to continue enter 3: ')
        if(x == "3"):
            pass
        else:
            print('\nProcess terminated by user\n')
            sys.exit(0)



def writeToDisk(dataFile, portfolio):
    filename = dataFile +  ".csv"   
    outfile = open(filename,'wb')
    portfolioList = portfolio.values.tolist()
    mydt = pd.DataFrame(portfolioList, columns = ['Date', 'StrategyOne','StrategyTwo', 'StrategyThree'])
    mydt.to_csv(filename, index=False, encoding='utf-8')
    outfile.close()




#  uses the pandas read csv format to load user database into RAM:
def loadFile2RAM(filename):
    infile = open(filename,'r')
    mydata = pd.read_csv(infile, encoding = "ISO-8859-1")
    infile.close()
    return mydata;


def cum_invest(prevBal, rateRet, contrib):
 
    return prevBal + ((rateRet)*prevBal) + contrib


def stratOne(sp_data, prevBal, contrib, contribInc):
    spList = sp_data.values.tolist()
   
    balanceList = []

    n = len(spList)
    for r in range(n):
        if(r==0):
            balance = contrib
            balanceFormatted = "{:.2f}".format(balance)
            balanceList.append( balanceFormatted )
            
            prevBal = balance
        else:
            date = str(spList[r][0])
          
            month = date.split('.')[1]
           
            if(month=='01'):
                contrib = contrib * (1.0 + contribInc)
                
            spROR = (spList[r][1] / spList[r-1][1]) - 1
           
            divROR = (spList[r][2] / 12) / spList[r][1] 
         
            portROR = spROR + divROR
         
            balance = cum_invest(prevBal, portROR, contrib)
            prevBal =  balance

            balance = round(balance, 2)
            balanceFormatted = "{:.2f}".format(balance)
            balanceList.append( balanceFormatted )
      
    return balanceList
            
        

def stratTwo(bond_data, prevBal, contrib, contribInc):
    bondList = bond_data.values.tolist()
    balanceList = []
    n = len(bondList)
    for r in range(n):
        if(r==0):
            balance = contrib
            balanceFormatted = "{:.2f}".format(balance)
            balanceList.append( balanceFormatted )

            prevBal = balance
        else:
            date = str(bondList[r][0])
         
            month = date.split('.')[1]
         
            if(month=='01'):
                contrib = contrib * (1.0 + contribInc)
               
            bondROR = (bondList[r][1]) / 1200
            #print('spROR: ', bondROR )
            portROR = bondROR 
          
            balance = cum_invest(prevBal, portROR, contrib)
            prevBal =  balance
            balance = round(balance, 2)
            balanceFormatted = "{:.2f}".format(balance)
            balanceList.append( balanceFormatted )
           
            
    return balanceList


def stratThree(sp_data, bond_data, prevBal, contrib, contribInc, lifecycleAlloc, lifecycleAllocDec):
    bondList = bond_data.values.tolist()
    spList = sp_data.values.tolist()
    balanceList = []
    if(len(bondList)!=len(spList)):
        print('date file length mismatch')
        sys.exit(1)
        
    n = len(bondList)
    for r in range(n):
        if(r==0):
            balance = contrib
            balanceFormatted = "{:.2f}".format(balance)
            balanceList.append( balanceFormatted )
            prevBal = balance
        else:
            date = str(bondList[r][0])
            month = date.split('.')[1]
          
            if(month=='01'):
                contrib = contrib * (1.0 + contribInc)
                # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv this entire line was missing!!!!!!!!!??????????
                lifecycleAlloc = lifecycleAlloc - lifecycleAllocDec
                
            spROR = (spList[r][1] / spList[r-1][1]) - 1
            divROR = (spList[r][2] / 12) / spList[r][1] 
            portROR = spROR + divROR
        
            spBal = (prevBal * (1 + portROR)) * lifecycleAlloc
            bondROR = (bondList[r][1]) / 1200
            
            bondBal = (prevBal * (1 + bondROR)) * (1 - lifecycleAlloc)
            balance = spBal + bondBal + contrib
            prevBal = balance
            balance = round(balance, 2)
            balanceFormatted = "{:.2f}".format(balance)
            balanceList.append( balanceFormatted )
           

    return balanceList


def isValidYear(year, startYear, endYear):
    if(year >= startYear and year <= endYear):
        return True
    else:
        print('input invalid: year value out of range: ')
        # sys.exit(2)
        return False
    
def isValidMonth(month):
    months = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    if(month in months):
        return True
    else:
      
        return False



def isValidDate(date, startDate, endDate):
    '''determines if a given date is correct type, within range, and valid year and month: '''
    
   
    
    if(not isinstance(date, float)):
        print('input invalid type, not float: ')
        # sys.exit(2)
        return False
    
    else:
        startYear = int(startDate)
      
    
        endYear = int(endDate)
       
        year = getYear(date, startYear, endYear)
      
        if(not isValidYear(year, startYear, endYear)):
            print('input invalid: year not within range: ')
            
            return False
        else:
            month = getMonth(date, year)
          
            if(not isValidMonth(month)):
                 print('input invalid: month out of range: ')
                 # sys.exit(2)
                 return False
            else:
                 
                 return True
        

    
def getYear(date, startYear, endYear):
     year = int(date)
     
     if(not isValidYear(year, startYear, endYear)):
         print('input invalid: year not within range: ', year)
         
         return False
     else:
         return year
     
def getMonth(date, year):
  
    
    mo = str(date)

    month = mo[5:7]
   
    if(len(month)==1 and int(month[0])==1):
      
        month = 10
    month = int(month)
 
    return month
    



# parses dates for validation and tolist():
#def dates(sp_data, bond_data, startDate, endDate):
def dates(sp_data, bond_data):    
    datesValid = True
    errorCode = 0
    dateListSP = []
    dateListTB = []
    startDate = 1970.01
    endDate = 2019.03

    
   
    # check length of data files for mismatch:
    if((len(dateListSP))!=len(dateListTB)):
        print('date file length mismatch')
        datesValid = False
        errorCode = 1
        return datesValid, errorCode
  
    
    if(sp_data.iloc[0,0]>startDate or sp_data.iloc[len(sp_data)-1,0]<startDate or endDate > sp_data.iloc[len(sp_data)-1,0]):
        print('\nstart or end date outside data range in sp_data\n')
        datesValid = False
        errorCode = 2
        return datesValid, errorCode
    
    if(bond_data.iloc[0,0]<startDate or endDate > bond_data.iloc[len(bond_data)-1,0]):
        print('\nstart or end date outside data range in bond_data\n')
        datesValid = False
        errorCode = 3
        return datesValid, errorCode
    
    dateValid = isValidDate(sp_data.iloc[0,0],startDate, endDate)
    if(dateValid):
        #print('start date is within range')
        pass
    else:
        print('\nInvalid date in sp_data\n')
        datesValid = False
        errorCode = 2
        return datesValid, errorCode
        
    dateValid = isValidDate(sp_data.iloc[len(sp_data)-1,0],startDate, endDate)
    if(dateValid):
        #print('end date is within range')
        pass
    else:
        print('\nInvalid date in sp_data\n')
        datesValid = False
        errorCode = 2
        return datesValid, errorCode
  
    
    
    for r in range(len(sp_data)):
        
        if(not isValidDate(sp_data.iloc[r, 0], startDate, endDate)):
           print ('found invalid date: ', sp_data.iloc[r, 0]) 
           print('\nInvalid date in sp_data\n')
           datesValid = False
           errorCode = 2
           return datesValid, errorCode
           #break
        elif(sp_data.iloc[r, 1] <= 0.0 or sp_data.iloc[r, 1]==None or not isinstance(sp_data.iloc[r, 1], float) or np.isnan(sp_data.iloc[r, 1])):
           print ('found invalid sp data: ', sp_data.iloc[r, 1]) 
           print('\nInvalid data in sp_data\n')
           datesValid = False
           errorCode = 2
           return datesValid, errorCode
           
        elif(sp_data.iloc[r, 2] < 0.0 or sp_data.iloc[r, 2]==None or not isinstance( sp_data.iloc[r, 2],float) or np.isnan(sp_data.iloc[r, 2])):
           print ('found invalid sp data: ', sp_data.iloc[r, 2]) 
           print('\nInvalid data in sp_data\n')
           datesValid = False
           errorCode = 2
           return datesValid, errorCode
           
    for r in range(len(bond_data)):
        
        if(not isValidDate(bond_data.iloc[r, 0], startDate, endDate)):
            print ('found invalid date: ', bond_data.iloc[r, 0])
            print('\nInvalid date in bond_data\n')
            datesValid = False
            errorCode = 3
            return datesValid, errorCode
           
        
        elif(bond_data.iloc[r, 1] < 0.0 or bond_data.iloc[r, 1]==None or not isinstance( bond_data.iloc[r, 1],float) or np.isnan(bond_data.iloc[r, 1])):
            print ('found invalid bond data: ', bond_data.iloc[r, 1])           
            print('\nInvalid data in bond_data\n')
            datesValid = False
            errorCode = 3
            return datesValid, errorCode
          
        else:
           continue
        
   
    return datesValid, errorCode

                
def isSequential(date, thisYearExpected, thisMonthExpected):

   
    thisYear  = int(date)
 
    thisMonth = getMonth(date, thisYear) 
 
    
    if(thisYear!=thisYearExpected or thisMonth!=thisMonthExpected):
        print('dates out of sequence\n')      
        return False
        
    else:
        return True



def chkSequence(spData, bondData, startDate, endDate):
    
  
    sequential = True
    errorCode = 0
  
    # initialize years and months:
    thisYear  = int(spData.iloc[0,0])
  

    thisMonth = getMonth(spData.iloc[0,0], thisYear)
    
    thisYearExpected = thisYear
    thisMonthExpected = thisMonth
    
    #monthCount = 0
    limit = 12
    for r in range(1, len(spData)):  # start should be 1, not 0
             
             if(thisMonthExpected==limit):     
                            
                thisMonthExpected = 1                               
                # update year:  # doesn't yet check end of years!
                thisYearExpected =  thisYearExpected + 1
              
                if(not isSequential(spData.iloc[r,0], thisYearExpected, thisMonthExpected)):
                   print ('found out-of-sequence date: ', spData.iloc[r, 0])
                   errorCode = 2
                   sequential = False
                   break

             elif(sequential):
                thisMonthExpected += 1
                  
                if(not isSequential(spData.iloc[r,0], thisYearExpected,  thisMonthExpected)):
                    print ('found out-of-sequence date: ', spData.iloc[r, 0])
                    errorCode = 2
                    sequential = False
                    break
                              
            
    
    if(sequential):
 
        sequential = True
        errorCode = 0
        thisYear  = int(bondData.iloc[0,0])
        #print('thisYear: ', thisYear)  
        thisMonth = getMonth(bondData.iloc[0,0], thisYear)
        thisYearExpected = thisYear
        thisMonthExpected = thisMonth

        limit = 12   
        for r in range(1, len(bondData)):
              
                 
                  if(thisMonthExpected == limit):
                                       
                      thisMonthExpected = 1                    
                     
                      thisYearExpected = thisYearExpected + 1
                     
                  else:
                      
                     
                      thisMonthExpected += 1                 
                                              
                  #proceed()
                  if(not isSequential(bondData.iloc[r,0], thisYearExpected, thisMonthExpected)):
                    print ('found out-of-sequence date: ', bondData.iloc[r, 0])
                    sequential = False
                    errorCode = 3
                    break
          
       
    return sequential, errorCode


#              args: both input files:
def fileValidation(sp_data, bond_data):
    """
        check both files for dates lined up
        check negative values as data error in files
        check, for each line in each file, that there are same (and correct) number of fields
        
    """
    filesValid = True
    
    # for each line, check 3 fields for sp_data, 2 for bond_data:
    for r in range(len(sp_data)):
        
        if(len(sp_data.columns) != 3):
           print ('invalid file input: sp_data requires 3 fields')  
           filesValid = False
           break
        else:
            continue
       
    for r in range(len(bond_data)):
          
        if(len(bond_data.columns) != 2):
           print ('invalid file input: bond_data requires 2 fields')  
           filesValid = False
           break    
        else:
           continue
    
  
    datesValid, errorCode = dates(sp_data, bond_data)
    if(not datesValid):
        # check data validity
        filesValid = False
        print('found invalid dates')
        sys.exit(errorCode)
    else:
        
       
        startDate = argv[3]
       
        endDate =    argv[3]
    
    
    #sequential = chkSequence(spData, bondData, startDate, endDate)
        sequential, errorCode = chkSequence(sp_data, bond_data, startDate, endDate)
        if(not sequential):
                print('found entries missing or out of sequence')
                filesValid = False
                sys.exit(errorCode)
        else:
                pass
    
    return filesValid


def validInputDate(date):
   
    digitsSet = {'0', '1', '2', '3', '4', '5', '6', '7', '8',  '9'}
    monthsSet =  {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'}
    leadDigitSet = {'1', '2'}
    
  
    
    date = str(date)
    
    if(len(date)!=7):
        return False
    
    if(date[4]!="."):
        return False
    
    if(date[0]=='0'):
         return False
    
    if(date[0]=='-'):
         return False
    
 
    if(date[0] not in leadDigitSet):
         
         return False
    
    # permissive year checK: all digits assumed valid in places 1-3
    for i in range(1,4):
        if(date[1] not in digitsSet):
            return False
    
    # check values of months:
    month = date.split('.')[1]
    if(month not in monthsSet):
        return False
    
    
      
    return True



def ret(argv):

     
    # test sp file name format:
    if(argv[1]!="sp_data.csv"):
        print('sp data file name format error')
        sys.exit(1) 
        
    if(argv[2]!="bond_data.csv"):
        print('bond data file name format error')
        sys.exit(1)
    
    
    startDate = argv[3]
    
    startDateValid = validInputDate(startDate)    
    if(not startDateValid):        
        print('date input error start date: ')
        sys.exit(1)
        
     
    endDate =   argv[4]
    endDateValid = validInputDate(endDate)
    if(not endDateValid):
         print('date input error end date: ')
         sys.exit(1) 
         
     # test for end year before start year:
    if(int(float((argv[4]))) < int(float((argv[3])))):
         print('start date greater than end date')
         sys.exit(1)     
   

    
  
    try:
        #sp_dataFile = 'sp_data.csv'    # argv[1]
        if(argv[1]=='sp_data.csv'):
            sp_dataFile =  argv[1]
            sp_data = loadFile2RAM(sp_dataFile)
      
        else:
            print('file read error; sp_data.csv file not found')
            sys.exit(1)
    except:
        print('sp_data.csv file not found')
        sys.exit(1)
        
    try:
        # load bond data:
        if(argv[2]=='bond_data.csv'):
            bond_dataFile =  argv[2]
            bond_data = loadFile2RAM(bond_dataFile)
        else:
            print('file read error; bond_data.csv file not found')
            sys.exit(1)    
        #print('bond_data.head(): \n', bond_data.head())
        #proceed()

    except:
        print('bond_data.csv file not found')
        sys.exit(1)
    

    # error code 2 for sp file, error code 3 for bond file:
    filesValid = fileValidation(sp_data, bond_data)
    if(not filesValid):
        print('file errors')
    else:
    
        
   
   
        
        # globals:
        prevBal = 0.00
        initContrib = 100.00
        contribInc  =   0.025 # decimal fraction of %
        lifecycleAlloc = 1.00
        lifecycleAllocDec = 0.02 # decimal fraction of %
           
     
        spData = sp_data[sp_data['Date'] >= float(startDate)]
                         
 
        spData = spData[spData['Date'] <= float(endDate)]
        
        dateList = []
        dateList = spData.iloc[:,0].values.tolist()
        for d in range(len(dateList)):

            dateList[d] = "{:.2f}".format(round(dateList[d], 2))
     
        
        stratOneList = stratOne(spData, prevBal, initContrib, contribInc)
       
        bondData = bond_data[bond_data['Date'] >= float(startDate)]
        bondData = bondData[bondData['Date'] <= float(endDate)]
       
        stratTwoList = stratTwo(bondData, prevBal, initContrib, contribInc)
        
        stratThreeList = stratThree(spData, bondData, prevBal, initContrib, contribInc, lifecycleAlloc, lifecycleAllocDec)

 
        portfolioDF = pd.DataFrame(dateList, columns=['Date'])
        portfolioDF['StrategyOne'] = stratOneList
        portfolioDF['StrategyTwo'] = stratTwoList
        portfolioDF['StrategyThree'] = stratThreeList
        filename =  'portfolio'
        writeToDisk(filename, portfolioDF)
        

if __name__ == "__main__":
    if len(argv) < 5:  # check for correct number of args
        print("Usage: python3 retirement.py file1_name file2_name ...")
        sys.exit(1)
   
    ret(argv)
