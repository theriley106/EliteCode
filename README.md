# EliteCode
<p align="center">
  <img src="static/leetcode.png" width="250"/>
<h4 align="center">Strategically Shuffling Leetcode Questions to Optimize DS&A Study Time</h4>
</p>

### What is the point of this program?

My interview preparation strategy involves doing 2 new Leetcode questions each day, and going back and re-solving an old question that was completed during a previous session.  

It's really easy to hit this 2 question target by picking questions that can be solved in a very similar way.  For instance:

- [231. Power of Two](https://leetcode.com/problems/power-of-two/)
- [326. Power of Three](https://leetcode.com/problems/power-of-three/)
- [342. Power of Four](https://leetcode.com/problems/power-of-four/)

To prevent this, I typically use the shuffle feature on Leetcode to pick random questions, but sometimes there will be 2 difficult questions in a row that are categorized as "Hard" and can take an hour or more to solve.

This program strategically shuffles Leetcode questions in a way that optimizes interview preparation/DS&A study time.

### What does "Strategically Shuffling Leetcode Questions" mean?

Leetcode has a "Shuffle" feature, but it simply generates a random question of any difficulty level.  EliteCode will generate a random question while taking into account specified difficulty weights.

For instance:

```bash
python elitecode --easy 5 --medium 3 --hard 1
```

Will generate random unsolved questions that most likely fall under *easy* or *medium* difficulty, with a small chance of the question being categorized as *hard*.

Meanwhile,

```bash
python elitecode --easy 1 --medium 5 --hard 1
```

Will generate unsolved questions that most likely fall under the *medium* difficulty, with a small chance of the question being categorized as *easy* or *hard*.

```bash
python elitecode --easy 5 --medium 0 --hard 0
```

Will only generate unsolved Leetcode questions that are categorized as *easy*.

The program has default weights that are used if no command line arguments are passed:

```javascript
{'medium': 30, 'hard': 10, 'easy': 60}
```

### How do you access my Leetcode question history?

EliteCode sends an authenticated request to the following API endpoint on Leetcode:

```bash
https://leetcode.com/api/problems/all/
```

This endpoint contains all problem descriptions and your personal Leetcode solution history.  It saves the data locally, and filters out questions that can only be accessed with a Leetcode premium account.

### How do I change the number of questions returned?

Simply use the "old" or "new" command line argument to specify the number of questions generated.  For example:

```bash
python elitecode --easy 5 --medium 0 --hard 0 --new 10
```

### How do I regenerate my Leetcode problem list to reflect new questions?

```bash
python elitecode --regenerate
```

