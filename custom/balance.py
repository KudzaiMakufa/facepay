from account.models import Account
from statement.models import Statement
class Balance():

    def check_balance(self,account):
        account = Account.objects.get(account=account)
        # account = Account.objects.all()
        return account
    def transferout(self,account , amount):
        account = Account.objects.get(account=account)
       
        account.amount  = account.amount - amount
        account.save()
        return account
    def transferin(self,account , amount):
        account = Account.objects.get(account=account)
       
        account.amount  = account.amount + amount
        account.save()
        return account
    def statementcreate(self,data):

        statement = Statement.objects.create(**data)
        print(statement)
    
    def getuserd(self,account):
        account = Account.objects.get(user_id=user_id)
       
        account.amount  = account.amount + amount
        account.save()
        return account
        
       
        
        return statement

