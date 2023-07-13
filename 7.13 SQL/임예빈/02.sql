USE my_testdb;

# 1
CREATE TABLE customer4 (
	no INT NOT NULL,
    name VARCHAR(30) DEFAULT "AAA",
    tell VARCHAR(15) DEFAULT "111",
    email VARCHAR(100) DEFAULT "abc@def.net"
);

SELECT * from customer4;
DESC customer4;

# 2
ALTER TABLE customer4 MODIFY tell varchar(100);

INSERT INTO customer4 values( 2022001, '서진수', '02)111-2222', 'seojinsu@gmail.com');
INSERT INTO customer4 values( 2022002, '손기동', '031)234-5678', 'skdong@daum.net');
INSERT INTO customer4 values( 2022003, '정진교', '055)233-4678', 'jjk12345@naver.com');
INSERT INTO customer4 values( 2022004, '홍길동', '054)4567-0987', 'hongkd1234@gmail.com');
INSERT INTO customer4 values( 2022004, '일지매', '053)2233-4455', 'onejm2222@daum.net');
SELECT * from customer4;

# 3
CREATE TABLE customer5 AS SELECT name, tell from customer4;
SELECT * FROM customer5;

# 4
ALTER TABLE customer5 ADD birth VARCHAR(20) DEFAULT '9999-12-31';
SELECT * FROM customer5;