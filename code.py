import numpy as np

# number of time slots is taken from the user
time_intervals = int(input("enter the number of time intervals: "))
agents= 20
job_prob = 0.5

# Implementation of Second price type auction based allocation scheme
print(" second price type auction-based allocation")
for t in range(time_intervals):
    print("at t =" + str(t+1))
    job_values = [0]*20
    lisst = []
    resources_available = np.random.binomial(20, 0.5)
    print(str(resources_available) + " resources are available")
    agent_job_prob = np.round(np.random.uniform(low=0, high=1, size=20),2)
    print(agent_job_prob)
    count = 0
    for agent in range(len(agent_job_prob)):
        if agent_job_prob[agent] >= 0.5:
            job_values[agent] = round(np.random.uniform(low=0, high=1),4)
            count+=1
    print(str(count) + "jobs are ready")
    print("job_values of agents:")
    print(job_values)
    if resources_available < count:
        for i in range(resources_available+1):
            tempp = np.argmax(job_values)
            lisst.append([np.argmax(job_values),job_values[tempp]])
            if job_values[tempp] == 0:
                break
            job_values[tempp] = 0

        final_list = []
        for i in range(len(lisst)-1):
            final_list.append([lisst[i][0],lisst[resources_available][1]]) 
        print("Allocation is done as follows: [agent, value]")
        print(final_list)
    else:
        print("Number of resources available is sufficient for all the jobs. So agents can bid with 0 and get resource")
        final_list =[]
        for i in range(len(job_values)):
            if job_values[i] != 0:
                final_list.append([i, 0])
        print("Allocation is done as follows: [agent, value]")
        print(final_list)
        print("___________________________________________")
    

# Implementation of First price type auction based allocation scheme
print(" First price type auction-based allocation")
for t in range(time_intervals):
    print("at t =" + str(t+1))
    job_values = [0]*20
    resources_available = 1
    agent_job_prob = np.round(np.random.uniform(low=0, high=1, size=20),2)
    count = 0
    for agent in range(len(agent_job_prob)):
        if agent_job_prob[agent] >= 0.5:
            job_values[agent] = round(np.random.uniform(low=0, high=1),4)
            count+=1
    print(str(count) + "jobs are ready")
    print("job_values of agents:")
    print(job_values)
    
    mul_factor = round((count - 1)/count,4)
    print("multiplication factor: "+ str(mul_factor))
    agent_won = np.argmax(job_values)
    print(job_values[agent_won])
    paid_job_value = mul_factor*job_values[agent_won]
    
    print("agent won : "+ str(agent_won))
    print("job value of the won agent: " + str(job_values[agent_won]))
    print("value paid by the won agent: " + str(paid_job_value))
    print("_________________________________________________")
        
    