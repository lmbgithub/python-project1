FROM python:3.9-bullseye
LABEL version="0.0.1" \
maintainer="Luis Manuel Barrios <luis@bv.studio>"

RUN mkdir /home/papp
RUN groupadd -r papp && useradd -g papp -m -u 1234 papp
RUN chown -R papp:papp /home/papp

USER 1234

# working directory
WORKDIR /home/papp

COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]