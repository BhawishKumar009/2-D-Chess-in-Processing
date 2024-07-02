# Welcome to code of 2-D Chess Game Implementation Using Python processing.

 
  
# GAME INFRORMATION
# The game  includes all chess moves except for castling, pawn promotion and en passant
# In order to make game fun, King can captured. 
# The aim would be to  play the shortest amount of time and make moves to capture King to win.

#GAME DETAILS
# This game incoporates features such as: 
# Proper Identation
# Varaibles , For Naming camelCase standard follow for most
# Functions ( Both Built-in and Created by me)
# Arrays
# Classes ( Approval given )
# For and While Loops 
# For user control: Mouse input and sound output
# Scoring System:  The one who captures King wins, also shows number of pieces captured
# Stages: MENU,INSTRUCTIONS,PLAY,RESULT
# Functional Programming combined with OOP

# ABOUT ME
# Name: KUMAR Bhawish
# STD ID : 23205172



# Next Comments would guide on how the game is implemented. 


# library for sound 
add_library('minim')
MusicPlayer=None

def setup():
    size(800, 1000)
    global whiteArr,blackArr,firstRun,W_MOVES,B_MOVES,id,turnCounter,Moves,GameStop,WhiteKinginCheck,BlackKinginCheck,kingMurdered
    global selectedP
    global capturedWhites,capturedBlacks
    global MusicPlayer
    # To Process Sound, Minim is used
    # Sound File are NON-COPYRIGHT hence free to use legally
    m = Minim(this)
    MusicPlayer= m.loadFile("Intro.mp3")
    MusicPlayer.play()
    # Calling Initialize to Setup the variables for first time  use
    Initialize()
    
    
    
# Initialize Sets up all the variables

def Initialize():
    global whiteArr,blackArr,firstRun,W_MOVES,B_MOVES,id,turnCounter,Moves,GameStop,WhiteKinginCheck,BlackKinginCheck,kingMurdered
    global selectedP
    global capturedWhites,capturedBlacks
    turnCounter=0
    capturedWhites=[]
    capturedBlacks=[]
    WhiteKinginCheck=False
    BlackKinginCheck=False
    kingMurdered=False
    Moves=[]
    id=None
    GameStop=False
    whiteArr=[]
    blackArr=[]
    W_MOVES=[]
    B_MOVES=[]
    Selected_Move=[]
    mousePressedOnce=False
    firstRun=True
    selectedP=None
    frameRate(30)
    
    global playButton, instructionButton,timeOptions,selectedTime,Exitbtn
    
    Exitbtn= None
    playButton = None
    instructionButton = None
    timeOptions = [1, 5, 10]
    selectedTime= None
    global GameState
    global firstTime
    global start_time,total_time
    global winner
    firstTime=True
    GameState=""
    GameStageOne()

    


# Classes have been used in this project after the approval. 
# The project include 2 classes : whitePiece and blackPiece.
# Both classes follow exactly same format/template. 
# Both classes include a number of varaibles of each piece to define it's position such as xpos, ypos are the x and y co-ordinates of the each piece
# set_Picture loads and displays the picture of each piece
# isValidPosition makes sure that move made is not out of the chess board
# AvailableMoves uses ids to generate moves of the piece. 
# All the other methods such as PawnMoves,BishopMoves are called by the AvailableMoves to generate the moves

class whitePiece(object):
    def __init__(self,xpos,ypos,id):
        self.xpos=xpos
        self.ypos=ypos
        self.id=id
        self.Moves=[]
        self.moves=[]
        self.original_x=xpos
        self.original_y=ypos
        
        
    def set_Picture(self,imgname):
        img=loadImage(imgname)
        image(img,self.xpos,self.ypos,100,100)
        
    def reset_to_original_position(self):
        self.xpos = self.original_xpos
        self.ypos = self.original_ypos
        
    def isValidPosition(self, xpos, ypos):
        return xpos >= 0 and xpos < 800 and ypos >= 0 and ypos < 800
    
     
    def BishopMoves(self):
        self.moves=[]
        # Daigonal Moves
        directions = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        
        
        for dx,dy in directions:
            bpc=0
            new_x=self.xpos+dx*100
            new_y=self.ypos+dy*100
            
            while self.isValidPosition(new_x,new_y) == True:
                if  isWhitePieceHere(new_x,new_y) == False:
                    if isBlackPieceHere(new_x,new_y) == False:
                        self.moves.append((new_x,new_y))
                        new_x+=dx*100
                        new_y+=dy*100
                    else:
                        if bpc == 0:
                            self.moves.append((new_x,new_y))
                            new_x+=dx*100
                            new_y+=dy*100
                            bpc=1
                            break
                        else:
                            break
                        
                else:
                    break
            
        return self.moves
    
    def KnightMoves(self):
        self.moves = []
        directions = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
    
        for dx, dy in directions:
            new_x = self.xpos + dx * 100
            new_y = self.ypos + dy * 100
        
            if self.isValidPosition(new_x, new_y):
                if not isWhitePieceHere(new_x, new_y):
                    self.moves.append((new_x, new_y))

        return self.moves

                
            
                
    
            
    def PawnMoves(self):
        self.moves=[]
        attacksAvail=False
        directions=[(-1,-1),(1,-1),(0,-1),(0,-2)]
        for i in range(4):
            new_x=self.xpos +  directions[i][0] * 100
            new_y=self.ypos +  directions[i][1] * 100
            if i == 0 or i == 1:
                # Check for attacks
                if isBlackPieceHere(new_x,new_y) == True:
                    self.moves.append((new_x,new_y))
                    attacksAvail=True
                     
                # append the attacks 
            if i == 3:    
                if self.ypos == 600 and attacksAvail == False:
                    self.moves.append((new_x,new_y))
            
            if i == 2:
                if isBlackPieceHere(new_x,new_y) ==  False:
                    self.moves.append((new_x,new_y))
                
        return self.moves

        
    def RookMoves(self):
        self.moves = []
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for dx,dy in directions:
            bpc=0
            new_x=self.xpos+dx*100
            new_y=self.ypos+dy*100
            
            while self.isValidPosition(new_x,new_y) == True:
                
                if  isWhitePieceHere(new_x,new_y) == False:
                    if  isBlackPieceHere(new_x,new_y) == False:
                        self.moves.append((new_x,new_y))
                        new_x+=dx*100
                        new_y+=dy*100
                    else:
                        if bpc == 0:
                            self.moves.append((new_x,new_y))
                            new_x+=dx*100
                            new_y+=dy*100
                            bpc=1
                            break
                        else:
                            break
                    
                else:
                    break

        return self.moves
    
    def QueenMoves(self):
        # Horizontal and Vertical 
        
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for dx,dy in directions:
            bpc=0
            new_x=self.xpos+dx*100
            new_y=self.ypos+dy*100
            
            while self.isValidPosition(new_x,new_y) == True:
                if  isWhitePieceHere(new_x,new_y) == False:
                    if isBlackPieceHere(new_x,new_y) ==  False:
                        self.moves.append((new_x,new_y))
                        new_x+=dx*100
                        new_y+=dy*100
                    else:
                        if bpc == 0:
                            self.moves.append((new_x,new_y))
                            new_x+=dx*100
                            new_y+=dy*100
                            bpc=1
                            break
                        else:
                            break
                    
                else:
                    break
        
        # Daigonal Moves
        directions = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        for dx,dy in directions:
            bpc=0
            new_x=self.xpos+dx*100
            new_y=self.ypos+dy*100
            
            while self.isValidPosition(new_x,new_y):
                if isWhitePieceHere(new_x,new_y) == False:
                    if isBlackPieceHere(new_x,new_y) == False:
                        self.moves.append((new_x,new_y))
                        new_x+=dx*100
                        new_y+=dy*100
                        
                    else:
                        if bpc == 0:
                            self.moves.append((new_x,new_y))
                            new_x += dx * 100
                            new_y += dy * 100
                            bpc=1
                            break
                        else:
                            break
                            
                else:
                    break

                
        return self.moves
    
    def KingMoves(self):
        directions=[(1, 0), (1, 1), (1, -1), (-1, 0),(-1, 1), (-1, -1), (0, 1), (0, -1)]
        
        for i in range(8):
            new_x=self.xpos+ directions[i][0]*100
            new_y=self.ypos+ directions[i][1]*100
            
            if self.isValidPosition(new_x,new_y):
                if isWhitePieceHere(new_x,new_y) == False:
                    self.moves.append((new_x,new_y))
               
                    
        return self.moves  
    
    def AvailableMoves(self):
        self.moves=[]
        
        #Pawn 
        if self.id >=0 and self.id <= 7 :
            return self.PawnMoves()
            
        #Bishop
        if self.id ==10 or self.id == 13:
            return self.BishopMoves()
            
            
              
        #Knight
        if self.id == 9 or self.id == 14:
            return self.KnightMoves()
    
            
        #Rook 
        if self.id == 8 or self.id == 15:
            return self.RookMoves()
            
        #Queen
        if self.id == 11:
            return self.QueenMoves()
            
        
        #King
        if self.id == 12:
            return self.KingMoves()
        
        
    # King making some moves invalid 
    
            
            
class blackPiece(object):
    def __init__(self,xpos,ypos,id):
        self.xpos=xpos
        self.ypos=ypos
        self.id=id
        self.Moves=[]
        self.moves=[]
        self.original_x=xpos
        self.original_y=ypos
        
        
    def set_Picture(self,imgname):
        img=loadImage(imgname)
        image(img,self.xpos,self.ypos,100,100)
    
    def reset_to_original_position(self):
        self.xpos = self.original_xpos
        self.ypos = self.original_ypos
        
        
    def isValidPosition(self, xpos, ypos):
        return xpos >= 0 and xpos < 800 and ypos >= 0 and ypos < 800
    
     
    def BishopMoves(self):
        self.moves=[]
        # Daigonal Moves
        directions = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        
        
        for dx,dy in directions:
            bpc=0
            new_x=self.xpos+dx*100
            new_y=self.ypos+dy*100
            
            while self.isValidPosition(new_x,new_y) == True:
                print("Bishop testing")
                print("bpc",bpc)
                
                if  isBlackPieceHere(new_x,new_y) == False:
                    if isWhitePieceHere(new_x,new_y) == False:
                        self.moves.append((new_x,new_y))
                        print(self.moves)
                        new_x+=dx*100
                        new_y+=dy*100
                    else:
                        if bpc == 0:
                            self.moves.append((new_x,new_y))
                            print(self.moves)
                            new_x+=dx*100
                            new_y+=dy*100
                            bpc=1
                            break
                        else:
                            print(self.moves)
                            break
                        
                else:
                    break
            
        return self.moves
    
    def KnightMoves(self):
        self.moves = []
        directions = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
    
        for dx, dy in directions:
            new_x = self.xpos + dx * 100
            new_y = self.ypos + dy * 100
        
            if self.isValidPosition(new_x, new_y):
                if not isBlackPieceHere(new_x, new_y):
                    self.moves.append((new_x, new_y))

        return self.moves
    
    
            
    def PawnMoves(self):
        self.moves=[]
        attacksAvail=False
        directions=[(-1,1),(1,1),(0,1),(0,2)]
        for i in range(4):
            new_x=self.xpos +  directions[i][0] * 100
            new_y=self.ypos +  directions[i][1] * 100
            if i == 0 or i == 1:
                # Check for attacks
                if isWhitePieceHere(new_x,new_y) == True:
                    self.moves.append((new_x,new_y))
                    attacksAvail=True
                     
                # append the attacks 
            if i == 3:    
                if self.ypos == 100 and attacksAvail == False:
                    self.moves.append((new_x,new_y))
            
            if i == 2:
                if isWhitePieceHere(new_x,new_y) == False:
                    self.moves.append((new_x,new_y))
                
        return self.moves
        

             

        
    def RookMoves(self):
        # Horizontal and Vertical 
        
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for dx,dy in directions:
            bpc=0
            new_x=self.xpos+dx*100
            new_y=self.ypos+dy*100
            
            while self.isValidPosition(new_x,new_y) == True:
                if  isBlackPieceHere(new_x,new_y) == False:
                    if isWhitePieceHere(new_x,new_y) == False:
                        self.moves.append((new_x,new_y))
                        new_x+=dx*100
                        new_y+=dy*100
                    else:
                        if bpc == 0:
                            self.moves.append((new_x,new_y))
                            new_x+=dx*100
                            new_y+=dy*100
                            bpc=1
                            break
                        else:
                            break
                    
                else:
                    break

        return self.moves  
    
    def QueenMoves(self):
        # Horizontal and Vertical 
        
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for dx,dy in directions:
            bpc=0
            new_x=self.xpos+dx*100
            new_y=self.ypos+dy*100
            
            while self.isValidPosition(new_x,new_y) == True:
                if  isBlackPieceHere(new_x,new_y) == False:
                    if isWhitePieceHere(new_x,new_y) == False:
                        
                        self.moves.append((new_x,new_y))
                        new_x+=dx*100
                        new_y+=dy*100
                    else:
                        if bpc == 0:
                            self.moves.append((new_x,new_y))
                            new_x+=dx*100
                            new_y+=dy*100
                            bpc=1
                            break
                        else:
                            break
                else:
                    break
        # Daigonal Moves
        directions = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        for dx,dy in directions:
            bpc=0
            new_x=self.xpos+dx*100
            new_y=self.ypos+dy*100
            
            while self.isValidPosition(new_x,new_y):
                if isBlackPieceHere(new_x,new_y) == False:
                    if isWhitePieceHere(new_x,new_y) == False:
                        self.moves.append((new_x,new_y))
                        new_x+=dx*100
                        new_y+=dy*100
                    else:
                        if bpc == 0:
                            self.moves.append((new_x,new_y))
                            new_x+=dx*100
                            new_y+=dy*100
                            bpc=1
                            break
                        else:
                            break
                else:
                    break
        return self.moves

    
    def KingMoves(self):
        directions=[(1, 0), (1, 1), (1, -1), (-1, 0),(-1, 1), (-1, -1), (0, 1), (0, -1)]
        
        for i in range(8):
            new_x=self.xpos+ directions[i][0]*100
            new_y=self.ypos+ directions[i][1]*100
            
            if self.isValidPosition(new_x,new_y):
                if isBlackPieceHere(new_x,new_y) == False:
                    self.moves.append((new_x,new_y))
               
                    
        return self.moves    

    
    def AvailableMoves(self):
        self.moves=[]
        
        #Pawn 
        if self.id >=8 and self.id <= 15  :
            return self.PawnMoves()
            
            
            
            
        #Bishop
        if self.id ==2 or self.id == 5:
            return self.BishopMoves()
            
            
              
        #Knight
        if self.id == 1 or self.id == 6:
            return self.KnightMoves()
    
            
            
        #Rook 
        if self.id == 0 or self.id == 7:
            return self.RookMoves()
            
        #Queen
        if self.id == 3:
            return self.QueenMoves()
            
        
        #King
        if self.id == 4:
            return self.KingMoves()
        
# Button class for menu buttons     
class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def display(self):
        fill(0,0,0,50)
        rect(self.x, self.y, self.w, self.h, 5)
        if self.overButton(mouseX,mouseY):
            # Changing color to back when hover
            fill(0,0,0) 
        rect(self.x, self.y, self.w, self.h, 5)
        
        fill(255)
        textSize(50)
        textAlign(CENTER, CENTER)
        text(self.text, self.x + self.w / 2, self.y + self.h / 2)

    def overButton(self, x, y):
        return self.x < x < self.x + self.w and self.y < y < self.y + self.h
            
# draw function just calls makePiece() 

#drawBoard() makes the board using rect and fill functions

def drawBoard():
    square_size = width / 8  # Calculate the size of each square


    for row in range(8):
        for col in range(8):
            x = col * square_size
            y = row * square_size

            # Alternate between two colors for the squares
            if (row + col) % 2 == 0:
                fill(255)  # White squares
                
            else:
                fill(148,0,211)    # Black squares

            rect(x, y, square_size, square_size)  # Draw the square


# Images displayed by looping through arrays

def makePieces():
    global whiteArr,blackArr,firstRun,WhiteKinginCheck,BlackKinginCheck
    if firstRun == True:
        x=0
        y=600
        
        for i in range(16):
            whiteArr.append(whitePiece(x,y,i))
            #print(whiteArr[i],i)
            whiteArr[i].set_Picture("w_"+str(i+1)+".png")
            x=x+100
            if x == 800 :
                y=y+100
                x=0
            
        #print(whiteArr[9].xpos)
        #print(whiteArr[9].ypos)  
        x = 0
        y = 0
        for j in range(16):
            blackArr.append(blackPiece(x,y,j))
            blackArr[j].set_Picture("b_"+str(j+1)+".png")
            x=x+100
            if x == 800 :
                y=y+100
                x=0 
        # print(isPieceHere(0,400)) Testing
        firstRun=False     
    else:
        # For updating 
        #print("updating")
        
        
        if is_king_in_check((whiteArr[12].xpos,whiteArr[12].ypos),blackArr) == True:
            BlackKinginCheck=True
        if is_king_in_check((blackArr[4].xpos,blackArr[4].ypos),whiteArr) == True:
            WhiteKinginCheck=True        
        
        
        for i in range(16):
            if WhiteKinginCheck== True:
                fill(255,0,0,5)
                rect(blackArr[4].xpos, blackArr[4].ypos, 100, 100)
                
            if BlackKinginCheck== True:
                fill(255,0,0,5)
                rect(whiteArr[12].xpos, whiteArr[12].ypos, 100, 100)
                
            
            whiteArr[i].set_Picture("w_"+str(i+1)+".png")
            blackArr[i].set_Picture("b_"+str(i+1)+".png")
            display_killedNumber()

            
# Most Important Part is Mouse Press
# When Mouse  is  Pressed, first the state of Game is checked
# According to  GameState certain code is  run. 
# If GameState = "" which means currently we are in Intro, then menu buttons clicks will be observed
# If GameState =="play", which means we are  currently in the game, then it checks for moves and moves the pieces accordingly
    

def mousePressed():
    global selectedP,W_MOVES,B_MOVES,id,turnCounter,Moves,WhiteKinginCheck,BlackKinginCheck,kingMurdered
    global selectedTime,timeBtn_radius,GameState,winner,firstTime

    if GameState == "Play":
        if (turnCounter  %   2) == 0 :
            if mouseButton == LEFT:
                
                for p in whiteArr:
                    if mouseX>= p.xpos and mouseX<=p.xpos+100 and mouseY>=p.ypos and mouseY<=p.ypos+100:
                        selectedP=p
                        id=p.id
                        Moves=p.AvailableMoves()
                        for move in Moves:
                            fill(255, 255, 0)
                            W_MOVES.append((move[0],move[1]))
                            rect(move[0],move[1],100,100)
                        
                        break
                    
            if mouseButton == RIGHT and selectedP!=None:
                for m in W_MOVES:
                    #print(m)
                    if m[0] <= mouseX <= m[0] + 100 and m[1] <= mouseY <= m[1]+100:
                        c=0
                        while id != whiteArr[c].id:
                            c=c+1
                        print(c)
                        whiteArr[c].xpos=m[0]
                        whiteArr[c].ypos=m[1]
                        
                        WhiteKinginCheck=False
                        BlackKinginCheck=False
                        turnCounter=turnCounter+1         
                        if is_king_in_check((blackArr[4].xpos,blackArr[4].ypos),whiteArr) == True:
                            #King Flashed Red
                            WhiteKinginCheck=True
                        Attacked(m[0],m[1],"white")
                        print("capWhite",capturedWhites)
                        print("capBlack",capturedBlacks)
                        if isKingCaptured() ==  True:
                            winner = "White"
                            GameState= "End"
                        else:

                            
                            drawBoard()
                            makePieces()
                            display_killedNumber()
                            
                            
                            selectedP=None
                            id=None
                            Moves=[]
                            break
                    
        else:
            if mouseButton == LEFT:
                for p in blackArr:
                    if mouseX>= p.xpos and mouseX<=p.xpos+100 and mouseY>=p.ypos and mouseY<=p.ypos+100:
                        selectedP=p
                        id=p.id
                        Moves=p.AvailableMoves()
                        id=p.id
                        for move in Moves:
                            fill(255, 255, 0)
                            B_MOVES.append((move[0],move[1]))
                            rect(move[0],move[1],100,100)
                        
                        break   
    
            if mouseButton == RIGHT and selectedP!=None:
                for m in B_MOVES:
                    if m[0] <= mouseX <= m[0] + 100 and m[1] <= mouseY <= m[1]+100:
                        c=0
                        while id != blackArr[c].id:
                            c=c+1
                        print(c)
                        blackArr[c].xpos=m[0]
                        blackArr[c].ypos=m[1]
                        WhiteKinginCheck=False
                        BlackKinginCheck=False
                        turnCounter=turnCounter+1
                        if is_king_in_check((whiteArr[12].xpos,whiteArr[12].ypos),blackArr) == True:
                            BlackKinginCheck=True
                        Attacked(m[0],m[1],"black")
                        print("capWhite",capturedWhites)
                        print("capBlack",capturedBlacks)
                        if isKingCaptured() ==  True:
                            winner = "Black"
                            GameState = "End"
                        else:
                            
                            drawBoard()
                            makePieces()
                            
                            selectedP=None
                            id = None 
                            Moves=[]
                            break
            
        
    elif GameState=="":
        if playButton.overButton(mouseX, mouseY):
            print("Play")
            GameState="Play"
        elif instructionButton.overButton(mouseX, mouseY):
            print("Instructions")
            GameState="Instructions"
        else:
            # Check if a time option is clicked
            for i, time in enumerate(timeOptions):
                timeX = width / 2 - 36 + 70 * i
                timeY = height / 2 + 300
                if dist(mouseX, mouseY, timeX, timeY) < timeBtn_radius:
                    selectedTime = time
                    print("Selected time: " + str(selectedTime) + " minutes")
                    
                    
    elif GameState == "End":
        if Exitbtn.overButton(mouseX,mouseY):
            print("Restart")
            firstTime=True
            Initialize()
            GameState=""
            
            
    elif GameState == "Instructions":
        if Exitbtn.overButton(mouseX,mouseY):
            firstTime=True
            GameState=""
        
            
            
            
        
# Checks  if there is a white piece at pos x,y    
def isWhitePieceHere(x,y):
    for indexes in range(16):
        if (x == whiteArr[indexes].xpos and y == whiteArr[indexes].ypos):
            isHere=True
            break
        else:
            isHere=False
            
    return isHere
# Checks if there is a black piece at pos x,y
def isBlackPieceHere(x,y):
    for indexes in range(16):
        if (x == blackArr[indexes].xpos and y == blackArr[indexes].ypos):
            isHere=True
            break
        else:
            isHere=False
            
    return isHere  

# Checks if the king is in check  
def is_king_in_check(king_position, opposing_pieces):
    for piece in opposing_pieces:
        print("king position", king_position, "piece: ",piece.AvailableMoves())
        if king_position in piece.AvailableMoves():
            return True
    return False
      
# Check is the piece has been attacked 
def Attacked(x,y,col):
    global capturedWhites,capturedBlacks
    idtoRemove=None
    if col == "white":
        for blackpiece  in blackArr :
            if x == blackpiece.xpos and y == blackpiece.ypos:
                # Black piece is attacked
                # We need to  remove the black piece from the board 
                # Add to black_captured 
                capturedBlacks.append(blackpiece)
                idtoRemove=blackpiece.id
                break 
    
        if idtoRemove!=None:
            blackArr[idtoRemove].xpos=0
            blackArr[idtoRemove].ypos=900
            #Making it invisible basically 
    else:
        for whitepiece  in whiteArr :
            if x == whitepiece.xpos and y == whitepiece.ypos:
                # white piece is attacked
                # We need to  remove the black piece from the board 
                capturedWhites.append(whitepiece)
                idtoRemove=whitepiece.id
                break 
    
        if idtoRemove!=None:
            whiteArr[idtoRemove].xpos=0
            whiteArr[idtoRemove].ypos=900
    
    
    

# Displays the Number of pieces captured
def display_killedNumber():
    textSize(20)
    text("White Captured : " + str(len(capturedWhites)) ,width-100, height-110)
    text("Black Captured : " + str(len(capturedBlacks)),width-100,height-80)
    
                        
        
# Checks if the king is captured     
def isKingCaptured():
    for capturedp in capturedWhites:
        if capturedp.id == 12:
            return True            
            
    
    
    for capturedp in capturedBlacks:
        if capturedp.id == 4:
            return True
    
    return False

# Displays Timer
def displayTime():
    global start_time,GameState,winner
    TimePassed=millis()-start_time
    timeinselected_time=selectedTime * 60 * 1000
    seconds=str(((timeinselected_time-TimePassed)/1000) -((((timeinselected_time-TimePassed)/1000)/60) * 60) )
    minutes=str(((timeinselected_time-TimePassed)/1000)/60)
    textSize(100)
    fill(255)
    if TimePassed >= timeinselected_time:
        seconds="00"
        minutes="00"
        winner="Draw"
        GameState="End"
        
        
    
    text(minutes+":"+seconds,width/2,900)


        
        
        
        
        
        



# Instructions 
def GameStageThree():
    global Exitbtn
    playBG=loadImage("background.jpg")
    image(playBG,0,0,800,1000)
    textSize(25)
    text("Notes: ",50,height/2-400)
    text("To make chess much more enjoyable to play with friends",width/2,height/2 - 300)
    text("I have added feature of killing the King. ",width/2,height/2 -200)
    text("The Game tests who can kill the king fastest.",width/2,height/2 - 100)
    text("IMPORTANT: ",100,height/2 + 100)
    text("To Play, you must select TIME.",width/2,height/2 + 200)
    Exitbtn=Button("X", width/2 - 50, height/2 + 300, 100, 100)
    Exitbtn.display()
    
    
# Result Part
def GameStageFour(winner):
    global Exitbtn
    # End Stage
    # Displays Winner or Time ran out/Draw
    playBG=loadImage("background.jpg")
    image(playBG,0,0,800,1000)
    textSize(150)
    fill(255)
    if winner == "Draw":
        text("Draw",width/2,height/2)
    elif winner == "Black":
        text("Black Won",width/2,height/2)
    else:
        text("White Won",width/2,height/2)
    Exitbtn=Button("X", width/2 - 50, height/2 + 300, 100, 100)
    Exitbtn.display()
    
    

    



#  Chess Game
def GameStageTwo():
    global firstTime,start_time
    if firstTime:
        firstTime=False
        start_time=millis()
        drawBoard()
     
    playBG=loadImage("background.jpg")
    image(playBG,0,800,800,200)
    makePieces()
    displayTime()
    
    
# Menu
def GameStageOne():
    global playButton, instructionButton, timeOptions, selectedTime,timeBtn_radius 

    
    bg = loadImage("BackgroundofWelcomePage.jpg")
    image(bg, 0, 0, width, height)
    
    # Shadowing
    textSize(75)
    textAlign(CENTER, CENTER)
    fill(0, 0, 0, 100) 
    text("Queen's Gambit", width / 2 + 5, height / 4 + 5)  
    fill(162, 11, 100)  
    text("Queen's Gambit", width / 2, height / 4)
    
    # Styling the buttons 
    buttonW = 360
    buttonH = 100
    buttonX = width / 2 - buttonW / 2
    buttonY_play = height / 2 - 20
    buttonY_instructions = height / 2 + 100
    playButton = Button("Play", buttonX, buttonY_play, buttonW, buttonH)
    instructionButton = Button("Instructions", buttonX, buttonY_instructions, buttonW, buttonH)
    
    playButton.display()
    instructionButton.display()
    #Radius  
    timeBtn_radius = 30  

    # Time Selection Part
    textSize(40)
    fill(255) 
    text("Select Time:", width / 2, height / 2 + 220)
    
    # Display time options
    timeBtn_radius = 30
    for i, time in enumerate(timeOptions):
        timeX = width / 2 - 36 + 70 * i
        timeY = height / 2 + 300
        if selectedTime == time:
            #Green Color Highlight
            fill(0,255,0)  
        else:
            fill(0,0,0,50)
        ellipse(timeX, timeY, timeBtn_radius * 2, timeBtn_radius * 2)  
        fill(255)  
        text(str(time), timeX, timeY)  
    textSize(20)
    text("Use Left Click to Select A Piece",width/2,height/2+440)
    text("Use Right Click to Drop the Piece",width/2,height/2 + 420)
    






def draw():
    global MovePlayer,KingCapturePlayer
    if GameState == "":
        MusicPlayer.play()
        
        GameStageOne()
        
    elif GameState == "Play":
        MusicPlayer.pause()
        MusicPlayer.rewind()
        GameStageTwo()
        
        
    
    elif GameState == "Instructions":
        GameStageThree()
        
    elif GameState == "End":
        GameStageFour(winner)

        
