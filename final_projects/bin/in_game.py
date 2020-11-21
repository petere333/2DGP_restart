from pico2d import *
from enemy import *
from player import *
from stage import *

player = None
image_back = None
endgame = False
closing = False
change_state = None
trash_can = []

score_font = None
current_score = None
moving = False


def init():
    global player, image_back, endgame, closing, change_state, enemies, enemy_bullets, player_bullets
    global player, moving, score_font, current_score, bullets_evade
    global catch_curve, catch_divide, catch_normal, num_curve, num_divide, num_normal, num_bullets
    global currentStage, stages, stage1, stage2, stage3, stage4, stage5

    catch_normal = 0
    catch_curve = 0
    catch_divide = 0
    num_normal = 0
    num_curve = 0
    num_divide = 0
    bullets_evade = 0
    num_bullets = 0
    currentStage = 0

    endgame = False
    closing = False
    moving = False
    change_state = None
    score_font = load_font("../res/score.ttf", 30)
    current_score = 0
    for i in range(len(player_bullets)):
        trash_can.append(player_bullets[-1])
        player_bullets.remove(player_bullets[-1])

    for i in range(len(enemies)):
        trash_can.append(enemies[-1])
        enemies.remove(enemies[-1])

    for i in range(len(enemy_bullets)):
        trash_can.append(enemy_bullets[-1])
        enemy_bullets.remove(enemy_bullets[-1])

    image_back = load_image("../res/back.png")
    player = Player()
    #  init stage
    stages = []
    stage1 = []
    stage2 = []
    stage3 = []
    stage4 = []
    stage5 = []

    stage1.append(CurveEnemy(375, 550, 6.5, 3))
    stage1.append(CurveEnemy(225, 550, 6.5, 3))
    stage1.append(CurveEnemy(425, 550, 8, 5))
    stage1.append(CurveEnemy(175, 550, 8, 5))

    stage1.append(DivideEnemy(225, 600, 0, 0, 10, True, 0))
    stage1.append(DivideEnemy(375, 600, 0, 0, 10, True, 0))

    stage1.append(Enemy(325, 500, 6))
    stage1.append(Enemy(275, 500, 6))
    stage1.append(Enemy(375, 500, 5.5))
    stage1.append(Enemy(225, 500, 5.5))
    stage1.append(Enemy(425, 500, 5))
    stage1.append(Enemy(175, 500, 5))

    stage2.append(Enemy(325, 500, 5.2))
    stage2.append(Enemy(275, 500, 5.2))
    stage2.append(Enemy(225, 500, 4.5))
    stage2.append(Enemy(375, 500, 4.5))

    stage2.append(Enemy(325, 550, 5))
    stage2.append(Enemy(275, 550, 5))

    stage2.append(Enemy(325, 450, 5))
    stage2.append(Enemy(275, 450, 5))
    stage2.append(Enemy(375, 450, 4.5))
    stage2.append(Enemy(225, 450, 4.5))
    stage2.append(Enemy(175, 450, 4))
    stage2.append(Enemy(425, 450, 4))

    stage2.append(CurveEnemy(425, 500, 5, 3.5))
    stage2.append(CurveEnemy(175, 500, 5, 3.5))

    stage2.append(CurveEnemy(375, 550, 5.5, 3.7))
    stage2.append(CurveEnemy(225, 550, 5.5, 3.7))

    stage2.append(DivideEnemy(425, 550, 0, 0, 5.5, True, 0))
    stage2.append(DivideEnemy(175, 550, 0, 0, 5.5, True, 0))

    stages.append(stage1)
    stages.append(stage2)
    # end init stage

    if len(enemies) == 0:
        for en in stages[currentStage]:
            enemies.append(en)
        print("number of enemies : ", len(enemies) + 1)
    pass


def update():
    global player, image_back, enemies, enemy_bullets, player_bullets, endgame, change_state, trash_can, num_bullets
    global catch_curve, catch_divide, catch_normal, current_score, bullets_evade, num_normal, num_curve, num_divide
    global stages, currentStage, maxStage
    #  모든 객체 상태 갱신
    player.update()
    for en in enemies:
        en.update()
        en.fire()
    for b in player_bullets:
        b.update()
    for eb in enemy_bullets:
        eb.update()

    for b in player_bullets:  # 적 기체와 아군 총알 충돌
        for en in enemies:
            if en.x-22 <= b.x <= en.x+22 and en.y-22 <= b.y <= en.y+22:
                b.crash = True
                en.collides = True
                if en.type == 1:
                    catch_normal += en.score
                    num_normal += 1
                elif en.type == 2:
                    catch_curve += en.score
                    num_curve += 1
                elif en.type == 3:
                    catch_divide += en.score
                    num_divide += 1
                current_score += en.score

    for en in enemies:  # 적 기체 제거
        if en.collides:
            trash_can.append(en)
            enemies.remove(en)
            print("number of enemies : ", len(enemies) + 1)
    for b in player_bullets:  # 아군 총알 제거
        if b.crash:
            trash_can.append(b)
            player_bullets.remove(b)

    for eb in enemy_bullets:  # 적 총알과 플레이어 충돌
        if player.x-22 <= eb.x <= player.x+22 and player.y-22 <= eb.y <= player.y+22:
            eb.crash = True
            player.collides = True
    for eb in enemy_bullets:  # 적 총알 맵 끝 도달
        if eb.crash:
            if eb.crashed_to_wall is True:
                bullets_evade += 5
                num_bullets += 1
                current_score += 5
            trash_can.append(eb)
            enemy_bullets.remove(eb)
            del eb

    for en in enemies:  # 적 기체와 플레이어 충돌
        if player.x-31 <= en.x <= player.x+31 and player.y-31 <= en.y <= player.y+31:
            player.collides = True

    if player.collides:  # 플레이어 사망
        trash_can.append(player)

        player = None
        for i in range(len(player_bullets)):
            trash_can.append(player_bullets[-1])
            player_bullets.remove(player_bullets[-1])

        for i in range(len(enemies)):
            trash_can.append(enemies[-1])
            enemies.remove(enemies[-1])

        for i in range(len(enemy_bullets)):
            trash_can.append(enemy_bullets[-1])
            enemy_bullets.remove(enemy_bullets[-1])

        for i in range(len(trash_can)):
            trash_can.remove(trash_can[-1])
        endgame = True
        change_state = 2

    elif len(enemies) == 0 and len(enemy_bullets) == 0:  # 플레이어 생존 및 모든 적 처치시
        if currentStage + 1 >= maxStage:  # 마지막 스테이지일 시 종료
            endgame = True
            change_state = 2
        else:  # 아니면 다음 스테이지 시작
            currentStage += 1

            for i in range(len(player_bullets)):
                trash_can.append(player_bullets[-1])
                player_bullets.remove(player_bullets[-1])
            for i in range(len(trash_can)):
                trash_can.remove(trash_can[-1])

            for en in stages[currentStage]:
                en.spawnedTime = time.time()
                en.last_fire = time.time()
                enemies.append(en)
            print("number of enemies : ", len(enemies) + 1)

def draw():
    global player, player_bullets, enemy_bullets, enemies, image_back, current_score, currentStage
    cs = currentStage+1
    image_back.draw(300, 400)
    player.draw()
    for en in enemies:
        en.draw()
    for b in player_bullets:
        b.draw()
    for eb in enemy_bullets:
        eb.draw()
    score_font.draw(0, 785, "Score : %d" % current_score, (255, 255, 255))
    score_font.draw(493, 785, "Stage %d" % cs, (255, 255, 255))
    pass


def handle_event():
    global player, endgame, closing, change_state, moving
    # prev_dx = boy.dx
    evt = get_events()
    for e in evt:
        if e.type == SDL_QUIT:
            endgame = True
            closing = True
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:

                endgame = True
                change_state = 2
            elif e.key == SDLK_LEFT:
                player.dx = -7

            elif e.key == SDLK_RIGHT:
                player.dx = 7

            elif e.key == SDLK_UP:
                player.dy = 7

            elif e.key == SDLK_DOWN:
                player.dy = -7
            elif e.key == SDLK_SPACE:
                player.fire()
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                player.dx = 0
            elif e.key == SDLK_RIGHT:
                player.dx = 0
            elif e.key == SDLK_UP:
                player.dy = 0
            elif e.key == SDLK_DOWN:
                player.dy = 0