class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __str__(self):
        entries = ''
        title = self.name.center(30, '*')
        for i in self.ledger:
            descr = i['description'][:23]
            am = i['amount']
            entries += f"{descr:23}{am:>7.2f}\n"
        entries += f"Total: {self.get_balance():.2f}"
        return f"{title}\n{entries}"

   
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -1 * amount, 'description': description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, name):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {name.name}")
            name.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

   

       

def create_spend_chart(categories):
    title = "Percentage spent by category"
    all_withd = []

    for category in categories:
        cat_withd = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                cat_withd += abs(entry['amount'])
        all_withd.append(cat_withd)    

   
    percentages = []
    total = sum(all_withd)
    for i in all_withd:
        #just for myself not to forget: (i / total * 100) gets the raw percentage
        # // 10 * 10 rounds it down to the nearest 10
        perc = int(i / total * 100) // 10 * 10
        percentages.append(perc)
   
    chart = title +'\n'
    for lab in range(100, -1, -10):
        chart += f"{lab:>3}|"
        for p in percentages:
            if p >= lab:
                chart += ' o '
            else:
                chart += '   '
        chart += ' \n'
    chart += '    ' + '-' * 3 * len(categories)+ '-' + '\n'
   
    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        chart += '    '
        for category in categories:
            if i < len(category.name):
                chart += f" {category.name[i]} "
            else:
                chart += "   "
   

        if i < max_len - 1:
            chart += " \n"
        else:
            chart += " "
   
    return chart





   




