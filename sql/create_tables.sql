USE filed;

CREATE TABLE IF NOT EXISTS payment_registry
(
  uuid VARCHAR(256) NOT NULL,
  credit_card_number INT(16) NOT NULL,
  card_holder VARCHAR(256) NOT NULL,
  expiration_date datetime NOT NULL,
  transaction_date datetime NOT NULL,
  security_code INT(3),
  amount DECIMAL(8,2),
  payment_gateway VARCHAR(128),
  transaction_status VARCHAR(64),

  CONSTRAINT PK_payment_registry PRIMARY KEY (uuid),
  CONSTRAINT CK_amount_positive CHECK (amount > 0)
);