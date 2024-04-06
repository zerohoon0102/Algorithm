from collections import deque
class Team:
    def __init__(self, team_lead:int):
        self.team_mate_list = []
        self.lead_team_mate_list = []
        self.team_lead_team = None
        self.least_earn = 10001
        self.chk_count = 0
    
    def add_team_mate(self, team_mate: int):
        self.team_mate_list.append(team_mate)
    
    def add_lead_team_mate(self, team_mate: int):
        self.lead_team_mate_list.append(team_mate)
    
    def set_least_earn(self, value: int):
        self.least_earn = min(self.least_earn, value)
    
    def set_team_lead_team(self, team_num: int):
        self.team_lead_team = team_num

def solution(sales, links):
    answer = 2**31 - 1
    
    # 팀장과 팀원 초기 정보 구축
    teams = {}
    for lead, mate in links:
        if lead-1 in teams:
            teams[lead-1].add_team_mate(mate-1)
        else:
            teams[lead-1] = Team(lead-1)
            teams[lead-1].add_team_mate(mate-1)
    
    leaf_teams = deque([])
    # 타팀의 팀장인 팀원을 별도로 담고, 팀장이 아닌 인원 중 가장 매출이 적은 인원 기록
    for team_lead in teams:
        team = teams[team_lead]
        for team_mate in team.team_mate_list:
            if team_mate in teams:
                team.add_lead_team_mate(team_mate)
                teams[team_mate].set_team_lead_team(team_lead)
            else:
                team.set_least_earn(sales[team_mate])
        
        if len(team.lead_team_mate_list) == 0:
            leaf_teams.append(team_lead)
    
    dp = {team_lead : [None, None] for team_lead in teams}
    
    # bottom-up 방식으로 값 추출
    while leaf_teams:
        team_lead = leaf_teams.popleft()
        team = teams[team_lead]
        
        get_bottom_team = 0
        chk = False
        for lead_team_mate in team.lead_team_mate_list:
            if dp[lead_team_mate][1] == None or dp[lead_team_mate][0] <= dp[lead_team_mate][1]:
                chk = True
                get_bottom_team += dp[lead_team_mate][0]
            else:
                get_bottom_team += dp[lead_team_mate][1]
        
        sel_team_lead = sales[team_lead]
        dp[team_lead][0] = sel_team_lead + get_bottom_team
        
        if chk:
            dp[team_lead][1] = get_bottom_team
        else:
            min_diff_sel = 2**31-1
            for lead_team_mate in team.lead_team_mate_list:
                diff_sel_team_earn = dp[lead_team_mate][0] - dp[lead_team_mate][1]
                min_diff_sel = min(min_diff_sel, diff_sel_team_earn)
            
            if len(team.lead_team_mate_list) > 0:
                dp[team_lead][1] = get_bottom_team + min_diff_sel
            
            if dp[team_lead][1] == None:
                dp[team_lead][1] = team.least_earn + get_bottom_team
            else:
                dp[team_lead][1] = min(dp[team_lead][1], team.least_earn + get_bottom_team)
        
        if team.team_lead_team != None:
            team_lead_team = teams[team.team_lead_team]
            team_lead_team.chk_count += 1
            if team_lead_team.chk_count == len(team_lead_team.lead_team_mate_list):
                leaf_teams.append(team.team_lead_team)
    
    answer = min(dp[0])
    return answer
