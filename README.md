README

### Intro

This is a little thing I did to decide what anime I should watch, because I’m an indecisive person who can’t decide for himself. 

The files are as follows:

### The Stuff Inside

calc.py: The program to calculate the “point values” of a show. Point values are based on certain factors as follows:

- How many more episodes I have to watch of it (if it’s a short, calculate based on time per episode times the # of episodes and then divide by 24 to get approx. number of full-length episodes)
	- Movie/short series (1-9 episodes) = +5 BP (Bogeun Points)
	- One cour series (10-19 episodes) = +3 BP
	- Two cour series (20-27 episodes) = 0 BP
	- Multi-cour series (28-99 episodes) = -3 BP
	- Hella long shows (100+ episodes) = -5 BP
- How many more seasons there are of it
	- None = +3 BP
	- One or Two = 0 BP
	- Three or more = -3 BP
- If more than one more season, how many episodes total?
	- One cour worth (10-19 episodes) = +2 BP
	- Two cour worth or more (20-100 episodes) = -2 BP
	- Hella long (100+ episodes) = -5 BP
- Essential anime series to watch? (kinda subjective I know)
	- yy (YES) = +10 BP
	- y (yes) = +4 BP
	- m (maybe) = +2 BP
	- n (no) = 0 BP
- Genre I like?
	- y (yes) = +3 BP
	- m (mmm…kinda) = 0 BP
	- n (no) = -3 BP
- Recommended to me personally?
	- y (yes) = +5 BP
	- c (by my long-distance friend) = +2 BP
	- n (no) = 0 BP
- Best Girl/Guy Regular in show? (also subjective)
	- y (yes) = +2 BP
	- n (no) = 0 BP
- Other Factors
	- Add/subtract depending on other factors

criteria.csv: The data file containing all of the data

calculated.csv: A data file with two columns: the show’s name and the point value associated with it adding up all of the factors. A higher point value means higher priority to watch, which is the main goal in all of this.

README.md: The file you're reading right now, dunderhead.

stats.py: A program to calculate some stats on the calculated.csv data. Nothing too complicated.

### Improvements/Future Things to Work On

Other than just adjusting the point values depending on which factors are important as well as adding other factors later down the road, I don’t think there’s much to be improved. Maybe streamline the code a little, but that’s a minor concern.

### Final Words

Thanks for looking at this code I guess. If you want to use something like this to decide shows for yourself, feel free to do so. Just credit me and stuff, you know the usual.
