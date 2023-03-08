working_info = {'months':489,'contribution':1000,'rate_of_return':0.045/12}
retired_info = {'months':384, 'contribution':-4000, 'rate_of_return':0.01/12}
start = 327 
initial_savings = 21345

def retirement(start, initial_savings, working_info, retired_info):
    start = 327 
    initial_savings = 21345
    working_info = {'months':489,'contribution':1000,'rate_of_return':0.045/12}
    retired_info = {'months':384, 'contribution':-4000, 'rate_of_return':0.01/12}
    months_till_retirement = start + working_info['months']
    months_after_retirement = months_till_retirement + retired_info['months']
    print ("Age {:3d} month {:2d} you have ${:,.2f}".format(27,3,initial_savings))
    
    start = start + 1 
    while start < months_after_retirement:
        if (start <= months_till_retirement):
            savings = (initial_savings*working_info['rate_of_return']) + initial_savings + working_info['contribution']
            age_years = start // 12
            months1 = start %12
            print ("Age {:3d} month {:2d} you have ${:,.2f}".format(age_years,months1,savings))
            start = start +1
            initial_savings = savings
        else:
           
            savings = (initial_savings*retired_info['rate_of_return']) + initial_savings + retired_info['contribution']
            age_years = start //12
            months2 = start%12
            print ("Age {:3d} month {:2d} you have ${:,.2f}".format(age_years,months2,savings))
            start = start +1
            initial_savings = savings
    
retirement(start ,initial_savings,working_info,retired_info)