from tkinter import TRUE


class User:
    def __init__(self, first_name, last_name, email, age, member, points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = 0
        self.gold_card_points = 0

    def display_info(self):
        print(f"First name: {self.first_name} Last name: {self.last_name} Email: {self.email} Age: {self.age} Rewards member: {self.is_rewards_member} Points: {self.gold_card_points}")
    
    #def enroll(self):
        #if self.is_rewards_member = True:
            #print()

    def spend_points(self, points):
        self.spend_points -= points

    def add_points(self, points):
        self.add_points += points

ichigo = User("Ichigo", "Kurosaki", "ichigo@bleach.com", "15", "True", "0")
van = User("Van", "Flyheight", "van@zoids.com", "14", "False", "0")
tanjiro = User("Tanjiro", "Kamado", "tanjiro@demonslayer.com", "13", "False", "0")

ichigo.spend_points(50)
ichigo.display_info()

van.spend_points(80)


