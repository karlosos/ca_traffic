from src.vec_2d import Vec2D
from src.traffic_lights import TrafficLight


def create_roundabout_double(mp):
    # Down
    for cell in mp.cellmap[21:28, 10]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[18:20, 11]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[21:28, 11]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[29:31, 11]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[19:20, 12]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[29:30, 12]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[15:16, 13]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[17:18, 13]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[31:32, 13]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[33:34, 13]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    # Up
    for cell in mp.cellmap[22:29, 39]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[19:21, 38]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[22:29, 38]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[30:32, 38]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[20:21, 37]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[30:31, 37]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[16:17, 36]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[18:19, 36]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[32:33, 36]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    for cell in mp.cellmap[34:35, 36]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    # left
    for cell in mp.cellmap[10, 22:29]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[11, 19:21]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[11, 22:29]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[11, 30:32]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[12, 20:21]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[12, 30:31]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[13, 16:17]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[13, 18:19]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[13, 32:33]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[13, 34:35]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    # right
    for cell in mp.cellmap[39, 21:28]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[38, 18:20]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[38, 21:28]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[38, 29:31]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[37, 19:20]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[37, 29:30]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[36, 15:16]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[36, 17:18]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[36, 31:32]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[36, 33:34]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

# left down
    for cell in mp.cellmap[10, 21:22]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

    for cell in mp.cellmap[11, 21:22]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

    for cell in mp.cellmap[11, 18:19]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

    for cell in mp.cellmap[12, 17:18]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

    for cell in mp.cellmap[12, 19:20]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

    for cell in mp.cellmap[13, 15:16]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

    for cell in mp.cellmap[13, 17:18]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

    for cell in mp.cellmap[14, 14:15]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

    for cell in mp.cellmap[14, 16:17]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

    for cell in mp.cellmap[15, 15:16]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

    for cell in mp.cellmap[16, 13:15]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

    for cell in mp.cellmap[17, 12:13]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

    for cell in mp.cellmap[18, 13:14]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

    for cell in mp.cellmap[20, 11:13]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, -1))

# right up
    for cell in mp.cellmap[39, 28:29]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

    for cell in mp.cellmap[38, 28:29]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

    for cell in mp.cellmap[38, 31:32]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

    for cell in mp.cellmap[37, 30:31]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

    for cell in mp.cellmap[37, 32:33]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

    for cell in mp.cellmap[36, 32:33]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

    for cell in mp.cellmap[36, 34:35]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

    for cell in mp.cellmap[35, 33:34]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

    for cell in mp.cellmap[35, 35:36]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

    for cell in mp.cellmap[34, 34:35]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

    for cell in mp.cellmap[33, 35:37]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

    for cell in mp.cellmap[32, 37:38]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

    for cell in mp.cellmap[31, 36:37]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

    for cell in mp.cellmap[29, 37:39]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 1))

# right down
    for cell in mp.cellmap[28:29, 10]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

    for cell in mp.cellmap[28:29, 11]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

    for cell in mp.cellmap[31:32, 11]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

    for cell in mp.cellmap[30:31, 12]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

    for cell in mp.cellmap[32:33, 12]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

    for cell in mp.cellmap[32:33, 13]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

    for cell in mp.cellmap[34:35, 13]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

    for cell in mp.cellmap[33:34, 14]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

    for cell in mp.cellmap[35:36, 14]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

    for cell in mp.cellmap[34:35, 15]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

    for cell in mp.cellmap[35:37, 16]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

    for cell in mp.cellmap[37:38, 17]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

    for cell in mp.cellmap[36:37, 18]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

    for cell in mp.cellmap[37:39, 20]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 1))

# left up
    for cell in mp.cellmap[21:22, 39]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))

    for cell in mp.cellmap[21:22, 38]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))

    for cell in mp.cellmap[18:19, 38]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))

    for cell in mp.cellmap[17:18, 37]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))

    for cell in mp.cellmap[19:20, 37]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))

    for cell in mp.cellmap[15:16, 36]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))

    for cell in mp.cellmap[17:18, 36]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))

    for cell in mp.cellmap[14:15, 35]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))

    for cell in mp.cellmap[16:17, 35]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))

    for cell in mp.cellmap[15:16, 34]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))

    for cell in mp.cellmap[13:15, 33]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))

    for cell in mp.cellmap[12:13, 32]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))

    for cell in mp.cellmap[13:14, 31]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))

    for cell in mp.cellmap[11:13, 29]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, -1))


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
    mp.cellmap[48, 52].trafficLight = TrafficLight(98, 58, Vec2D(0, -1))
    mp.cellmap[52, 48].trafficLight = TrafficLight(98, 58, Vec2D(0, 1))
    mp.cellmap[48, 48].trafficLight = TrafficLight(98, 0, Vec2D(1, 0))
    mp.cellmap[52, 52].trafficLight = TrafficLight(98, 0, Vec2D(-1, 0))


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


def create_cross_section_t_up_light(mp):
    for cell in mp.cellmap[1, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[2:, 49]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[3, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[2:, 51]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))
    mp.cellmap[0, 52].trafficLight = TrafficLight(98, 58, Vec2D(0, -1))
    mp.cellmap[4, 48].trafficLight = TrafficLight(98, 58, Vec2D(0, 1))
    mp.cellmap[4, 52].trafficLight = TrafficLight(98, 0, Vec2D(-1, 0))


def create_cross_section_t_down_light(mp):
    for cell in mp.cellmap[96, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[:98, 49]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[98, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[:98, 51]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))
    mp.cellmap[95, 52].trafficLight = TrafficLight(98, 58, Vec2D(0, -1))
    mp.cellmap[99, 48].trafficLight = TrafficLight(98, 58, Vec2D(0, 1))
    mp.cellmap[95, 48].trafficLight = TrafficLight(98, 0, Vec2D(1, 0))


def create_cross_section_t_left_light(mp):
    for cell in mp.cellmap[49, 2:]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[:, 1]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[51, 2:]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[:, 3]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))
    mp.cellmap[48, 0].trafficLight = TrafficLight(98, 0, Vec2D(1, 0))
    mp.cellmap[48, 4].trafficLight = TrafficLight(98, 58, Vec2D(0, -1))
    mp.cellmap[52, 4].trafficLight = TrafficLight(98, 0, Vec2D(-1, 0))


def create_cross_section_t_right_light(mp):
    for cell in mp.cellmap[49, :98]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[:, 96]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[51, :98]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[:, 98]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))
    mp.cellmap[52, 95].trafficLight = TrafficLight(98, 58, Vec2D(0, 1))
    mp.cellmap[52, 99].trafficLight = TrafficLight(98, 0, Vec2D(-1, 0))
    mp.cellmap[48, 95].trafficLight = TrafficLight(98, 0, Vec2D(1, 0))


def trafficlightsetup(mp):
    mp.cellmap[0, 0].trafficLight = TrafficLight(98, 0)


def prioritysetup(mp):
    mp.cellmap[0, 0].kind = "road"
    mp.cellmap[0, 0].priority = True
