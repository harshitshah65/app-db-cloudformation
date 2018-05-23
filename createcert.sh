openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365 -subj "/C=US/ST=Oregon/L=Portland/O=Jio/CN=localhost"
