import pygame, random

pygame.init()

genislik, yukseklik = 1200, 750

pencere = pygame.display.set_mode((genislik, yukseklik))

pygame.mixer.music.load("arkaPlan.mp3")
pygame.mixer.music.play(-1, 0,0)
seviye_yukselme_ses = pygame.mixer.Sound("seviyeYukselme.mp3")
yeme_sesi = pygame.mixer.Sound("jump.mp3")
carpisma_sesi = pygame.mixer.Sound("carpisma.mp3")

HIZ = 10
saat = pygame.time.Clock()
FPS = 30
kontrol = 0

canavar = pygame.image.load("canavar.png")
canavar_koordinat = canavar.get_rect()
canavar_koordinat.topleft = ((genislik/2, yukseklik/2))

yem = pygame.image.load("para.png")
yem_koordinat = yem.get_rect()
yem_koordinat.topleft = (150, 150)

engel_sayisi = 2
engel_listesi = []
engel_resmi = pygame.image.load("engel.png")

for _ in range(engel_sayisi):
    engel_koordinat = engel_resmi.get_rect()
    engel_koordinat.x = random.randint(0, genislik-32)
    engel_koordinat.y = random.randint(91, yukseklik-32)
    engel_listesi.append(engel_koordinat)

arka_plan = pygame.image.load("arkaPlanResim.jpg")
arka_plan = pygame.transform.scale(arka_plan, (genislik, yukseklik))

font = pygame.font.SysFont("consolas", 64)
skor = 0

durum = True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            durum = False
    
    pencere.blit(arka_plan, (0, 0))
    pencere.blit(canavar, canavar_koordinat)
    pencere.blit(yem, yem_koordinat)
    
    for engel in engel_listesi:
        pencere.blit(engel_resmi, engel)

    yazi = font.render("Skor: " + str(skor), True, (255, 0, 0), (255, 255, 255))
    yazi_koordinat = yazi.get_rect()
    yazi_koordinat.topleft = (20, 20)

    pygame.draw.line(pencere, (255, 0, 255), (0, 90), (1200, 90), 3)
    pencere.blit(yazi, yazi_koordinat)

    tus = pygame.key.get_pressed()
    if tus[pygame.K_LEFT] and canavar_koordinat.left > 0:
        canavar_koordinat.x -= HIZ
    elif tus[pygame.K_RIGHT] and canavar_koordinat.right < genislik:
        canavar_koordinat.x += HIZ
    elif tus[pygame.K_UP] and canavar_koordinat.top > 0:
        canavar_koordinat.y -= HIZ
    elif tus[pygame.K_DOWN] and canavar_koordinat.bottom < yukseklik:
        canavar_koordinat.y += HIZ

    if canavar_koordinat.colliderect(yem_koordinat):
        yeme_sesi.play()
        yem_koordinat.x = random.randint(0, genislik-32)
        yem_koordinat.y = random.randint(91, yukseklik-32)
        skor += 1
    
    for engel in engel_listesi:
        if canavar_koordinat.colliderect(engel):
            carpisma_sesi.play()
            engel.x = random.randint(0, genislik-32)
            engel.y = random.randint(91, yukseklik-32)
            skor -= 1

    if skor > 1:
        canavar = pygame.image.load("canavar1.png")
        if kontrol == 0:
            seviye_yukselme_ses.play()
            canavar_koordinat = canavar.get_rect()
            canavar_koordinat.topleft = ((genislik/2, yukseklik/2))
            HIZ = 5
            kontrol += 1
            
        if tus[pygame.K_LEFT] and canavar_koordinat.left > 0:
            canavar_koordinat.x -= HIZ
        elif tus[pygame.K_RIGHT] and canavar_koordinat.right < genislik:
            canavar_koordinat.x += HIZ
        elif tus[pygame.K_UP] and canavar_koordinat.top > 0:
            canavar_koordinat.y -= HIZ
        elif tus[pygame.K_DOWN] and canavar_koordinat.bottom < yukseklik:
            canavar_koordinat.y += HIZ

        if canavar_koordinat.colliderect(yem_koordinat):
            yeme_sesi.play()
            yem_koordinat.x = random.randint(0, genislik-32)
            yem_koordinat.y = random.randint(91, yukseklik-32)
            skor += 1
        
        for engel in engel_listesi:
            if canavar_koordinat.colliderect(engel):
                carpisma_sesi.play()
                engel.x = random.randint(0, genislik-32)
                engel.y = random.randint(91, yukseklik-32)
                skor -= 1

    pygame.display.update()
    saat.tick(FPS)

pygame.quit()
