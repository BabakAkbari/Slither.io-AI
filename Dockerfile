FROM ubuntu

RUN apt-get update && apt-get clean && apt-get install -y \
    x11vnc \
    xvfb \
    fluxbox \
    wmctrl \
    wget \
    gnupg \
    gnupg2 \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get -y install google-chrome-stable

RUN apt-get update && apt-get install -y \
    python3 \
    python3-setuptools \
    python3-pip\
    unzip \
    curl

RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

RUN pip3 install selenium

RUN cd /home
RUN wget https://bintray.com/tigervnc/stable/download_file?file_path=tigervnc-1.10.1.x86_64.tar.gz
RUN ls -all
RUN mv download_file?file_path=tigervnc-1.10.1.x86_64.tar.gz tigervnc-1.10.1.x86_64.tar.gz
RUN tar xzf tigervnc-1.10.1.x86_64.tar.gz
RUN cd /tigervnc-1.10.1.x86_64 && chown -R root:root usr && ls && mv usr local && tar czf local.tgz local && tar xzf local.tgz -C /usr/ && update-icon-caches /usr/local/share/icons/*

RUN useradd apps \
    && mkdir -p /home/apps \
    && chown -v -R apps:apps /home/apps
RUN chmod 777 /home/apps
#RUN export DISPLAY=:0
#COPY bootstrap.sh /
#RUN chmod 777 /bootstrap.sh
COPY . /home/apps
RUN chmod 777 /home/apps
#CMD '/bootstrap.sh'
