ALTER TABLE pessoas ADD genero VARCHAR(1) NOT NULL AFTER nascimento
UPDATE pessoas SET genero = 'F' WHERE id = 1