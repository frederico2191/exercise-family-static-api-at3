from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "first_name": "John",
                "last_name": "Jackson",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
             {
                "first_name": "Jane",
                "last_name": "Jackson",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "first_name": "Jimmy",
                "last_name": "Jackson",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 5)

    def add_member(self, member):
        # fill this method and update the return
        if not member['id']: member['id']=self._generateId()
        member ["last_name"] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if "id" in member and member["id"] == id:
                self._members.remove(member)
                break

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if "id" in member and member["id"] == id:
                return member
        
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
