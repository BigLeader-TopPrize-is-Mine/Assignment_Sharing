use my_testdb ;
select * from professor;

desc professor;

# 1
select
profno as 교수번호, name 교수이름, id ID
from professor where id < 'h';

# 2
select
profno as 교수번호, name 교수이름, deptno 학과번호
from professor where deptno IN(101, 102) ;

# 3
select
profno as 교수번호, name 교수이름, hpage 홈페이지주소
from professor where hpage IS NOT NULL ;

# 4
select
profno as 교수번호, name 교수이름, deptno 학과번호, bonus BONUS
from professor where deptno IN (101, 102) AND bonus IS NOT NULL ;

# 5
select
studno as 학번, name 이름, deptno1 1전공번호
from student ;

select
profno as 교수번호, name 교수이름, deptno 학과번호
from professor ;

select
studno as 번호, name 이름, deptno1 학과번호
from student 
where deptno1 = 101
UNION ALL
select
profno as 교수번호, name 교수이름, deptno 학과번호
from professor
where deptno = 101;



