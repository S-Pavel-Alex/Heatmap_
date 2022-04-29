FROM python

WORKDIR /heatmap

COPY ./req.txt /heatmap/req.txt

RUN pip3 install -r req.txt

COPY . /heatmap

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]