show databases;
use my_testdb;
show tables;

-- 1번
select profno as '교수번호', name '교수 이름', id 'ID' from professor where name < 'H';

-- 2번
select profno as '교수번호', name '교수 이름', deptno '학과번호' from professor WHERE deptno = 101 or deptno = 102;

-- 3번
select profno as '교수번호', name '교수 이름', hpage '홈페이지 주소' from professor where hpage IS NOT NULL;

-- 4번
select profno as '교수번호', name '교수 이름', deptno '학과번호', bonus 'BONUS' 
from professor WHERE bonus IS NOT NULL ORDER BY name;

-- 5번
SELECT studno as '번호', name '이름', deptno1 '전공번호' from student where deptno1 = 101
UNION
SELECT deptno as '번호', name '이름', deptno '학과번호' from professor where deptno = 101; 

