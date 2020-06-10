FROM python:3

ADD aries_basic_controller aries_basic_controller
ADD requirements.txt .
ADD setup.py .
ADD README.md .

RUN pip3 install --no-cache-dir -e .


#ADD demo/.env .
ADD demo/example.py .
EXPOSE 443

CMD [ "python", "./example.py" ]