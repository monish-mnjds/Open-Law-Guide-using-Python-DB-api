create table lawyers(lawyername varchar(50), expertise varchar(50), phone varchar(50), fees varchar(50));
insert into lawyers values('senguttuvan','criminal law','9894123241','100000');
select * from lawyers;
update lawyers set lawyername='mr. senguttuvan' where fees =100000;
insert into lawyers values('mrs. manjula','family law','9894145545','10000');
insert into lawyers values('mr. sridhar','criminal law','9748545665','80000');
insert into lawyers values('mr. rajkumar','civil law','9845564452','70000');
insert into lawyers values('mrs. kamala','family law','8878454542','20000');
insert into lawyers values('mr. arivu','criminal law','8745545125','60000');
insert into lawyers values('mrs. udayavani','civil law','9894784456','30000');
insert into lawyers values('mr. prabhakar','criminal law','9894544551','50000');
insert into lawyers values('mr. rathinakumar','civil law','9894775445','40000');
insert into lawyers values('mrs. kanchana','civil law','8456664123','90000');
commit;
