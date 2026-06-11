CREATE table newest AS
  SELECT title, year from titles order by year desc limit 10;


CREATE table dog_movies AS 
  SELECT title, character from titles, principals on titles.tconst=principals.tconst where character like "%dog%";


CREATE table leads AS 
  SELECT name, count(*) as lead_roles from names, principals 
  on names.nconst=principals.nconst 
  where ordering=1 
  group by names.nconst
  having count(*) > 10;


CREATE table long_movies AS 
  SELECT (year - year%10) || "s" as decade, count(*) as count from titles
  where runtime > 180
  group by (year - year%10) || "s";
  

