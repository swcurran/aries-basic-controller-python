FROM python:3

ADD aries_basic_controller aries_basic_controller
ADD requirements.txt .
ADD setup.py .
ADD README.md .
ADD demo/researcher.py .
ADD demo/data_owner.py .
ADD demo/agent.py .
RUN pip3 install --no-cache-dir -e .

