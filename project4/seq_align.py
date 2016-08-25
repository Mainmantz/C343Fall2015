#! /usr/bin/env python

import sys, time, random
import pygame

e_aplh = "abcdefghijklmnopqrstuvwxyz"
dna_alph = "ACGT"

# generate random string drawn from the given alphabet and of a given length
def gen_random_string(alphabet, length):
    a_len = len(alphabet)
    ret = ""
    for n in range(length):
        ret += alphabet[random.randint(0, a_len-1)]
    return ret

# print gen_random_string(e_aplh, 5)

SPACE_CHAR = '_'
SPACE_PENALTY = -1

# the scoring function
def s(x, y):
    if x == SPACE_CHAR or y == SPACE_CHAR:
        return SPACE_PENALTY
    elif x == y:
        return 2
    else:
        return -2

TILE_SIZE = 40
tile_color = (255, 255, 255)
highlight_color = (120, 129, 250)

def init_board(m, n):
    screen = pygame.display.set_mode(((m+2)*TILE_SIZE, (n+2)*TILE_SIZE))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Dot Board')
    pygame.font.init()
    font = pygame.font.Font(None, 15)
    return screen, font

def create_tile(font, text, color):
    tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
    tile.fill(color)
    b1 = font.render(text, 1, (0, 0, 0))
    tile.blit(b1, (TILE_SIZE/2, TILE_SIZE/2))
    return tile

def render_board(board, font, s1, s2, F):
    for i in range(len(s1)):
        tile = create_tile(font, s1[i], tile_color)
        board.blit(tile, ((i+2)*TILE_SIZE, 0))
    tile = create_tile(font, '', tile_color); board.blit(tile, (0, 0))
    tile = create_tile(font, '', tile_color); board.blit(tile, (TILE_SIZE, 0))
    for j in range(len(s2)):
        tile = create_tile(font, s2[j], tile_color)
        board.blit(tile, (0, (j+2)*TILE_SIZE))
    tile = create_tile(font, '', tile_color); board.blit(tile, (0, TILE_SIZE))
    for (x,y) in sorted(F.keys()):
        tile = create_tile(font, str(F[(x,y)]), tile_color)
        board.blit(tile, ((x+1)*TILE_SIZE, (y+1)*TILE_SIZE))
############################################################################
   
   
# the scoring function
def score(x, y):
    if x == SPACE_CHAR or y == SPACE_CHAR:
        return SPACE_PENALTY
    elif x == y:
        return 2
    else:
        return -2    
   
def seq_align(s1, s2, enable_graphics=True):
   # variables
    best_score = 0  # we will have an optimal score and need to keep track
    location_best = (0,0)
      # make a array[][]   
    matrix = [[0 for x in range(len(s1)+1)] for y in range(len(s2)+1)]

  # get the outer bounds
    for x in range(1, len(s2)+1):
        matrix[x][0] = x * -1
    
    for y in range(1, len(s1)+1):
        matrix[0][y] = y * -1
        
    for x in range(1, len(s2)+1):
        for y in range(1, len(s1)+1):
            matrix[x][y] = max(
                matrix[x-1][y-1] + score(s1[y-1], s2[x-1]), #diagonal
                matrix[x-1][y] + SPACE_PENALTY, #right
                matrix[x][y-1] + SPACE_PENALTY  #left
                )
            
            if matrix[x][y] > best_score:
                best_score  = matrix[x][y]
                location_best = (x,y)

    s1_len = len(s1)
    s2_len = len(s2)
    while location_best[0] != 0 and location_best[1] != 0:
        
        x = location_best[0]
        y = location_best[1]

        best_score  = max(
            matrix[x][y-1],   # up
            matrix[x-1][y],   # left
            matrix[x-1][y-1]  # diag
            )
        if best_score  == matrix[x-1][y-1]: # diag
            location_best = (x-1, y-1)
            s1_len -= 1
            s2_len -= 1

        elif best_score  == matrix[x][y-1]: # up
            location_best = (x, y-1)
            s1_len -= 1
            s2 = s2[:s2_len] + '_' + s2[s2_len:]

        elif best_score == matrix[x-1][y]: # left
            location_best = (x-1, y)
            s2_len -= 1
            s1 = s1[:s1_len] + '_' + s1[s1_len:]
#    print(len(s1))
#    format_tb(matrix,len(s1))
    return s1, s2


        # a.addSpace(i)  add a space if down
        # b.addSpace(i)  add a space if right
        # string = string[:i] + '_' + string[i:]
        # matrix[i][j] = max(diag, down, right)
############################################################################

if len(sys.argv) == 2 and sys.argv[1] == 'test':
    f=open('tests.txt', 'r');tests= eval(f.read());f.close()
    cnt = 0; passed = True
    for ((s1, s2), (a1, a2)) in tests:
        (ret_a1, ret_a2) = seq_align(s1, s2, False)
        if (ret_a1 != a1) or (ret_a2 != a2):
            print("test#" + str(cnt) + " failed...")
            passed = False
        cnt += 1
    if passed: print("All tests passed!")
elif len(sys.argv) == 2 and sys.argv[1] == 'gentests':
    tests = []
    for n in range(25):
        m = random.randint(8, 70); n = random.randint(8, 70)
        (s1, s2) = (gen_random_string(dna_alph, m), gen_random_string(dna_alph, n))
        (a1, a2) = seq_align(s1, s2, False)
        tests.append(((s1, s2), (a1, a2)))
    f=open('tests.txt', 'w');f.write(str(tests));f.close()
else:
    l = [('ACACACTA', 'AGCACACA'), ('IMISSMISSISSIPI', 'MYMISSISAHIPPIE')]
    enable_graphics = True
    if enable_graphics: pygame.init()
    for (s1, s2) in l:
        print 'sequences:'
        print (s1, s2)
        
        m = len(s1)
        n = len(s2)
        
        print 'alignment: '
        print seq_align(s1, s2, enable_graphics)

    if enable_graphics: pygame.quit()




  #  score = 0
  #  d = {}
  #  dictionary =  map(lambda a, b: d.update({a, b}), s1, s2)

