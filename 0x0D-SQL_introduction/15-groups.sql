-- 15. Number by score
-- script that lists the number of records with the same score
SELECT score, COUNT(score) AS number from second_table
GROUP BY score ORDER BY number DESC;
