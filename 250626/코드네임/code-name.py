MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Agent:
    def __init__(self,codename, score):
        self.codename = codename
        self.score = score

agents = [Agent(codenames[i],scores[i]) for i in range(MAX_N)]

min_score_agent = agents[0]
for agent in agents[1:]:
    if min_score_agent.score > agent.score:
        min_score_agent = agent

print(min_score_agent.codename, min_score_agent.score)