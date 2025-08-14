import sys
import pygame
import math
import random
from multiprocessing import Process

pygame.init()

# 创建屏幕
def create_screen():
    screen = pygame.display.set_mode((400, 600))
    pygame.display.set_caption("Rolling Cosine Graph")
    screen.fill((0, 255, 255))

    # 绘制坐标轴
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (400, 300), 2)  # x 轴
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), 2)  # y 轴

    return screen

def run_window():
    screen = create_screen()
    offset = 0  # 定义初始滚动偏移量

    # 获取当前窗口的位置（随机）
    screen_rect = screen.get_rect()
    new_x = random.randint(0, 800)  # 随机生成一个新的 x 坐标
    new_y = random.randint(0, 600)  # 随机生成一个新的 y 坐标
    screen_rect.topleft = (new_x, new_y)  # 设置窗口的起始位置

    # 主循环
    while True:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 每次关闭窗口时新增两个新窗口
                for _ in range(1):
                    Process(target=run_window).start()
                return

        # 绘制背景
        screen.fill((0, 255, 255))

        # 绘制坐标轴
        pygame.draw.line(screen, (0, 0, 0), (0, 300), (400, 300), 2)  # x 轴
        pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), 2)  # y 轴

        # 绘制滚动 cos 图像
        draw_cosine(screen, offset)

        # 更新偏移量，实现滚动效果
        offset += 2

        # 刷新屏幕
        pygame.display.flip()

        # 控制帧率
        pygame.time.Clock().tick(60)

def draw_cosine(screen, offset):
    for x in range(0, 400):  # x 的范围覆盖整个屏幕宽度
        # 将屏幕上的 x 映射到数学坐标系，并加上偏移量实现滚动
        math_x = (x + offset) / 50  # 控制滚动速度
        math_y = math.cos(math_x)  # 计算 cos 值

        # 将数学坐标系的 y 值映射到屏幕坐标
        screen_y = 300 - int(math_y * 100)  # 放大 100 倍并翻转 y

        # 在屏幕上绘制点
        pygame.draw.circle(screen, (0, 0, 255), (x, screen_y), 2)

if __name__ == "__main__":
    run_window()
