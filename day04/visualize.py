import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Read input
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "i.txt")
lines = open(input_file).read().splitlines()

# Parse into set of positions for O(1) lookup
rolls = set()
max_i = len(lines)
max_j = len(lines[0]) if lines else 0

for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch == '@':
            rolls.add((i, j))

# Constants
CELL_SIZE = 4
PADDING = 15
WIDTH = max_j * CELL_SIZE + PADDING * 2
HEIGHT = max_i * CELL_SIZE + PADDING * 2 + 50
FPS = 60

# Colors
BG_COLOR = (15, 15, 35)
PAPER_COLOR = (255, 220, 100)
RED_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)
ACCENT_COLOR = (100, 200, 255)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paper Roll Removal - FAST")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 14)

DIRS = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

def count_neighbors(pos, rolls_set):
    """Count neighbors in O(1) using set lookup"""
    i, j = pos
    count = 0
    for di, dj in DIRS:
        if (i+di, j+dj) in rolls_set:
            count += 1
    return count

def find_removable(rolls_set):
    """Find all removable rolls in one pass"""
    removable = set()
    for pos in rolls_set:
        if count_neighbors(pos, rolls_set) < 4:
            removable.add(pos)
    return removable

# Pre-create surface for faster blitting
grid_surface = pygame.Surface((WIDTH, HEIGHT))

def draw_fast(rolls_set, to_remove_set, iteration, total_removed):
    """Optimized drawing"""
    grid_surface.fill(BG_COLOR)
    
    # Draw stats
    text = font.render(f"Iter: {iteration} | Removed: {total_removed} | Current: {len(to_remove_set)}", True, TEXT_COLOR)
    grid_surface.blit(text, (PADDING, 5))
    
    # Draw all rolls at once
    offset_y = PADDING + 35
    for i, j in rolls_set:
        x = PADDING + j * CELL_SIZE
        y = offset_y + i * CELL_SIZE
        color = RED_COLOR if (i, j) in to_remove_set else PAPER_COLOR
        pygame.draw.rect(grid_surface, color, (x, y, CELL_SIZE-1, CELL_SIZE-1))
    
    screen.blit(grid_surface, (0, 0))

# Main loop
iteration = 0
total_removed = 0
to_remove = set()
show_red = False
running = True
started = False
paused = False
frame_skip = 0

# Start button
button_rect = pygame.Rect(WIDTH // 2 - 60, HEIGHT // 2 - 20, 120, 40)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not started:
                    started = True
                else:
                    paused = not paused
            elif event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not started and button_rect.collidepoint(event.pos):
                started = True
    
    if started and not paused and rolls:
        frame_skip += 1
        
        # Slow down to see the animation
        if frame_skip >= 15:  # Every 15 frames (about 4 iterations per second)
            frame_skip = 0
            
            if not show_red:
                # Find removable
                to_remove = find_removable(rolls)
                
                if to_remove:
                    show_red = True
                    iteration += 1
                else:
                    # Done
                    text = font.render("COMPLETE!", True, (100, 255, 100))
                    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))
                    pygame.display.flip()
            else:
                # Remove them
                rolls -= to_remove
                total_removed += len(to_remove)
                show_red = False
    
    # Draw
    if not started:
        # Show start screen
        grid_surface.fill(BG_COLOR)
        
        # Draw initial grid
        offset_y = PADDING + 35
        for i, j in rolls:
            x = PADDING + j * CELL_SIZE
            y = offset_y + i * CELL_SIZE
            pygame.draw.rect(grid_surface, PAPER_COLOR, (x, y, CELL_SIZE-1, CELL_SIZE-1))
        
        # Draw start button
        pygame.draw.rect(grid_surface, (50, 150, 50), button_rect)
        pygame.draw.rect(grid_surface, (100, 255, 100), button_rect, 3)
        
        button_font = pygame.font.Font(None, 24)
        button_text = button_font.render("START", True, TEXT_COLOR)
        text_rect = button_text.get_rect(center=button_rect.center)
        grid_surface.blit(button_text, text_rect)
        
        # Instructions
        inst_text = font.render("Click START or press SPACE to begin", True, ACCENT_COLOR)
        grid_surface.blit(inst_text, (WIDTH // 2 - inst_text.get_width() // 2, button_rect.bottom + 20))
        
        screen.blit(grid_surface, (0, 0))
    else:
        draw_fast(rolls, to_remove if show_red else set(), iteration, total_removed)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
