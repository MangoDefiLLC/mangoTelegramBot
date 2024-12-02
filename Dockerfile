# Base image
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port (optional for a bot, mainly for health checks)
EXPOSE 3000

# Command to run the bot
CMD ["node", "app/app.js"]
