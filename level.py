
# def level_design(block_size):
#     design = {}
#     objects = []
#     collectibles = []
#     destinations = []
#     for j in range(0,4):
#         if j == 0:
#             objects.append(0)
#             collectibles.append(0)
#             destinations.append(0)
#         if j == 1:
#             blocks = []
#             traps = []
#             heart1 = Heart(block_size * 7, WIN_HEIGHT - block_size * 4, 16, 16)
#             heart2 = Heart(block_size * 18, WIN_HEIGHT - block_size * 6, 16, 16)
#             heart3 = Heart(block_size * 32, WIN_HEIGHT - block_size * 4, 16, 16)
#             heart4 = Heart(block_size * 21, WIN_HEIGHT - block_size * 2, 16, 16)
#             heart5 = Heart(block_size * 25, WIN_HEIGHT - block_size * 4, 16, 16)
#             heart6 = Heart(4700, WIN_HEIGHT - block_size * 2, 16, 16)
#             heart7 = Heart(5350, WIN_HEIGHT - block_size * 2, 16, 16)

#             pineapples = [
#               Pineapple(block_size * 15, WIN_HEIGHT - block_size * 4, 12, 12),  
#               Pineapple(block_size * 16, WIN_HEIGHT - block_size * 5, 12, 12),
#               Pineapple(block_size * 17, WIN_HEIGHT - block_size * 6, 12, 12),
#               Pineapple(block_size * 24, WIN_HEIGHT - block_size * 4, 12, 12),
#               Pineapple(block_size * 31, WIN_HEIGHT - block_size * 4, 12, 12),
#               Pineapple(4800, WIN_HEIGHT - block_size * 3, 12, 12),
#               Pineapple(5000, WIN_HEIGHT - block_size * 2, 12, 12),
#               Pineapple(5100, WIN_HEIGHT - block_size * 3, 12, 12),
#             ]

#             speed1 = Speed(block_size * 10, WIN_HEIGHT - block_size - 64, 32, 32)
#             speed2 = Speed(3500, WIN_HEIGHT - block_size - 64, 32, 32)
#             collectibles_bullets = CollectibleBullets(block_size * 28, WIN_HEIGHT - block_size - 64, 32, 32)
#             #blocks and traps
#             fire = Fire(4200, WIN_HEIGHT - block_size - 64, 16, 32)
#             monster = Monster(block_size * 22, WIN_HEIGHT - block_size - 64, 16, 32, block_size * 2)
#             floor = [Block(i * block_size, WIN_HEIGHT - block_size, block_size) for i in range(-WIN_WIDTH // block_size, (WIN_WIDTH * 20)// block_size)]

#             placed_traps = set()  # set to keep track of placed trap coordinates
        
#             for i in range(5):  # create 5 traps
#                 while True:
#                     x = random.randint(block_size * 4, WIN_WIDTH * 5 - block_size * 4)  # generate a random x coordinate within a range
#                     y = WIN_HEIGHT - block_size - 30  # set y-coordinate to floor level
#                     # check if there's a block at this position
#                     for block in blocks:
#                         if block.x <= x <= block.x + block.width and block.y <= y <= block.y + block.height:
#                             # there's a block at this position, adjust y-coordinate
#                             y = block.y - 43
#                             break  # stop iterating over blocks since we found one that overlaps
#                     # check if the coordinates are already taken by another trap
#                     if (x,y) not in placed_traps:        
#                     # add the trap to the list and add its coordinates to the placed set
#                         trap = Trap(x, y, 16, 32)
#                         trap.change_image("Idle")
#                         traps.append(trap)
#                         placed_traps.add((x, y))
#                         break # found an available coordinate, break out of the loop
#             #design
#             objects.append([*floor, 
#                         Block(0, WIN_HEIGHT - block_size * 2, block_size), 
#                         Block(block_size * 3, WIN_HEIGHT - block_size * 4, block_size),
#                         Block(block_size * 5, WIN_HEIGHT - block_size * 3, block_size),
#                         Block(block_size * 6, WIN_HEIGHT - block_size * 3, block_size),
#                         Block(block_size * 7, WIN_HEIGHT - block_size * 3, block_size),
#                         Block(block_size * 14, WIN_HEIGHT - block_size * 3, block_size),
#                         Block(block_size * 15, WIN_HEIGHT - block_size * 3, block_size),
#                         Block(block_size * 16, WIN_HEIGHT - block_size * 4, block_size),
#                         Block(block_size * 17, WIN_HEIGHT - block_size * 5, block_size),
#                         Block(block_size * 24, WIN_HEIGHT - block_size * 3, block_size),
#                         Block(block_size * 25, WIN_HEIGHT - block_size * 3, block_size),
#                         Block(block_size * 30, WIN_HEIGHT - block_size * 3, block_size),
#                         Block(block_size * 31, WIN_HEIGHT - block_size * 3, block_size),
#                         Block(block_size * 32, WIN_HEIGHT - block_size * 3, block_size),
#                         *traps, fire, monster])
#             destinations.append(Destination(5500, WIN_HEIGHT - block_size - 128, 32, 32))
#             collectibles.append([heart1, heart2, heart3, heart4, heart5, heart6, heart7, speed1, speed2, collectibles_bullets, *pineapples])
#         if j == 2:
#             blocks = []
#             traps = []
#             heart1 = Heart(block_size * 13, WIN_HEIGHT - block_size * 5, 16, 16)
#             heart2 = Heart(block_size * 17, WIN_HEIGHT - block_size * 8, 16, 16)
#             heart3 = Heart(block_size * 20, WIN_HEIGHT - block_size * 17, 16, 16)
#             heart4 = Heart(block_size * 25, WIN_HEIGHT - block_size * 10, 16, 16)
#             speed = Speed(900, WIN_HEIGHT - block_size - 64, 32, 32)
#             speed1 = Speed(block_size * 19, WIN_HEIGHT - block_size * 7 - 64, 32, 32)
#             collectibles_bullets = CollectibleBullets(1100, WIN_HEIGHT - block_size - 64, 32, 32)
#             #blocks and traps
#             fire = Fire(700, WIN_HEIGHT - block_size - 64, 16, 32)
#             # fire.on()
#             floor = [Block2(i * block_size, WIN_HEIGHT - block_size, block_size) for i in range(-WIN_WIDTH // block_size, (WIN_WIDTH * 20)// block_size)]

#             placed_traps = set()  # set to keep track of placed trap coordinates
        
#             for i in range(5):  # create 5 traps
#                 while True:
#                     x = random.randint(block_size * 4, WIN_WIDTH * 5 - block_size * 4)  # generate a random x coordinate within a range
#                     y = WIN_HEIGHT - block_size - 30  # set y-coordinate to floor level
#                     # check if there's a block at this position
#                     for block in blocks:
#                         if block.x <= x <= block.x + block.width and block.y <= y <= block.y + block.height:
#                             # there's a block at this position, adjust y-coordinate
#                             y = block.y - 43
#                             break  # stop iterating over blocks since we found one that overlaps
#                     # check if the coordinates are already taken by another trap
#                     if (x,y) not in placed_traps:        
#                     # add the trap to the list and add its coordinates to the placed set
#                         trap = Trap(x, y, 16, 32)
#                         trap.change_image("Idle")
#                         traps.append(trap)
#                         placed_traps.add((x, y))
#                         break # found an available coordinate, break out of the loop
#             #design
#             pineapples = [
#                 Pineapple(block_size * 14, WIN_HEIGHT - block_size * 5, 16, 16),
#                 Pineapple(block_size * 14.5, WIN_HEIGHT - block_size * 5.5, 16, 16),
#                 Pineapple(block_size * 15, WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(block_size * 24, WIN_HEIGHT - block_size * 19, 16, 16),
#                 Pineapple(block_size * 24.5, WIN_HEIGHT - block_size * 19, 16, 16),
#                 Pineapple(block_size * 25, WIN_HEIGHT - block_size * 19, 16, 16),
#                 Pineapple(block_size * 24, WIN_HEIGHT - block_size * 19.5, 16, 16),
#                 Pineapple(block_size * 24.5, WIN_HEIGHT - block_size * 19.5, 16, 16),
#                 Pineapple(block_size * 25, WIN_HEIGHT - block_size * 19.5, 16, 16),
#                 Pineapple(block_size * 17, WIN_HEIGHT - block_size * 23, 16, 16),
#                 Pineapple(block_size * 16.5, WIN_HEIGHT - block_size * 23, 16, 16),
#                 Pineapple(block_size * 16, WIN_HEIGHT - block_size * 23, 16, 16),
#                 Pineapple(block_size * 23.5, WIN_HEIGHT - block_size * 9, 16, 16),
#                 Pineapple(block_size * 26, WIN_HEIGHT - block_size * 10, 16, 16),
#                 Pineapple(block_size * 27, WIN_HEIGHT - block_size * 11, 16, 16),
#                 Pineapple(block_size * 17, WIN_HEIGHT - block_size * 19, 16, 16),
#                 Pineapple(block_size * 17.5, WIN_HEIGHT - block_size * 19, 16, 16),
#                 Pineapple(block_size * 18, WIN_HEIGHT - block_size * 19, 16, 16),
#             ]
#             objects.append([*floor, 
#                         Block2(10, WIN_HEIGHT - block_size * 2, block_size), 
#                         Block2(block_size * 13, WIN_HEIGHT - block_size * 3, block_size),
#                         Block2(block_size * 15, WIN_HEIGHT - block_size * 5, block_size),
#                         Block2(block_size * 17, WIN_HEIGHT - block_size * 6, block_size),
#                         Block2(block_size * 17, WIN_HEIGHT - block_size * 7, block_size),
#                         Block2(block_size * 19, WIN_HEIGHT - block_size * 7, block_size),
#                         Block2(block_size * 21, WIN_HEIGHT - block_size * 7, block_size),
#                         Block2(block_size * 23, WIN_HEIGHT - block_size * 8, block_size),
#                         Block2(block_size * 25, WIN_HEIGHT - block_size * 9, block_size),
#                         Block2(block_size * 27, WIN_HEIGHT - block_size * 10, block_size),
#                         Block2(block_size * 25, WIN_HEIGHT - block_size * 12, block_size),
#                         Block2(block_size * 23, WIN_HEIGHT - block_size * 14, block_size),
#                         Block2(block_size * 21, WIN_HEIGHT - block_size * 16, block_size),
#                         Block2(block_size * 19, WIN_HEIGHT - block_size * 16, block_size),
#                         Block2(block_size * 17, WIN_HEIGHT - block_size * 18, block_size),
#                         Block2(block_size * 24, WIN_HEIGHT - block_size * 18, block_size),
#                         Block2(block_size * 19, WIN_HEIGHT - block_size * 20, block_size),
#                         Block2(block_size * 17, WIN_HEIGHT - block_size * 22, block_size),
#                         Block2(block_size * 15, WIN_HEIGHT - block_size * 22, block_size),
#                         Block2(block_size * 14, WIN_HEIGHT - block_size * 22, block_size),
#                         Block2(block_size * 13, WIN_HEIGHT - block_size * 24, block_size),
#                         *traps, fire])
#             destinations.append(Destination(block_size * 12.5, WIN_HEIGHT - block_size * 24 - 128, 32, 32))
#             collectibles.append([heart1, heart2, heart3,heart4, speed, speed1, collectibles_bullets, *pineapples])

#         if j == 3:
#             blocks = []
#             traps = [
#                 Trap(1350, WIN_HEIGHT - block_size - 30, 16, 32),
#                 Trap(1450, WIN_HEIGHT - block_size - 30, 16, 32),
#                 Trap(3000, WIN_HEIGHT - block_size - 30, 16, 32),
#                 Trap(3600, WIN_HEIGHT - block_size*6.5 - 30, 16, 32),
#                 Trap(4350, WIN_HEIGHT - block_size - 30, 16, 32),
#                 Trap(5750, WIN_HEIGHT - block_size*3 - 30, 16, 32),
#                 Trap(5800, WIN_HEIGHT - block_size - 30, 16, 32),
#                 Trap(6000, WIN_HEIGHT - block_size - 30, 16, 32),
#                 Trap(7700 + block_size *7, WIN_HEIGHT - block_size*5 - 30, 16, 32),
#                 Trap(9000, WIN_HEIGHT - block_size - 30, 16, 32),
#             ]
#             heart1 = Heart(block_size * 5.2, WIN_HEIGHT - block_size * 6.5, 16, 16)
#             heart2 = Heart(7200, WIN_HEIGHT - block_size * 5, 16, 16)
#             heart3 = Heart(3560, WIN_HEIGHT - block_size * 5, 16, 16)
#             heart4 = Heart(6900, WIN_HEIGHT - block_size*2.2, 16, 16)
#             hearts = [heart1, heart2, heart3, heart4]
#             speed1 = Speed(900, WIN_HEIGHT - block_size - 64, 32, 32)
#             speed2 = Speed(4300, WIN_HEIGHT - block_size*6.5 - 64, 32, 32)
#             speed3 = Speed(7500, WIN_HEIGHT - block_size - 64, 32, 32)
#             speed4 = Speed(7500 + block_size *10, WIN_HEIGHT - block_size - 64, 32, 32)
            
#             collectibles_bullets = [
#                 CollectibleBullets(3120, WIN_HEIGHT - block_size * 5.5, 32, 32),
#                 CollectibleBullets(4000, WIN_HEIGHT - block_size * 1.5, 32, 32)
#                                     ]
#             #blocks and traps
#             monster = Monster(block_size * 8 + 25, WIN_HEIGHT - block_size * 5.5, 24, 24, 200)
#             monster2 = Monster(4000, WIN_HEIGHT - block_size * 7, 24, 24, 320)
#             monster3 = Monster(4900, WIN_HEIGHT - block_size * 1.8, 24, 24, 320)
#             monster4 = Monster(3000, WIN_HEIGHT - block_size * 1.8, 24, 24, 320)
#             monster5 = Monster(6770, WIN_HEIGHT - block_size * 1.8, 24, 24, 400)
#             monster6 = Monster(7550, WIN_HEIGHT - block_size * 1.8, 24, 24, 500)
#             monster7 = Monster(8000, WIN_HEIGHT - block_size * 1.8, 24, 24, 500)
#             monsters = [monster, monster2, monster3, monster4, monster5, monster6, monster7]

#             fires = [
#                 Fire(3900, WIN_HEIGHT - block_size - 64, 16, 32),
#                 Fire(3500, WIN_HEIGHT - block_size - 64, 16, 32),
#                 Fire(3650, WIN_HEIGHT - block_size - 64, 16, 32),
#                 Fire(5200, WIN_HEIGHT - block_size*6.5 - 64, 16, 32),
#                 Fire(5750, WIN_HEIGHT - block_size - 64, 16, 32),
#             ]

#             pineapples = [
#                 Pineapple(block_size * 3, WIN_HEIGHT - block_size * 2, 16, 16),
#                 Pineapple(block_size * 3.5, WIN_HEIGHT - block_size * 2, 16, 16),
#                 Pineapple(block_size * 4, WIN_HEIGHT - block_size * 2, 16, 16),
#                 Pineapple(block_size * 5.5, WIN_HEIGHT - block_size * 2, 16, 16),
#                 Pineapple(block_size * 6, WIN_HEIGHT - block_size * 2, 16, 16),
#                 Pineapple(block_size * 6.5, WIN_HEIGHT - block_size * 2, 16, 16),

#                 Pineapple(block_size * 8, WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(block_size * 9, WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(block_size * 10, WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(block_size * 17.5, WIN_HEIGHT - block_size * 4.2, 16, 16),
#                 Pineapple(block_size * 18, WIN_HEIGHT - block_size * 4.2, 16, 16),
#                 Pineapple(block_size * 18.5, WIN_HEIGHT - block_size * 4.2, 16, 16),
#                 Pineapple(block_size * 26, WIN_HEIGHT - block_size * 6.5, 16, 16),

#                 Pineapple(2200 + block_size *0.7, WIN_HEIGHT - block_size * 1.7, 16, 16),
#                 Pineapple(2200 + block_size *2.2, WIN_HEIGHT - block_size * 1.7, 16, 16),
#                 Pineapple(2200 + block_size *2.7, WIN_HEIGHT - block_size * 1.7, 16, 16),

#                 Pineapple(block_size * 19.5, WIN_HEIGHT - block_size * 1.7, 16, 16),
#                 Pineapple(block_size * 20, WIN_HEIGHT - block_size * 1.7, 16, 16),
#                 Pineapple(block_size * 20.5, WIN_HEIGHT - block_size * 1.7, 16, 16),

#                 Pineapple(2150, WIN_HEIGHT - block_size * 5.5, 16, 16),
#                 Pineapple(2150, WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(2150, WIN_HEIGHT - block_size * 6.5, 16, 16),

#                 Pineapple(2320, WIN_HEIGHT - block_size * 5.5, 16, 16),
#                 Pineapple(2320, WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(2320, WIN_HEIGHT - block_size * 6.5, 16, 16),


#                 Pineapple(2850, WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(2850, WIN_HEIGHT - block_size * 5.5, 16, 16),


#                 Pineapple(2850 + 150, WIN_HEIGHT - block_size * 2, 16, 16),
#                 Pineapple(2900 + 150, WIN_HEIGHT - block_size * 2, 16, 16),
#                 Pineapple(2950 + 150, WIN_HEIGHT - block_size * 2, 16, 16),
#                 Pineapple(3000 + 150, WIN_HEIGHT - block_size * 2, 16, 16),
#                 Pineapple(3050 + 150, WIN_HEIGHT - block_size * 2, 16, 16),
#                 Pineapple(2850 + 150, WIN_HEIGHT - block_size * 2.5, 16, 16),
#                 Pineapple(2900 + 150, WIN_HEIGHT - block_size * 2.5, 16, 16),
#                 Pineapple(2950 + 150, WIN_HEIGHT - block_size * 2.5, 16, 16),
#                 Pineapple(3000 + 150, WIN_HEIGHT - block_size * 2.5, 16, 16),
#                 Pineapple(3050 + 150, WIN_HEIGHT - block_size * 2.5, 16, 16),
                
#                 #upper
#                 Pineapple(3400, WIN_HEIGHT - block_size * 7, 16, 16),
#                 Pineapple(3400 + block_size * 0.5, WIN_HEIGHT - block_size * 7, 16, 16),
#                 Pineapple(3400 + block_size * 1, WIN_HEIGHT - block_size * 7, 16, 16),
#                 Pineapple(3580 + block_size * 0.5, WIN_HEIGHT - block_size * 7, 16, 16),
#                 Pineapple(3580 + block_size * 1, WIN_HEIGHT - block_size * 7, 16, 16),
#                 Pineapple(3800, WIN_HEIGHT - block_size * 8, 16, 16),
#                 Pineapple(3800 + block_size * 0.5, WIN_HEIGHT - block_size * 8, 16, 16),
#                 Pineapple(3800 + block_size * 1, WIN_HEIGHT - block_size * 8, 16, 16),
#                 Pineapple(3800 + block_size * 2, WIN_HEIGHT - block_size * 7, 16, 16),
#                 Pineapple(3800 + block_size * 2.5, WIN_HEIGHT - block_size * 7, 16, 16),

#                 #lower (thin blocks)
#                 Pineapple(3950, WIN_HEIGHT - block_size * 4.5, 16, 16),
#                 Pineapple(4000, WIN_HEIGHT - block_size * 4.5, 16, 16),
#                 Pineapple(4050, WIN_HEIGHT - block_size * 4.5, 16, 16),
#                 Pineapple(3950, WIN_HEIGHT - block_size * 4, 16, 16),
#                 Pineapple(4000, WIN_HEIGHT - block_size * 4, 16, 16),
#                 Pineapple(4050, WIN_HEIGHT - block_size * 4, 16, 16),

#                 Pineapple(4340, WIN_HEIGHT - block_size * 1.8, 16, 16),
#                 Pineapple(4380, WIN_HEIGHT - block_size * 1.8, 16, 16),
#                 Pineapple(4420, WIN_HEIGHT - block_size * 1.8, 16, 16),
#                 Pineapple(4460, WIN_HEIGHT - block_size * 1.8, 16, 16),
#                 Pineapple(4500, WIN_HEIGHT - block_size * 1.8, 16, 16),

#                 #thickblock
#                 Pineapple(4650, WIN_HEIGHT - block_size * 4, 16, 16),
#                 Pineapple(4700, WIN_HEIGHT - block_size * 4, 16, 16),

#                 Pineapple(4950, WIN_HEIGHT - block_size * 2.5, 16, 16),
#                 Pineapple(4990, WIN_HEIGHT - block_size * 2.5, 16, 16),
#                 Pineapple(5030, WIN_HEIGHT - block_size * 2.5, 16, 16),
#                 Pineapple(5070, WIN_HEIGHT - block_size * 2.5, 16, 16),
#                 Pineapple(5110, WIN_HEIGHT - block_size * 2.5, 16, 16),
#                 Pineapple(4950, WIN_HEIGHT - block_size * 3, 16, 16),
#                 Pineapple(4990, WIN_HEIGHT - block_size * 3, 16, 16),
#                 Pineapple(5030, WIN_HEIGHT - block_size * 3, 16, 16),
#                 Pineapple(5070, WIN_HEIGHT - block_size * 3, 16, 16),
#                 Pineapple(5110, WIN_HEIGHT - block_size * 3, 16, 16),

#                 Pineapple(5170, WIN_HEIGHT - block_size * 7.7, 16, 16),
#                 Pineapple(5210, WIN_HEIGHT - block_size * 7.7, 16, 16),
#                 Pineapple(5250, WIN_HEIGHT - block_size * 7.7, 16, 16),

#                 Pineapple(5700, WIN_HEIGHT - block_size * 6.5, 16, 16),
#                 Pineapple(5740, WIN_HEIGHT - block_size * 6.5, 16, 16),
#                 Pineapple(5810, WIN_HEIGHT - block_size * 6.5, 16, 16),


#                 Pineapple(5830 + block_size * 1, WIN_HEIGHT - block_size * 5.5, 16, 16),
#                 Pineapple(5830 + block_size * 1,WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(6130 + block_size * 1,WIN_HEIGHT - block_size * 4, 16, 16),
#                 Pineapple(6130 + block_size * 1,WIN_HEIGHT - block_size * 6.5, 16, 16),
#                 Pineapple(6170 + block_size * 1,WIN_HEIGHT - block_size * 6.5, 16, 16),
#                 Pineapple(6270 + block_size * 1,WIN_HEIGHT - block_size * 6.5, 16, 16),

#                 Pineapple(6800 ,WIN_HEIGHT - block_size * 4, 16, 16),
#                 Pineapple(6840 ,WIN_HEIGHT - block_size * 4, 16, 16),
#                 Pineapple(6880 ,WIN_HEIGHT - block_size * 4, 16, 16),

#                 Pineapple(7300 ,WIN_HEIGHT - block_size * 4, 16, 16),
#                 Pineapple(7300 + block_size * 0.5,WIN_HEIGHT - block_size * 4, 16, 16),

#                 #cheeto
#                 Pineapple(block_size * 68,WIN_HEIGHT - block_size * 5, 16, 16),
#                 Pineapple(block_size * 68.5,WIN_HEIGHT - block_size * 5, 16, 16),
#                 Pineapple(block_size * 69,WIN_HEIGHT - block_size * 5, 16, 16),

#                 Pineapple(block_size * 71.5,WIN_HEIGHT - block_size * 4.5, 16, 16),
#                 Pineapple(block_size * 72,WIN_HEIGHT - block_size * 4.5, 16, 16),
#                 Pineapple(block_size * 72.5,WIN_HEIGHT - block_size * 4.5, 16, 16),
#                 Pineapple(block_size * 71.5,WIN_HEIGHT - block_size * 5.5, 16, 16),
#                 Pineapple(block_size * 72,WIN_HEIGHT - block_size * 5.5, 16, 16),
#                 Pineapple(block_size * 72.5,WIN_HEIGHT - block_size * 5.5, 16, 16),

#                 Pineapple(block_size * 74,WIN_HEIGHT - block_size * 6.5, 16, 16),
#                 Pineapple(block_size * 74.5,WIN_HEIGHT - block_size * 6.5, 16, 16),

#                 #Hi
#                 Pineapple(block_size * 78.7,WIN_HEIGHT - block_size * 5, 16, 16),
#                 Pineapple(block_size * 78.7,WIN_HEIGHT - block_size * 5.5, 16, 16),
#                 Pineapple(block_size * 78.7,WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(block_size * 79.2,WIN_HEIGHT - block_size * 5.5, 16, 16),
#                 Pineapple(block_size * 79.7,WIN_HEIGHT - block_size * 5, 16, 16),
#                 Pineapple(block_size * 79.7,WIN_HEIGHT - block_size * 5.5, 16, 16),
#                 Pineapple(block_size * 79.7,WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(block_size * 80.5,WIN_HEIGHT - block_size * 5, 16, 16),
#                 Pineapple(block_size * 80.5,WIN_HEIGHT - block_size * 5.5, 16, 16),
#                 Pineapple(block_size * 80.5,WIN_HEIGHT - block_size * 6, 16, 16),

#                 #morecheeto
#                 Pineapple(block_size * 79,WIN_HEIGHT - block_size * 7, 16, 16),
#                 Pineapple(block_size * 78.5,WIN_HEIGHT - block_size * 6.5, 16, 16),
#                 Pineapple(block_size * 79,WIN_HEIGHT - block_size * 6.5, 16, 16),
#                 Pineapple(block_size * 79.5,WIN_HEIGHT - block_size * 6.5, 16, 16),


#                 Pineapple(block_size * 85,WIN_HEIGHT - block_size * 7.5, 16, 16),
#                 Pineapple(block_size * 85.5,WIN_HEIGHT - block_size * 7, 16, 16),
#                 Pineapple(block_size * 86,WIN_HEIGHT - block_size * 6.5, 16, 16),

#                 Pineapple(block_size * 89,WIN_HEIGHT - block_size * 7, 16, 16),
#                 Pineapple(block_size * 89.5,WIN_HEIGHT - block_size * 7, 16, 16),

#                 Pineapple(block_size * 91.5,WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(block_size * 92,WIN_HEIGHT - block_size * 6, 16, 16),

#                 Pineapple(block_size * 94.5,WIN_HEIGHT - block_size * 4.5, 16, 16),
#                 Pineapple(block_size * 94.5,WIN_HEIGHT - block_size * 4, 16, 16),
#                 Pineapple(block_size * 95,WIN_HEIGHT - block_size * 4.5, 16, 16),
#                 Pineapple(block_size * 95,WIN_HEIGHT - block_size * 4, 16, 16),

#                 Pineapple(block_size * 96,WIN_HEIGHT - block_size * 7, 16, 16),
#                 Pineapple(block_size * 96.5,WIN_HEIGHT - block_size * 7, 16, 16),
#                 Pineapple(block_size * 97,WIN_HEIGHT - block_size * 7, 16, 16),
#                 Pineapple(block_size * 97.5,WIN_HEIGHT - block_size * 6.5, 16, 16),
#                 Pineapple(block_size * 98,WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(block_size * 98.5,WIN_HEIGHT - block_size * 5.5, 16, 16),
#                 Pineapple(block_size * 99,WIN_HEIGHT - block_size * 5, 16, 16),
#                 Pineapple(block_size * 99.5,WIN_HEIGHT - block_size * 4.5, 16, 16),
#                 Pineapple(block_size * 100,WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(block_size * 100.5,WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(block_size * 101,WIN_HEIGHT - block_size * 6, 16, 16),
#                 Pineapple(block_size * 101.5,WIN_HEIGHT - block_size * 6, 16, 16),
                

#             ]
#             floor = [Block3(i * block_size, WIN_HEIGHT - block_size, block_size) for i in range(-WIN_WIDTH // block_size, (WIN_WIDTH * 11)// block_size)]

#             #design
#             objects.append([*floor, 
#                         Block3(0, WIN_HEIGHT - block_size * 2, block_size), 
#                         Block3(block_size * 5, WIN_HEIGHT - block_size * 5.5, block_size), 
#                         #small floating 
#                         Block3(block_size * 8, WIN_HEIGHT - block_size * 5, block_size),
#                         Block3(block_size * 9, WIN_HEIGHT - block_size * 5, block_size),
#                         Block3(block_size * 10, WIN_HEIGHT - block_size * 5, block_size),

#                         Block3(1200, WIN_HEIGHT - block_size * 2, block_size), 
#                         Block3(1350, WIN_HEIGHT - block_size * 5, block_size),
#                         Block3(1700, WIN_HEIGHT - block_size * 3.5, block_size), 
#                         Block3(1950, WIN_HEIGHT - block_size * 3.5, block_size), 

#                         Block3(2200, WIN_HEIGHT - block_size * 3.5, block_size), 
#                         Block3(2200 + block_size*3, WIN_HEIGHT - block_size * 3.5, block_size),
 
#                         Block3(2470, WIN_HEIGHT - block_size * 6, block_size),
#                         Block3(2470+block_size, WIN_HEIGHT - block_size * 6, block_size),

#                         Block3(2850, WIN_HEIGHT - block_size * 2, block_size),
#                         Block3(2850, WIN_HEIGHT - block_size * 3, block_size),
#                         Block3(3100, WIN_HEIGHT - block_size * 5, block_size),
#                         Block3(3350, WIN_HEIGHT - block_size * 2, block_size),
#                         Block3(3350, WIN_HEIGHT - block_size * 3, block_size),

#                         #upper level
#                         Block3(3200 + block_size *1, WIN_HEIGHT - block_size * 6.5, block_size),
#                         Block3(3200 + block_size *2, WIN_HEIGHT - block_size * 6.5, block_size),
#                         Block3(3200 + block_size *3, WIN_HEIGHT - block_size * 6.5, block_size),
#                         Block3(3200 + block_size *4, WIN_HEIGHT - block_size * 6.5, block_size),
#                         Block3(3200 + block_size *5, WIN_HEIGHT - block_size * 6.5, block_size),
                        
#                         Block3(3200 + block_size *8, WIN_HEIGHT - block_size * 6.5, block_size),
#                         Block3(3200 + block_size *9, WIN_HEIGHT - block_size * 6.5, block_size),
#                         Block3(3200 + block_size *10, WIN_HEIGHT - block_size * 6.5, block_size),
#                         Block3(3200 + block_size *11, WIN_HEIGHT - block_size * 6.5, block_size),

#                         Block3(3000 + block_size *14, WIN_HEIGHT - block_size * 6.5, block_size),
#                         #thin blocks
#                         Block3(3750, WIN_HEIGHT - block_size * 2, block_size),
#                         Block3(3750, WIN_HEIGHT - block_size * 3, block_size),
#                         Block3(4170, WIN_HEIGHT - block_size * 2, block_size),
#                         Block3(4170, WIN_HEIGHT - block_size * 3, block_size),

                        
#                         #thick blocks
#                         Block3(4650, WIN_HEIGHT - block_size * 2, block_size),
#                         Block3(4650, WIN_HEIGHT - block_size * 3, block_size),
#                         Block3(4650 + block_size, WIN_HEIGHT - block_size * 2, block_size),
#                         Block3(4650 + block_size, WIN_HEIGHT - block_size * 3, block_size),
#                         Block3(5300, WIN_HEIGHT - block_size * 2, block_size),
#                         Block3(5300, WIN_HEIGHT - block_size * 3, block_size),
#                         Block3(5300 + block_size, WIN_HEIGHT - block_size * 2, block_size),
#                         Block3(5300 + block_size, WIN_HEIGHT - block_size * 3, block_size),


#                         Block3(5000 + block_size , WIN_HEIGHT - block_size * 6.5, block_size),
#                         Block3(5000 + block_size *2, WIN_HEIGHT - block_size * 6.5, block_size),
#                         Block3(5000 + block_size *3, WIN_HEIGHT - block_size * 6.5, block_size),
#                         Block3(5000, WIN_HEIGHT - block_size * 5.5, block_size),

#                         #steps
#                         Block3(5600 + block_size, WIN_HEIGHT - block_size * 3, block_size),
#                         Block3(5500 + block_size, WIN_HEIGHT - block_size * 5, block_size),
#                         Block3(5800 + block_size, WIN_HEIGHT - block_size * 4.5, block_size),
#                         Block3(6000 + block_size, WIN_HEIGHT - block_size * 6, block_size),
#                         Block3(6100 + block_size, WIN_HEIGHT - block_size * 3.5, block_size),
#                         Block3(6250 + block_size, WIN_HEIGHT - block_size * 6, block_size),
#                         Block3(6450 + block_size, WIN_HEIGHT - block_size * 4, block_size),

#                         #hidden
#                         Block3(6800, WIN_HEIGHT - block_size * 3.5, block_size),
#                         Block3(6800 + block_size, WIN_HEIGHT - block_size * 3.5, block_size),

#                         Block3(7370, WIN_HEIGHT - block_size * 2, block_size),
                        
#                         Block3(7300+ block_size * 3, WIN_HEIGHT - block_size * 4.5, block_size),
#                         Block3(7300+ block_size * 4, WIN_HEIGHT - block_size * 4.5, block_size),
#                         Block3(7300+ block_size * 5, WIN_HEIGHT - block_size * 5.5, block_size),

#                         Block3(6870 + block_size *2, WIN_HEIGHT - block_size * 5.5, block_size),
#                         Block3(7100 + block_size *2, WIN_HEIGHT - block_size * 6.5, block_size),
#                         Block3(7100 + block_size *3, WIN_HEIGHT - block_size * 6.5, block_size),

#                         Block3(7300 + block_size *2, WIN_HEIGHT - block_size * 3.5, block_size),
              
#                         #big gap

#                         Block3(7500 + block_size *7.5, WIN_HEIGHT - block_size * 6, block_size),
#                         Block3(7500 + block_size *8.5, WIN_HEIGHT - block_size * 5, block_size),
#                         Block3(7500 + block_size *9.5, WIN_HEIGHT - block_size * 4, block_size),

#                         Block3(9100, WIN_HEIGHT - block_size * 3.5, block_size),
#                         Block3(8450 + block_size *3, WIN_HEIGHT - block_size * 4.8, block_size),
#                         Block3(8450 + block_size *4, WIN_HEIGHT - block_size * 4.8, block_size),

#                         Block3(8950 + block_size *3, WIN_HEIGHT - block_size * 6, block_size),
#                         Block3(8950 + block_size *5, WIN_HEIGHT - block_size * 3, block_size),
#                         Block3(8950 + block_size *7, WIN_HEIGHT - block_size * 5, block_size),
#                         Block3(8950 + block_size *8, WIN_HEIGHT - block_size * 5, block_size),

#                         Block3(9900, WIN_HEIGHT - block_size * 3.7, block_size),
#                         Block3(9900 + block_size, WIN_HEIGHT - block_size * 3.7, block_size),







#                         *traps, *fires, *monsters])
#             destinations.append(Destination(10000, WIN_HEIGHT - block_size*4.5, 32, 32))
#             collectibles.append([*hearts, speed1, speed2, speed3, speed4, *collectibles_bullets, *pineapples])

#     design["objects"] = objects
#     design["collectibles"] = collectibles
#     design["destinations"] = destinations
#     return design


# level1 = {
#     "objects": [
#         *[Block(i * block_size, WIN_HEIGHT - block_size, block_size) for i in range(-WIN_WIDTH // block_size, (WIN_WIDTH * 20)// block_size)],
#         Monster(block_size * 22, WIN_HEIGHT - block_size - 64, 16, 32, block_size * 2),
#         Fire(4200, WIN_HEIGHT - block_size - 64, 16, 32),

#         Block(0, WIN_HEIGHT - block_size * 2, block_size), 
#         Block(block_size * 3, WIN_HEIGHT - block_size * 4, block_size),
#         Block(block_size * 5, WIN_HEIGHT - block_size * 3, block_size),
#         Block(block_size * 6, WIN_HEIGHT - block_size * 3, block_size),
#         Block(block_size * 7, WIN_HEIGHT - block_size * 3, block_size),
#         Block(block_size * 14, WIN_HEIGHT - block_size * 3, block_size),
#         Block(block_size * 15, WIN_HEIGHT - block_size * 3, block_size),
#         Block(block_size * 16, WIN_HEIGHT - block_size * 4, block_size),
#         Block(block_size * 17, WIN_HEIGHT - block_size * 5, block_size),
#         Block(block_size * 24, WIN_HEIGHT - block_size * 3, block_size),
#         Block(block_size * 25, WIN_HEIGHT - block_size * 3, block_size),
#         Block(block_size * 30, WIN_HEIGHT - block_size * 3, block_size),
#         Block(block_size * 31, WIN_HEIGHT - block_size * 3, block_size),
#         Block(block_size * 32, WIN_HEIGHT - block_size * 3, block_size),
#     ],
#     "collectibles": [
#         Heart(block_size * 7, WIN_HEIGHT - block_size * 4, 16, 16),
#         Heart(block_size * 18, WIN_HEIGHT - block_size * 6, 16, 16),
#         Heart(block_size * 32, WIN_HEIGHT - block_size * 4, 16, 16),
#         Heart(block_size * 21, WIN_HEIGHT - block_size * 2, 16, 16),
#         Heart(block_size * 25, WIN_HEIGHT - block_size * 4, 16, 16),
#         Heart(4700, WIN_HEIGHT - block_size * 2, 16, 16),
#         Heart(5350, WIN_HEIGHT - block_size * 2, 16, 16),

#         Pineapple(block_size * 15, WIN_HEIGHT - block_size * 4, 12, 12),  
#         Pineapple(block_size * 16, WIN_HEIGHT - block_size * 5, 12, 12),
#         Pineapple(block_size * 17, WIN_HEIGHT - block_size * 6, 12, 12),
#         Pineapple(block_size * 24, WIN_HEIGHT - block_size * 4, 12, 12),
#         Pineapple(block_size * 31, WIN_HEIGHT - block_size * 4, 12, 12),
#         Pineapple(4800, WIN_HEIGHT - block_size * 3, 12, 12),
#         Pineapple(5000, WIN_HEIGHT - block_size * 2, 12, 12),
#         Pineapple(5100, WIN_HEIGHT - block_size * 3, 12, 12),

#         Speed(block_size * 10, WIN_HEIGHT - block_size - 64, 32, 32),
#         Speed(3500, WIN_HEIGHT - block_size - 64, 32, 32),
#         CollectibleBullets(block_size * 28, WIN_HEIGHT - block_size - 64, 32, 32)
#     ],
#     "destination": [
#         Destination(5500, WIN_HEIGHT - block_size - 128, 32, 32)
#     ]
# }

# level2 = {
#     "objects": [
#         *[Block3(i * block_size, WIN_HEIGHT - block_size, block_size) for i in range(-WIN_WIDTH // block_size, (WIN_WIDTH * 11)// block_size)],
#         Block3(0, WIN_HEIGHT - block_size * 2, block_size), 
#         Block3(block_size * 5, WIN_HEIGHT - block_size * 5.5, block_size), 
#         #small floating 
#         Block3(block_size * 8, WIN_HEIGHT - block_size * 5, block_size),
#         Block3(block_size * 9, WIN_HEIGHT - block_size * 5, block_size),
#         Block3(block_size * 10, WIN_HEIGHT - block_size * 5, block_size),

#         Block3(1200, WIN_HEIGHT - block_size * 2, block_size), 
#         Block3(1350, WIN_HEIGHT - block_size * 5, block_size),
#         Block3(1700, WIN_HEIGHT - block_size * 3.5, block_size), 
#         Block3(1950, WIN_HEIGHT - block_size * 3.5, block_size), 

#         Block3(2200, WIN_HEIGHT - block_size * 3.5, block_size), 
#         Block3(2200 + block_size*3, WIN_HEIGHT - block_size * 3.5, block_size),

#         Block3(2470, WIN_HEIGHT - block_size * 6, block_size),
#         Block3(2470+block_size, WIN_HEIGHT - block_size * 6, block_size),

#         Block3(2850, WIN_HEIGHT - block_size * 2, block_size),
#         Block3(2850, WIN_HEIGHT - block_size * 3, block_size),
#         Block3(3100, WIN_HEIGHT - block_size * 5, block_size),
#         Block3(3350, WIN_HEIGHT - block_size * 2, block_size),
#         Block3(3350, WIN_HEIGHT - block_size * 3, block_size),

#         #upper level
#         Block3(3200 + block_size *1, WIN_HEIGHT - block_size * 6.5, block_size),
#         Block3(3200 + block_size *2, WIN_HEIGHT - block_size * 6.5, block_size),
#         Block3(3200 + block_size *3, WIN_HEIGHT - block_size * 6.5, block_size),
#         Block3(3200 + block_size *4, WIN_HEIGHT - block_size * 6.5, block_size),
#         Block3(3200 + block_size *5, WIN_HEIGHT - block_size * 6.5, block_size),
        
#         Block3(3200 + block_size *8, WIN_HEIGHT - block_size * 6.5, block_size),
#         Block3(3200 + block_size *9, WIN_HEIGHT - block_size * 6.5, block_size),
#         Block3(3200 + block_size *10, WIN_HEIGHT - block_size * 6.5, block_size),
#         Block3(3200 + block_size *11, WIN_HEIGHT - block_size * 6.5, block_size),

#         Block3(3000 + block_size *14, WIN_HEIGHT - block_size * 6.5, block_size),
#         #thin blocks
#         Block3(3750, WIN_HEIGHT - block_size * 2, block_size),
#         Block3(3750, WIN_HEIGHT - block_size * 3, block_size),
#         Block3(4170, WIN_HEIGHT - block_size * 2, block_size),
#         Block3(4170, WIN_HEIGHT - block_size * 3, block_size),

        
#         #thick blocks
#         Block3(4650, WIN_HEIGHT - block_size * 2, block_size),
#         Block3(4650, WIN_HEIGHT - block_size * 3, block_size),
#         Block3(4650 + block_size, WIN_HEIGHT - block_size * 2, block_size),
#         Block3(4650 + block_size, WIN_HEIGHT - block_size * 3, block_size),
#         Block3(5300, WIN_HEIGHT - block_size * 2, block_size),
#         Block3(5300, WIN_HEIGHT - block_size * 3, block_size),
#         Block3(5300 + block_size, WIN_HEIGHT - block_size * 2, block_size),
#         Block3(5300 + block_size, WIN_HEIGHT - block_size * 3, block_size),


#         Block3(5000 + block_size , WIN_HEIGHT - block_size * 6.5, block_size),
#         Block3(5000 + block_size *2, WIN_HEIGHT - block_size * 6.5, block_size),
#         Block3(5000 + block_size *3, WIN_HEIGHT - block_size * 6.5, block_size),
#         Block3(5000, WIN_HEIGHT - block_size * 5.5, block_size),

#         #steps
#         Block3(5600 + block_size, WIN_HEIGHT - block_size * 3, block_size),
#         Block3(5500 + block_size, WIN_HEIGHT - block_size * 5, block_size),
#         Block3(5800 + block_size, WIN_HEIGHT - block_size * 4.5, block_size),
#         Block3(6000 + block_size, WIN_HEIGHT - block_size * 6, block_size),
#         Block3(6100 + block_size, WIN_HEIGHT - block_size * 3.5, block_size),
#         Block3(6250 + block_size, WIN_HEIGHT - block_size * 6, block_size),
#         Block3(6450 + block_size, WIN_HEIGHT - block_size * 4, block_size),

#         #hidden
#         Block3(6800, WIN_HEIGHT - block_size * 3.5, block_size),
#         Block3(6800 + block_size, WIN_HEIGHT - block_size * 3.5, block_size),

#         Block3(7370, WIN_HEIGHT - block_size * 2, block_size),
        
#         Block3(7300+ block_size * 3, WIN_HEIGHT - block_size * 4.5, block_size),
#         Block3(7300+ block_size * 4, WIN_HEIGHT - block_size * 4.5, block_size),
#         Block3(7300+ block_size * 5, WIN_HEIGHT - block_size * 5.5, block_size),

#         Block3(6870 + block_size *2, WIN_HEIGHT - block_size * 5.5, block_size),
#         Block3(7100 + block_size *2, WIN_HEIGHT - block_size * 6.5, block_size),
#         Block3(7100 + block_size *3, WIN_HEIGHT - block_size * 6.5, block_size),

#         Block3(7300 + block_size *2, WIN_HEIGHT - block_size * 3.5, block_size),

#         #big gap

#         Block3(7500 + block_size *7.5, WIN_HEIGHT - block_size * 6, block_size),
#         Block3(7500 + block_size *8.5, WIN_HEIGHT - block_size * 5, block_size),
#         Block3(7500 + block_size *9.5, WIN_HEIGHT - block_size * 4, block_size),

#         Block3(9100, WIN_HEIGHT - block_size * 3.5, block_size),
#         Block3(8450 + block_size *3, WIN_HEIGHT - block_size * 4.8, block_size),
#         Block3(8450 + block_size *4, WIN_HEIGHT - block_size * 4.8, block_size),

#         Block3(8950 + block_size *3, WIN_HEIGHT - block_size * 6, block_size),
#         Block3(8950 + block_size *5, WIN_HEIGHT - block_size * 3, block_size),
#         Block3(8950 + block_size *7, WIN_HEIGHT - block_size * 5, block_size),
#         Block3(8950 + block_size *8, WIN_HEIGHT - block_size * 5, block_size),

#         Block3(9900, WIN_HEIGHT - block_size * 3.7, block_size),
#         Block3(9900 + block_size, WIN_HEIGHT - block_size * 3.7, block_size),


#     ],
#     "collectibles": [
#         Heart(block_size * 13, WIN_HEIGHT - block_size * 5, 16, 16),
#         Heart(block_size * 17, WIN_HEIGHT - block_size * 8, 16, 16),
#         Heart(block_size * 20, WIN_HEIGHT - block_size * 17, 16, 16),
#         Heart(block_size * 25, WIN_HEIGHT - block_size * 10, 16, 16),
#         Speed(900, WIN_HEIGHT - block_size - 64, 32, 32),
#         Speed(block_size * 19, WIN_HEIGHT - block_size * 7 - 64, 32, 32),
#         CollectibleBullets(1100, WIN_HEIGHT - block_size - 64, 32, 32),
#         Pineapple(block_size * 14, WIN_HEIGHT - block_size * 5, 16, 16),
#         Pineapple(block_size * 14.5, WIN_HEIGHT - block_size * 5.5, 16, 16),
#         Pineapple(block_size * 15, WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(block_size * 24, WIN_HEIGHT - block_size * 19, 16, 16),
#         Pineapple(block_size * 24.5, WIN_HEIGHT - block_size * 19, 16, 16),
#         Pineapple(block_size * 25, WIN_HEIGHT - block_size * 19, 16, 16),
#         Pineapple(block_size * 24, WIN_HEIGHT - block_size * 19.5, 16, 16),
#         Pineapple(block_size * 24.5, WIN_HEIGHT - block_size * 19.5, 16, 16),
#         Pineapple(block_size * 25, WIN_HEIGHT - block_size * 19.5, 16, 16),
#         Pineapple(block_size * 17, WIN_HEIGHT - block_size * 23, 16, 16),
#         Pineapple(block_size * 16.5, WIN_HEIGHT - block_size * 23, 16, 16),
#         Pineapple(block_size * 16, WIN_HEIGHT - block_size * 23, 16, 16),
#         Pineapple(block_size * 23.5, WIN_HEIGHT - block_size * 9, 16, 16),
#         Pineapple(block_size * 26, WIN_HEIGHT - block_size * 10, 16, 16),
#         Pineapple(block_size * 27, WIN_HEIGHT - block_size * 11, 16, 16),
#         Pineapple(block_size * 17, WIN_HEIGHT - block_size * 19, 16, 16),
#         Pineapple(block_size * 17.5, WIN_HEIGHT - block_size * 19, 16, 16),
#         Pineapple(block_size * 18, WIN_HEIGHT - block_size * 19, 16, 16),

#     ],
#     "destination": [
#         Destination(block_size * 12.5, WIN_HEIGHT - block_size * 24 - 128, 32, 32)
#     ]
# }

# level3 = {
#     "objects": [
#         *[Block2(i * block_size, WIN_HEIGHT - block_size, block_size) for i in range(-WIN_WIDTH // block_size, (WIN_WIDTH * 20)// block_size)],
#         Block2(10, WIN_HEIGHT - block_size * 2, block_size), 
#         Block2(block_size * 13, WIN_HEIGHT - block_size * 3, block_size),
#         Block2(block_size * 15, WIN_HEIGHT - block_size * 5, block_size),
#         Block2(block_size * 17, WIN_HEIGHT - block_size * 6, block_size),
#         Block2(block_size * 17, WIN_HEIGHT - block_size * 7, block_size),
#         Block2(block_size * 19, WIN_HEIGHT - block_size * 7, block_size),
#         Block2(block_size * 21, WIN_HEIGHT - block_size * 7, block_size),
#         Block2(block_size * 23, WIN_HEIGHT - block_size * 8, block_size),
#         Block2(block_size * 25, WIN_HEIGHT - block_size * 9, block_size),
#         Block2(block_size * 27, WIN_HEIGHT - block_size * 10, block_size),
#         Block2(block_size * 25, WIN_HEIGHT - block_size * 12, block_size),
#         Block2(block_size * 23, WIN_HEIGHT - block_size * 14, block_size),
#         Block2(block_size * 21, WIN_HEIGHT - block_size * 16, block_size),
#         Block2(block_size * 19, WIN_HEIGHT - block_size * 16, block_size),
#         Block2(block_size * 17, WIN_HEIGHT - block_size * 18, block_size),
#         Block2(block_size * 24, WIN_HEIGHT - block_size * 18, block_size),
#         Block2(block_size * 19, WIN_HEIGHT - block_size * 20, block_size),
#         Block2(block_size * 17, WIN_HEIGHT - block_size * 22, block_size),
#         Block2(block_size * 15, WIN_HEIGHT - block_size * 22, block_size),
#         Block2(block_size * 14, WIN_HEIGHT - block_size * 22, block_size),
#         Block2(block_size * 13, WIN_HEIGHT - block_size * 24, block_size),
#         Fire(700, WIN_HEIGHT - block_size - 64, 16, 32).

#         Trap(1350, WIN_HEIGHT - block_size - 30, 16, 32),
#         Trap(1450, WIN_HEIGHT - block_size - 30, 16, 32),
#         Trap(3000, WIN_HEIGHT - block_size - 30, 16, 32),
#         Trap(3600, WIN_HEIGHT - block_size*6.5 - 30, 16, 32),
#         Trap(4350, WIN_HEIGHT - block_size - 30, 16, 32),
#         Trap(5750, WIN_HEIGHT - block_size*3 - 30, 16, 32),
#         Trap(5800, WIN_HEIGHT - block_size - 30, 16, 32),
#         Trap(6000, WIN_HEIGHT - block_size - 30, 16, 32),
#         Trap(7700 + block_size *7, WIN_HEIGHT - block_size*5 - 30, 16, 32),
#         Trap(9000, WIN_HEIGHT - block_size - 30, 16, 32),

#         Fire(3900, WIN_HEIGHT - block_size - 64, 16, 32),
#         Fire(3500, WIN_HEIGHT - block_size - 64, 16, 32),
#         Fire(3650, WIN_HEIGHT - block_size - 64, 16, 32),
#         Fire(5200, WIN_HEIGHT - block_size*6.5 - 64, 16, 32),
#         Fire(5750, WIN_HEIGHT - block_size - 64, 16, 32),

#         Monster(block_size * 8 + 25, WIN_HEIGHT - block_size * 5.5, 24, 24, 200),
#         Monster(4000, WIN_HEIGHT - block_size * 7, 24, 24, 320),
#         Monster(4900, WIN_HEIGHT - block_size * 1.8, 24, 24, 320),
#         Monster(3000, WIN_HEIGHT - block_size * 1.8, 24, 24, 320),
#         Monster(6770, WIN_HEIGHT - block_size * 1.8, 24, 24, 400),
#         Monster(7550, WIN_HEIGHT - block_size * 1.8, 24, 24, 500),
#         Monster(8000, WIN_HEIGHT - block_size * 1.8, 24, 24, 500)
#     ],
#     "collectibles": [
#         Heart(block_size * 5.2, WIN_HEIGHT - block_size * 6.5, 16, 16),
#         Heart(7200, WIN_HEIGHT - block_size * 5, 16, 16),
#         Heart(3560, WIN_HEIGHT - block_size * 5, 16, 16),
#         Heart(6900, WIN_HEIGHT - block_size*2.2, 16, 16),
#         Speed(900, WIN_HEIGHT - block_size - 64, 32, 32),
#         Speed(4300, WIN_HEIGHT - block_size*6.5 - 64, 32, 32),
#         Speed(7500, WIN_HEIGHT - block_size - 64, 32, 32),
#         Speed(7500 + block_size *10, WIN_HEIGHT - block_size - 64, 32, 32),
#         CollectibleBullets(3120, WIN_HEIGHT - block_size * 5.5, 32, 32),
#         CollectibleBullets(4000, WIN_HEIGHT - block_size * 1.5, 32, 32),

#         Pineapple(block_size * 3, WIN_HEIGHT - block_size * 2, 16, 16),
#         Pineapple(block_size * 3.5, WIN_HEIGHT - block_size * 2, 16, 16),
#         Pineapple(block_size * 4, WIN_HEIGHT - block_size * 2, 16, 16),
#         Pineapple(block_size * 5.5, WIN_HEIGHT - block_size * 2, 16, 16),
#         Pineapple(block_size * 6, WIN_HEIGHT - block_size * 2, 16, 16),
#         Pineapple(block_size * 6.5, WIN_HEIGHT - block_size * 2, 16, 16),

#         Pineapple(block_size * 8, WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(block_size * 9, WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(block_size * 10, WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(block_size * 17.5, WIN_HEIGHT - block_size * 4.2, 16, 16),
#         Pineapple(block_size * 18, WIN_HEIGHT - block_size * 4.2, 16, 16),
#         Pineapple(block_size * 18.5, WIN_HEIGHT - block_size * 4.2, 16, 16),
#         Pineapple(block_size * 26, WIN_HEIGHT - block_size * 6.5, 16, 16),

#         Pineapple(2200 + block_size *0.7, WIN_HEIGHT - block_size * 1.7, 16, 16),
#         Pineapple(2200 + block_size *2.2, WIN_HEIGHT - block_size * 1.7, 16, 16),
#         Pineapple(2200 + block_size *2.7, WIN_HEIGHT - block_size * 1.7, 16, 16),

#         Pineapple(block_size * 19.5, WIN_HEIGHT - block_size * 1.7, 16, 16),
#         Pineapple(block_size * 20, WIN_HEIGHT - block_size * 1.7, 16, 16),
#         Pineapple(block_size * 20.5, WIN_HEIGHT - block_size * 1.7, 16, 16),

#         Pineapple(2150, WIN_HEIGHT - block_size * 5.5, 16, 16),
#         Pineapple(2150, WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(2150, WIN_HEIGHT - block_size * 6.5, 16, 16),

#         Pineapple(2320, WIN_HEIGHT - block_size * 5.5, 16, 16),
#         Pineapple(2320, WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(2320, WIN_HEIGHT - block_size * 6.5, 16, 16),


#         Pineapple(2850, WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(2850, WIN_HEIGHT - block_size * 5.5, 16, 16),


#         Pineapple(2850 + 150, WIN_HEIGHT - block_size * 2, 16, 16),
#         Pineapple(2900 + 150, WIN_HEIGHT - block_size * 2, 16, 16),
#         Pineapple(2950 + 150, WIN_HEIGHT - block_size * 2, 16, 16),
#         Pineapple(3000 + 150, WIN_HEIGHT - block_size * 2, 16, 16),
#         Pineapple(3050 + 150, WIN_HEIGHT - block_size * 2, 16, 16),
#         Pineapple(2850 + 150, WIN_HEIGHT - block_size * 2.5, 16, 16),
#         Pineapple(2900 + 150, WIN_HEIGHT - block_size * 2.5, 16, 16),
#         Pineapple(2950 + 150, WIN_HEIGHT - block_size * 2.5, 16, 16),
#         Pineapple(3000 + 150, WIN_HEIGHT - block_size * 2.5, 16, 16),
#         Pineapple(3050 + 150, WIN_HEIGHT - block_size * 2.5, 16, 16),
        
#         #upper
#         Pineapple(3400, WIN_HEIGHT - block_size * 7, 16, 16),
#         Pineapple(3400 + block_size * 0.5, WIN_HEIGHT - block_size * 7, 16, 16),
#         Pineapple(3400 + block_size * 1, WIN_HEIGHT - block_size * 7, 16, 16),
#         Pineapple(3580 + block_size * 0.5, WIN_HEIGHT - block_size * 7, 16, 16),
#         Pineapple(3580 + block_size * 1, WIN_HEIGHT - block_size * 7, 16, 16),
#         Pineapple(3800, WIN_HEIGHT - block_size * 8, 16, 16),
#         Pineapple(3800 + block_size * 0.5, WIN_HEIGHT - block_size * 8, 16, 16),
#         Pineapple(3800 + block_size * 1, WIN_HEIGHT - block_size * 8, 16, 16),
#         Pineapple(3800 + block_size * 2, WIN_HEIGHT - block_size * 7, 16, 16),
#         Pineapple(3800 + block_size * 2.5, WIN_HEIGHT - block_size * 7, 16, 16),

#         #lower (thin blocks)
#         Pineapple(3950, WIN_HEIGHT - block_size * 4.5, 16, 16),
#         Pineapple(4000, WIN_HEIGHT - block_size * 4.5, 16, 16),
#         Pineapple(4050, WIN_HEIGHT - block_size * 4.5, 16, 16),
#         Pineapple(3950, WIN_HEIGHT - block_size * 4, 16, 16),
#         Pineapple(4000, WIN_HEIGHT - block_size * 4, 16, 16),
#         Pineapple(4050, WIN_HEIGHT - block_size * 4, 16, 16),

#         Pineapple(4340, WIN_HEIGHT - block_size * 1.8, 16, 16),
#         Pineapple(4380, WIN_HEIGHT - block_size * 1.8, 16, 16),
#         Pineapple(4420, WIN_HEIGHT - block_size * 1.8, 16, 16),
#         Pineapple(4460, WIN_HEIGHT - block_size * 1.8, 16, 16),
#         Pineapple(4500, WIN_HEIGHT - block_size * 1.8, 16, 16),

#         #thickblock
#         Pineapple(4650, WIN_HEIGHT - block_size * 4, 16, 16),
#         Pineapple(4700, WIN_HEIGHT - block_size * 4, 16, 16),

#         Pineapple(4950, WIN_HEIGHT - block_size * 2.5, 16, 16),
#         Pineapple(4990, WIN_HEIGHT - block_size * 2.5, 16, 16),
#         Pineapple(5030, WIN_HEIGHT - block_size * 2.5, 16, 16),
#         Pineapple(5070, WIN_HEIGHT - block_size * 2.5, 16, 16),
#         Pineapple(5110, WIN_HEIGHT - block_size * 2.5, 16, 16),
#         Pineapple(4950, WIN_HEIGHT - block_size * 3, 16, 16),
#         Pineapple(4990, WIN_HEIGHT - block_size * 3, 16, 16),
#         Pineapple(5030, WIN_HEIGHT - block_size * 3, 16, 16),
#         Pineapple(5070, WIN_HEIGHT - block_size * 3, 16, 16),
#         Pineapple(5110, WIN_HEIGHT - block_size * 3, 16, 16),

#         Pineapple(5170, WIN_HEIGHT - block_size * 7.7, 16, 16),
#         Pineapple(5210, WIN_HEIGHT - block_size * 7.7, 16, 16),
#         Pineapple(5250, WIN_HEIGHT - block_size * 7.7, 16, 16),

#         Pineapple(5700, WIN_HEIGHT - block_size * 6.5, 16, 16),
#         Pineapple(5740, WIN_HEIGHT - block_size * 6.5, 16, 16),
#         Pineapple(5810, WIN_HEIGHT - block_size * 6.5, 16, 16),


#         Pineapple(5830 + block_size * 1, WIN_HEIGHT - block_size * 5.5, 16, 16),
#         Pineapple(5830 + block_size * 1,WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(6130 + block_size * 1,WIN_HEIGHT - block_size * 4, 16, 16),
#         Pineapple(6130 + block_size * 1,WIN_HEIGHT - block_size * 6.5, 16, 16),
#         Pineapple(6170 + block_size * 1,WIN_HEIGHT - block_size * 6.5, 16, 16),
#         Pineapple(6270 + block_size * 1,WIN_HEIGHT - block_size * 6.5, 16, 16),

#         Pineapple(6800 ,WIN_HEIGHT - block_size * 4, 16, 16),
#         Pineapple(6840 ,WIN_HEIGHT - block_size * 4, 16, 16),
#         Pineapple(6880 ,WIN_HEIGHT - block_size * 4, 16, 16),

#         Pineapple(7300 ,WIN_HEIGHT - block_size * 4, 16, 16),
#         Pineapple(7300 + block_size * 0.5,WIN_HEIGHT - block_size * 4, 16, 16),

#         #cheeto
#         Pineapple(block_size * 68,WIN_HEIGHT - block_size * 5, 16, 16),
#         Pineapple(block_size * 68.5,WIN_HEIGHT - block_size * 5, 16, 16),
#         Pineapple(block_size * 69,WIN_HEIGHT - block_size * 5, 16, 16),

#         Pineapple(block_size * 71.5,WIN_HEIGHT - block_size * 4.5, 16, 16),
#         Pineapple(block_size * 72,WIN_HEIGHT - block_size * 4.5, 16, 16),
#         Pineapple(block_size * 72.5,WIN_HEIGHT - block_size * 4.5, 16, 16),
#         Pineapple(block_size * 71.5,WIN_HEIGHT - block_size * 5.5, 16, 16),
#         Pineapple(block_size * 72,WIN_HEIGHT - block_size * 5.5, 16, 16),
#         Pineapple(block_size * 72.5,WIN_HEIGHT - block_size * 5.5, 16, 16),

#         Pineapple(block_size * 74,WIN_HEIGHT - block_size * 6.5, 16, 16),
#         Pineapple(block_size * 74.5,WIN_HEIGHT - block_size * 6.5, 16, 16),

#         #Hi
#         Pineapple(block_size * 78.7,WIN_HEIGHT - block_size * 5, 16, 16),
#         Pineapple(block_size * 78.7,WIN_HEIGHT - block_size * 5.5, 16, 16),
#         Pineapple(block_size * 78.7,WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(block_size * 79.2,WIN_HEIGHT - block_size * 5.5, 16, 16),
#         Pineapple(block_size * 79.7,WIN_HEIGHT - block_size * 5, 16, 16),
#         Pineapple(block_size * 79.7,WIN_HEIGHT - block_size * 5.5, 16, 16),
#         Pineapple(block_size * 79.7,WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(block_size * 80.5,WIN_HEIGHT - block_size * 5, 16, 16),
#         Pineapple(block_size * 80.5,WIN_HEIGHT - block_size * 5.5, 16, 16),
#         Pineapple(block_size * 80.5,WIN_HEIGHT - block_size * 6, 16, 16),

#         #morecheeto
#         Pineapple(block_size * 79,WIN_HEIGHT - block_size * 7, 16, 16),
#         Pineapple(block_size * 78.5,WIN_HEIGHT - block_size * 6.5, 16, 16),
#         Pineapple(block_size * 79,WIN_HEIGHT - block_size * 6.5, 16, 16),
#         Pineapple(block_size * 79.5,WIN_HEIGHT - block_size * 6.5, 16, 16),


#         Pineapple(block_size * 85,WIN_HEIGHT - block_size * 7.5, 16, 16),
#         Pineapple(block_size * 85.5,WIN_HEIGHT - block_size * 7, 16, 16),
#         Pineapple(block_size * 86,WIN_HEIGHT - block_size * 6.5, 16, 16),

#         Pineapple(block_size * 89,WIN_HEIGHT - block_size * 7, 16, 16),
#         Pineapple(block_size * 89.5,WIN_HEIGHT - block_size * 7, 16, 16),

#         Pineapple(block_size * 91.5,WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(block_size * 92,WIN_HEIGHT - block_size * 6, 16, 16),

#         Pineapple(block_size * 94.5,WIN_HEIGHT - block_size * 4.5, 16, 16),
#         Pineapple(block_size * 94.5,WIN_HEIGHT - block_size * 4, 16, 16),
#         Pineapple(block_size * 95,WIN_HEIGHT - block_size * 4.5, 16, 16),
#         Pineapple(block_size * 95,WIN_HEIGHT - block_size * 4, 16, 16),

#         Pineapple(block_size * 96,WIN_HEIGHT - block_size * 7, 16, 16),
#         Pineapple(block_size * 96.5,WIN_HEIGHT - block_size * 7, 16, 16),
#         Pineapple(block_size * 97,WIN_HEIGHT - block_size * 7, 16, 16),
#         Pineapple(block_size * 97.5,WIN_HEIGHT - block_size * 6.5, 16, 16),
#         Pineapple(block_size * 98,WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(block_size * 98.5,WIN_HEIGHT - block_size * 5.5, 16, 16),
#         Pineapple(block_size * 99,WIN_HEIGHT - block_size * 5, 16, 16),
#         Pineapple(block_size * 99.5,WIN_HEIGHT - block_size * 4.5, 16, 16),
#         Pineapple(block_size * 100,WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(block_size * 100.5,WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(block_size * 101,WIN_HEIGHT - block_size * 6, 16, 16),
#         Pineapple(block_size * 101.5,WIN_HEIGHT - block_size * 6, 16, 16)
#     ],
#     "destination": [
#         Destination(block_size * 12.5, WIN_HEIGHT - block_size * 24 - 128, 32, 32)
#     ]
# }