import pygame
import random
from ButtonCreater import button 
import os

##os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

##centered the window
os.environ['SDL_VIDEO_CENTERED'] = "True"

#dimentions
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 660

MAX_BARS = 80

MIN_BAR_WIDTH = 10

MIN_BAR_HEIGHT = 50
MAX_BAR_HEIGHT = 450
#dimentions

#same width and lenth for all buttons
ButtonW = 200
ButtonL = 50

##all buttons self explaining by there names
suffelButton = button((0,255,0), 1040 ,SCREEN_HEIGHT - 100,ButtonW,ButtonL,'Stop and Suffel')

bubbleButton = button((0,255,0), 1040 ,20,ButtonW,ButtonL,'Bubble Sort')
insertionButton = button((0,255,0), 1040 ,90,ButtonW,ButtonL,'Insertion Sort')
selectionButton = button((0,255,0), 1040 ,160,ButtonW,ButtonL,'Selection Sort')
quickButton = button((0,255,0), 1040 ,230,ButtonW,ButtonL,'Quick Sort')
mergeButton = button((0,255,0), 1040 ,300,ButtonW,ButtonL,'Merge Sort')
heapButton = button((0,255,0), 1040 ,370,ButtonW,ButtonL,'Heap Sort')

arrDefaultSize = button((0,255,0),200,SCREEN_HEIGHT - 100,ButtonW,ButtonL,'Default')
arrSmallSize = button((0,255,0), 420 ,SCREEN_HEIGHT - 100,ButtonW,ButtonL,'Small(with values)')
arrLargeSize = button((0,255,0), 640 ,SCREEN_HEIGHT - 100,ButtonW,ButtonL,'Large')

ontext = False #text on bars

## class for drawing bars
class Bar(object):

    def __init__(self,x,y):
        self.x = x;
        self.y = y;

    def draw(self,surface,color):
        pygame.draw.rect(surface, color , (self.x,0,MIN_BAR_WIDTH,self.y))
        
        #when small size bar values will appeare
        if ontext:
            basicfont = pygame.font.SysFont(None, 25)
            text = basicfont.render(str(self.y ), True, (255, 0, 0), (255, 255, 255))
            textrect = text.get_rect()
            textrect.centerx = self.x + 15
            textrect.centery = 20
            surface.blit(text, textrect)

#### heapsort  ####

def heapify(win,n,i):

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if (buttonclick(suffelButton,pos,event)):
            suffel()
            return
    if (Stop): return
    
    large = i
    l = i*2 + 1
    r = i*2 + 2

    if l<n and obj[large].y < obj[l].y: large = l

    if r<n and obj[large].y < obj[r].y: large = r

    if large != i:

        obj[large].y,obj[i].y = obj[i].y,obj[large].y
        
        var = [i,large]
        redrawwin(win,"heap",var)

        heapify(win,n,large)

def heapSort(win):

    n = MAX_BARS

    clock = pygame.time.Clock()
    
    for i in range(n//2 -1,-1,-1):
        if (Stop): return
        pygame.time.delay(200)
        clock.tick(0)
        heapify(win,n,i)

    for i in range(n-1,0,-1):
        if (Stop): return
        pygame.time.delay(200)
        clock.tick(0)

        obj[i].y,obj[0].y = obj[0].y,obj[i].y

        var = [i,0]
        redrawwin(win,"heap",var)

        heapify(win,i,0)


def heapAnimate (var,surface):

    r = var[0]
    g = var[1]
    color = (0,0,0)
    for i in range(MAX_BARS):
        if (i == r):
            color = (255,0,0)
        elif (i == g):
            color = (0,255,0)
        else:
            color = (0,0,0)
        obj[i].draw(surface,color)
    

#### heapsort ends ####

##### mergesort #####

def merge(win,l,m,r):
    n1 = m-l +1
    n2 = r - m

    L = [0]* (n1)
    R = [0]* (n2)
    
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if (buttonclick(suffelButton,pos,event)):
            suffel()
            return
        
    if (Stop): return
    
    for i in range(0,n1):
        L[i] = obj[l + i].y
    for j in range(0,n2):
        R[j] = obj[m+1+j].y

    i = 0
    j = 0
    k = l

    while i< n1 and  j < n2:
        if L[i] <= R[j]:
            obj[k].y = L[i]
            c = l+i
            i += 1
        else:
            obj[k].y = R[j]
            c = m + l + j
            j += 1
    
        var = [k,c]
        redrawwin(win,"merge",var)
        k += 1
        

    while i< n1:
        obj[k].y = L[i]
        c = l+i
        
        var = [k,c]
        redrawwin(win,"merge",var)
        
        i += 1
        k += 1

    while j<n2:
        obj[k].y = R[j]
        c = l + m +j
        
        var = [k,c]
        redrawwin(win,"merge",var)
        
        j += 1
        k += 1



def mergeSort(win,l,r):
    clock = pygame.time.Clock()
    if  (l<r and not Stop):
        pygame.time.delay(150)
        clock.tick(10)
        
        mid = (l + (r-1))//2

        mergeSort(win,l,mid)
        mergeSort(win,mid+1,r)

        merge(win,l,mid,r)

def mergeAnimate(var,surface):

    r = var[0]
    b = var[1]
    
    for i in range(MAX_BARS):
        if (i == r):
            color = (255,0,0)
        elif (i == b):
            color = (0,0,255)
        else:
            color = (0,0,0)
        obj[i].draw(surface,color)
    

##### mergesort ends ###



##### quickSort #####

def swap(i,j):
    temp = obj[i].y
    obj[i].y =  obj[j].y
    obj[j].y = temp

def part(win,low,up):
    
    piv = obj[up].y
    i = (low -1)
    clock = pygame.time.Clock()
    for j in range(low,up):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if (buttonclick(suffelButton,pos,event)):
                suffel()
                return MAX_BARS
            
        pygame.time.delay(50)
        clock.tick(20)
        if (obj[j].y<=piv):
            i += 1
            swap(i,j)
            var= [up,i,j]
            redrawwin(win,"quick",var)
    
        
    swap(i+1,up)
    var = [i+1,MAX_BARS,MAX_BARS]
    redrawwin(win,"quick",var)
    
    return i+1
        

def quickSort(win,low,up):
    if (low<up and not Stop):
        
        pi = part(win,low,up)

        quickSort(win,low,pi-1)
        quickSort(win,pi+1,up)

def quickAnimate(var,surface):

    r = var[0]
    g = var[1]
    b = var[2]
    
    for i in range(MAX_BARS):
        if (i == r):
            color = (255,0,0)
        elif (i == g):
            color = (0,255,0)
        elif (i == b):
            color = (0,0,255)
        else:
            color = (0,0,0)
        obj[i].draw(surface,color)

#### quick sort ends #############



#### selection sort ######
def get_min(i):
    m = obj[i].y
    r = i
    for j in range(i+1,MAX_BARS):
        if (m>obj[j].y):
            m=obj[j].y
            r = j
    return r

def selctionSort(win):
    
    clock = pygame.time.Clock()
    
    for i in range (0,MAX_BARS):
        if not Stop:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                
                if (buttonclick(suffelButton,pos,event)):
                    suffel()

            
            pygame.time.delay(200)
            clock.tick(30)
            mini = get_min(i)

            temp = obj[mini].y
            obj[mini].y = obj[i].y
            obj[i].y = temp

            var = [mini,i]
            
            redrawwin(win,"selction",var)
        else: return

def selctionAnimate(var,surface):

    r = var[0]
    g = var[1]
    
    for i in range(MAX_BARS):
        if (i == r):
            color = (255,0,0)
        elif (i == g):
            color = (0,255,0)
        else:
            color = (0,0,0)  
        obj[i].draw(surface,color)    


#### selction sort ends ######


#### insertion sort ##

def insertionSort(win):
    clock = pygame.time.Clock()
    
    for i in range (1,MAX_BARS):
        if not Stop:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                
                if (buttonclick(suffelButton,pos,event)):
                    suffel()
            
            pygame.time.delay(200)
            clock.tick(30)
            key = obj[i].y
            j=i-1
            while (j>=0 and obj[j].y >key):
                
                
                obj[j+1].y = obj[j].y
                j -= 1
            obj[j+1].y = key

            var = [i,j]
            
            redrawwin(win,"insertion",var)
        else: return
    

def insertionAnimate(var,surface):

    r = var[0]
    g = var[1]
    
    for i in range(MAX_BARS):

        if (i == r):
            color = (255,0,0)
        elif (i == g):
            color = (0,255,0)
        else:
            color = (0,0,0)  
        obj[i].draw(surface,color)

### insersion ends ##########


#####bulblle sort #########

### bubble sort animate #####
def bubbleAnimate(var,surface):
    j = var[0]
    c = var[1]
    
    for i in range(MAX_BARS):
        if (i == j):
            if (c==1):
                color = (255,0,0)
            else:
                color = (0,255,0)
        elif (i == j +1):
            if (c==0):
                color = (255,0,0)
            else:
                color = (0,255,0)
        else:
            color = (0,0,0)
            
        obj[i].draw(surface,color)
    

def bubbleSort(win):
    
    j =0
    c =0
    i = 0
    f = True
    clock = pygame.time.Clock()
    while f and not Stop:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if (buttonclick(suffelButton,pos,event)):
                suffel()
        
        pygame.time.delay(70)
        clock.tick(200)
        if (i == MAX_BARS - 1):
            f = False
            return
            
            
        if (j == MAX_BARS - 1 -i):
            j =0
            i +=1
        
        
        if (obj[j].y > obj[j+1].y ):
            
            temp = obj[j].y
            obj[j].y= obj[j+1].y
            obj[j+1].y = temp
            c=1
            j += 1
            
        else:
            c=0
            j +=1
            
        var = [j,c]
        redrawwin(win,"bubble",var)

### bubble sort ends #####


#### hendel button click ####

def buttonclick(mybutton,pos,event):
    
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if mybutton.isOver(pos):
            return True

    if event.type ==pygame.MOUSEMOTION:
        if mybutton.isOver(pos):
            mybutton.color = (255,0,0)
        else:
            mybutton.color = (0,255,0)

    return False

###resuffel the array and stop running algo

def suffel():
    global obj,Stop
    Stop = True
    
    for i in range(MAX_BARS):
        ny = random.randint(MIN_BAR_HEIGHT,MAX_BAR_HEIGHT)
        obj[i].y = ny


    
###### the main code
        

#####redrare window###

##perameter var contains the indexes of bars to change colors
def redrawwin(surface,Algo,var):
        
    surface.fill((240,230,140)) ##fill surface with khakhi color

    ###animating the selcted algorithem
    if (Algo == "no") :
        for i in range(MAX_BARS):
            obj[i].draw(surface,(0,0,0))
    elif (Algo == "bubble") :
        bubbleAnimate(var,surface)
    elif (Algo == "insertion") :
        insertionAnimate(var,surface)
    elif (Algo == "selction") :
        selctionAnimate(var,surface)
    elif (Algo == "quick") :
        quickAnimate(var,surface)
    elif (Algo == "merge") :
        mergeAnimate(var,surface)
    elif (Algo == "heap") :
        heapAnimate(var,surface)
    
    
    pygame.draw.line(surface,(138,54,15), (0,480),(980,480)) #horizental boundry for bars
    pygame.draw.line(surface,(138,54,15), (980,0),(980,480)) #vertical boundry for bars   

    ##drawing all then buttons

    ##sorting buttons
    bubbleButton.draw(surface,(0,0,0))
    insertionButton.draw(surface,(0,0,0))
    selectionButton.draw(surface,(0,0,0))
    quickButton.draw(surface,(0,0,0))
    mergeButton.draw(surface,(0,0,0))
    heapButton.draw(surface,(0,0,0))

    ##change array size
    arrDefaultSize.draw(surface,(0,0,0))
    arrSmallSize.draw(surface,(0,0,0))
    arrLargeSize.draw(surface,(0,0,0))

    ##stop and suffel
    suffelButton.draw(surface,(0,0,0))
    
    pygame.display.update() ##update the diaplay





def main():
    global obj,Stop,MIN_BAR_WIDTH,MAX_BARS,ontext #veiables used globly
    
    pygame.init()
    
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Sorting Visulizer')
    
    obj = [] ##empty list taken to fill with  bars

    x = MIN_BAR_WIDTH ##set x to min width of bars
    

    Stop = True ## variable used to stop algos while running
    

    ## adding bars of random height to the list
    for i in range(MAX_BARS): 
        y = random.randint(MIN_BAR_HEIGHT,MAX_BAR_HEIGHT)
        obj.append(Bar(x,y))
        x += ( MIN_BAR_WIDTH + 2 ) ## gap between each bar is 2.
    
    
    
    running  = True ##project is set running
    
    while running:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            ##checking click on all the buttons
            
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif (buttonclick(suffelButton,pos,event)): 
                suffel()
                
            ##when click on sorting buttons seting Stop to false as defult is true
            elif (buttonclick(bubbleButton,pos,event)):
                Stop = False
                bubbleSort(win)
            elif (buttonclick(insertionButton,pos,event)):
                Stop = False
                insertionSort(win)
            elif (buttonclick(selectionButton,pos,event)):
                Stop = False
                selctionSort(win)
            elif (buttonclick(quickButton,pos,event)):
                Stop = False
                quickSort(win,0,MAX_BARS - 1)
            elif (buttonclick(mergeButton,pos,event)):
                Stop = False
                mergeSort(win,0,MAX_BARS - 1)
            elif (buttonclick(heapButton,pos,event)):
                Stop = False
                heapSort(win)
                
            ###changing arr size here and recalling the main
            elif (buttonclick(arrLargeSize,pos,event)):
                MAX_BARS = 138
                MIN_BAR_WIDTH = 5
                
                ontext = False ##no text on large size
                running = False
                main()
                
            elif (buttonclick(arrDefaultSize,pos,event)):
                MAX_BARS = 80
                MIN_BAR_WIDTH = 10
                
                ontext = False ##no text on default size
                running = False
                main()
                
            elif (buttonclick(arrSmallSize,pos,event)):
                MAX_BARS = 25
                MIN_BAR_WIDTH = 34
                
                running = False 
                ontext = True ##text only small size
                main()
                
        redrawwin(win,"no",[]) ##redraw window when no algo is selected
    
main()
