#SQL Tables

# --- Table Creation ---
# HITBOX TABLE 
create_hitbox_table = """
CREATE TABLE Hitboxes (
    hitbox_id INTEGER PRIMARY KEY,
    image_id INTEGER NOT NULL,
    x INTEGER NOT NULL,
    y INTEGER NOT NULL,
    width INTEGER NOT NULL,
    height INTEGER NOT NULL,
    type TEXT NOT NULL,
    FOREIGN KEY (image_id) REFERENCES Images(image_id)
);
"""

# IMAGE TABLE
create_image_table = """
CREATE TABLE Images (
    image_id INTEGER PRIMARY KEY,
    file_path TEXT NOT NULL,
    width INTEGER NOT NULL
    height INTEGER NOT NULL
    pivot_x INTEGER NOT NULL
    pivot_y INTEGER NOT NULL
    duration REAL NOT NULL
   );   
"""

# ANIMATION TABLE
create_animation_table = """
CREATE TABLE Animations (
    animation_id INTEGER PRIMARY KEY,
    animation_name TEXT NOT NULL,
    description TEXT,
    order INTEGER NOT NULL,
    image_id INTEGER NOT NULL,
    FOREIGN KEY (image_id) REFERENCES Images(image_id)
   );
"""

# SOUND TABLE
create_sound_table = """
CREATE TABLE Sounds (
    sound_id INTEGER PRIMARY KEY,
    animation_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    start_time REAL NOT NULL DEFAULT 0,
    volume REAL NOT NULL DEAFULT 1,
    loop INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY(animation_id) REFERENCES Animation(animation_id)
);
"""

# --- Junction Table Creation ---
# ANIMATION IMAGE JUNCTION TABLE
create_junction_animation_image_table = """
CREATE TABLE Animation_Image (
  Animation_id INTEGER,
  Image_id INTEGER,
  PRIMARY KEY (Animation_id, image_id),
  FOREIGN KEY (Animation_id) REFERENCES Animation (id),
  FOREIGN KEY (Image_id) REFERENCES Image (id)
);
"""

# IMAGE HITBOX JUNCTION TABLE
create_junction_image_hitbox_table = """
CREATE TABLE Image_Hitbox (
  Image_id INTEGER,
  Hitbox_id INTEGER,
  PRIMARY KEY (Image_id, Hitbox_id),
  FOREIGN KEY (Image_id) REFERENCES Image (id),
  FOREIGN KEY (Hitbox_id) REFERENCES Hitbox (id)
);
"""
# ------------------------------------------        

# --- Adding to table ---

def add_hitbox_db(image_id, x, y, width, height, hitbox_type):
    
    out = f"""
    INSERT INTO
      Hitboxes (image_id, x, y, width, height, type)
    VALUES ({image_id}, {x}, {y}, {width}, {height}, '{hitbox_type}');
    """
    def add_into_junction_table_image_hitbox():
        pass
    return out

def add_image_db(path, piv_x, piv_y, width, height, duration):

    out = f"""
    INSERT INTO
      Images (file_path, pivot_x, pivot_y, width, height, duration)
    VALUES ('{path}', {piv_x}, {piv_y}, {width}, {height}, {duration});
    """
    return out

def add_animation_db(name, image_id, order, description = ''):
    out = f"""
    INSERT INTO
      Animations (name, image_id, order, description)
    VALUES ('{name}', {image_id}, {order}, '{description}');
    """
    
    def add_into_junction_table_animation_image():
        pass
    return out    

def add_sound_db(path, name, animation_id, start_time = 0.0, volume = 1, loop = 0):
    out = f"""
    INSERT INTO
      Sounds (file_path, name, animation_id, start_time, volume, loop)
    VALUES ('{path}', {name}, {animation_id}, {start_time}, {volume}, {loop});
    """
    return out
# ------------------------------------------

# --- removing from table ---
def delete_animation_by_name():
    """
    will delete all assosiations with animation by 
    """

# --- Queries ---
def table_insert(table: str):
    """
    Allows a clean insert from one table into another by eliminating the close statement
    """
    return table.replace(";", "")
