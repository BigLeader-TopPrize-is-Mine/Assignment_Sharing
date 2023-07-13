-- 1번
select profno as 교수번호, name as 이름, id as ID
from Professor
where substring(id,1,1) between 'A' and 'G';

-- 2번
select profno as 교수번호, name 교수이름, deptno 학과번호
from Professor
where deptno in(101, 102);

-- 3번
select profno as 교수번호, name 교수이름, hpage 홈페이지주소
from Professor
where hpage is not null;

-- 4번
select profno as 교수번호, name 교수이름, deptno 학과번호, bonus as BONUS
from Professor
where deptno in(101,102) and bonus is not null;

-- 5번
select studno as 번호 , name 이름, deptno1 학과번호 
from Student
where deptno1 = 101
union all
select profno as 번호 , name 이름, deptno 학과번호
from Professor
where deptno = 101;


