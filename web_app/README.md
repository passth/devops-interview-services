# Web app

A Python server that renders the user interface, accepts files from users, and communicates with the PDF miner to extract text from PDFs. Use the instructions at the parent folder to execute this application locally.

## Environment variables

| Key         | Description | Example |
| -----------  | ----------- |----------- |
| `SECRET_KEY` | A string that is used to provide cryptographic signing, and should be kept secret. | django-insecure-d462upu)4h4fx!8vl1%g+^#rjk)m#y^1tsul89bq^ttgni+9k= |
| `DB_URL` | The connection string to the database | postgres://user:password@host:port/dbname |
| `ALLOWED_HOSTS` | A list of host/domain names that your Django site is allowed to serve. The format for the environment variable is a comma separated string. | localhost,otherdomain |
| `PDF_MINER_API_URL` | The base URL to access the PDF miner application | http://localhost:8001/
