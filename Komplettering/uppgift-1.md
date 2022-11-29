You arrive at Commander Lambdas spacebase at Venus fuel depot, only to discover it's protected by a password. The minions had written the password on a sticky note, but someone threw it out the air lock 

However, they do remember a few key facts about the password:

- It is a six-digit number
- The value is within the range given below
- Two adjacent digits are the same (like 22 in 122345)
- Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679)
- There was at least one even and one odd number

Other than the range rule, the following examples are true:

111112 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 5 -> 0).
123789 does not meet these criteria (no double).
111111 does not meet these criteria (all odd numbers)

How many different passwords within the range given below meet these criteria?

Starting from the number: 138345
All the way to, including the number: 836215

Write a python script that parse all numbers in the above given range, print only and  every number that fits into the rules above, print the total number of rows that fits this password requirement schema
