import math 

class Category:
    def __init__(self, category):
        self.category = category;
        self.ledger = []
    
    def deposit(self, amount, description=""):
        """
        Adds a deposit to the ledger.
        :param amount: The amount deposited.
        :param description: A brief description (optional).
        """
        self.ledger.append({
            "amount": amount,
            "description": description
        })
    
    def withdraw(self, amount, description=""):
        """
        Adds a withdrawal to the ledger.
        :param amount: The amount to withdraw.
        :param description: A brief description (optional).
        :return: Boolean value indicating whether the withdrawal was successful.
        """
        if self.check_funds(amount):
            self.ledger.append({
                "amount": amount * -1,
                "description": description
            })
            return True
        return False
    
    def get_balance(self):
        """
        Returns the total balance from all ledger entries.
        :return: Total balance after all deposits and withdrawals.
        """
        return sum([item["amount"] for item in self.ledger])

    def transfer(self, amount, destination_category):
        """
        Takes an amount from this category and transfers to another category.
        :param amount: The amount to transfer.
        :param destination_category: The category to transfer to.
        """        
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination_category.category}")
            destination_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False
    
    def check_funds(self, amount):
        """
        Checks if the total amount from all ledger transactions is more than the given amount.
        :param amount: The amount to check the balance against
        """
        return self.get_balance() >= amount

    def __str__(self):
        """
        String representation of the Category object.
        Displays the title line, each ledger item, and the total balance.
        """
        output_str = f"{self.category:*^30}\n"
        for item in self.ledger:
            amount = item["amount"]
            description = item["description"][0:23]
            output_str += f"{description:<23} {amount:.2f}\n"
        
        output_str += f"Total: {self.get_balance():.2f}"
        
        return output_str

def create_spend_chart(categories):
    pass # Calculate total withdrawals per category
    withdrawals = [sum(item['amount'] for item in cat.ledger if item['amount'] < 0) for cat in categories]
    total_withdrawals = sum(withdrawals)

    # Calculate percentage spent by category (rounded down to nearest 10)
    percentages = [math.floor((w / total_withdrawals * 100)) if total_withdrawals != 0 else 0 for w in withdrawals]

    # Build the vertical bar chart lines
    chart_lines = []
    for i in range(100, -1, -10):
        line = f"{i:3d}| "
        for percent in percentages:
            line += "o  " if percent >= i else "   "
        #line += "  "  # Add two more spaces at the end for consistency
        chart_lines.append(line)

    # Create the horizontal line
    dash_line = "    " + "-" * (3 * len(categories) + 1)

    # Format the category names vertically
    max_len = max(len(cat.category) for cat in categories)
    vertical_names = []
    for i in range(max_len):
        line = "     "
        for cat in categories:
            line += cat.category[i] if i < len(cat.category) else " "
            line += "  "
        line = line.rstrip() + "  "  # Ensure trailing two spaces
        vertical_names.append(line)

    # Final result
    result = (
        "Percentage spent by category\n" +
        "\n".join(chart_lines) +
        "\n" + dash_line +
        "\n" + "\n".join(vertical_names)
    )

    return result

food = Category('Food')
food.deposit(900, 'deposit')
food.withdraw(100, 'milk')
clothing = Category('Clothing')
clothing.deposit(1000, 'initial deposit')
clothing.withdraw(200, 'shirts')
auto = Category('Auto')
auto.deposit(500, 'car funds')
auto.withdraw(300, 'tires')
print(create_spend_chart([food, clothing, auto]))
