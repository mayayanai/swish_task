FROM python:3.10.4-alpine
COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN  apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "./main.py" ]