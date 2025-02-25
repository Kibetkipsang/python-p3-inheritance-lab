#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    def learn(self, new_knowledge):
        if isinstance(new_knowledge, str) and new_knowledge.strip():
            self.knowledge.append(new_knowledge)
            return f"Learned: {new_knowledge}!"
        else:
            "No new knowledge!"
        