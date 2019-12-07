CREATE OR REPLACE FUNCTION pseudo_encrypt(SEQUENCE text) returns int AS $$
DECLARE
l1 int;
l2 int;
r1 int;
r2 int;
sid int;
i int:=0;
BEGIN
    SELECT nextval(SEQUENCE) INTO sid;
    l1:= (sid >> 16) & 65535;
    r1:= sid & 65535;
    WHILE i < 3 LOOP
        l2 := r1;
        r2 := l1 # ((((1166 * r1 + 150889) % 714025) / 714025.0) * 32767)::int;
        l1 := l2;
        r1 := r2;
        i := i + 1;
    END LOOP;
    RETURN ((r1 << 16) + l1);
END;
$$ LANGUAGE plpgsql strict immutable;

CREATE SEQUENCE message_sequence
    START WITH 1
    INCREMENT BY 1
    MINVALUE 1
    NO MAXVALUE
    CACHE 1;

CREATE TABLE message (
    id integer PRIMARY KEY DEFAULT pseudo_encrypt('message_sequence'),
    subject text NOT NULL,
    message text NOT NULL
);