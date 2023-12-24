import pygame


def points_file():
    file = open("points.txt").readline()
    list_of_points = []
    for i in file.split(', '):
        points = [float(j.replace(',', '.')) for j in i[1:-1].split(';')]
        list_of_points.append(points)
    return list_of_points


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Zoom')
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    list_of_points = points_file()
    scale = 10
    center_w = width // 2
    center_h = height // 2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    scale += 1
                elif event.y == -1 and scale > 0:
                    scale -= 1
        screen.fill((0, 0, 0))
        x, y = list_of_points[0]
        for i in range(1, len(list_of_points)):
            x1, y1 = list_of_points[i]
            x = center_w + x * scale
            y = center_h - y * scale
            x1 = center_w + x1 * scale
            y1 = center_h - y1 * scale
            start_coords = (x, y)
            top_coords = (x1, y1)
            pygame.draw.line(screen, (255, 255, 255), start_coords, top_coords, 1)
            x, y = list_of_points[i]
        pygame.display.flip()
