FROM travisci/ci-garnet:packer-1512502276-986baf0

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY commands.py /home/travis/
COPY build.sh /home/travis/
RUN chown -v travis. /home/travis/commands.py /home/travis/build.sh
