# Write your MySQL query statement below
select *,if(z < x+y and  y < x+z and x<y+z,'Yes','No') as triangle from Triangle 