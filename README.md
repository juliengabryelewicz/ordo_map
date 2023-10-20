# Ordo_map

Application Ordo permettant d'afficher une carte du monde et d'y ajouter des points à cliquer selon votre convenance.

Vous pouvez créer un fichier sous le nom de ordo_map.json dans le dossier parameters de votre application Ordo et y ajouter les points de votre choix dans un tableau : 

```
{
     "markers" : [
        {
            "title":"Mon titre",
            "lat":50.7333,
            "lon":2.2833,
            "width_popup" : 400,
            "height_popup" : 200,
            "content":"Mon contenu"
        }
    ],
    "lat": 50.6394,
    "lon": 3.057,
    "zoom": 5
}
```

Les paramètres lat, lon et zoom à coté de markers sont les paramètres génériques de la carte.

## Ajouter l'application

Sur Ordo, déposer ce dossier dans "plugins" dans votre application Ordo.

Puis, sur parameters/ordo.json, ajouter Ordo_map de cette manière : 

```
{
    "plugins" : ["ordo_map"]
}
```
