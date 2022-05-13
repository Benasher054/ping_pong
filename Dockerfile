FROM ubuntu
WORKDIR /app
COPY app.py .
RUN  apt update
Run  apt install -y python3
Run  apt install -y python3-pip
RUN pip3 install flask
EXPOSE 5000
CMD FLASK_APP=/app/app.py flask run --host=0.0.0.0