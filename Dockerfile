FROM nikolaik/python-nodejs:latest

WORKDIR /Studenthut

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

WORKDIR /Studenthut/frontend/
COPY frontend/package*.json .
RUN npm install

WORKDIR /Studenthut/
COPY . .

WORKDIR /Studenthut/frontend/
COPY frontend/ .
RUN npm run build
RUN rm -rf node_modules

EXPOSE 8000

WORKDIR /Studenthut/
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
