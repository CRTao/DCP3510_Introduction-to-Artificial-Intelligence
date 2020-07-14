import crossword_tools
import constants
import tkinter

def display_puzzle_solutions(puzzle, solution_set, new_puzzle):
    def on_restart_button():
        new_puzzle()
    
    
    solution_coord_maps = crossword_tools.get_puzzle_coordmaps(puzzle, solution_set)
    display_coordmaps_on_pages(solution_coord_maps, 
                               solution_coord_maps[0].get_max_x() + 1, 
                               solution_coord_maps[0].get_max_y() + 1, 
                               True, constants.NEW_PUZZLE_BTN_TEXT, 
                               on_restart_button, True)

def display_coordmaps_on_pages(coordmaps, grid_width, grid_height,
                               show_middle_btn=False, middle_btn_text=None,
                               middle_button_action=None, 
                               close_on_middle_btn=False):
    MIN_WIDTH = 6
    BORDER_WIDTH = 1
    
    grid_width = max(grid_width + 2 * BORDER_WIDTH, MIN_WIDTH)
    grid_height = grid_height + 2 * BORDER_WIDTH
    num_coordmaps = len(coordmaps)
    grid_tiles = []
    current_page = 0
    
    def display_coordmap(coordmap):
        for x in range(len(grid_tiles)):
            for y in range(len(grid_tiles[x])):
                char_at_tile = coordmap.get_val(x - BORDER_WIDTH, y - BORDER_WIDTH)
                if char_at_tile:
                    grid_tiles[x][y].configure(text=char_at_tile, 
                                               background=constants.GUI_SELECTED_TILE_COLOR, 
                                               activebackground=constants.GUI_SELECTED_TILE_COLOR)
                else:
                    grid_tiles[x][y].configure(text=" ", 
                                               background=constants.GUI_DESELECTED_TILE_COLOR, 
                                               activebackground=constants.GUI_DESELECTED_TILE_COLOR)
    
    def next_page(next_page_btn, prev_page_btn):
        nonlocal current_page
        if current_page + 1 >= num_coordmaps:
            return
        
        current_page = current_page + 1
        if current_page + 1 >= num_coordmaps:
            next_page_btn.configure(state=tkinter.DISABLED)
        
        prev_page_btn.configure(state=tkinter.NORMAL)
        
        display_coordmap(coordmaps[current_page])
        
    def prev_page(next_page_btn, prev_page_btn):
        nonlocal current_page
        if current_page <= 0:
            return
        
        current_page = current_page - 1
        if current_page <= 0:
            prev_page_btn.configure(state=tkinter.DISABLED)

        next_page_btn.configure(state=tkinter.NORMAL)
            
        display_coordmap(coordmaps[current_page])
    
    def on_middle_btn_click(root):
        if close_on_middle_btn:
            root.destroy()
        
        if middle_button_action:
            middle_button_action()
    
    if not coordmaps:
        return
        
    root = tkinter.Tk()
    
    for x in range(grid_width):
        grid_tiles.append([])
        for y in range(grid_height):
            tile = tkinter.Button(root, borderwidth=1, height="2", width="2", 
                                  background=constants.GUI_DESELECTED_TILE_COLOR, 
                                  activebackground=constants.GUI_DESELECTED_TILE_COLOR, 
                                  disabledforeground="black",
                                  state=tkinter.DISABLED, font=("Monospace", 12))
            grid_tiles[x].append(tile)
            tile.grid(row=y, column=x)

    if len(coordmaps) <= 1:
        next_btn_state = tkinter.DISABLED
    else:
        next_btn_state = tkinter.NORMAL
        
    next_btn = tkinter.Button(borderwidth=1, 
                              background=constants.GUI_DESELECTED_TILE_COLOR, 
                              text=constants.RIGHT_BTN_TEXT, 
                              state=next_btn_state)
    prev_btn = tkinter.Button(borderwidth=1, 
                              background=constants.GUI_DESELECTED_TILE_COLOR, 
                              text=constants.LEFT_BTN_TEXT, 
                              state=tkinter.DISABLED)
    middle_btn = tkinter.Button(borderwidth=1, 
                               background=constants.GUI_DESELECTED_TILE_COLOR, 
                               text=middle_btn_text, 
                               command=lambda: on_middle_btn_click(root))
    
    next_btn.configure(command=lambda: next_page(next_btn, prev_btn))
    prev_btn.configure(command=lambda: prev_page(next_btn, prev_btn))
    
    next_btn.grid(row=grid_height, column=grid_width - 2, columnspan=2)
    prev_btn.grid(row=grid_height, column=0, columnspan=2)
    middle_btn.grid(row=grid_height, column=int(grid_width / 2 - 1), 
                   columnspan = 2 + grid_width % 2)
    
    display_coordmap(coordmaps[0])
    
    root.mainloop()
