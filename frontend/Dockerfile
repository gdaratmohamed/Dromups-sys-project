# **** Etape 1 : concstruction de l'image avec Node.js *****
# utiliser l'image officielle node.js version 20 comme base pour la construction
FROM node:20 AS builder
# Repartoire ou seront copies les fichiers et ou les commandes seront exucteés
WORKDIR /usr/src/app

#copier seulement le fichier package.json pour tirer parti du cache Docker
COPY package.json ./

# installer les dependances avec yarn
RUN yarn install

#copier les fichiers source dans l'image
COPY . .

# lancer la commmande de construction pour générer les fichiers optimisées
RUN yarn run build

# --------------------------------------------------------------
# **** Etape 2 : serveur de production avec nginx ****
# -------------------------------------------------------------


# utiliser une image legère d'nginx pour servir les fichiers statiques
FROM nginx:alpine

COPY --from=builder /usr/src/app/dist /usr/share/nginx/html


EXPOSE 80

CMD ["nginx" , "-g", "daemon off ;"]





