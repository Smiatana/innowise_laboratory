drop table if exists students;
create table students (
    id integer primary key,
    full_name text,
    birth_year integer
);

drop table if exists grades;
create table grades (
    id integer primary key,
    student_id integer,
    subject text,
    grade integer,

    foreign key (student_id) references students(id)
);

insert into students (full_name, birth_year) values
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);

insert into grades (student_id, subject, grade) values
    (1, 'Math', 88),
    (1, 'English', 92),
    (1, 'Science', 85),
    (2, 'Math', 75),
    (2, 'History', 83),
    (2, 'English', 79),
    (3, 'Science', 95),
    (3, 'Math', 91),
    (3, 'Art', 89),
    (4, 'Math', 84),
    (4, 'Science', 88),
    (4, 'Physical Education', 93),
    (5, 'English', 90),
    (5, 'History', 85),
    (5, 'Math', 88),
    (6, 'Science', 72),
    (6, 'Math', 78),
    (6, 'English', 81),
    (7, 'Art', 94),
    (7, 'Science', 87),
    (7, 'Math', 90),
    (8, 'History', 77),
    (8, 'Math', 83),
    (8, 'Science', 80),
    (9, 'English', 96),
    (9, 'Math', 89),
    (9, 'Art', 92);

create index idx_grades_student_id on grades(student_id);
create index idx_students_full_name on students(full_name);
create index idx_students_birth_year on students(birth_year);
create index idx_grades_subject on grades(subject);
create index idx_grades_grade on grades(grade);

select g.grade from grades g 
join students s on g.student_id = s.id
where s.full_name = 'Alice Johnson';

select s.full_name, avg(g.grade)
from grades g join students s on g.student_id = s.id 
group by s.full_name;

select * from students where birth_year > 2004;

select subject, avg(grade) from grades group by subject;

select s.full_name, g.grade 
from students s join grades g on s.id = g.student_id
group by s.full_name having g.grade < 80; 