FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r requirements.txt
RUN chmod ugo+rwx entrypoint.sh

COPY . .

RUN chmod +x /usr/src/app/entrypoint.sh
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]