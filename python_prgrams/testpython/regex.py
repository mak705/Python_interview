^ Matches the begning of a line
$ Matches the end of a line
. Mathches any character
\s Matches white space
\S Matches any non white space character
* Repeats a character zero or more times
*? Repeats a character zero or more times(non greedy)
+ Repeats a character one or more times
+? Repeats a character one or more times(non greedy)
[aeiou] Matches a single character in the listed set
[^XYZ] Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
( Indicates where string extraction has to start
) Indicates where string extraction has to end
##Fine Tunning Match
X-sieve: CMU Sieve 2.3
^X-\S+:
^ Match the start of chara
\S Match any non whitespace character
+ One or mor times(* means zero or more times)
-----------------------------------------------------------------------
^	Matches the beginning of a line
$	Matches the end of the line
.	Matches any character
\s	Matches whitespace
\S	Matches any non-whitespace character
*	Repeats a character zero or more times
*?	Repeats a character zero or more times (non-greedy)
+	Repeats a character one or more times
+?	Repeats a character one or more times (non-greedy)
[aeiou]	Matches a single character in the listed set
[^XYZ]	Matches a single character not in the listed set
[a-z0-9]	The set of characters can include a range
(	Indicates where string extraction is to start
)	Indicates where string extraction is to end
