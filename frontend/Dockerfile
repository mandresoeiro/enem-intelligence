# ==========================================================
# ⚛️ Frontend — Next.js + TypeScript + Sass
# ==========================================================
FROM node:20-alpine

# Diretório de trabalho
WORKDIR /usr/src/app

# Copia dependências
COPY package*.json ./

# Instala pacotes
RUN npm install

# Copia o restante do projeto
COPY . .

# Compila o projeto (opcional em dev)
RUN npm run build

# Expõe porta do Next.js
EXPOSE 3000

# Comando padrão
CMD ["npm", "run", "dev"]
