FROM nginx:1.13-alpine
RUN rm /etc/nginx/conf.d/default.conf

# Note that this considers the context is at: ../../
# this dockerfile is located at: docker/proxy/
COPY docker/proxy/nginx.conf /etc/nginx/nginx.conf
COPY src/app/static usr/src/app/src/app/static
