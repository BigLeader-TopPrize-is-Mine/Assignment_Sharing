-- 1번 문제
select profno as '교수번호', name '교수이름', id 'ID' 
from Professor
where id  < 'H';

-- 2번 문제
select profno as '교수번호', name '교수이름', deptno '교수번호'
from Professor
where deptno >= 101 AND deptno <= 102;

-- 3번 문제
select profno as '교수번호', name '교수이름', hpage '홈페이지'
from Professor
where hpage is not null;

-- 4번 문제
select profno as '교수번호', name '교수이름', deptno '교수번호', bonus 'BONUS'
from Professor
where deptno >= 101 AND deptno <= 102 AND bonus is not null;


-- 5번 문제
select studno as '번호', name '이름', deptno1 '학과번호'
from student 
where deptno1 = 101
UNION ALL
select profno as '교수번호', name '교수이름', deptno '학과번호'
from professor
where deptno = 101;
