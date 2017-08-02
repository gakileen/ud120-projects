#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    errors = (net_worths-predictions)**2
    cleaned_data =zip(ages,net_worths,errors)
    cleaned_data = sorted(cleaned_data,key=lambda x:x[2][0], reverse=True)
    limit = int(len(net_worths)*0.1)

    return cleaned_data[limit:]


def biggestOutlier(predictions, ages, net_worths):
    all_data = []

    ### your code goes here
    size = len(ages)

    for i in range(size):
        i_age = ages[i]
        i_net_worth = net_worths[i]
        i_error = (i_net_worth - predictions[i]) * (i_net_worth - predictions[i])
        all_data.append((i_age, i_net_worth, i_error))

    cleaned_data = sorted(all_data, key = lambda t: t[2], reverse = True)[0]

    print cleaned_data

    return cleaned_data
