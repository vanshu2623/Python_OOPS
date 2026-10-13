# class IPL_Cricket_Player:
#     def __init__(self,j_no,n,r,w,team_n):
#         self.jersey_no = j_no
#         self.name = n
#         self.runs = r
#         self.wickets = w
#         self.team_name = team_n 
#     def display(self):
#         print("Jersey Number:",self.jersey_no)
#         print("Name:",self.name) 
#         print("Runs:",self.runs) 
#         print("Wickets:",self.wickets) 
#         print("Team_Name:",self.team_name)       
         
# cp1 = IPL_Cricket_Player(18,"Virat Kohli",4556,0,"RCB")
# cp2 = IPL_Cricket_Player(1,"Rajat Patidar",2564,0,"RCB")
# cp3 = IPL_Cricket_Player(19,"Dinesh Karthik",3604,0,"RCB")
# cp4 = IPL_Cricket_Player(9,"Tim David",6587,0,"RCB")
# cp5 = IPL_Cricket_Player(8,"Bhuvneshwar Kumar",45,40,"RCB")

# cp1.display()
# cp2.display()
# cp3.display()
# cp4.display()
# cp5.display()

class IPL_Cricket_Player:
    def __init__(self,j_no,n,r,w,team_n):
        self.jersey_no = j_no
        self.name = n
        self.runs = r
        self.wickets = w
        self.team_name = team_n 

cp1 = IPL_Cricket_Player(18,"Virat Kohli",4556,0,"RCB")
cp2 = IPL_Cricket_Player(1,"Rajat Patidar",2564,0,"RCB")
cp3 = IPL_Cricket_Player(19,"Dinesh Karthik",3604,0,"RCB")
cp4 = IPL_Cricket_Player(9,"Tim David",6587,0,"RCB")
cp5 = IPL_Cricket_Player(8,"Bhuvneshwar Kumar",45,40,"RCB")

rcb_team = []
rcb_team.append(cp1)
rcb_team.append(cp2)
rcb_team.append(cp3)
rcb_team.append(cp4)
rcb_team.append(cp5)

rcb = IPL_Cricket_Player(rcb_team)