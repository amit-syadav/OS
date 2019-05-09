from itertools import accumulate


def table(AT,BT,CT,TAT,WT):
	print ("Process\t\tAT\t\tBT\t\tCT\t\tTAT\t\tWT\n")
	for i in range(len(AT)):
		print ("P",i+1,"\t\t",AT[i],"\t\t",BT[i],"\t\t",CT[i],"\t\t",TAT[i],"\t\t",WT[i],"\n",sep="")


def FCFS(arrival_time,burst_time):
	
	completion_time = list(accumulate(burst_time))
	turn_around_time = [ct - at for ct, at in zip(completion_time, arrival_time)]
	waiting_time = [tat - bt for tat, bt in zip(turn_around_time, burst_time)]

	print ("\nFCFS Implementation :")
	table(arrival_time,burst_time,completion_time,turn_around_time,waiting_time)
	print("Order of Execution: ",end="")
	[print("P"+str(i)+" ",end="") for i in range(len(arrival_time))]
	print ("\nAverage TurnAroundTime : ",sum(turn_around_time)/len(turn_around_time))
	print ("Average WaitingTime    : ",sum(waiting_time)/len(waiting_time))


def main():

	arrival_time = [int(val) for val in input("Enter arrival time for each process: ").split()]
	burst_time = [int(val) for val in input("Enter burst time for each process: ").split()]

	FCFS(arrival_time,burst_time)

main()
