# Number Guessing Game

## Test Plan

Here is the testing I did to make sure everything works correctly according to the project requirements.

| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---|---|---|---|---|
| 1 | "Too low" hint | Guessed 4 when the secret was 57 | Game should say "TOO LOW!" | Printed "The entered number is TOO LOW! You have 9 attempts remaining." | Yes |
| 2 | "Too high" hint | Guessed 60 when the secret was 57 | Game should say "TOO HIGH!" | Printed "The entered number is TOO HIGH! You have 8 attempts remaining." | Yes |
| 3 | Correct guess | Guessed 57 on the 3rd try | Print a win message showing 3 attempts | Printed "57 is the correct number! You guessed it in 3 attempts. Well done!" | Yes |
| 4 | Input validation | Typed "abc" instead of a number | Reject input | Printed "Invalid input" and asked again | Yes |
| 5 | Blank input | Just pressed Enter without typing | Reject input | Printed "Invalid input" | Yes |
| 6 | Out of range guess | Guessed 60 on Easy mode | Reject input | Printed "Invalid input" | Yes |
| 7 | Negative number guess | Guessed -5 | Reject input | Printed "Invalid input" | Yes |
| 8 | Easy mode selection | Picked level 1 | Range 1-50, max 10 attempts | Range was 1-50, allowed 10 attempts | Yes |
| 9 | Medium mode selection | Picked level 2 | Range 1-100, max 8 attempts | Range was 1-100, allowed 8 attempts | Yes |
| 10 | Hard mode selection | Picked level 3 | Range 1-500, max 10 attempts | Range was 1-500, allowed 10 attempts | Yes |
| 11 | Out of attempts loss | Purposely missed 8 guesses on Medium | Game ends, reveals the secret number | Game ended and printed "You've used all your attempts. The correct number was 57." | Yes |
| 12 | Time challenge timeout | Picked mode 2 and waited 61 seconds | Game ends, reveals the secret number | Game ended and printed "You've run out of time! The correct number was 57." | Yes |
| 13 | Timer countdown display | Started Time Challenge and waited 5s | Shows remaining time before next guess | Console printed "You have 55 seconds remaining." | Yes |
