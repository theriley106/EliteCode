# EliteCode
<p align="center">
  <img src="static/leetcode.png" width="250"/>
<h4 align="center">Strategically Shuffling Leetcode Questions to Optimize DS&A Study Time</h4>
</p>

### What does this do?

EliteCode sends an authenticated request to the following API endpoint on Leetcode:

```bash
https://leetcode.com/api/problems/all/
```

This endpoint contains all problem descriptions and your personal Leetcode solution history.  It saves the data locally

### What does "Strategically Shuffling Leetcode Questions" mean?

Leetcode has a "Shuffle" feature, but it simply generates a random question of any difficulty level.  EliteCode will generate a random question while taking into account specified difficulty weights.

For instance:

```bash
python elitecode --easy 5 --medium 3 --hard 1
```

Will generate random questions that most likely fall under easy or medium difficulty, with a small chance of the question being categorized as a hard difficulty.

```python
python elitecode --easy 1 --medium 5 --hard 1
```

Will generate questions that most likely fall under the *medium* difficulty, with a small chance of the question being categorized as either a medium or hard difficulty.

```python
python elitecode --easy 5 --medium 0 --hard 0
```

This can make it difficult if you're trying to 

My Leetcode strategy entails doing 2 new questions, and going back and re-solving an old question each day.  

EliteCode makes it really easy to
