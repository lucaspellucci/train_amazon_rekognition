FROM python:3

WORKDIR /work

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#COPY . .

#CMD [ "python", "./script.py" ]
ENTRYPOINT [ "python", "./script.py" ]
