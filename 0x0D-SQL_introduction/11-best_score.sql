-- Lists all records with score >= 10 of the table second_table of the database
SELECT score, name FROM second_table
       WHERE score >= 10
       ORDER BY score DESC, name;