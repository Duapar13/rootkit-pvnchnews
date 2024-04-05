import requests
import random
import string
import os
from tqdm import tqdm

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_likes(post_id, num_executions, action_type=1):
    if action_type == 1:
        action_name = "likes"
    elif action_type == 2:
        action_name = "dislikes"
    else:
        print("Type d'action non valide.")
        return
    
    url = f"https://tanguygibrat.fr/projets/pvnchnews/action.php?t={action_type}&id={post_id}"
    token = "967a3600229fc1eb821a8d8a68ddce172d1ff0ff66a4a329a6dd7b4c8f72289c"
    actions = 0

    def send_request(_):
        pseudo = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
        cookies = {'pseudo': pseudo, 'token': token}
        response = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            return 1
        return 0

    for _ in tqdm(range(num_executions), desc=f"Adding {action_name}"):
        result = send_request(None)
        actions += result

    print(f"Total de {action_name} : {actions}")

def add_comments(post_id, num_executions):
    url = f"https://tanguygibrat.fr/projets/pvnchnews/post.php?id={post_id}"
    token = "967a3600229fc1eb821a8d8a68ddce172d1ff0ff66a4a329a6dd7b4c8f72289c"
    comments = 0

    def send_request(_):
        pseudo = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
        cookies = {'pseudo': pseudo, 'token': token}
        data = {'texte': "sdfsdfsdfsd", 'commenter': "Commenter"}
        response = requests.post(url, cookies=cookies, data=data)
        if response.status_code == 200:
            return 1
        return 0

    for _ in tqdm(range(num_executions), desc="Adding comments"):
        result = send_request(None)
        comments += result

    print(f"Total de commentaires : {comments}")

def delete_post(post_id, pseudo):
    url = f"https://tanguygibrat.fr/projets/pvnchnews/delete_post.php?del={post_id}"
    token = "967a3600229fc1eb821a8d8a68ddce172d1ff0ff66a4a329a6dd7b4c8f72289c"
    success = 0

    def send_request(_):
        cookies = {'pseudo': pseudo, 'token': token}
        response = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            return 1
        return 0

    for _ in tqdm(range(1), desc="Deleting post"):
        result = send_request(None)
        success += result

    if success:
        print(f"Article {post_id} supprimé avec succès.")
    else:
        print(f"Impossible de supprimer l'article {post_id}.")

def main():
    while True:
        clear_screen()
        print("Menu:")
        print("1. Rajouter des likes à un post")
        print("2. Rajouter des commentaires à un post")
        print("3. Rajouter des dislikes à un post")
        print("4. Supprimer un article de blog")
        print("5. Quitter")
        
        choice = input("Choisissez une option : ")
        
        if choice == "1":
            post_id = input("Entrez l'ID du post : ")
            num_executions = int(input("Combien de fois voulez-vous exécuter le script ? "))
            add_likes(post_id, num_executions, action_type=1)
        elif choice == "2":
            post_id = input("Entrez l'ID du post : ")
            num_executions = int(input("Combien de fois voulez-vous exécuter le script ? "))
            add_comments(post_id, num_executions)
        elif choice == "3":
            post_id = input("Entrez l'ID du post : ")
            num_executions = int(input("Combien de fois voulez-vous exécuter le script ? "))
            add_likes(post_id, num_executions, action_type=2)
        elif choice == "4":
            post_id = input("Entrez l'ID de l'article à supprimer : ")
            pseudo = input("Entrez le pseudo de l'auteur de l'article : ")
            delete_post(post_id, pseudo)
        elif choice == "5":
            break
        else:
            print("Option invalide.")
        
        input("Appuyez sur Entrée pour revenir au menu.")

if __name__ == "__main__":
    main()
