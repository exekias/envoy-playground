FROM golang:1.17

RUN mkdir /control
WORKDIR /control

COPY . .
RUN go build -o main .

CMD ["/control/main"]