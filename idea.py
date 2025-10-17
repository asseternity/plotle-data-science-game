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

# !!! UPDATED: half data mystery, half management sim !!!

# 1) Do the backend first
# [v] make one team's total deaths equal total kills of the opposition
# [v] add game elements that are chance/timing based --- something has a chance to happen once per in game minute
# at first: just runes spawning and neutral monsters being killed
# add to the player's stats 
# [v] incorporate runes and neutrals into how the game determines player stats and, therefore, the winners!
# [v] add cheaters

# 2) PIVOT: make it an actual game: esports manager
# [v] have player objects where their skills affect the outcome
# [v] IGL: gives +% or -% to other players' performances (not themselves) based on leadership stat | can be assigned and changed in Team class
# [_] create a system that will run 100 simulations and give me W-L to tell me balance
# [_] create manager / between matches UI
# [_] player generators
# [_] recruitment systems
# [_] switch players between roles
# [_] incorporate pandas: generate a DF from the match report and interactive / changeable visualizations 
# [numbers / players / type of graph]
# !!! Pandas layer – THE “ENGINE under the hood for the interactive portion. Each match can export a .csv or .pkl for reproducibility.
# [_] create post-match cheaters finding UI: 
# [LEFT]  Expected probabilities / baselines  
# [CENTER]  Interactive plot (generated with Pandas/Matplotlib/Plotly)  
# [RIGHT]  Player data / filters / suspected cheaters
# [_] find cheaters among opposition based on data for rewards and penalties on timing and accuracy

# 3) EXPAND and POLISH
# [_] add heroes and show specific heroes on the match report and hero descriptions on the game lore and mechanics info cards
# [_] more timing and chance based mechanics for ultimate data science
# [_] create a game mechanics / chances print with lore and explanations
# [_] tweak cheating numbers
# [_] Cheater realism – Instead of just scaling kills/assists, occasionally break correlations 
# (e.g., high kills but no runes taken, or extreme KDA inconsistency with team averages). That makes detection more subtle
# [_] Data storytelling – Add post-match “press report” text generated from outliers 
# (“Fans are questioning how ylari_x secured 47 kills with only 2 rune pickups…”).

# 4) Host
# 5) Local savegame files
# 6) Pygame dots fighting
# 7) So the game will have two windows -> data science recruitment / cheating highlighting & match window