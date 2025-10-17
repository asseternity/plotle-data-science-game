# --- PLOTLE ---
# - browser
# - logic game 
# - daily/weekly 
# - uses Pandas / data science

# Idea: 
# A fake videogame esports tournament just happened
# On the left, you see probabilities of events happening from the game code
# On the right, you see player stats, how many times things have happened across playtime
# By identifying statistically improbable stats of a player, you have to finalize your list of cheaters and non-cheaters
# There's tons of stats everywhere
# Statistics differ based on player's "role" on the team, making just looking at the numbers harder
# By picking players and particular stats and the type of graph, you can generate the plot in the central window (PLOTLE!)
# You are given bonus points if you highlight which stats gave away the cheater
# Negative points for mistakes on stats or cheaters
# The faster you do - the more points
# Weekly leaderboards, with week's winners recorded forever

# Workflow:

# Iterate: make a simple prototype first with:
# - random seed
# - random team names
# - random usernames
# - 3 players per team
# - 2 teams
# - 2 possible roles
# - 5 stats per player

# 1) Do the backend first
# [v] make one team's total deaths equal total kills of the opposition
# [v] add game elements that are chance/timing based --- something has a chance to happen once per in game minute
# at first: just runes spawning and neutral monsters being killed
# add to the player's stats 
# [v] incorporate runes and neutrals into how the game determines player stats and, therefore, the winners!
# [v] add cheaters

# 2) PIVOT: make it an actual game: esports manager
# [_] have player objects where their skills affect the outcome
# [_] player generators
# [_] recruitment systems
# [_] find cheaters among opposition based on data
# [_] incorporate pandas: generate a DF from the match report and interactive / changeable visualizations 
# [numbers / players / type of graph]

# 3) POLISH
# [_] expand 
# [_] create a game mechanics / chances print with lore and explanations
# [_] tweak cheating numbers
# [_] a console game to spot cheaters: with time and accuracy based score
# [_] now full console version like above description 

# 4) Local frontend
# 5) Host
# 6) DB [or have local savegame files instead of a DB]
# 7) Maybe even add a pygame dots fighting!
# 8) So the game will have two windows -> data science recruitment / cheating highlighting & match window