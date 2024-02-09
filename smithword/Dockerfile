FROM node:20.9

# install simple http server for serving static content
#RUN npm install -g http-server


# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
RUN mkdir client
RUN mkdir server
COPY ./client/package*.json ./client
COPY ./server/package*.json ./server

# install project dependencies
#RUN cd client
WORKDIR /app/client
RUN npm install ./client
# build app for production with minification
RUN npm --prefix ./client run build

#RUN cd server
WORKDIR /app/server
RUN npm install ./server
#RUN cd ..
# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .


#RUN npm run build
WORKDIR /app
RUN mv ./client/dist ../server/
#RUN cd ../server

EXPOSE 3000
EXPOSE 3001
CMD [ "node", "./server/index.js" ]