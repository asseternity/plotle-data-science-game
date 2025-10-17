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
# [_] add cheaters
# [_] create a game mechanics / chances print with lore and explanations
# [_] a console game to spot cheaters: with time and accuracy based score
# [_] now full console version like above description 

# 2) Then do the frontend locally
# 3) Then punch up the frontend
# 4) Then host
# 5) Then DB
