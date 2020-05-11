#!/bin/usr/python
import random

list_of_bowlers=[]
list_of_batsman=[]
list_of_wicket_keeper=[]
list_of_All_Rounder=[]

list_indians=[]
list_overseas=[]

list_of_bowlers_overseas=[]
list_of_batsman_overseas=[]
list_of_wicket_keeper_overseas=[]
list_of_All_Rounder_overseas=[]

list_already_visited={}

fp=open("dataset.txt","r")
dataset=fp.readlines()
i=1
for line in dataset:
	# print(i)
	i=i+1
	player_data=line.split(":")
	# for item in player_data:
	# 	print(item)
	# print("*"*30)
	if(player_data[1]!="India"):
		list_overseas.append(player_data)
	if(player_data[1]=="India"):
		list_indians.append(player_data)
	list_already_visited[player_data[0]]=1
	if(player_data[1]=="India" and player_data[2]=="Batsman"):
		list_of_batsman.append(player_data)
	elif(player_data[1]=="India" and player_data[2]=="Bowler"):
		list_of_bowlers.append(player_data)
	elif(player_data[1]=="India" and player_data[2]=="All-Rounder"):
		list_of_All_Rounder.append(player_data)
	elif(player_data[1]=="India" and player_data[2]=="Wicket Keeper"):
		list_of_wicket_keeper.append(player_data)
	elif(player_data[1]!="India" and player_data[2]=="Batsman"):
		list_of_batsman_overseas.append(player_data)
	elif(player_data[1]!="India" and player_data[2]=="Bowler"):
		list_of_bowlers_overseas.append(player_data)
	elif(player_data[1]!="India" and player_data[2]=="All-Rounder"):
		list_of_All_Rounder_overseas.append(player_data)
	elif(player_data[1]!="India" and player_data[2]=="Wicket Keeper"):
		list_of_wicket_keeper_overseas.append(player_data)

# for batsman in list_of_batsman:
# 	print(batsman)

# ind=1
# for k,v in list_already_visited.items():
# 	print(ind," ",k,":",v)
# 	ind=ind+1
# random.shuffle(list_of_batsman)
# # # for batsman in list_of_batsman:
# # # 	print(batsman)
# print(len(list_of_batsman))
# random.shuffle(list_of_bowlers)
# print(len(list_of_bowlers))
# random.shuffle(list_of_wicket_keeper)
# print(len(list_of_wicket_keeper))
# random.shuffle(list_of_All_Rounder)
# print(len(list_of_All_Rounder))

# random.shuffle(list_of_batsman_overseas)
# print(len(list_of_batsman_overseas))
# random.shuffle(list_of_bowlers_overseas)
# print(len(list_of_bowlers_overseas))
# random.shuffle(list_of_wicket_keeper_overseas)
# print(len(list_of_wicket_keeper_overseas))
# random.shuffle(list_of_All_Rounder_overseas)
# print(len(list_of_All_Rounder_overseas))

# random.shuffle(list_overseas)


fconfig=open("config.txt","r")
config_data=fconfig.readlines()
# print(config_data)
constraints=[]
for i in range(0,5):
	constraints.append(config_data[i].strip().split(":"))

for constraint in constraints:
	print(constraint)

min_os=int(constraints[0][1])
max_os=int(constraints[0][2])
min_bat=int(constraints[1][1])
max_bat=int(constraints[1][2])
min_bol=int(constraints[2][1])
max_bol=int(constraints[2][2])
min_wk=int(constraints[3][1])
max_wk=int(constraints[3][2])
min_ar=int(constraints[4][1])
max_ar=int(constraints[4][2])

print("os : ",min_os," ",max_os)
print("bat : ",min_bat," ",max_bat)
print("bol : ",min_bol," ",max_bol)
print("wk : ",min_wk," ",max_wk)
print("ar : ",min_ar," ",max_ar)
# print("os : ",min_os," ",max_os)



team_no=int(config_data[5].split(":")[1])
print("team_no : ",team_no)

team_names=[]

for i in range(6,len(config_data)):
	team_names.append(config_data[i].strip())

teams=[]

for team in team_names:
	print(team)
	teams.append(list())

# print(team_names)

# for team in teams:
# 	pass

# overseas
for ii in range(1,team_no+1):
	name=team_names[ii].split()
	name="_".join(name)
	name+=".txt"
	print(name)

	team=[]
	count_bat=0
	count_bol=0
	count_wk=0
	count_ar=0
	current_team=0
	# count_os=random.randint(min_os,max_os)
	count_os=max_os
	for ind in range(0,count_os):
		for i in range(0,len(list_overseas)):
			# print(list_overseas[i])
			lo=list_overseas[i]
			# print(lo[0])
			if(list_already_visited[lo[0]]==1):
				if(lo[2]=="Batsman"):
					if(count_bat<min_bat):
						team.append(list_overseas[i])
						count_bat+=1
						current_team+=1
						list_already_visited[lo[0]]=0
						break
				elif(lo[2]=="Bowler"):
					if(count_bol<max_bol):
						team.append(list_overseas[i])
						count_bol+=1
						list_already_visited[lo[0]]=0
						current_team+=1
						break
				elif(lo[2]=="Wicket Keeper"):
					if(count_wk<min_wk):
						team.append(list_overseas[i])
						count_wk+=1
						list_already_visited[lo[0]]=0
						current_team+=1
						break
				elif(lo[2]=="All-Rounder"):
					if(count_ar<min_ar):
						team.append(list_overseas[i])
						count_ar+=1
						list_already_visited[lo[0]]=0
						current_team+=1
						break
				

	# random.shuffle(list_of_batsman)
	# random.shuffle(list_of_bowlers)
	# random.shuffle(list_of_wicket_keeper)
	# random.shuffle(list_of_All_Rounder)

	print(count_bat," ",count_bol," ",count_wk," ",count_ar," ",current_team)
	print("hello")
	# indian players

	# minimum

	while(count_bat<min_bat):
		for i in range(0,len(list_of_batsman)):
			if(list_already_visited[list_of_batsman[i][0]]==1):
				count_bat+=1
				current_team+=1
				team.append(list_of_batsman[i])
				list_already_visited[list_of_batsman[i][0]]=0
				break

	print("Hello3")
	while(count_ar<min_ar):
		for i in range(0,len(list_of_All_Rounder)):
			if(list_already_visited[list_of_All_Rounder[i][0]]==1):
				count_ar+=1
				current_team+=1
				team.append(list_of_All_Rounder[i])
				list_already_visited[list_of_All_Rounder[i][0]]=0
				break

	print("Hello1")
	while(count_bol<min_bol):
		for i in range(0,len(list_of_bowlers)):
			if(list_already_visited[list_of_bowlers[i][0]]==1):
				count_bol+=1
				current_team+=1
				team.append(list_of_bowlers[i])
				list_already_visited[list_of_bowlers[i][0]]=0
				break

	print("Hello2")
	while(count_wk<min_wk):
		for i in range(0,len(list_of_wicket_keeper)):
			if(list_already_visited[list_of_wicket_keeper[i][0]]==1):
				count_wk+=1
				current_team+=1
				team.append(list_of_wicket_keeper[i])
				list_already_visited[list_of_wicket_keeper[i][0]]=0
				break

	print(count_bat," ",count_bol," ",count_wk," ",count_ar," ",current_team)


	# complete team

	while(current_team<18):
		for i in range(0,len(list_indians)):
			# print(list_overseas[i])
			lo=list_indians[i]
			# print(lo[0])
			if(list_already_visited[lo[0]]==1):
				if(lo[2]=="Batsman"):
					if(count_bat<max_bat):
						team.append(list_indians[i])
						count_bat+=1
						current_team+=1
						list_already_visited[lo[0]]=0
						break
				elif(lo[2]=="Bowler"):
					if(count_bol<max_bol):
						team.append(list_indians[i])
						count_bol+=1
						list_already_visited[lo[0]]=0
						current_team+=1
						break
				elif(lo[2]=="Wicket Keeper"):
					if(count_wk<max_wk):
						team.append(list_indians[i])
						count_wk+=1
						list_already_visited[lo[0]]=0
						current_team+=1
						break
				elif(lo[2]=="All-Rounder"):
					if(count_ar<max_ar):
						team.append(list_indians[i])
						count_ar+=1
						list_already_visited[lo[0]]=0
						current_team+=1
						break
	print(count_bat," ",count_bol," ",count_wk," ",count_ar," ",current_team)

	f=open(name,"w")
	f.write("Team: ")
	f.write(team_names[ii])
	f.write("\n\n")
	count=1
	for i in team:
		print(i)
		f.write("Player ")
		f.write(str(count))
		f.write("\n")
		f.write("Name : ")
		f.write(i[0])
		f.write("\n")
		f.write("Country : ")
		f.write(i[1])
		f.write("\n")
		f.write("Ability : ")
		f.write(i[2])
		f.write("\n")
		f.write("Fees : ")
		f.write(i[3])
		f.write("\n")
		count+=1

	f.close()

print("completed")




















