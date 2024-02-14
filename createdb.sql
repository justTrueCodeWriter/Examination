create table questions(
  question_id integer primary key,
  question text,
  difficulty_level integer
);

create table answers(
  question_id integer,
  answer text,
  is_correct boolean,
  difficulty_level integer
);
