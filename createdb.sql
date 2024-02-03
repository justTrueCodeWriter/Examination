create table questions(
  question_id integer primary key,
  question text,
  correct_answer_number integer,
  difficulty_level integer
);
create table answers(
  question_id integer,
  answer text,
  difficulty_level integer
);
