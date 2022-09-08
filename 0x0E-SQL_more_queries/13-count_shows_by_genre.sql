-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT g.`name`
  FROM `hbtn_0d_tvshows` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`

       INNER JOIN `hbtn_0d_tvshows` AS t
       ON t.`id` = s.`show_id`
       WHERE t.`title` = "Dexter"
 ORDER BY g.`name`;
