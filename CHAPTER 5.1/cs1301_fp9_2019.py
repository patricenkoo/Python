CS1301 Final Problem 9
 Bookmark this page
For our last data analysis-inspired problem, let's go back to one of my favorite examples: Pokemon. Pokemon is a popular video game franchise by Nintendo which features over 800 monsters, called Pokemon, each with unique names, types, and statistics.

The dataset you'll have for this problem contains every Pokemon through Generation 7, including their alternate forms. You don't need to understand Pokemon to solve this problem, though: games are just good candidates for this kind of analysis because they often have well-formed, complete datasets.

To solve these problems, you just need to know a couple things. First, each row of the dataset corresponds to a Pokemon. Each row has 13 columns, in this order:

Number: The numbered ID of the Pokemon, an integer
Name: The name of the Pokemon, a string
Type1: The Pokemon's primary type, a string
Type2: The Pokemon's secondary type, a string (this may be blank; you may assume Type1 and Type2 will never be the same)
HP: The Pokemon's HP statistic, an integer in the range 1 to 255
Attack: The Pokemon's Attack statistic, an integer in the range 1 to 255
Defense: The Pokemon's Defense statistic, an integer in the range 1 to 255
SpecialAtk: The Pokemon's Special Attack statistic, an integer in the range 1 to 255
SpecialDef: The Pokemon's Special Defense statistic, an integer in the range 1 to 255
Speed: The Pokemon's Speed statistic, an integer in the range 1 to 255
Generation: What generation the Pokemon debuted in, an integer in the range 1 to 7
Legendary: Whether the Pokemon is considered "legendary" or not, either TRUE or FALSE (for you hardcore fans, we've grouped Legendary and Mythical Pokemon together for simplicity)
Mega: Whether the Pokemon is "Mega" or not, either TRUE or FALSE
Use this information to answer the questions below. Note that although you can do this problem without objects, it will probably be much easier if you initially create a Pokemon object with the 13 attributes above, add a method for calculating a total power based on the sum of those six stats (HP, Attack, Defense, SpecialAtk, SpecialDef, and Speed), read the file into a list of instances of that object, and then do your reasoning based on that list.

CS1301 Final Problem 9 (External resource)

CS1301 Final Problem 9
0.0/3.0 points (graded)
How many Pokemon have only one type? In other words, for how many Pokemon is Type2 blank?
  unanswered 
 
What is the most common type? Include both Type1 and Type2 in your count.
  unanswered 
What Pokemon has the highest HP statistic?
  unanswered 
Excluding Pokemon that are either Mega or Legendary, what Pokemon has the highest Defense statistic?
  unanswered 
Among Legendary Pokemon, what is the most common type? Include both Type1 and Type2 in your count.
  unanswered 
In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed), what is the weakest Legendary Pokemon? If there is a tie, list any of the tying Pokemon.
  unanswered 
In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed), what is the strongest non-Legendary, non-Mega Pokemon? If there is a tie, list any of the tying Pokemon.
  unanswered 
What type has the highest average Speed statistic? Include both Type1 and Type2 in your calculation.
  unanswered 
Rounded to the nearest integer, what is that highest average Speed statistic? Include both Type1 and Type2 in your calculation.
  unanswered 
 
Among all 7 Pokemon generations, which generation had the highest average sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?
  unanswered 
 
Rounded to the nearest integer, how much higher was that statistic than the next-closest generation's average sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?
  unanswered 
 
Rounded to the nearest integer, how much higher is the average sum of all six stats among Mega Pokemon than their non-Mega versions? Note that Mega Pokemon share the same Number (the first column) as their non-Mega versions, which will allow you to find all Pokemon that have a Mega version.
  unanswered 
 
SubmitSome problems have options such as save, reset, hints, or show answer. These options follow the Submit button.