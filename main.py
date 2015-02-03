from tbay import User, Item, Bid, session, datetime

def main():
    
    # Creating rows for User table
    user = session.query(User).first()
    user.username = 'solange'
    session.commit()
    
    # Creating rows for Item table
    ball = Item()
    ball.name = 'ball'
    ball.description = 'Basketball'
    ball.start_time = datetime.utcnow
    session.add(ball)
    session.commit()
    
if __name__ == '__main__':
    main()