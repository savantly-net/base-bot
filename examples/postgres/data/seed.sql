-- seed.sql
CREATE TABLE documents (
  id SERIAL PRIMARY KEY,
  text TEXT,
  title TEXT
);

INSERT INTO documents (text, title) VALUES ('Document 1 text', 'Document 1');
INSERT INTO documents (text, title) VALUES ('Document 2 text', 'Document 2');
INSERT INTO documents (text, title) VALUES ('Document 3 text', 'Document 3');
