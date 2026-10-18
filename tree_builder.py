
class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node.
        right (EmployeeNode): The right child node.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        side = side.strip().lower()

        if side not in ("left", "right"):
            print("Error: Side must be left or right.")
            return False

        # Start searching from the root.
        if current_node is None:
            if self.root is None:
                print("Error: Add a team lead first.")
                return False
            current_node = self.root

        # Insert the employee if the manager is found.
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is not None:
                    print(f"Error: {manager_name}'s left position is occupied.")
                    return False
                current_node.left = EmployeeNode(employee_name)
            else:
                if current_node.right is not None:
                    print(f"Error: {manager_name}'s right position is occupied.")
                    return False
                current_node.right = EmployeeNode(employee_name)

            return True

        # Recursively search the left branch.
        if current_node.left is not None:
            if self.insert(
                manager_name, employee_name, side, current_node.left
            ):
                return True

        # Recursively search the right branch.
        if current_node.right is not None:
            if self.insert(
                manager_name, employee_name, side, current_node.right
            ):
                return True

        # Report a missing manager after searching the whole tree.
        if current_node is self.root:
            print(f"Error: Manager '{manager_name}' was not found.")

        return False

    def print_tree(self, node=None, level=0):
        # Begin at the root when print_tree() is called normally.
        if node is None:
            if level == 0:
                node = self.root
                if node is None:
                    print("The company directory is empty.")
                    return
            else:
                return

        print("  " * level + "- " + node.name)

        # Print each branch recursively.
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# Test your code here









# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")




# DESIGN MEMO
#
# Recursive insertion works by starting at the root of the company tree
# and checking whether the current employee is the manager who should
# receive a new employee. If the manager is found, the program checks
# whether the requested left or right position is available. If the
# position is empty, a new EmployeeNode is created and connected to
# the manager. If the manager is not found, the method searches the
# left and right branches recursively until it finds the correct manager.
#
# One challenge with insertion is keeping track of the current node
# while searching through different levels of the tree. Another
# challenge is handling errors when a manager does not exist or the
# requested position is already occupied. The program must search both
# branches before deciding that a manager cannot be found. It must also
# check that the requested side is either left or right. These checks
# help keep the reporting structure organized and prevent incorrect
# insertions.
#
# Trees are useful in real-world systems when information has a natural
# hierarchy. A company directory is a good example because employees
# report to managers, who may report to other managers. Trees are also
# useful for organizing computer files and folders, representing
# website elements, and supporting decision-making systems. Compared
# with a flat collection of data, a tree makes parent-child relationships
# easier to represent and follow. This assignment uses a binary tree,
# which allows each employee to have up to two direct reports. Although
# this structure works for the assignment, real companies may need
# trees that allow each manager to supervise more than two employees.
