FROM ubuntu:20.04

COPY resources resources

RUN bash resources/utils.sh
RUN bash resources/isolate.sh

RUN rm -rf resources

COPY langagues langagues
RUN bash langagues/python.sh
RUN bash langagues/node.sh

RUN rm -rf langagues
