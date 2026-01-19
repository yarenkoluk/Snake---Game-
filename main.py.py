import pygame 
import random 
from pygame import mixer #müzik için mixeri import ettim.

class Node: #yılanın her bir hücresi için node sınıfı.
 def __init__(self,row,col,next=None): 
  self.row = row #yılanın satır ksımı
  self.col = col #yılanın sutün kısmı
  self.next= next #sonraki hücreyi tutacak.

class Snake: #yılan sınıfı
    def __init__(self,initial_row,inital_col): #yılanın başlangıç pozisyonu
        self.head= Node(initial_row,inital_col) #yılanın başı
        self.length = 1 #yılanın uzunluğu 

    def add_head(self,row, col): #yılanın başını eklemek için fonk.
        new_head = Node(row,col) #yeni baş oluşturuyorum.
        new_head.next = self.head #yeni başın sonraki kısmı eski baş olacak.
        self.head = new_head #yeni baş yılanın yeni başı olur
        self.length += 1 # yılanın uzunluğu 1 artar

    def remove_tail(self): #yılanın kuyrugunu silmek için fonksiyon
        if self.head.next is None: #eğer yılanın başından sonra hiç hücre yoksa:
            return #hiçbir şey yapma
        current = self.head #şuanki hğcre baş
        while current.next.next: #sondan bir önceki hücreye gelene kadar dömngü
             current = current.next #sonraki hücreye gwç
        current.next = None 
        self.length -= 1 #yılanın uzunluğu 1 azalır.
  
    def traverse(self): #yılanın tüm hücrelerini dolaşmak için fonksiyon
        node  = [] #boş liste
        current = self.head #şaunki hücre boş
        while current: #şuanki hücre dolu ise
            node.append((current.row, current.col)) #hücrenin row ve col değerlerini listwyw ekle
            current = current.next #bir sonrakine geç 
        return node 
    def check_self_collision(self): #kendi kendine çarpıyor mu 
        head = (self.head.row, self.head.col)
        return head in self.traverse()[1:]

pygame.init() #pygame başlatır.
mixer.init() #sesi başlatır.
  
try:
  mixer.music.load("music.mp3") #müzik dosyamı yükledim.
  mixer.music.play(-1) # müziği oynattım , parametre olarak -1 çünkü oyun kapanana kadar çalmasını isterim.
except Exception as e:
  print("The music file could not be loaded the game continues silently.", e)
width = int(400) #penceremin x ekseni uzunluğu
height = int(400) #penceremin y ekseni uzunluğu
cell_size = 20 #yılanın her bir hücresinin boyutu 
square_size = 20 # her karem 20x20 piksel 
rows = height//square_size #ekran yüksekliği/kare = kaç satır
cols = width // square_size #ekran genişliği (x)/kare = kaç sutün
snake = Snake(rows //2, cols//2) #yılanın başlangıç poziyonu pencerimin ortasında.
food_pos = [random.randint(0,rows-1), random.randint(0,cols-1)] #yemek için rastgele bir pozisyon belirledim

direction = "RIGHT" #başlangıç yönü sağ.
change_to = direction #değiştirilecek yön başlangıç yönü.
grid = [[0] * cols for _ in range(rows)] #ekranda görülecek boş bir grid oluşturdum.
window = pygame.display.set_mode((width,height))#pencereyi açacak ama hemen kapanacak
pygame.display.set_caption("YAREN SNAKE GAME") #Penceremde görünecek başlık

clock=pygame.time.Clock() #oyun hızını ayarlamak için.

def draw_grid(): #gridi çizmek için fonksiyon oluşturdum.
   for i in range(rows): #satırları tek tek dolaşıyor.
      for j in range(cols): #sutünları (y ekseni) tek tek dolaşıyor.
          if grid[i][j] == 0: #eğer griddeki hücre 0 ise boş demk.
            pygame.draw.rect(window , (169,169,169),(j*square_size,i*square_size,square_size,square_size),1) #window = nereye çizileceği, (169,169,169)= GRİ RENK, (j*square) = kare x koordintı, (i*square) = kare y kordinatı, square_size = genişlik ve yükseklik.
          else: #eğer hücre 0 değilse.
            pygame.draw.rect(window, (0,0,0),(j*square_size,i*square_size,square_size,square_size),1) #(0,0,0) = siyah renkte olack, 1 = çizgi kalınlıgı = 1 piksel.

def draw_snake(): # yılanı çizdirmek için fonksiyon oluşturdum.
  for row, col in snake.traverse():
   pygame.draw.rect(window,(255,205,180),(col*square_size,row*square_size,square_size,square_size)) # yılanı çizer.

score = 0
def draw_score(): #skoru göstermek için fonksiyon ouşturdum.
  score_font = pygame.font.SysFont("comicsansms",25) #yazı tipi ve boyutu.
  score_surface = score_font.render(("Score: " + str(score)), True,(40,0,60)) 
  score_rect = score_surface.get_rect(height=10,width=100) #skorun konumu 
  window.blit(score_surface,score_rect) #skoru pencereye çizdiriyorum

food_pos = [random.randint(0,rows-1), random.randint(0,cols-1)] #yemek için rastgele bir pozisyon belirledim
def draw_food( ): #yemeği çizmek için fonksiyon oluşturdum.
  global score #skoru global yaptım yani fonksiyon içinde de kullanabilirim.
  row =food_pos[0] #yemeğin satır pozisyonu
  col =food_pos[1] #yemeğin sutün pozisyonu
  pygame.draw.rect(window,(255,215,0),(col*square_size,row*square_size,square_size,square_size)) #yemeği drw ile çizer.
  
def draw_game_over(): #oyun bitti yazısı için fokn-siyon oluşturdum.
   window.fill((40,0,60)) #pencere mor oldu.
   write = myfont.render("GAME OVER :(",True,(240,240,240) )
   font = write.get_rect(center = (width//2,height//2)) #yazının konumunu otada olacak.
   window.blit(write,font) #yazıyı pencereye çizdirdim
   pygame.display.update() #ekranı güncelledim.
   pygame.time.delay(5000) #5 saniye bekledim.
   
   for font in pygame.font.get_fonts(): #pygame de ki tüm font isimlerini yazdırmak için döngü
     print(font)
myfont= pygame.font.SysFont("bookmanoldstyle",50) #yazı tipi ve boyutu sectim

running =True #döngü başlatmak için değişkenim.
while running: #döngü başlattım.
    clock.tick(7) #oyun hızı 10
    
    for event in pygame.event.get(): # mouse ve klavye hareketlenini kontrol ediyorum.
       if event.type == pygame.QUIT: # eğer çarpı tuşunda,işaretindeysem:
        running =False #döngüyü kırıyorum,bitiriyorum.

       if event.type == pygame.KEYDOWN: #eğer klavyeden bir tuşa basılırsa:
        if event.key == pygame.K_RIGHT and direction != "LEFT": #eğer sağ ok tuşuna bsılırsa:
           change_to ="RIGHT"
          
        elif event.key == pygame.K_LEFT and direction != "RIGHT": #eğer sol ok tuşuna basılırsa:
            change_to = "LEFT"
            
        elif event.key == pygame.K_UP and direction != "DOWN":
             change_to = "UP"
         
        elif event.key== pygame.K_DOWN and direction != "UP": # eğer aşağı yönlü oka basılırsa: elif event.key == pygame.K_UP : # eğer yukarı yönlü tuşa basarsam:
            change_to = "DOWN"
           
    direction = change_to
    new_row = snake.head.row
    new_col = snake.head.col
    if direction == "RIGHT":
       new_col +=1 
       
    elif direction == "LEFT":
       new_col -= 1
      
    elif direction == "UP":
       new_row -= 1
      
    elif direction == "DOWN":
       new_row += 1
      
      # SINIR KONTROLÜ
    
    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
        draw_game_over()
        snake = Snake(rows // 2, cols // 2)  # restart için başlangıç konumu
        score = 0 # skor sıfırlanır
        direction ="RIGHT"
        change_to = "RIGHT"
        continue #sonraki göndgü
         
    
    if (new_row,new_col) in snake.traverse(): #eğer yılan kendine çarparsa 
        draw_game_over() #oyun bitter 
        snake = Snake(rows // 2, cols // 2) #yeni başlangıç konumu 
        score = 0 #skor 0landı
        direction = "RIGHT"
        change_to = "RIGHT"
        continue 
           
    snake.add_head(new_row,new_col) 
         # YEMEK KONTROLÜ
    if (new_row, new_col) == tuple(food_pos): #eğer yılanın başının row,col değeri == yemeğin row,col değeri ise
               score += 1 #skor 1 artar
               food_pos = [random.randint(0, rows - 1), random.randint(0, cols - 1)] #yemek için yeni ratgele pozisyon
               while tuple(food_pos) in snake.traverse(): #yemek yılanın üzerinde oluşmasın.
                   food_pos = [random.randint(0, rows - 1), random.randint(0, cols - 1)]
    else: 
                snake.remove_tail()
    

       

    window.fill((144, 238, 144)) #pencereyi yesil renkte yaptım. 144,238,144 = yesil renkmis
    draw_grid() #gridi yazdırdım.
    draw_snake() # yılanı çizmek için fonksiyonu çağırdım. 
    draw_food() #yemeği çizmek için fonksiyonu çağırdım.
    draw_score() #skoru çizmek için fonksiyonu çağırdım.
    pygame.display.flip() #ekranı güncelleme işlemi yaptım.
pygame.quit() #pygame kaoandı.