from src.vec_2d import Vec2D
from src.traffic_lights import TrafficLigth


def create_roundabout(mp):
    # Down
    for cell in mp.cellmap[18:31, 0]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[15:18, 1]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[31:34, 1]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[13:15, 2]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[34:36, 2]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[11:13, 3]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[36:38, 3]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[10:11, 4]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[38:39, 4]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[9:10, 5]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[39:40, 5]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[8:9, 6]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[40:41, 6]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[7:8, 7]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[41:42, 7]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[6:7, 8]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[42:43, 8]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[5:6, 9]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[43:44, 9]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[4:5, 10]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[44:45, 10]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[3:4, 11]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[45:46, 11]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[2:3, 13]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[46:47, 13]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[1:2, 15]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[47:48, 15]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[0:1, 18]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[48:49, 18]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    # Up
    for cell in mp.cellmap[19:32, 49]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[16:19, 48]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[32:35, 48]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[14:16, 47]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[35:37, 47]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[12:14, 46]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[37:39, 46]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[11:12, 45]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[39:40, 45]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[10:11, 44]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[40:41, 44]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[9:10, 43]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[41:42, 43]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[8:9, 42]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[42:43, 42]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[7:8, 41]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[43:44, 41]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[6:7, 40]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[44:45, 40]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[5:6, 39]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[45:46, 39]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[4:5, 38]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[46:47, 38]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[3:4, 36]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[47:48, 36]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[2:3, 34]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[48:49, 34]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[1:2, 31]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[49:50, 31]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    # left
    for cell in mp.cellmap[0, 19:32]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[1, 16:19]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[1, 32:35]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[2, 14:16]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[2, 35:37]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[3, 12:14]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[3, 37:39]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[4, 11:12]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[4, 39:40]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[5, 10:11]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[5, 40:41]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[6, 9:10]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[6, 41:42]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[7, 8:9]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[7, 42:43]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[8, 7:8]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[8, 43:44]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[9, 6:7]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[9, 44:45]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[10, 5:6]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[10, 45:46]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[11, 4:5]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[11, 46:47]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[13, 3:4]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[13, 47:48]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[15, 2:3]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[15, 48:49]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[18, 1:2]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[18, 49:50]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    # right
    for cell in mp.cellmap[49, 18:31]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[48, 15:18]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[48, 31:34]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[47, 13:15]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[47, 34:36]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[46, 11:13]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[46, 36:38]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[45, 10:11]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[45, 38:39]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[44, 9:10]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[44, 39:40]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[43, 8:9]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[43, 40:41]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[42, 7:8]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[42, 41:42]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[41, 6:7]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[41, 42:43]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[40, 5:6]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[40, 43:44]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[39, 4:5]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[39, 44:45]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[38, 3:4]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[38, 45:46]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[36, 2:3]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[36, 46:47]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[34, 1:2]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[34, 47:48]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[31, 0:1]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[31, 48:49]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))


def create_cross_section(mp):
    for cell in mp.cellmap[25, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[:, 25]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))


def create_cross_section_x(mp):
    for cell in mp.cellmap[49, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[:, 49]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[51, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[:, 51]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))


def create_cross_section_x_light(mp):
    for cell in mp.cellmap[49, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[:, 49]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[51, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[:, 51]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))
    mp.cellmap[48, 52].trafficLight = TrafficLigth(98, 58)
    mp.cellmap[52, 48].trafficLight = TrafficLigth(98, 58)
    mp.cellmap[48, 48].trafficLight = TrafficLigth(98, 0)
    mp.cellmap[52, 52].trafficLight = TrafficLigth(98, 0)


def create_cross_section_t_up(mp):
    for cell in mp.cellmap[0, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[1:, 49]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[2, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[1:, 51]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))


def create_cross_section_t_down(mp):
    for cell in mp.cellmap[97, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[:99, 49]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[99, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[:99, 51]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))


def create_cross_section_t_left(mp):
    for cell in mp.cellmap[49, 1:]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[:, 0]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[51, 1:]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[:, 2]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))


def create_cross_section_t_right(mp):
    for cell in mp.cellmap[49, :99]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[:, 97]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[51, :99]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[:, 99]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))
