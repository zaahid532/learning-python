goal_list = ["python","HTML","CSS"]
goal_list += ["database","Django"]
file = open("newnote.txt","a")
file.write("\n")
for goal in goal_list:
    file.write(f"master {goal}\n")
file.close()