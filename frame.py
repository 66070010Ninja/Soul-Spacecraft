# เปิดใช้งาน pygame os และ random
import pygame ,os , random
pygame.init()

# เรียกใช้งานใช้ font
pygame.font.init()

# กำหนดขนาด windows หน่วย pixel
width, height = 750, 750
windows = pygame.display.set_mode((width, height))

# ตั้งชื่อ caption_display
pygame.display.set_caption('Space of Arcana')

# ดึงรูปภาพจากไฟล์ เพื่อนำมาใช้งาน (โดยที่นี้จะทดสอบโดย โหลดไฟล์จาก Flie Foloder ที่มีชื่อว่า assets เพื่อลองทำการดึงภาพมาใช้งาน)

# space_ship ฝั่งศัตรู
red_space_ship = pygame.image.load(os.path.join('Image/Ship/pixel_ship_red_small.png'))
green_space_ship = pygame.image.load(os.path.join('Image/Ship/pixel_ship_green_small.png'))
blue_space_ship = pygame.image.load(os.path.join('Image/Ship/pixel_ship_blue_small.png'))

# space_ship_player
yellow_space_ship = pygame.image.load(os.path.join('Image/Ship/pixel_ship_yellow.png'))

# Lasers
red_laser = pygame.image.load(os.path.join('Image/Laser/pixel_laser_red.png'))
green_laser = pygame.image.load(os.path.join('Image/Laser/pixel_laser_green.png'))
blue_laser = pygame.image.load(os.path.join('Image/Laser/pixel_laser_blue.png'))
yellow_laser = pygame.image.load(os.path.join('Image/Laser/pixel_laser_yellow.png'))

# Background (เรียกใช้ background-black.png และปรับขนาด ให้เท่ากับ width, height)
background = pygame.transform.scale(pygame.image.load(os.path.join('Image/Game/background-black.png')), (width, height))

# กำหนดลักษณะ laser
class laser:
    def __init__(self, x, y, img):
        '''laser'''
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        '''draw laser'''
        window.blit(self.img, (self.x, self.y))
    
    def move(self, vel):
        '''move'''
        self.y += vel
    
    def off_screen(self, height):
        '''off screen'''
        return self.y < height and self.y >= 0

    def collision(self, obj):
        '''collision'''
        return collide(obj, self)

# กำหนดลักษณะของ ship
class ship:
    def __init__(self, x, y, health = 100):
        '''Object'''
        self.x = x # ตำแหน่ง x
        self.y = y # ตำแหน่ง y
        self.health = health # เลือดตัวละคร
        self.ship_img = None # ภาพของ ship
        self.laser_img = None # ภาพ laser
        self.lasers = [] # จำนวน laser
        self.cool_down_counter = 0 # ระยะเวลาที่ใช้ยิง

    def draw(self, window):
        '''draw Object'''
        # ให้วาดรูปจาก ship_img
        window.blit(self.ship_img, (self.x, self.y))
    
    # เก็บค่าความกว้าง
    def get_width(self):
        '''width'''
        return self.ship_img.get_width()

    # เก็บค่าความสูง
    def get_height(self):
        '''height'''
        return self.ship_img.get_height()

# กำหนดลักษณะ player
class player(ship):
    def __init__(self, x, y, health=100):
        '''Player'''
        super().__init__(x, y, health)
        self.ship_img = yellow_space_ship
        self.laser_img = yellow_laser
        self.mask = pygame.mask.from_surface(self.ship_img) # สร้าง hitbox
        self.max_health = health

class enemier(ship):
    # สร้าง dict เก็บลักษณะของ enemy แต่ละชุด
    color_map = {
                'red': (red_space_ship, red_laser),
                'green': (green_space_ship, green_laser),
                'blue' : (blue_space_ship, blue_laser)
                }

    def __init__(self, x, y, color, health=100):
        '''enemy'''
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.color_map[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        # การเครลื่อที่ของ enemy
        '''move enemy'''
        self.y += vel

def collide(obj1, obj2):
    '''collide'''
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.x
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():
    '''run game'''
    run = True
    fps = 60
    level = 0
    lives = 5

    # เรียกใช้ font โดยใช้ font type comicsans ขนาด 50 pixel
    main_font = pygame.font.SysFont('comicsans', 50)
    lost_font = pygame.font.SysFont('comicsans', 60)

    # กำหนด enemies
    enemies = []
    wave_length = 5
    enemy_vel = 1

    # กำหนดระยะการเดิน
    player_vel = 5

    # กำหนดตัว players
    players = player(300, 650)

    clock = pygame.time.Clock()

    # คำสั่ง lost
    lost =  False
    lost_count = 0

    def redraw_window():
        '''วาด background'''
        # ให้ดาวรูปจาก background ในตำแหน่ง (0, 0)
        windows.blit(background, (0, 0))
        
        # วาด text
        lives_label = main_font.render(f'Lives : {lives}', 1, (255, 255, 255))
        leve_label = main_font.render(f'Level : {level}', 1, (255, 255, 255))

        # วาด enemy
        for enemy in enemies:
            enemy.draw(windows)

        # วาด players
        players.draw(windows)

        # ให้วาด text livse ในตำแหน่ง (10, 10)
        windows.blit(lives_label, (10, 10))
        # ให้วาด text leve ในตำแหน่ง (width - width ของ text level - 10, 10)
        windows.blit(leve_label, (width - leve_label.get_width()-10, 10))

        if lost:
            # ให้วาด text lost ในตำแหน่ง (width/2 - width ของ lost_label/2, 350)
            lost_label = lost_font.render('You Lost!!', 1, (255, 255, 255))
            windows.blit(lost_label, (width/2 - lost_label.get_width()/2, 350))


        pygame.display.update()

    # เปิด windows
    while run:
        # run fps/time
        clock.tick(fps)
        redraw_window()

        if lives <= 0 or players.health <= 0:
            # เช็ค live กับ health ของ player
            lost = True
            lost_count += 1

        if lost:
            # รอ 3 fps แล้วปิดโปรแกรม
            if lost_count > fps * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            # เช็คจำนวน enemies
            level += 1
            wave_length += 5
            for _ in range(wave_length):
                # สุ่มตำแน่ง width , ความสูง และ enemies
                enemy = enemier(random.randrange(50, width-100), random.randrange(-1500, -100), random.choice(['red', 'blue', 'green']))
                enemies.append(enemy)

        for event in pygame.event.get():
            # เช็คว่า เมื่อกดปุ่ม QUIT ให้ออกจากเกม
            if event.type == pygame.QUIT:
                run = False

        # การเคลื่อนโดยใช้ keyboard
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and players.x - player_vel > 0:
            # key a = left
            players.x -= player_vel
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and players.x + player_vel + players.get_width() < width:
            # key d = right
            players.x += player_vel
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and players.y - player_vel > 0:
            # key w = up
            players.y -= player_vel
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and players.y + player_vel + players.get_height() < height:
            # key s = down
            players.y += player_vel

        for enemy in enemies[:]:
            # ให้ enemy เคลื่อนที่ตามคำสั่ง move
            enemy.move(enemy_vel)
            if enemy.y + enemy.get_height() > height:
                # เช็คว่า enemy ลงถึงตำแหน่งที่ระบุข้างต้น
                lives -= 1
                enemies.remove(enemy)
main()

# ddd
